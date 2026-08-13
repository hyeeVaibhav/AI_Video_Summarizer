import os
from transcriber import extract_audio, transcribe_audio
from summarizer import summarize_text
from utils import chunked_summary

def video_to_summary(
    video_path: str, 
    model_size: str = "tiny", 
    summarizer_model_name: str = "Falconsai/text_summarization", # The new "Goldilocks" model
    use_chunking: bool = False
) -> str:
    audio_path = "temp_audio.wav"
    
    print("Extracting audio...")
    extract_audio(video_path, audio_path)
    
    print("Transcribing audio...")
    transcript = transcribe_audio(audio_path, model_size=model_size)
    
    print("Summarizing text...")
    if use_chunking and len(transcript) > 2000:
        final_summary = chunked_summary(
            transcript, 
            lambda text: summarize_text(text, model_name=summarizer_model_name)
        )
    else:
        final_summary = summarize_text(transcript, model_name=summarizer_model_name)
        
    if os.path.exists(audio_path):
        os.remove(audio_path)
        
    return final_summary