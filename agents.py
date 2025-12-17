from crewai import Agent
from crewai.llm import LLM
from tools import yt_tool
from dotenv import load_dotenv
import os

load_dotenv()

# Explicit Groq LLM
groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.2,
    max_tokens=600   
)


blog_researcher = Agent(
    role="YouTube Researcher",
    goal="Find and extract useful information about {topic} from YouTube videos",
    backstory="Expert at understanding educational YouTube content.",
    tools=[yt_tool],
    llm=groq_llm,
    verbose=False,
    memory=False,
    allow_delegation=False
)

blog_writer = Agent(
    role="Technical Blog Writer",
    goal="Write a clear and beginner-friendly blog on {topic}",
    backstory="Skilled at explaining complex topics in simple language.",
    tools=[],
    llm=groq_llm,
    verbose=False,
    memory=False,
    allow_delegation=False
)
