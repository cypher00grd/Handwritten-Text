# 🧠 Automated Grading System

An intelligent OCR-powered system for automatic evaluation of handwritten answer sheets.  
It leverages **computer vision** and **transformer-based OCR** to detect roll numbers, extract marks, and streamline grading.

---

## 🚀 Features:

- 📸 **Live Camera Capture** — Use your Android phone as an **IP webcam** to capture answer sheet snapshots in real-time.  
- 📁 **Image Upload Option** — Supports manual upload of `.jpg` images.  
- 🧠 **Region Detection** — Automatically crops essential regions:
  - Roll number (digits)
  - Roll number (in words)
  - Total marks  
- 🔍 **Handwriting OCR** — Powered by [`microsoft/trocr-large-handwritten`](https://huggingface.co/microsoft/trocr-large-handwritten) from **Hugging Face** for high-accuracy handwritten text recognition.  
- 🎨 **Preprocessing Magic** — Enhances image quality using:
  - CLAHE (Contrast Limited Adaptive Histogram Equalization)
  - Gaussian Blur
  - Adaptive Thresholding  
- 🖥 **Streamlit UI** — Interactive and clean web interface for live grading and visualization.  
- 🧾 **Cropped Output Storage** — Saves cropped image segments for manual verification if needed.

---

## 🛠 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit |
| **OCR Engine** | Hugging Face Transformers (TrOCR) |
| **Image Processing** | OpenCV, PIL |
| **Others** | NumPy, Requests |

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/automated-grading-system.git
cd automated-grading-system
