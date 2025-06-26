import pytesseract
from PIL import Image
import os
import google.generativeai as genai
import google.api_core.exceptions

genai.configure(api_key="GEMINI_APY_KEY_IS_HERE")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    image = Image.open(image_path)  # Open image
    text = pytesseract.image_to_string(image)  # OCR to get text
    return text.strip()

def get_answer_from_gemini(question):
    model = genai.GenerativeModel("models/gemini-1.5-flash-latest")  # Try a less restricted model
    try:
        response = model.generate_content(f"Answer this question:\n{question}")
        return response.text.strip()
    except google.api_core.exceptions.ResourceExhausted as e:
        return (
            "❌ Quota exceeded for Gemini API. "
            "Wait for quota reset, upgrade your plan, or use a different model.\n"
            f"Details: {e}"
        )
    except Exception as e:
        return f"❌ An error occurred: {e}"

if __name__ == "__main__":
    print("Available models:")
    for m in genai.list_models():
        print(m.name)
    image_path = input("📷 Enter image file path (e.g., question.jpg): ")

    print("\n🔍 Extracting text from image...")
    question = extract_text_from_image(image_path)
    print(f"\n📝 Question: {question}")

    print("\n🤖 Thinking...")
    answer = get_answer_from_gemini(question)

    print(f"\n✅ Answer: {answer}")
