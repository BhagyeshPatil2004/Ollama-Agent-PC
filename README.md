# 🖥️ Local AI PC Controller Agent

> Control your PC with natural language commands — fully local, no cloud, no API costs.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black?style=flat-square)
![LangChain](https://img.shields.io/badge/LangChain-Agent-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-MVP-orange?style=flat-square)

---

## 💡 What is this?

A local AI agent that listens to your text commands and autonomously controls your PC — opening apps, navigating browsers, typing text, pressing shortcuts, and more.

**No OpenAI. No Gemini. No internet required. Everything runs on your machine.**

```
You:    "Open Chrome and go to youtube.com"
Agent:  ✅ Opened Chrome
        ✅ Opened URL: https://youtube.com
```

---

## ✨ Features

- 🧠 **Fully Local** — powered by Ollama + Gemma 2 (or any local LLM)
- 🖱️ **App Control** — open any installed application
- ⌨️ **Text Automation** — type anything at cursor position
- 🌐 **Browser Navigation** — open URLs instantly
- ⌨️ **Keyboard Shortcuts** — press any key or combo (ctrl+s, alt+f4, etc.)
- 🔗 **Multi-step Commands** — chain actions in one sentence
- 🔒 **100% Private** — nothing leaves your machine

---

## 🗂️ Project Structure

```
pc-controller/
│
├── agent.py          ← main file — run this
├── tools.py          ← PC actions (open app, type, navigate)
└── requirements.txt  ← dependencies
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/BhagyeshPatil2004/pc-controller-agent.git
cd pc-controller-agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Ollama & pull your model
```bash
# Install Ollama from https://ollama.com
ollama pull gemma2
```

### 4. Run the agent
```bash
# Terminal 1 — start Ollama
ollama serve

# Terminal 2 — run the agent
python agent.py
```

---

## 🎮 Usage

Once running, just type your command:

```
🎤 Your command: Open Notepad
🎤 Your command: Open Notepad and type Hello World
🎤 Your command: Open Chrome and go to youtube.com
🎤 Your command: Press ctrl+s
🎤 Your command: Open Calculator
```

Type `quit` to exit.

---

## 🛠️ Supported Commands

| Action | Example |
|--------|---------|
| Open app | `Open Chrome` / `Open Notepad` / `Open VS Code` |
| Type text | `Type Hello World` |
| Open URL | `Go to github.com` |
| Press key | `Press ctrl+s` / `Press alt+f4` |
| Multi-step | `Open Notepad and type my name is Bhagyesh` |

---

## ⚙️ Configuration

To add more apps, edit the `APPS` dictionary in `tools.py`:

```python
APPS = {
    "chrome":      "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "notepad":     "notepad.exe",
    "vscode":      "code",
    "spotify":     "C:/Users/YourName/AppData/Roaming/Spotify/Spotify.exe",  # add yours
    "calculator":  "calc.exe",
}
```

To switch LLM models, edit `agent.py`:
```python
llm = Ollama(model="gemma2")   # or llama3, mistral, phi3
```

---

## 📦 Requirements

- Python 3.10+
- [Ollama](https://ollama.com) installed
- Gemma 2 (or any Ollama-supported model)
- Windows OS (Mac support coming soon)
- ~8GB RAM recommended

---

## 🗺️ Roadmap

- [x] MVP — open apps, type text, open URLs
- [ ] Screenshot feedback loop (self-healing agent)
- [ ] Voice input via Whisper
- [ ] Mac & Linux support
- [ ] Browser automation via Playwright
- [ ] Benchmark: compare Gemma 2 vs LLaMA 3 vs Mistral

---

## 🔬 Research

This project is part of a final year B.Tech research paper exploring:

> *"How do local LLMs compare in accuracy and efficiency for multi-step PC automation tasks, and how does visual feedback improve task completion rates?"*

Benchmark results and paper coming soon.

---

## 🙋 Author

**Bhagyesh Patil**
- GitHub: [@BhagyeshPatil2004](https://github.com/BhagyeshPatil2004)
- LinkedIn: [bhagyeshpatil2004](https://linkedin.com/in/bhagyeshpatil2004/)

---

## 📄 License

Free to use, modify, and distribute.

---

> ⭐ If this project helped you, consider giving it a star!
