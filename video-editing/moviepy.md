# moviepy

Moviepy can do cutting, concatenating, creating clips from still images, etc.

If it is a longer movie then one can use subclip method to quickly check out
the result of the current step you are trying to do.

Here we add a still image video clip to the beginning of the main video clip:
```python
from moviepy.editor import *
clip = VideoFileClip(f_video).subclip(t_start=(0, 6.5))
image_clip = ImageClip(f_image).set_duration(10)
video = concatenate_videoclips([
    image_clip,
    clip
])
video.write_videofile("video_out.mp4", audio_codec="libvorbis")
```
