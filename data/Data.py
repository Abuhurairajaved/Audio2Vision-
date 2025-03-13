import os
import logging
from datasets import load_dataset

# Configure logging
logging.basicConfig(level=logging.INFO)

# Default dataset path (Can be overridden dynamically)
DEFAULT_DATASET_PATH = r"D:\multimodal\data\audio-dataset-flickr-soundnet\Dataset\Data"

def find_audio_files(dataset_path):
    """Recursively find all audio files in the given directory."""
    audio_files = []
    for root, _, files in os.walk(dataset_path):
        for file in files:
            if file.endswith((".wav", ".mp3")):  # More efficient check
                audio_files.append(os.path.join(root, file))

    if not audio_files:
        raise FileNotFoundError(f"No audio files found in {dataset_path}")

    logging.info(f"Total audio files found: {len(audio_files)}")
    return audio_files

def load_flickr_dataset(dataset_path=DEFAULT_DATASET_PATH):
    """Loads and returns the Flickr audio dataset."""
    try:
        audio_files = find_audio_files(dataset_path)

        # Load dataset using found audio files
        dataset = load_dataset(
            "cssen/audio-dataset-flickr-soundnet",
            data_files={"train": audio_files},
            cache_dir="./flickr_audio_dataset"
        )

        logging.info("Dataset loaded successfully!")
        return dataset

    except Exception as e:
        logging.error(f"Error loading dataset: {e}")
        return None
