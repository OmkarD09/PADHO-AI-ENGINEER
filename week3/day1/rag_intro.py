import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"




#step 1
knowledge_base={
    "age" : " The age of Omkar is 21 years:",
    "net worth": " The net worth of Omkar is 1.5 million dollars:",
}

#step 2 retrevial
def retrieve_info(question):
    question=question.lower()
    if "age" in question:
        return knowledge_base["age"]
    elif "net worth" in question:
        return knowledge_base["net worth"]
    else:
        return None


def ask_llm(question):
    context=retrieve_info(question)
    if context is None:
        return "I don't have that information in my knowledge base."
    
    sys_prompt=f"""answer in one line only.Answer only based on this context, do not hallucinate. Context : {context}"""
    system_message={
        "role":"system",
        "content":sys_prompt
    }
    user_message={
        "role":"user",
        "content":question
    
    }
    messages=[system_message,user_message]
    response=client.chat.completions.create(model=model,messages=messages, stream=True)
    answer = ""
    for chunk in response:
        answer += chunk.choices[0].delta.content or ""
    return answer

question="how old omkar is?"
answer=ask_llm(question)
print(answer)
