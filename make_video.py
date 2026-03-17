import textwrap
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy import *
import random
import os
from make_alert_call import calling


def video(riddle_text):
    # Paths
    music_folder = r"C:\Users\NANDULA SINDHURA\Documents\python_projects\AI_Music"
    image_folder = r"C:\Users\NANDULA SINDHURA\Documents\python_projects\Instagram_reel_images"
    output_folder = r"C:\Users\NANDULA SINDHURA\Documents\python_projects\codes\Trending\output"

    # Pick random background image
    image_file = random.choice(os.listdir(image_folder))
    img_path = os.path.join(image_folder, image_file)
    img = Image.open(img_path).convert("RGB")

    #  Force 9:16 aspect ratio (1080x1920)
    target_width, target_height = 1080, 1920
    img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arialbd.ttf", 60)
    except:
        print(" Default font used")
        font = ImageFont.load_default()

    
    wrapped_question = textwrap.wrap(riddle_text, width=30)
    image_width, image_height = img.size
    line_height = 80
    text_start_y = image_height // 2 - (len(wrapped_question) * line_height) // 2

    for i, line in enumerate(wrapped_question):
        bbox = draw.textbbox((0, 0), line, font=font)
        line_width = bbox[2] - bbox[0]
        x = (image_width - line_width) // 2
        y = text_start_y + i * line_height
        draw.text((x, y), line, font=font, fill=(255, 255, 255))

    # Save temp image
    temp_img_path = os.path.join(image_folder, "temp_riddle_img.png")
    img.save(temp_img_path)


    clip_duration = 12
    clip = ImageClip(temp_img_path, duration=clip_duration).resized((1080, 1920))
    clip = clip.with_position(("center", "center")).with_fps(30)

    
    music_file = random.choice(os.listdir(music_folder))
    music_path = os.path.join(music_folder, music_file)
    music_clip = AudioFileClip(music_path)

    if music_clip.duration < clip_duration:
        loops = int(np.ceil(clip_duration / music_clip.duration))
        music = concatenate_audioclips([music_clip] * loops).subclipped(0, clip_duration)
    else:
        music = music_clip.subclipped(0, clip_duration)

    
    
    output_video = f'Cricket_Riddle.mp4'


    output_video_path = os.path.join(output_folder, output_video)

    
    final_clip = clip.with_audio(music).resized((1080, 1920))

  
    final_clip.write_videofile(
        output_video_path,
        fps=30,
        codec="libx264",
        audio_codec="aac",
        threads=4,
        preset="medium",
        ffmpeg_params=[
            "-vf",
            "scale=1080:1920:force_original_aspect_ratio=decrease,"
            "pad=1080:1920:(ow-iw)/2:(oh-ih)/2"
        ]
    )

    print(" Instagram Reel created at:", output_video_path)
    print("Video completed")

    
    if os.path.exists(temp_img_path):
        print("enterd")
        os.remove(temp_img_path)
        print("removed")
        print(f"🗑️ Deleted: {temp_img_path}")
    else:
        print("else block")
        print(f" File not found: {temp_img_path}")
    final_clip.close()
    clip.close()
    music.close()
    music_clip.close()
    
    
    

    

