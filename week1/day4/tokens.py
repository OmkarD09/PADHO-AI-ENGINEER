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

prompt1 = " hello"
prompt2 = " how are you?"
prompt3 = "Tell me the concept of time travelling in 1000 words"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
        "role": role,
        "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=50,
    )

    usage = response.usage
    finish_reason = response.choices[0].finish_reason if response.choices else "N/A"

    print(
        f"Prompt: {prompt} ---> "
        f"User Tokens: {usage.prompt_tokens} | "
        f"System Tokens: {usage.completion_tokens} | "
        f"Total Tokens: {usage.total_tokens} | "
        f"Finish Reason: {finish_reason}"
    )




