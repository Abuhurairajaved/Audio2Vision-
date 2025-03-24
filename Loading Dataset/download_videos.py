import yt_dlp
import pandas as pd
import os

# Load dataset (CSV file with video metadata)
csv_file = "D:/multimodal/VGGSound/data/vggsound.csv"
df = pd.read_csv(csv_file)

# Select only the first 1000 videos (adjust as needed)
df_sampled = df.iloc[:1000]
video_ids = df_sampled.iloc[:, 0].tolist()  # Assuming video_id is in the first column

# Output directory
output_dir = "D:/multimodal/VGGSound/videos"
os.makedirs(output_dir, exist_ok=True)

# Log failed downloads
failed_videos_file = "D:/multimodal/VGGSound/failed_videos.txt"

# Function to download videos
def download_video(video_id):
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, f'{video_id}.mp4'),
        'format': '18',  # Standard MP4 format
        'quiet': False,   # Show download progress
        'noplaylist': True,
        'ignoreerrors': True,  # Ignore errors and continue
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([video_url])
        if result != 0:  # If download fails
            with open(failed_videos_file, "a") as f:
                f.write(video_id + "\n")
            print(f"❌ Skipped (Failed/Private): {video_id}")

# Start downloading videos
for idx, video_id in enumerate(video_ids, 1):
    print(f"📥 Downloading {idx}/{len(video_ids)}: {video_id}")
    download_video(video_id)

print("\n🎉 Download process completed!")
print(f"❌ Failed videos are logged in: {failed_videos_file}")
