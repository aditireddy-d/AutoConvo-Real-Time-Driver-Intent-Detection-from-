# 🚗 AutoConvo — Real-Time Driver Intent Detection System

AutoConvo is a real-time **speech-to-intent understanding** pipeline designed for in-car assistance.  
It fuses **OpenAI Whisper (ASR)** for speech recognition with **DistilBERT** for natural language intent detection —  
optimized for **NVIDIA Jetson Nano** edge deployment using **TensorRT**.

---

## 🎯 Overview

| Component | Description |
|------------|--------------|
| **Whisper ASR** | Transcribes driver’s voice commands to text. |
| **DistilBERT Intent Model** | Classifies transcribed text into 7+ driver intent categories. |
| **Context Tracker** | Maintains conversation history and previous intents. |
| **TensorRT Optimization** | Speeds up inference by 2.5× for real-time edge operation. |

---

## 🧩 Architecture Flow

```
🎙️ Voice Input (.wav)
     ↓
Whisper ASR → Text
     ↓
DistilBERT → Intent Classification
     ↓
Context Tracker → Dialogue Handling
     ↓
🚘 Action / Response Generation
```

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **PyTorch**, **Transformers (Hugging Face)**
- **OpenAI Whisper**
- **ONNX Runtime**, **TensorRT**
- **CUDA 12+ / Jetson Nano**
- **FastAPI (optional)** for serving the pipeline

---

## 📂 Repository Structure

```
AUTOConvo/
│
├── AutoConvo_src_files/             # Main source code modules
│   ├── asr_whisper.py               # Whisper ASR transcription
│   ├── context_tracker.py           # Context & dialogue handling
│   ├── inference_pipeline.py        # End-to-end inference entrypoint
│   ├── intent_model.py              # DistilBERT intent classifier
│   ├── mic_recording.py             # Real-time audio capture
│   ├── preprocess_audio.py          # Noise cleaning + formatting
│   └── utils.py                     # Helper functions & logging
│
├── models/
│   ├── distilbert_finetuned/        # Fine-tuned intent classifier
│   │   ├── config.json
│   │   └── pytorch_model.bin
│   ├── onnx/                        # Intermediate ONNX export
│   │   └── intent_model.onnx
│   ├── tensorrt/                    # TensorRT optimized engine
│   │   └── intent_model.trt
│   └── whisper/                     # Whisper ASR weights
│       └── whisper_model.bin
│
├── Noise/                           # Realistic background test audio
│   ├── traffic.wav
│   ├── car-engine.wav
│   ├── passengers.wav
│   └── rain-inside-car.wav
│
├── tests/                           # Unit & module tests
│   ├── test_asr.py
│   ├── test_context.py
│   └── test_intent_model.py
│
├── requirements.txt                 # Python dependencies
└── README.md                        # Project overview (this file)
```

---

## 🚀 Quick Start

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the end-to-end pipeline
```bash
python AutoConvo_src_files/inference_pipeline.py --audio Noise/traffic.wav
```

### 3️⃣ Example Output
```
[ASR] "navigate to home"
[INTENT] → navigate_home
[CONTEXT] Added to session memory
[RESPONSE] Starting navigation to home.
[INFO] End-to-end latency: 392.8 ms
```

---

## ⚡ Model Performance

| Model | Type | Size | Latency | Accuracy |
|--------|------|------|----------|-----------|
| DistilBERT | PyTorch | 324 MB | 950 ms | 91.7% |
| DistilBERT | ONNX | 65 MB | 620 ms | 91.7% |
| DistilBERT | TensorRT (FP16) | 45 MB | **~385 ms** | 91.4% |

> Optimized with TensorRT for Jetson Nano inference.

---

## 🧠 Supported Intents
```
play next song
navigate to home
increase volume
call contact
open maps
turn off ac
show nearest gas station
```
---

## 🧪 Example Tests
```bash
pytest tests/test_asr.py
pytest tests/test_intent_model.py
```

---

## 🧰 Future Enhancements
- Multi-intent understanding (e.g., “Play music and call contact”)
- Emotion-aware dialogue system
- Multilingual command recognition (Whisper Large V3)
- FastAPI or gRPC service deployment

---

## 👨‍💻 Author
**Atharva Patil**  
M.S. Data Science @ RIT  
Building intelligent, edge-deployable AI systems for multimodal and autonomous understanding.

[LinkedIn](https://www.linkedin.com/in/atharva-patil-420660200/)  
[GitHub](https://github.com/atharvapatil24)
