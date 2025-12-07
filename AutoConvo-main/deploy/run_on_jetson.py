import os
import subprocess

def run_pipeline():
    print("Recording...")
    os.system("python3 src/mic_recording.py")

    print("Running inference...")
    os.system("python3 src/inference_pipeline.py")

if __name__ == "__main__":
    run_pipeline()
