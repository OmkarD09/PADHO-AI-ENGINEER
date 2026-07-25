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

class Ticket(BaseModel):
    name: str
    issue: str
    request: str
    email: str
    phone: str
    
schema = Ticket.model_json_schema()

response_format = {
    "type": "json_object"
}

system_prompt = f"""Extract the following information from the text and return it in JSON format according to the schema: {schema}"""

message_system = {
    "role": "system",
    "content": system_prompt
}




text = "Hello, I am Omkar, Yesterday I Bought a new phone from your store,\
        but it is not working properly, I want to return it and get my money back.\
        Please help me with the return process. Email: omkar@example.com phone: 123-456-7890"
       
prompt = f"""This is a customer Ticket, Please extract the following information from the text:{text}"""
message = {
    "role": role,
    "content": prompt
    }

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)


answer = response.choices[0].message.content
print(answer)

#isko padhte kaise hain

import json
raw_json=answer
data_file=json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.issue)
print(ticket.request)
print(ticket.email)
print(ticket.phone)