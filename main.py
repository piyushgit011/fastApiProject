from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import asyncio
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import math
from pexelsapi.pexels import Pexels
import requests
import os
from moviepy.editor import VideoFileClip
from moviepy.video.fx.speedx import speedx
from moviepy.editor import *
import moviepy.editor as mpe
import speech_recognition as sr
import datetime
from pydub import AudioSegment
import os
import time
# import rq
# from rq import Queue
# from redis import Redis


app = FastAPI()
# redis_conn = Redis()

# queue = Queue(connection=redis_conn)

def round_time_to_nearest_second(milliseconds):
    # Convert milliseconds to seconds and round to the nearest whole number
    return int(round(milliseconds / 1000.0))

def first():
    #text = "In the ever-evolving landscape of finance, cryptocurrency emerges as a beacon of innovation, offering a unique blend of opportunity and challenge. As investors, we are at the forefront of a digital revolution, where the potential for significant returns goes hand in hand with volatility and risk. Cryptocurrency investment isn't just about buying digital assets; it's about understanding the technology that powers them and the market dynamics that influence their value. With thorough research, strategic planning, and a diversified portfolio, the adventurous investor can navigate this new terrain. The future of finance is unfolding before our eyes, and cryptocurrency stands at its heart. Embrace the opportunity to be part of this groundbreaking journey."
    audio = AudioSegment.from_file("content/Gold a precious meta (3).wav")
    audio_length_seconds = len(audio) / 1000.0

    # Detect non-silent chunks
    nonsilent_chunks = detect_nonsilent(audio, min_silence_len=1000, silence_thresh=-32)

    # Adjust times to proper seconds and handle the last segment extension
    adjusted_chunks = []
    for start, end in nonsilent_chunks:
        start_sec = round_time_to_nearest_second(start)
        end_sec = round_time_to_nearest_second(end)
        adjusted_chunks.append((start_sec, end_sec))

    # Ensure the last segment extends to the end of the audio if needed
    if adjusted_chunks:
        last_start, last_end = adjusted_chunks[-1]
        if last_end < audio_length_seconds:
            # Adjust the end time of the last segment to the audio length
            adjusted_chunks[-1] = (last_start, math.ceil(audio_length_seconds))

    for i, (start_sec, end_sec) in enumerate(adjusted_chunks):
        print(f"Segment {i + 1}: Starts at {start_sec}s, Ends at {end_sec}s")

    # Optionally, export adjusted segments
    for i, (start_sec, end_sec) in enumerate(adjusted_chunks):
        start_ms, end_ms = start_sec * 1000, end_sec * 1000
        segment = audio[start_ms:end_ms]
        segment.export(f"segment_adjusted_{i + 1}.mp3", format="mp3")

def second():
    audio = AudioSegment.from_file("content/Gold a precious meta (3).wav")
    audio_length_seconds = len(audio) / 1000.0

    # Detect non-silent chunks
    nonsilent_chunks = detect_nonsilent(audio, min_silence_len=1000, silence_thresh=-32)

    # Adjust times to proper seconds
    adjusted_chunks = []
    for start, end in nonsilent_chunks:
        start_sec = round_time_to_nearest_second(start)
        end_sec = round_time_to_nearest_second(end)
        adjusted_chunks.append((start_sec, end_sec))

    # Correct the end time of each segment to match the start of the next for continuity
    for i in range(len(adjusted_chunks) - 1):
        current_start, current_end = adjusted_chunks[i]
        next_start, next_end = adjusted_chunks[i + 1]

        # If current segment end does not align with next segment start, adjust it
        if current_end < next_start:
            adjusted_chunks[i] = (current_start, next_start)

    # Ensure the last segment extends to the end of the audio if needed
    if adjusted_chunks:
        last_start, last_end = adjusted_chunks[-1]
        if last_end < audio_length_seconds:
            # Adjust the end time of the last segment to the audio length
            adjusted_chunks[-1] = (last_start, math.ceil(audio_length_seconds))

    for i, (start_sec, end_sec) in enumerate(adjusted_chunks):
        print(f"Segment {i + 1}: Starts at {start_sec}s, Ends at {end_sec}s")

    print(adjusted_chunks)

