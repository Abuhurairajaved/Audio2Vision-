# 🎵 Audio2Vision

**Audio2Vision** is a multimodal AI project that takes an **audio input**, converts it into **text**, and then generates a **corresponding image** using deep learning models. The project leverages **Whisper** for speech-to-text transcription and **Stable Diffusion** for text-to-image generation.

---

## 🚀 Features
- 🎤 **Audio to Text**: Converts audio input into text using **Whisper**.
- 🖼 **Text to Image**: Generates images from transcribed text using **Stable Diffusion**.
- 🔍 **Self-Supervised Learning**: Fine-tuned to improve **audio-to-image** matching.
- 📊 **Dataset Handling**: Supports the **VGGSound dataset** for multimodal training.
- 🏗 **Modular Codebase**: Clean, reusable, and well-structured for **deployment**.

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Abuhurairajaved/Audio2Vision-
cd Audio2Vision-
```

### 2️⃣ Install Dependencies
Make sure you have Python **3.8+** and install the required packages:
```bash
pip install -r requirements.txt
```

### 3️⃣ Download Dataset
Download **VGGSound** videos and extract audio:
```bash
python download_videos.py  # Downloads videos
python extract_audio.py     # Extracts audio from videos
```

### 4️⃣ Preprocess Data
Prepare the dataset for training:
```bash
python preprocess.py
```

### 5️⃣ Train the Model
Fine-tune the model on your dataset:
```bash
python train.py
```

### 6️⃣ Generate Images
Test the model by generating images from new audio inputs:
```bash
python generate.py --input_audio "path/to/audio.wav"
```

---

## 📂 Project Structure
```
Audio2Vision-
│── dataset.py           # Loads & processes dataset
│── extract_audio.py     # Extracts audio from videos
│── preprocess.py        # Prepares dataset for training
│── train.py             # Trains the AI model
│── generate.py          # Generates images from new audio inputs
│── README.md            # Project documentation
│── requirements.txt     # Python dependencies
└── ...
```

---

## 🖥 Technologies Used
- **Python** 🐍
- **Whisper** 🎤 (for speech-to-text transcription)
- **Stable Diffusion** 🖼 (for text-to-image generation)
- **PyTorch** 🔥 (for deep learning training)
- **Torchaudio** 🎵 (for audio processing)

---

## 🤝 Contributors
- **[Abuhurairajaved](https://github.com/Abuhurairajaved)** (Lead Developer)

🙌 Feel free to contribute and improve the project!

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## ⭐ Show Some Love!
If you found this project useful, **star** ⭐ the repo to support development!
