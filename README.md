# TaskPilot

**A simple tool-using AI agent that understands user instructions, plans tasks, and executes actions using available tools.**

TaskPilot is an experimental AI agent built with Python and the Groq API. It follows a structured reasoning workflow to understand user queries, decide what needs to be done, interact with tools, and return results.

## 🧠 How It Works

TaskPilot follows a five-step workflow:

1. **Start** – Understand the user's request.
2. **Plan** – Break the task into smaller steps.
3. **Action** – Select and execute the appropriate tool.
4. **Observe** – Analyze the tool's execution result.
5. **Output** – Return the final result to the user.

## 🛠️ Tech Stack

- Python
- Groq API
- Large Language Models (LLMs)

## 📁 Project Structure

```text
TaskPilot/
│
├── main.py
├── system-prompt.txt
├── .env
└── README.md
```

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd TaskPilot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install groq python-dotenv
```

### 4. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the project

```bash
python main.py
```

## 🔧 Available Tools

| Tool | Description |
|---|---|
| `run_command` | Executes a system command and returns its output. |

## 🎯 Project Goals

- [x] Define the agent's reasoning workflow.
- [x] Create an external system prompt.
- [ ] Integrate Groq API.
- [ ] Implement JSON response parsing.
- [ ] Build a tool execution mechanism.
- [ ] Implement the Start → Plan → Action → Observe → Output loop.
- [ ] Add filesystem tools.
- [ ] Add file reading and editing capabilities.
- [ ] Improve error handling and execution safety.

## 📌 Vision

The goal is to gradually evolve TaskPilot from a basic tool-using AI agent into a capable coding agent that can understand projects, work with files, execute commands, and help developers accomplish real-world tasks.

**Built as a learning project to explore AI agents, LLMs, and tool orchestration.**