# 🧠 Research Buddy Agent (Gemini + arXiv API)

## 📚 Project Overview

**Research Buddy Agent** is an AI-powered assistant designed to help **professors**, **PG students**, and **researchers** save time during their research workflow. It takes a user-input domain (like *machine learning*) and:

- Suggests innovative research ideas
- Searches arXiv for the most relevant papers
- Summarizes abstracts of the papers using Google's Gemini API

This tool is part of the **TeachMate AI** suite for smart academic tools.

---

## 🚀 Features

- 💡 Suggests **real research project ideas** based on user input
- 🔍 Searches **relevant papers in real-time** using the arXiv API
- ✍️ Summarizes **abstracts of top papers** using Google's **Gemini Pro** model
- 🧠 Supports latest Gemini models like `gemini-1.5-pro-latest`
- 🖥️ Simple **Command Line Interface (CLI)**

---

## 🔍 How It Works

1. You input a domain like `"computer vision"` or `"quantum computing"`  
2. Gemini suggests **5 innovative research ideas**  
3. Agent fetches **top 3 papers from arXiv** in that domain  
4. Gemini **summarizes each paper's abstract**

---

## 🛠️ Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- A valid **Google Gemini API key**
- Internet connection (for arXiv + Gemini access)

---

### 🔧 Installation

1. **Clone this repository**:
```bash
git clone https://github.com/yourusername/research-buddy-agent.git
cd research-buddy-agent
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
4. **Set up your .env file**:
```bash
Create a .env file in the root directory and paste:

GEMINI_API_KEY=your-gemini-api-key-here
```
---

## ▶️ Running the Agent
```bash
python research_buddy_agent_arxiv.py
```
###
- Enter your research domain (e.g., machine learning, bioinformatics):
It will then:

- Generate 💡 research ideas
- Fetch 📖 top 3 papers from arXiv
- Provide 📝 summarized abstracts using Gemini

---

## 🧪 Example Output

###
Enter your research domain: machine learning

💡 Suggested Research Ideas:
1. Federated Learning for Personalized Healthcare
2. Explainable AI for Climate Change Mitigation
...

📖 Fetching relevant papers from arXiv...

🔹 Title: Lecture Notes: Optimization for Machine Learning

🔗 Link: http://arxiv.org/abs/1909.03550v1

📄 Summary:These lecture notes cover optimization techniques for ML presented at Princeton...

---

## 📂 File Structure
```bash
📁 research-buddy-agent/
│
├── research_buddy_agent_arxiv.py     # Main logic file
├── .env                              # Gemini API key (not uploaded)
├── requirements.txt                  # All dependencies
└── README.md                         # You're reading it!

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
🌐 Convert to Streamlit web app

📄 Export paper summaries to PDF/CSV

🔗 Add citation generation (BibTeX format)

💬 Add chat-based query refinement with Gemini
