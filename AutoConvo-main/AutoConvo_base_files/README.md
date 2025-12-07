# AutoConvo: Real-Time Driver Intent Detection

AutoConvo is a lightweight, real-time voice assistant designed for in-vehicle systems. It processes voice commands, classifies driver intent, and responds accordingly with support for multi-turn conversations and offline deployment on Jetson Nano.

## 🚗 Features
- Whisper ASR for speech-to-text
- Fine-tuned DistilBERT for intent classification
- PyDub-based noise injection for realistic audio training
- Multi-turn memory-based conversation
- TensorRT optimization for Jetson Nano deployment

## 📁 Project Structure
- `src/` – Core modules (ASR, intent, context, etc.)
- `models/` – Trained, ONNX, and TensorRT models
- `deploy/` – Export + deployment scripts
- `tests/` – Unit tests
- `data/` – Raw, noise, and processed audio
- `run_demo.py` – Run the full demo locally

## 🔧 How to Run
```bash
pip install -r requirements.txt
python run_demo.py
```
