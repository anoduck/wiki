```text
#  _____ _____ __  __
# |  ___|  ___|  \/  |_ __   ___  __ _
# | |_  | |_  | |\/| | '_ \ / _ \/ _` |
# |  _| |  _| | |  | | |_) |  __/ (_| |
# |_|   |_|   |_|  |_| .__/ \___|\__, |
#                    |_|         |___/
#
```

## ffmpeg

Let me start this page clearly stating the truth of the subject at hand, that is ffmpeg is fucking __AWESOME!__ 
Admittedly, I have not had to use it as much as others, but everytime I have used it, I have discovered a
whole new functionality to the program, that simply rocks the bejeezus out of me. As far as I can tell, it can
do just about anything with video media that needs to be done. 

Stating this, I have started this page to keep track of commands I have encountered using ffmpeg. For a full
understanding of all that ffmpeg can do, either seek help within the man pages or phone a friend.

1. Repairing a corrupt TS file: `ffmpeg –i corrupted_input.ts –map –ignore_unknown/-copy_unknown –c copy fixed.ts` (incorrect)
2. Repairing a corrupt mp4 file: `ffmpeg -i input.mp4 -c copy output.mp4`
3. Concatenate several files: `ffmpeg -i input1.mp4 -i input2.mp4 -i input3.mp4 output.mp4`
4. Convert video format: `ffmpeg -i input.mp4 output.avi`
5. Extract sound stream: `ffmpeg -i video1.avi -vn -ar 44100 -ac 2 -ab 192 -f mp3 audio3.mp3`
6. Check video corruption: `ffmpeg –v error –i corrupted_input.ts -f null – &> corruptions.log`
7. Convert video to images: `ffmpeg -i Video_36.wmv -an -f image2 filename%03d.jpg`
8. Perform post-processing: `ffmpeg -i Video_of_something.mp4 -vf fspp=4:10 -c copy output.mp4`

### Converting files to more editing friendly codecs

In all the following commands, if audio reformating is not desired, replace all arguements to the `-c:a` flag
with `-c:a copy`. This can significantly reduce error messages for uncooperative audio formats.

1. ProRes 422LT with one audio track in MOV: `ffmpeg -i (input file) -c:v prores -profile:v 1 -c:a pcm_s16le (output).mov`
2. ProRes 422 HQ with two discrete audio tracks in MOV: `ffmpeg -i (input file) -map 0:0 -map 0:1 -map 0:2 -c:v prores -profile:v 3 -c:a:0 pcm_s16le -c:a:1 pcm_s16le (output).mov`
3. DNxHD 115 for 1080p23.976, with one audio track in MXF Op1a: `ffmpeg -i (input file) -c:v dnxhd -b:v 115M -c:a pcm_s16le (output).mxf`
4. Converting to DNxHD 145 720p59.94 at 48kHz for MOV: `ffmpeg -i (input file) -c:v dnxhd -b:v 145M -c:a pcm_s16le -r 60000/1001 -ar 48000 -vf scale=1280:720 (output).mov`
5. Rewrapping to an MOV file, keeping source codecs and formats: `ffmpeg -i (input file) -c:v copy -c:a copy (output).mov`
6. Rewrapping video, and re-encoding audio: `ffmpeg -i (input file) -c:v copy -c:a pcm_s16le (output).mov`
7. Encoding H.264 using NVENC using Constant Quality Rate Factor 18, High Profile: `ffmpeg -i (input file) -c:v h264_nvenc -cq 18 -profile:v high -c:a aac -b:a 128k (output).mp4`
8. Encoding H.265 using HEVC using Constant Quality Rate Factor 28, Medium Profile: `ffmpeg -i (input file) -c:v h265_hevc -cq 28 -profile:v medium -c:a copy (output).mp4`

### Batch merge of files in folder

It seems `ffmpeg` changed their script flags very recently, as a result, many "how-tos" and "tutorials" use
the old flag convention. This is is most evident with advice concerning how to merge several video files
together. The correct method can be found in the [project's wiki page.](https://trac.ffmpeg.org/wiki). Below
is a dirty example of how to do it.

```bash
#!/bin/bash
for i in ./*.mp4; do
  echo "file $i" >>mylist.txt
done

ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4
```

### Working with ffmpegs bitstream filter

Normally one would use the bitstream filter to convert video files to streaming formats, but what we
want to do is the exact opposite. We want to remove all the additional metadata that is added to a
bitstream file, and the best means to accomplish this is to run ffmpeg straight without a flag, as you would
to convert a file between different codecs. 

### Slowdown, crop, zoom, and minterpolate for smoothing.

Recently there was the need to slow down the speed of a video, as the video only lasted fourteen mere seconds.
The video picture also needed to be cropped, since only 25% of the picture showed content that was important,
the other 75% of the picture was grass. So here is what was done.

1. Video at half speed: `ffmpeg -i $INPUT.VIDEO -filter:v "setpts=2.0*PTS" $OUTPUT.VIDEO`
2. Crop and Zoom video picture: `ffmpeg -i $INPUT.VIDEO -vf "scale=2*iw:-1, crop=in_w:in_h/2:0:0" $OUTPUT.VIDEO`
3. Minterpolate video to smooth image: `ffmpeg -i $INPUT.VIDEO -filter:v "minterpolate='mi_mode=mci:mc_mode=aobmc:vsbmc=1:fps=60'" $OUTPUT.VIDEO`

Of all of these, the crop and zoom has the highest potential of generating the most confusion, so let's take a
moment to review it. First off, `-vf` and `-filter:v` are equivocal, just one is long hand and the other is short.
Next, note `iw` and `in_w` both stand for input width, as `ih` and `in_h` stands for input height, and both
inputs, width and height, can be multiplied and divided within the filter designations as you see above. Using
`-1` for a value will make ffmpeg compute the value automatically for you. 

The scale filter takes two parameters `WIDTH:HEIGHT`, where the crop filter is more complex and takes four
parameters `WIDTH:HEIGHT:LEFT:RIGHT`. The parameters of the crop filter are read from the top left corner of
the picture. From left to right, and from top to bottom. Thus is why in the provided example, you will see the
designated height of the picture is one half of the original height, and ffmpeg was told to crop from the zero
position. Which meant the bottom half of the image is to be cut out. If you wanted to cut out the top half of
the image you could use `in_w:in_h/2:0:in_h/2`. If you wanted to cut the width in half to only show the
bottom right corner, you would use `in_w/2:in_h/2:in_w/2:in_h/2`. 

One final word about the commands above, the example referrenced for minterpolate used a frames per second
rate of 120. For the sake of time needed to process and upload time, this was cut in half to 60. 120 just felt
too high for a short video lasting only a few seconds.

I guess that about covers it.

### Filters (That we have tried)

It is important to mention the [ffmpeg filter guide](https://trac.ffmpeg.org/wiki/FilteringGuide).

- Cropping
- deblocking
- vaguesmooth
- scale
