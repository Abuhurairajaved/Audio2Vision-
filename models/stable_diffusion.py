import torch
from diffusers import StableDiffusionPipeline
from config import DEVICE

def load_stable_diffusion_model():
    """Loads and returns the Stable Diffusion model."""
    model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
    model.to(DEVICE)
    return model
