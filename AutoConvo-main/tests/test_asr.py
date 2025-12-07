import unittest
from src.asr_whisper import transcribe_audio

class TestWhisperASR(unittest.TestCase):
    def test_transcription_output(self):
        text = transcribe_audio("data/processed/noisy_call_pranjal.wav")
        self.assertIsInstance(text, str)
        self.assertGreater(len(text), 0)

if __name__ == "__main__":
    unittest.main()
