from asr_whisper import transcribe_audio
from intent_model import IntentClassifier
from context_tracker import ContextTracker

intent_map = {
    0: "play_music",
    1: "call_contact",
    2: "navigate_home"
}

def run_pipeline(audio_path, model_path):
    text = transcribe_audio(audio_path)
    print(f"Transcript: {text}")

    context = ContextTracker()
    resolved_text = context.resolve(text)

    classifier = IntentClassifier(model_path)
    label_id = classifier.predict(resolved_text)
    intent = intent_map.get(label_id, "unknown")

    context.update(intent, {"name": "Pranjal"} if "Pranjal" in text else {})
    print(f"Detected Intent: {intent}")

if __name__ == "__main__":
    run_pipeline("data/processed/noisy_call_pranjal.wav", "models/distilbert_finetuned")
