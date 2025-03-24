import os
import json

# Paths
AUDIO_DIR = "D:/multimodal/VGGSound/audio"
LABELS_JSON = "D:/multimodal/VGGSound/video_labels.json"

def load_vggsound_dataset():
    """Loads the VGGSound dataset with labeled audio files."""

    # Load labels from JSON
    with open(LABELS_JSON, "r") as f:
        labels_dict = json.load(f)  # Dictionary {video_id: label}

    # Get all available audio files
    audio_files = {f.split(".")[0] for f in os.listdir(AUDIO_DIR) if f.endswith(".wav")}

    dataset = []
    missing_labels = []

    for video_id, label in labels_dict.items():
        if video_id in audio_files:
            dataset.append({
                "audio_path": os.path.join(AUDIO_DIR, f"{video_id}.wav"),
                "label": label
            })
        else:
            missing_labels.append(video_id)

    # Print results
    print(f"✅ Found {len(dataset)} labeled audio files.")
    print(f"❌ Missing {len(missing_labels)} labeled files (audio not found).")

    if missing_labels:
        print("⚠️ Saving missing labels to `missing_audio.json`...")
        with open("D:/multimodal/VGGSound/missing_audio.json", "w") as f:
            json.dump(missing_labels, f, indent=4)

    print(f"🔹 Sample Data: {dataset[:5]}")  # Show first 5 samples
    return dataset

# Test loading
if __name__ == "__main__":
    dataset = load_vggsound_dataset()
