import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="live_input.wav", duration=4, fs=16000):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print(f"Saved: {filename}")

if __name__ == "__main__":
    record_audio()
