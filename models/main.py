import os
import torch
import whisper
from diffusers import StableDiffusionPipeline
from dataset import load_vggsound_dataset

# Paths
MODEL_SAVE_PATH = "D:/multimodal/trained_model"
GENERATED_IMAGES_DIR = "D:/multimodal/VGGSound/generated_images"
os.makedirs(GENERATED_IMAGES_DIR, exist_ok=True)

# ✅ Load Dataset
dataset = load_vggsound_dataset()

# ✅ Load Models
device = "cuda" if torch.cuda.is_available() else "cpu"
whisper_model = whisper.load_model("base").to(device)
text_to_image_model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to(device)

def audio_to_text(audio_path):
    """Convert audio to text using Whisper."""
    try:
        result = whisper_model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        print(f"❌ Failed to transcribe {audio_path}: {e}")
        return None

def generate_image(prompt):
    """Generate an image from text using Stable Diffusion."""
    try:
        image = text_to_image_model(prompt).images[0]
        return image
    except Exception as e:
        print(f"❌ Failed to generate image for prompt: {prompt}. Error: {e}")
        return None

# ✅ Generation Process
for idx, data in enumerate(dataset):
    audio_path, label = data["audio_path"], data["label"]

    print(f"🎤 Processing {idx+1}/{len(dataset)}: {audio_path}")

    try:
        # Step 1: Convert Audio to Text
        generated_text = audio_to_text(audio_path)
        if not generated_text:
            continue  # Skip if transcription failed
        
        print(f"📝 Generated Text: {generated_text}")

        # Step 2: Generate Image from Text
        generated_image = generate_image(generated_text)
        if generated_image is None:
            continue  # Skip if image generation failed

        # Step 3: Save Image
        image_filename = os.path.basename(audio_path).replace(".wav", ".png")
        image_path = os.path.join(GENERATED_IMAGES_DIR, image_filename)
        generated_image.save(image_path)
        print(f"📸 Saved Image: {image_path}")

    except Exception as e:
        print(f"❌ Error processing {audio_path}: {e}")

# ✅ Save the trained model (for fine-tuning later)
text_to_image_model.save_pretrained(MODEL_SAVE_PATH)
print(f"🎯 Model saved at {MODEL_SAVE_PATH}!")
