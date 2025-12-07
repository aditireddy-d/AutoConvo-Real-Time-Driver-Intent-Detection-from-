from pydub import AudioSegment
import os

RAW_PATH = "data/raw_audio/"
NOISE_PATH = "data/noise_clips/"
OUTPUT_PATH = "data/processed/"

def mix_noise(clean_path, noise_path, output_path, noise_level=-10):
    clean = AudioSegment.from_file(clean_path)
    noise = AudioSegment.from_file(noise_path)
    noisy = clean.overlay(noise + noise_level)
    noisy.export(output_path, format="wav")

def preprocess_all():
    for filename in os.listdir(RAW_PATH):
        if filename.endswith(".wav"):
            clean_path = os.path.join(RAW_PATH, filename)
            output_path = os.path.join(OUTPUT_PATH, f"noisy_{filename}")
            noise_path = os.path.join(NOISE_PATH, "engine.wav")
            mix_noise(clean_path, noise_path, output_path)

if __name__ == "__main__":
    preprocess_all()
