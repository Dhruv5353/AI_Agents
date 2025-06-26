# Smart Classroom

Welcome to Smart Classroom, an interactive and AI-powered learning environment designed to help you master any topic. This application uses a team of specialized AI agents to provide clear explanations, generate quizzes, evaluate your performance, and create concise study notes.

## 🚀 Features

- **Interactive Learning**: Engage with an AI tutor that explains complex concepts in simple terms.
- **Real-World Examples**: Understand topics better with practical, real-world analogies.
- **Follow-Up Questions**: Get instant clarification on any doubts you may have.
- **Automated Quiz Generation**: Test your knowledge with dynamically generated multiple-choice quizzes.
- **Instant Feedback**: Receive immediate evaluation of your quiz performance, with detailed explanations for incorrect answers.
- **Personalized Study Notes**: Get a structured summary of each session, highlighting key concepts, examples, and common mistakes.

## 🛠️ How It Works

Smart Classroom employs a team of four AI agents, each with a specific role:

- **Professor Newton**: The expert educator who breaks down complex topics and provides clear explanations.
- **Quiz Maker**: The quiz creator who generates multiple-choice questions based on the lesson.
- **Quiz Evaluator**: The strict evaluator who grades your quiz, provides your score, and explains any mistakes.
- **Study Buddy**: The organized assistant who creates structured study notes for you to review later.

The application follows a simple, interactive workflow:
1. You enter a topic you want to learn.
2. Professor Newton explains the topic.
3. You can ask follow-up questions.
4. The Quiz Maker generates a 10-question quiz.
5. You take the quiz.
6. The Quiz Evaluator grades your answers and provides feedback.
7. The Study Buddy creates a summary of the key takeaways.

## 📋 Prerequisites

- Python 3.7+
- A Google API key for Gemini

## ⚙️ Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root of the project and add your Google API key:
   ```
   GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
   ```

## ▶️ Usage

To start the interactive classroom, run the `smartclass.py` script from your terminal:

```bash
python smartclass.py
```

You will be welcomed to the Smart Classroom and prompted to enter a topic you want to learn. Follow the on-screen instructions to interact with the AI agents.
