import pandas as pd
import json
import os

# Paths
csv_file = "D:/multimodal/VGGSound/data/vggsound.csv"
video_folder = "D:/multimodal/VGGSound/videos"
output_json = "D:/multimodal/VGGSound/video_labels.json"

# Load dataset
df = pd.read_csv(csv_file)

# Extract video IDs and labels
video_labels = {}
for _, row in df.iterrows():
    video_id = row["video_id"]
    label = row["category"]

    # Check if the video exists in the downloaded videos folder
    video_path = os.path.join(video_folder, f"{video_id}.mp4")
    if os.path.exists(video_path):
        video_labels[video_id] = label

# Save the labels to a JSON file
with open(output_json, "w") as f:
    json.dump(video_labels, f, indent=4)

print(f"✅ Labeled {len(video_labels)} videos. Saved labels to {output_json}.")