def third():
    segments = [(0, 11), (11, 21), (21, 32), (32, 41), (41, 48), (48, 53)]
    time_differences = [end - start for start, end in segments]

    time_differences
    keywords = ["Cryptocurrency", "Digital revolution", "Market dynamics", "Diversified portfolio", "Future finance",
                "Embrace opportunity"]
    pexel = Pexels('VbzeAkZpankLKM0HPXTvbjzhRkxUl2jQdzhrKqsEJU7lemhk0JN4HQIq')
    keywords = ["Cryptocurrency", "Digital revolution", "Market dynamics", "Diversified portfolio", "Future finance",
                "Embrace opportunity"]
    dura = [11, 10, 11, 9, 7, 5]
    id = []
    i = 0;
    for key in keywords:
        search_videos = pexel.search_videos(query=key, per_page=1)
        i = i + 1
        print(search_videos)
        id.append(search_videos['videos'][0]['id'])
        print(search_videos['videos'][0]['id'])
    print(id)
   # from pexelsapi.pexels import Pexels
    pexel = Pexels('VbzeAkZpankLKM0HPXTvbjzhRkxUl2jQdzhrKqsEJU7lemhk0JN4HQIq')

    for id in id:
        url_video = 'https://www.pexels.com/video/' + str(id) + '/download'
        r = requests.get(url_video)
        with open(str(id) + '.mp4', 'wb') as outfile:
            outfile.write(r.content)

def trim_video(video_path, start_time, end_time, output_path,codec='libx264'):
  if not os.path.exists(video_path):
    raise FileNotFoundError(f"Video file not found: {video_path}")

  try:
    clip = VideoFileClip(video_path)
    trimmed_clip = clip.subclip(start_time, end_time)
    trimmed_clip.write_videofile(output_path)
    print(f"Video trimmed successfully and saved to: {output_path}")
  except Exception as e:
    print(f"Error trimming video: {e}")

def fourth():
    video_path = "6799742.mp4"
    start_time = 1  # in seconds
    end_time = 7  # in seconds
    output_path = "/content/"

    trim_video(video_path, start_time, end_time, output_path)
    ids = [5665495, 3163534, 6799742, 7322355, 7164240, 4873454]
    times = [11, 10, 11, 9, 7, 5]

    # Loop through each video ID and time
    for i, (video_id, desired_time) in enumerate(zip(ids, times), start=1):
        # Load the video
        clip = VideoFileClip(f"{video_id}.mp4")

        # Calculate the actual duration of the clip
        actual_duration = clip.duration

        # Check if the actual duration is less than the desired time
        if actual_duration < desired_time:
            # Calculate the speed factor to stretch the video to the desired time
            speed_factor = actual_duration / desired_time
            # Apply the speed change to stretch the video
            adjusted_clip = speedx(clip, factor=speed_factor)
            # Trim or extend the adjusted clip to the desired time to ensure correct length
            final_clip = adjusted_clip.subclip(0, desired_time)
        else:
            # If the video duration is longer than the desired time, just trim it
            final_clip = clip.subclip(0, desired_time)

        # Save the adjusted video with incremental filenames
        final_clip.write_videofile(f"adjusted_{i}.mp4")

def fifth():
    # from moviepy.editor import *

    # Desired output resolution for YouTube Shorts
    output_width = 1080
    output_height = 1920

    # List to store clips to be merged
    clips = []

    # Function to resize and crop the video to fill the screen
    def resize_and_fill(clip, output_width, output_height):
        # Calculate the aspect ratio of the input clip and the output resolution
        clip_aspect_ratio = clip.w / clip.h
        output_aspect_ratio = output_width / output_height

        if clip_aspect_ratio > output_aspect_ratio:
            # If the clip is wider than the output, scale by height and crop the sides
            scaled_clip = clip.resize(height=output_height)
            # Crop sides to match output width
            crop_x = (scaled_clip.w - output_width) / 2
            final_clip = scaled_clip.crop(x1=crop_x, width=output_width, height=output_height)
        else:
            # If the clip is taller than the output, scale by width and crop the top/bottom
            scaled_clip = clip.resize(width=output_width)
            # Crop top/bottom to match output height
            crop_y = (scaled_clip.h - output_height) / 2
            final_clip = scaled_clip.crop(y1=crop_y, width=output_width, height=output_height)

        return final_clip

    # Load each video by its filename, resize and fill the screen, and add it to the list
    for i in range(1, 7):  # Adjust the range according to the number of your videos
        clip = VideoFileClip(f"adjusted_{i}.mp4")
        # Resize and fill the screen without leaving black bars
        filled_clip = resize_and_fill(clip, output_width, output_height)
        clips.append(filled_clip)

    # Concatenate all clips in the list using the compose method to handle different sizes gracefully
    final_clip = concatenate_videoclips(clips, method="compose")

    # Write the result to a file, using a codec compatible with YouTube
    final_clip.write_videofile("merged_video_for_youtube_shorts.mp4", codec="libx264", fps=24)  # Specify fps if needed

