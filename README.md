# 🧠🎥 Multi-Agent YouTube → Blog Generator (CrewAI + Groq)

A **multi-agent AI system** built with **CrewAI** that researches educational YouTube content and automatically generates a **beginner-friendly technical blog** using a **Groq-powered LLM**.

The system uses **two specialized agents** working sequentially:
1. A **YouTube Researcher** agent that extracts insights from a specific YouTube channel.
2. A **Technical Blog Writer** agent that converts the research into a clean, structured Markdown blog.

---

## 🚀 What This Project Does

- Takes a **topic** as input  
- Searches **YouTube videos** from a specific channel (e.g. *3Blue1Brown*)  
- Extracts **key ideas, intuition, and explanations**  
- Writes a **complete technical blog post**  
- Saves the final output as a **Markdown file**

---

## 🤖 Agent Architecture

| Agent | Role | Responsibility |
|------|-----|---------------|
| **YouTube Researcher** | Research Agent | Finds and extracts insights from YouTube videos |
| **Technical Blog Writer** | Writing Agent | Writes a beginner-friendly blog from the research |

Agents run **sequentially** using CrewAI’s workflow engine.

---

## 🧩 Core Components

### 🧠 LLM
- **Provider:** Groq  
- **Model:** `llama-3.1-8b-instant`  
- **Temperature:** 0.2  
- **Max Tokens:** 600  

### 🛠 Tool
- **YoutubeChannelSearchTool**  
- Restricted to a **specific YouTube channel**  
  - Example used: `https://www.youtube.com/@3blue1brown`

### 🧱 Frameworks & Libraries
- CrewAI  
- Groq LLM  
- crewai-tools  
- python-dotenv  

---

## 📁 Project Structure

## 📁 Project Structure

```text

├── agents.py       # Defines the AI agents (Researcher & Writer)
├── tasks.py        # Defines research and writing tasks
├── tools.py        # YouTube channel search tool
├── cre.py          # Crew setup and execution
├── final_blog.md   # Generated blog output (created at runtime)
└── .env            # Environment variables (Groq API key)
```


---

## 🧠 Agent Definitions

### 🔍 YouTube Researcher Agent
- Searches YouTube videos related to the topic  
- Extracts:
  - Main ideas  
  - Intuition  
  - Key explanations  
- Uses a **YouTube search tool**  
- No memory, no delegation (fully controlled)

### ✍️ Technical Blog Writer Agent
- Converts research into a **clear, simple blog**  
- Output format: **Markdown**  
- Saves output to `final_blog.md`

---

## 📝 Tasks Workflow

### 1️⃣ Research Task
- Input: `{topic}`  
- Output: Structured research summary  
- Agent: **YouTube Researcher**

### 2️⃣ Writing Task
- Input: Research summary  
- Output: Full blog post in Markdown  
- Agent: **Technical Blog Writer**  
- File Output: `final_blog.md`

---

## ⚙️ Execution Flow

The crew runs in **sequential mode**:

YouTube Researcher → Technical Blog Writer → Markdown Blog File


Crew configuration:
- Memory: ❌ Disabled  
- Cache: ❌ Disabled  
- Max RPM: 5 (prevents Groq rate limits)

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install crewai crewai-tools python-dotenv
```

### 2️⃣ Set up environment variables
Create a `.env` file in the root directory:

```ini
GROQ_API_KEY=your_groq_api_key_here
```

### 3️⃣ Run the crew
```bash
python cre.py
```

---

## 📄 Output

The final blog is saved as:

`final_blog.md`

Console output also displays the generated content.

---

## 💡 Example Topic Used

**Topic:** How pi was almost 6.283185 (Tau vs Pi) – 3Blue1Brown

---

## 🔮 Future Improvements (Optional)

- [ ] Support multiple YouTube channels
- [ ] Add web article research alongside YouTube
- [ ] Enable agent memory for long research chains
- [ ] Add CLI or web UI (Streamlit / FastAPI)
- [ ] Allow user-defined output formats (HTML / PDF)

---

## 📝 License

**MIT License**

Free to use, modify, and distribute.

---

## 🙌 Credits

- **CrewAI** for agent orchestration
- **Groq** for ultra-fast LLM inference
- **3Blue1Brown** for high-quality educational content

