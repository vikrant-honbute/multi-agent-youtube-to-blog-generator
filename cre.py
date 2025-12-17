from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

tech_crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=False,     # 🔴 DISABLED (important)
    cache=False,      # 🔴 DISABLED
    max_rpm=5        # 🔴 Prevent Groq rate-limit
)

result = tech_crew.kickoff(
    inputs={
        "topic": "How pi was almost 6.283185 (Tau vs Pi) – 3Blue1Brown"
    }
)

print("\n===== FINAL OUTPUT =====\n")
print(result)
