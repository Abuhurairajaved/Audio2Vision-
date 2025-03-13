import os
from config import GENERATED_IMAGES_DIR

def generate_image(text_to_image_model, prompt):
    """Generates an image from text using Stable Diffusion."""
    image = text_to_image_model(prompt).images[0]
    return image

def save_image(image, audio_path):
    """Saves the generated image using the original audio filename."""
    image_filename = os.path.basename(audio_path).replace(".wav", ".png")
    image_path = os.path.join(GENERATED_IMAGES_DIR, image_filename)
    image.save(image_path)
    print(f"Saved Image: {image_path}")
    return image_path
