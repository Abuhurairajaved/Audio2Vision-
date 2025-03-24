import os

audio_dir = "D:/multimodal/VGGSound/audio"
audio_files = [f for f in os.listdir(audio_dir) if f.endswith(".wav")]

print(f"✅ Total audio files present: {len(audio_files)}")