def sixth():
    import moviepy.editor as mpe

    # Paths for your video and audio files
    video_path = "merged_video_for_youtube_shorts.mp4"
    audio_path = "content/Gold a precious meta (3).wav"

    # Load the video and audio files
    video = mpe.VideoFileClip(video_path)
    audio = mpe.AudioFileClip(audio_path)

    # Check the durations
    print(f"Video duration: {video.duration}")
    print(f"Audio duration: {audio.duration}")

    # If the audio is longer than the video, loop the video to match the audio duration
    if audio.duration > video.duration:
        # Calculate how many times the video should be looped
        loop_count = int(audio.duration // video.duration) + 1
        # Loop the video
        video = mpe.concatenate_videoclips([video] * loop_count)

    # Trim the looped video to match the audio duration exactly
    video = video.subclip(0, audio.duration)

    # Set the audio of the video clip to the new audio file
    final_clip = video.set_audio(audio)

    # Specify the output path for the final video
    output_path = f"output_video1.mp4"

    # Write the final video file with specified codecs
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred in {func.__name__}: {e}")
            return None
    return wrapper

# Define the function to split text into chunks
@handle_errors
def split_text(text, chunk_size=3):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield ' '.join(words[i:i+chunk_size])

# Define the function to generate SRT with non-overlapping subtitles
def generate_srt_non_overlapping(text_chunks, audio_length, output_file='subtitles.srt'):
    num_chunks = len(text_chunks)
    chunk_duration = audio_length / num_chunks
    with open(output_file, 'w') as f:
        for i, chunk in enumerate(text_chunks):
            start_time = i * chunk_duration
            end_time = (i + 1) * chunk_duration - 0.1  # Adjust the end time to prevent overlap
            if i == num_chunks - 1:  # Do not adjust the last chunk's end time
                end_time += 0.1

            # Convert times to HH:MM:SS,mmm format
            start_time_str = str(datetime.timedelta(seconds=start_time)).split(".")[0]
            start_time_str += ',' + str(int(start_time % 1 * 1000)).zfill(3)
            end_time_str = str(datetime.timedelta(seconds=end_time)).split(".")[0]
            end_time_str += ',' + str(int(end_time % 1 * 1000)).zfill(3)

            f.write(f"{i+1}\n")
            f.write(f"{start_time_str} --> {end_time_str}\n")
            f.write(f"{chunk}\n\n")

def seventh():
    text = "In the ever-evolving landscape of finance, cryptocurrency emerges as a beacon of innovation, offering a unique blend of opportunity and challenge. As investors, we are at the forefront of a digital revolution, where the potential for significant returns goes hand in hand with volatility and risk. Cryptocurrency investment isn't just about buying digital assets; it's about understanding the technology that powers them and the market dynamics that influence their value. With thorough research, strategic planning, and a diversified portfolio, the adventurous investor can navigate this new terrain. The future of finance is unfolding before our eyes, and cryptocurrency stands at its heart. Embrace the opportunity to be part of this groundbreaking journey."
    text_chunks = list(split_text(text))
    audio_length = 52  # Length of your audio in seconds

    print("Generating subtitles.srt...")
    generate_srt_non_overlapping(text_chunks, audio_length)
    print("Subtitles generated successfully!")

@app.get("/")
async def root():
    return {"message": "Hello World"}

# def generate_video(text: str):
#     first()
#     second()
#     third()
#     fourth()
#     fifth()
#     sixth(id)
#     seventh()

#     # Generate the video file
#     video = f"output_video{id}.mp4"
#     return video

# @app.post("/generate_video")
# async def start_generate_video(text: str):
#     # Enqueue the generate_video function with the provided text
#     job = queue.enqueue(generate_video, text)
#     global id = job.id
#     return {"job_id": job.id}

# @app.get("/check_job/{job_id}")
# async def check_job_status(job_id: str):
#     # Fetch the job from the queue by its ID
#     job = rq.job.Job.fetch(job_id, connection=redis_conn)

#     # Check if the job is finished
#     if job.is_finished:
#         # If job is finished, return the generated video
#         video = f"output_video{job_id}.mp4"
#         file_object = open(video, "rb")
#         return StreamingResponse(file_object, media_type="video/mp4")
#     elif job.is_failed:
#         # If job failed, return an error message
#         return {"status": "failed", "message": "Video generation failed"}
#     else:
#         # If job is still in progress, return its status
#         return {"status": "in_progress"}

@app.post("/generate_video")
async def generate_video(text: str):
    # video = generate_video_from_text(text)
    # video = generate_video_from_text(text)

    first()

    second()

    third()

    fourth()

    fifth()

    sixth()

    seventh()

    # After all tasks are completed, generate the video file
    video = "output_video1.mp4"
    file_object = open(video, "rb")
    return StreamingResponse(file_object, media_type="video/mp4")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
