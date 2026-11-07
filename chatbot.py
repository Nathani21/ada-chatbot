# Learn to build a local Python AI chatbot in minutes using Ollama. This tutorial demonstrates setting up Ollama and running Llama 3 locally, bypassing subscription fees. The process also includes creating a Python environment and using the Ollama model within a Python script.

# Create a LOCAL Python AI Chatbot In Minutes Using Ollama -  https://www.youtube.com/watch?v=d0o89z134CQ&list=PPSV&t=253s

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.
Here is the conversation history: {context}
Question: {question}
Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the ADA AI ChatBot! Type 'exit' to quit.")
    while True:
        user_input = input("YOU: ")
        if user_input.lower() == 'exit':
            break

        result = chain.invoke({"context": context, "question": user_input})
        print("ADA: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()