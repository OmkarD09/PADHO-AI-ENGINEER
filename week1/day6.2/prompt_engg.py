import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"



def llm_ans(prompt):
    message = {
        "role": "user",
        "content": prompt
        
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    return answer

bad_prompts= """
#ROLE
You are a support assistant at a mobile/laptop company
#TASK
You have to classify the issue in a category
#CONSTRAINTS
You have to classify the issue in one of the following categories:
Techincal, Billing, Return
#OUTPUT FORMAT
Your answer should be in one word only. The one word shoulf be one ot the categories mentioned in the constraints section.
#EXAMPLE
For instance, if the user complaint says he want a refund for his laptop, your answer should be "Return"
#FALLBACK
if you are not sure about the category, you can say "Not Sure" or "Other"
This is a user complaint:
My laptop is not working, i want refund

Classify this
"""
print(llm_ans(bad_prompts))