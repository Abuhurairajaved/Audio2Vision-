import json

labels_file = "D:/multimodal/VGGSound/video_labels.json"

with open(labels_file, "r") as f:
    video_labels = json.load(f)

# Print first 10 labels
for video_id, label in list(video_labels.items())[:10]:
    print(f"🎬 Video: {video_id} → 🔖 Label: {label}")

print(f"\n✅ Total labeled videos: {len(video_labels)}")
