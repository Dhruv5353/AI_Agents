# 🧠 Image Question Solver Agent

## 📚 Project Overview

**Image Question Solver Agent** is an AI-powered tool designed to help students instantly get answers to complex questions by simply uploading an image. Whether the question includes **handwritten math**, **printed science questions**, or **diagram-based content**, this tool can extract the text using **OCR (Tesseract)** and provide an accurate answer using **Google’s Gemini Pro model**.

This project is part of the TeachMate platform and aims to make academic problem-solving easier for students who face difficulties typing out long or visual questions.

---

## 🚀 Features

- 📷 **Image Upload**: Accepts images of handwritten, printed, or scanned questions (JPG, PNG, etc.)
- 🔎 **OCR Extraction**: Uses Tesseract OCR to extract clean text from image input.
- 🤖 **AI-Powered Answering**: Integrates with Gemini Pro via Google Generative AI to give instant answers.
- 💬 **Natural Language Output**: Answers are presented in an easy-to-understand format with simple explanations.
- ⚡ **CLI-Based Version**: Lightweight command-line interface version for fast testing.

---

## 🔍 How It Works

The agent follows a simple 2-step process:

1. **Text Extraction**:
   - The uploaded image is read using **Tesseract OCR**.
   - The extracted text (the question) is cleaned and passed to the AI model.

2. **Answer Generation**:
   - The cleaned question is sent to **Gemini Pro** via Google Generative AI API.
   - The agent generates a **natural language response** answering the question clearly and accurately.

---

## 🛠️ Setup and Installation

### ✅ Prerequisites
- Python 3.8+
- A valid **Google Gemini API Key**
- Tesseract OCR installed

### 🔧 Steps

1. **Clone the Repository**:
```bash
git clone https://github.com/YourUsername/image-question-solver.git
cd image-question-solver
```
2. **Create a Virtual Environment**:
```bash
python -m venv venv

# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```
3. **Install Required Dependencies**:
```bash
pip install -r requirements.txt
```
4. **Install Tesseract OCR**:
```bash
Download and install from:
👉 https://github.com/tesseract-ocr/tesseract/wiki

Then add this line in your Python file:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```
5. **Set Up Gemini API Key**:
```bash
Create a .env file in the root directory and add the following line:
GEMINI_API_KEY=your-gemini-api-key-here
```
---

## ▶️ Running the Application
```bash
python image_question_solver_gemini.py
```
###
- Enter the image path when prompted (e.g., sample_images/question1.png)
- The agent will extract the question text and return the Gemini-generated answer

---

## 📂 File Structure
```bash
📁 image-question-solver/
│
├── image_question_solver_gemini.py     # Main logic file
├── requirements.txt                    # Python dependencies
├── .env                                # Gemini API key file (excluded from version control)
├── sample_images/                      # Folder containing sample images
└── README.md                           # Project documentation
```
---

## 🤖 Sample Output
```bash
📷 Input Image: question1.png
📝 Extracted Text: "What is the square root of 144?"
✅ Answer: The square root of 144 is 12.
```
---

## 🙋‍♂️ Author
```bash
Dhruv Lokadiya
B.Tech Computer Science | CHARUSAT
AI Intern at Trionic Technologies LLP
```
---

## 💡 Future Enhancements
###
🔢 Integrate Mathpix API for better math recognition

🎤 Add voice input support

🌐 Convert into a Streamlit web app

🧠 Add long-term memory to store previously solved questions

