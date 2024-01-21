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

1. Repairing a corrupt TS file: `ffmpeg –i corrupted_input.ts –map –ignore_unknown/-copy_unknown –c copy fixed.ts`
2. Repairing a corrupt mp4 file: `ffmpeg -i input.mp4 -c copy output.mp4`
3. Concatenate several files: `ffmpeg -i input1.mp4 -i input2.mp4 -i input3.mp4 output.mp4`
4. Convert video format: `ffmpeg -i input.mp4 output.avi`
5. Extract sound stream: `ffmpeg -i video1.avi -vn -ar 44100 -ac 2 -ab 192 -f mp3 audio3.mp3`
6. Check video corruption: `ffmpeg –v error –i corrupted_input.ts -f null – &> corruptions.log`
7. Convert video to images: `ffmpeg -i Video_36.wmv -an -f image2 filename%03d.jpg`
8. Perform post processing: `ffmpeg -i Video_of_something.mp4 -vf fspp=4:10 -c copy output.mp4`

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

### Filters (That we have tried)

- Cropping
- deblocking
- vaguesmooth
- scale
