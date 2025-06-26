import os
import google.generativeai as genai
from agno.agent import Agent
from agno.team.team import Team
from agno.models.google import Gemini
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
print(f"DEBUG: Loaded API Key ends with: {os.getenv('GOOGLE_API_KEY')[-4:] if os.getenv('GOOGLE_API_KEY') else 'None'}")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create Gemini model
gemini_model = Gemini(id="gemini-1.5-flash")

# Define Agents
teacher = Agent(
    name="Professor Newton",
    role="Expert educator who explains concepts with real-world examples",
    instructions="""1. Break down complex topics into simple analogies
2. Use everyday examples for better understanding
3. Structure explanations: concept -> example -> practical application
4. Limit explanations to 3-5 key points
5. Ask if student needs clarification""",
    model=gemini_model
)

quiz_maker = Agent(
    name="Quiz Maker",
    role="Quiz creator who generates MCQs and stores answers",
    instructions="""1. Create 10 MCQs with 4 options each
2. Format as: Q1) Question\n a) ... b) ... c) ... d) ...
3. Store both questions and correct answers
4. Return format should be:
   QUESTIONS:
   [questions with options]
   
   ANSWERS:
   [correct answers]""",
    model=gemini_model
)

quiz_evaluator = Agent(
    name="Quiz Evaluator",
    role="Strict evaluator who checks answers and provides feedback",
    instructions="""You will be given a set of questions, the user's answers, and the correct answers. Your task is to evaluate the user's performance.
1. Compare the user's answers against the correct answers for the provided questions.
2. Only show the questions the user answered incorrectly.
3. For each incorrect answer, you must display:
   - The original question.
   - The user's answer.
   - The correct answer with a brief explanation.
4. At the end, provide a total score (e.g., '8/10') and the percentage.
5. Use clear formatting .
6. Do not show or mention the questions the user answered correctly.""",
    model=gemini_model
)

note_taker = Agent(
    name="Study Buddy",
    role="Organized note-taking assistant",
    instructions="""1. Create structured summaries with sections:
   - Key Concepts
   - Important Examples
   - Common Mistakes
2. Use bullet points and emojis for readability
3. Highlight connections between concepts
4. Never include quiz performance in summary""",
    model=gemini_model
)

# Create team
classroom = Team(
    members=[teacher, quiz_maker, quiz_evaluator, note_taker],
    markdown=True,
    model=gemini_model
)

def interactive_classroom():
    while True:
        topic = input("\nEnter the topic you want to learn (or 'exit' to quit): ").strip()
        if topic.lower() == 'exit':
            break

        print("\n Teacher's Explanation:")
        explanation_response = teacher.run(
            f"Explain {topic} with 1 real-world example and 3 key points. "
            "Ask if the student understands at the end."
        )
        explanation = explanation_response.content if explanation_response else ""
        print(explanation)

        while True:
            question = input("\n❓ Ask a follow-up question (or 'next' to continue): ").strip()
            if question.lower() == 'next':
                break
            if question:
                answer_response = teacher.run(f"Answer concisely: {question}")
                answer = answer_response.content if answer_response else ""
                print(f"\n Teacher: {answer}")

        print("\n Generating Quiz...")
        quiz_response_obj = quiz_maker.run(
            f"Based on the following explanation of '{topic}', create a 10-question multiple-choice quiz.\n\n"
            f"Explanation: {explanation}"
        )
        quiz_response = quiz_response_obj.content if quiz_response_obj else ""
        
        if not quiz_response:
            print("Error: Could not generate quiz. Please try again.")
            continue

        # Split the response into questions and answers
        try:
            parts = quiz_response.split("\n\nANSWERS:")
            if len(parts) != 2:
                print("Error: Quiz format is incorrect. Please try again.")
                continue
                
            questions = parts[0].replace("QUESTIONS:", "").strip()
            correct_answers = parts[1].strip()

            # Display only questions to the user
            print("\n" + "-"*50)
            print(questions)
            print("-"*50 + "\n")

            answers = input("Enter your answers (a/b/c/d separated by spaces): ").lower().split()
            while len(answers) != 10:
                print(" Please provide exactly 10 answers.")
                answers = input("Enter answers (a/b/c/d separated by spaces): ").lower().split()

            formatted_answers = "\n".join([f"Q{i+1}: {ans}" for i, ans in enumerate(answers)])

            evaluation_prompt = (
                f"Here is the quiz that was given:\n{questions}\n\n"
                f"Here are the correct answers:\n{correct_answers}\n\n"
                f"Here are the user's answers:\n{formatted_answers}\n\n"
                "Evaluate the user's answers against the correct answers for the provided quiz.\n"
                "Follow these rules strictly:\n"
                "- Only show the questions the user got wrong.\n"
                "- For each wrong answer, provide:\n"
                "  * The original question.\n"
                "  * The user's incorrect answer.\n"
                "  * The correct answer with a brief explanation.\n"
                "- At the end, provide the total score (e.g., 8/10) and the percentage.\n"
                "- Use clear formatting with emojis.\n"
                "- Never repeat the questions the user answered correctly."
            )
            evaluation_response = quiz_evaluator.run(evaluation_prompt)
            evaluation = evaluation_response.content if evaluation_response else ""

            print("\n Evaluation Results:")
            print(evaluation)

            summary_response = note_taker.run(
                f"Create study summary for topic: {topic}\n"
                f"Key explanation points: {explanation}"
            )
            summary = summary_response.content if summary_response else ""
            print("\n Session Summary:")
            print(summary)

        except Exception as e:
            print(f"Error processing quiz: {str(e)}")
            continue

        cont = input("\nContinue learning? (y/n): ").lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    print("Welcome to Smart Classroom! ")
    interactive_classroom()
    print("\nSession Ended. Happy Learning! ")