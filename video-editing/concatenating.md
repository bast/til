# Concatenate vides with ffmpeg

Adding an intro-slide to a video:
```bash
for video in video1 video2; do
    ffmpeg -framerate 30 -loop 1 -t 5 -i ${video}-in.jpg -i ${video}.mkv -loop 1 -t 5 -i ${video}-out.jpg -f lavfi -t 5 -i anullsrc -filter_complex "[0][3][1:v]
[1:a][2][3]concat=n=3:v=1:a=1[outv][outa]" -map "[outv]" -map "[outa]" ${video}-with-slides.mkv
done
```
