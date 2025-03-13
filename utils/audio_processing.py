def audio_to_text(whisper_model, audio_path):
    """Converts an audio file to text using Whisper."""
    result = whisper_model.transcribe(audio_path)
    return result["text"]
