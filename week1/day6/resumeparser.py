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


hr_requirements = """
JOB TITLE: Full Stack Developer

REQUIRED SKILLS:
- React.js
- JavaScript
- Node.js
- Express.js
- MongoDB
- REST API development
- Git and GitHub

EXPERIENCE:
- Minimum 2 years of relevant web development experience
- Experience building full-stack web applications
- Experience working with frontend and backend integration
- Experience with authentication and authorization

EDUCATION:
- Bachelor's degree in Computer Science, Computer Engineering,
  Information Technology, or related field

PREFERRED SKILLS:
- TypeScript
- Next.js
- Docker
- AWS
- MySQL
- CI/CD
- Tailwind CSS

PROJECT REQUIREMENTS:
- At least 2 relevant full-stack projects
- Experience developing REST APIs
- Experience with database design and integration
- Deployment experience is preferred

ADDITIONAL REQUIREMENTS:
- Understanding of Data Structures and Algorithms
- Understanding of software development practices
- Experience working with Git-based team workflows
- Good problem-solving skills
- Good written and verbal communication skills

SELECTION WEIGHTS:
- Required Skills: 35%
- Relevant Experience: 25%
- Projects: 15%
- Education: 10%
- Preferred Skills: 10%
- Certifications and Achievements: 5%

MINIMUM MATCH SCORE:
- 75% or above: Shortlist
- 60% to 74%: Manual HR Review
- Below 60%: Not Shortlisted
"""

system_prompt = f"""You are a HR manager. match the candidate's resume with the job requirements provided below. Extract the following information from the resume:{hr_requirements}. """

message_system = {
    "role": "system",
    "content": system_prompt
}




text = """
ARJUN MEHTA
Full Stack Developer

Pune, Maharashtra, India
Email: arjun.mehta@example.com
Phone: +91 98765 43210
LinkedIn: linkedin.com/in/arjunmehta
GitHub: github.com/arjunmehta

PROFESSIONAL SUMMARY

Full Stack Developer with 2+ years of experience building scalable web
applications using React.js, Node.js, Express.js, and MongoDB. Experienced
in developing REST APIs, authentication systems, responsive user interfaces,
and cloud-deployed applications.

TECHNICAL SKILLS

Frontend: React.js, JavaScript, HTML5, CSS3, Tailwind CSS, Bootstrap
Backend: Node.js, Express.js, REST APIs
Databases: MongoDB, MySQL
Tools: Git, GitHub, Postman, Docker, VS Code
Cloud: AWS EC2, Vercel
Languages: JavaScript, Java, Python

WORK EXPERIENCE

Full Stack Developer - TechNova Solutions
July 2024 - Present | Pune, India

- Developed web applications using React.js, Node.js, Express.js, and MongoDB.
- Designed REST APIs for authentication, product management, and orders.
- Improved API response time by 30% through database query optimization.
- Implemented JWT authentication and role-based access control.
- Collaborated with a team of five developers using Git and GitHub.
- Deployed backend services on AWS EC2.

Web Development Intern - PixelWorks
January 2024 - June 2024 | Remote

- Built responsive React components for internal applications.
- Integrated frontend applications with REST APIs.
- Fixed UI bugs and improved mobile responsiveness.
- Worked with Git-based development and code review workflows.

PROJECTS

ShopSphere - E-Commerce Platform
Technologies: React.js, Node.js, Express.js, MongoDB, Tailwind CSS

- Developed a full-stack e-commerce application.
- Created REST APIs for users, products, orders, and reviews.
- Implemented an admin dashboard for product and order management.
- Deployed the application using Vercel and cloud infrastructure.

TaskFlow - Project Management Application
Technologies: React.js, Node.js, MongoDB, Docker

- Built a project management system for tasks and team collaboration.
- Implemented JWT authentication and protected API routes.
- Containerized the backend application using Docker.

EDUCATION

Bachelor of Engineering in Computer Engineering
Savitribai Phule Pune University
2020 - 2024
CGPA: 8.4/10

CERTIFICATIONS

- AWS Cloud Practitioner Essentials
- MongoDB Developer Fundamentals
- JavaScript Algorithms and Data Structures

ACHIEVEMENTS

- Won 2nd place in a university-level web development hackathon.
- Solved 300+ programming problems across coding platforms.
- Led a four-member team during a 24-hour software development hackathon.

LANGUAGES

English - Professional Proficiency
Hindi - Professional Proficiency
Marathi - Native
"""
       
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

