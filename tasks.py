from crewai import Task
from agents import blog_researcher, blog_writer

# Research Task
research_task = Task(
    description=(
        "Search YouTube videos related to the topic {topic} "
        "and extract the main ideas, intuition, and key explanations."
    ),
    expected_output=(
        "A structured research summary with key points and insights."
    ),
    agent=blog_researcher,
)

# Writing Task (THIS is where file output happens)
write_task = Task(
    description=(
        "Using the research summary, write a clear, well-structured "
        "blog post explaining the topic {topic} in simple terms."
    ),
    expected_output=(
        "A complete blog post written in markdown format."
    ),
    agent=blog_writer,
    output_file="final_blog.md"   # ✅ OUTPUT WILL BE SAVED HERE
)
