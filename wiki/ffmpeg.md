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
