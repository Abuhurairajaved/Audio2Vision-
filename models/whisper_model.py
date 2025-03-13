import whisper

def load_whisper_model(model_size="base"):
    """Loads and returns the Whisper model."""
    return whisper.load_model(model_size)
