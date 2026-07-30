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
role = "user"

from pydantic import BaseModel

class JobDescription(BaseModel):
    role: str
    required_skills: list[str]
    preffered_skills: list[str]
    minimum_experience: float|None
    educational_requirement: str
    responsibilities: list[str]
    
    jobd_schema = JobDescription.model_json_schema()




system_prompt = f"""You are a HR manager. match the candidate's resume with the job requirements provided below. Extract the following information from the resume:{hr_requirements}. """

message_system = {
    "role": "system",
    "content": system_prompt
}


       
prompt = f"""This is a customer Ticket, Please extract the following information from the text:{text}"""
message = {
    "role": role,
    "content": prompt
    }

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages)


answer = response.choices[0].message.content
print(answer)

#isko padhte kaise hain

