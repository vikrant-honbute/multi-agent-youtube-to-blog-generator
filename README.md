CrewAI Multi-Agent YouTube to Blog Generator

A multi-agent AI system built using CrewAI that automatically researches educational YouTube videos and converts them into well-structured technical blog posts.

This project demonstrates agent collaboration, tool-augmented LLM reasoning, and real-world AI orchestration using Groq-powered language models.

🚀 Project Overview

Instead of using a single AI model, this system uses multiple specialized AI agents, each responsible for a specific task:

A Research Agent searches YouTube videos and extracts key insights

A Writer Agent converts those insights into a clear, readable blog post

CrewAI coordinates the workflow between agents

The final output is generated as a Markdown blog file.

🧠 Key Concepts Demonstrated

Multi-agent AI architecture

Agent role separation (research vs writing)

Tool-augmented LLM workflows

Sequential task orchestration using CrewAI

Real-world challenges like rate limiting and retries

Clean, modular Python project structure

🏗️ Architecture
User Topic
   ↓
Research Agent
   ↓  (YouTube Channel Search Tool)
Extracted Insights
   ↓
Writer Agent
   ↓
Markdown Blog Output

🛠️ Tech Stack

Python

CrewAI

CrewAI Tools

Groq LLMs (via LiteLLM)

YouTube Channel Search Tool

python-dotenv

📂 Project Structure
.
├── agents.py        # Agent definitions (Researcher & Writer)
├── tools.py         # YouTube channel search tool
├── tasks.py         # Task definitions for each agent
├── cre.py           # Crew orchestration and execution
├── outputs/         # Sample generated blog outputs
├── README.md
└── .gitignore

⚙️ How It Works (Step-by-Step)

User provides a topic

CrewAI assigns the topic to the Research Agent

Research Agent uses a YouTube search tool to extract insights

Research output is passed to the Writer Agent

Writer Agent generates a structured blog post

Blog is saved as a Markdown file

▶️ How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/crewai-youtube-blog-generator.git
cd crewai-youtube-blog-generator

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here

5️⃣ Run the project
python cre.py

📄 Example Output

Sample generated blog files are available in:

outputs/sample_blog.md


The output is generated automatically in Markdown format, ready for publishing.

💡 What This Project Demonstrates

Designing AI systems using agent-based architecture

Integrating external tools with LLM reasoning

Managing LLM constraints such as token limits and retries

Building scalable and maintainable GenAI pipelines

Practical use of CrewAI beyond basic demos

📌 Use Cases

Automated blog generation from educational content

Research summarization from video platforms

Content pipelines for technical writers

Demonstration of multi-agent AI systems for interviews

📄 License

MIT License

🙌 Acknowledgements

CrewAI for multi-agent orchestration

Groq for fast LLM inference

3Blue1Brown and similar creators for educational inspiration

✅ Final Notes

This project is designed to showcase real-world AI system design, not just prompt engineering.
It reflects production-style thinking with agent coordination, tooling, and orchestration.
