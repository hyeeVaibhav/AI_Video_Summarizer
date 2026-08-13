import streamlit as st
import whisper
import subprocess
import os

def extract_audio(video_path: str, audio_path: str = "temp_audio.wav") -> str:
    if os.path.exists(audio_path):
        os.remove(audio_path)
    # FFmpeg command
    command = [
        "ffmpeg", "-i", video_path, "-q:a", "0", "-map", "a", audio_path, "-y"
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return audio_path

@st.cache_resource
def load_whisper_model(model_size):
    # This keeps the model in memory so it doesn't reload constantly
    return whisper.load_model(model_size)

def transcribe_audio(audio_path: str, model_size: str = "tiny") -> str:
    # We use 'tiny' by default for maximum CPU speed
    model = load_whisper_model(model_size)
    result = model.transcribe(audio_path)
    return result["text"]