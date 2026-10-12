import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("Open_API_KEY")

if not api_key:
    raise ValueError("Open_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

Ques = {
    "Java": [
        "Who created the Java Programming Language?",
        "What are JVM and JRE in Java?",
        "What is the difference between JDK and JRE?",
        "What are Class and Object in Java?",
        "What is the difference between an Interface and Abstract class in Java?",
        "What is the difference between a constructor and a method in Java?"
    ],

    "Python": [
        "Who created Python?",
        "What are List and Tuple in Python?",
        "What is the syntax for defining a function in Python?",
        "What are Set and Dictionary in Python?",
        "What is the main use of Python?"
    ],

    "JavaScript": [
        "Who created JavaScript?",
        "Why is JavaScript used in Front-End and Back-End Development?",
        "What is the difference between JavaScript and Java?",
        "What is the difference between var, let and const in JavaScript?",
        "What is DOM in JavaScript?"
    ]
}

topic_names = list(Ques.keys())

for i, name in enumerate(topic_names, start=1):
    print(f"{i}. {name}")

try:
    choice = int(input("Choose a topic: 1. Java 2. Python 3. JavaScript: "))
    topic = topic_names[choice - 1]

except (ValueError, IndexError):
    print("Invalid choice")
    raise SystemExit

qa = ""

for q in Ques[topic]:
    print(f"\n{q}")
    user_answer = input("Enter your answer: ")

    qa += f"Q: {q}\nUser's answer: {user_answer}\n\n"

evaluation_prompt = (
    f"You are a programming teacher evaluating a beginner's {topic} answers.\n"
    f"Evaluate every answer separately.\n"
    f"For each question:\n"
    f"1. Display the question.\n"
    f"2. Show the user's answer.\n"
    f"3. Mark it Correct, Partially Correct, or Incorrect.\n"
    f"4. Explain why the answer is correct or incorrect.\n"
    f"5. Provide the correct answer in simple language.\n"
    f"6. Give a final score out of {len(Ques[topic]) * 10}.\n\n"
    f"Here are the questions and answers:\n\n{qa}"
)

try:
    result = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": evaluation_prompt
            }
        ],
        temperature=0.3
    )

    print("\n========== EVALUATION RESULT ==========\n")
    print(result.choices[0].message.content)

except Exception as e:
    print(f"Error while evaluating answers: {e}")