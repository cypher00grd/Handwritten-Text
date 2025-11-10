# Handwritten-Text Recogniser
The objective of our project is to use Optical Character Recognition (OCR) library to accurately read handwritten registration numbers and total marks obtained and update them in an Excel sheet with a single click. The entire system is implemented as a web-based application for ease of use and accessibility.


Features
📸 Live Camera Capture: Use your Android phone as an IP webcam to take answer sheet snapshots.
📁 Image Upload Option: Supports uploading .jpg images manually.
🧠 Region Detection: Automatically crops:
Roll number (digits)
Roll number (in words)
Total marks
🔍 Handwriting OCR: Uses microsoft/trocr-large-handwritten from HuggingFace for handwritten text recognition.
🎨 Preprocessing Magic: Uses CLAHE, Gaussian blur, and adaptive thresholding to clean up image noise.
🖥 Streamlit UI: Clean, interactive interface for live grading.
🧾 Cropped Output: Saves cropped segments for manual verification if needed.
🛠 Tech Stack
Frontend: Streamlit
OCR Engine: HuggingFace Transformers (TrOCR)
Image Processing: OpenCV, PIL
Others: NumPy, Requests
📦 Installation
Clone the Repository:
git clone https://github.com/your-username/automated-grading-system.git
cd automated-grading-system
