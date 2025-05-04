from moviepy.editor import VideoFileClip, vfx

# Load the video
input_path = "/Users/pinet/Downloads/immimic.mp4"  # Replace with your file path
output_path = "/Users/pinet/Downloads/immimic2.mp4"

# Load and speed up the video
clip = VideoFileClip(input_path)
sped_up_clip = clip.fx(vfx.speedx, factor=4)

# Write the result
sped_up_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
