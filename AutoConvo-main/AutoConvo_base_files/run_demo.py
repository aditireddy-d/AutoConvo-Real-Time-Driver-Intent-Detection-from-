from src.mic_recording import record_audio
from src.inference_pipeline import run_pipeline

if __name__ == "__main__":
    record_audio("live_input.wav")
    run_pipeline("live_input.wav", "models/distilbert_finetuned")
