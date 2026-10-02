import os

from google import genai;
from dotenv import load_dotenv
        
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key= api_key )

Ques = {
"Java" : [
        "Who create The Java Programming Language?",
        "What is JVM and JRE in Java?",
        "What is the difference between JDK and JRE?",
        "What is Class And Object in java?",
        "What is The difference between an Interface and Abstract class in Java?",
        "What is the difference between a constructor and a method in Java?"
        ],
"Python" : [
          "Who create Python?",
          "What is List and Tuple in Python?",
          "What is the Syntax of constructing a function in Python?",
          "what is the Set and Dictionary in Python?",
          "what is the main use of Python?"
          ],
"JavaScript" : [
            "Who create JavaScript?",
            "Why JavaScirpt is used in Front-End or Back End Development?",
            "What is the difference between JavaScript and Java?",
            "what is the difference between var, let and const in JavaScript?",
            "what is DOM in JavaScript?"
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
    print(q)
    user_answer = input("Enter your answer: ")
    qa += f"Q: {q}\nUser's answer: {user_answer}\n\n"

evaluation_prompt = (
    f"Check these {topic} answers. For each one, tell if it is right or wrong "
    f"and give the correct answer:\n\n{qa}"
)
result = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=evaluation_prompt,
)
print(result.text)