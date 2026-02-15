Step 1 — Make sure Ollama is running
bashollama serve
Open a new terminal and leave this running in the background.

Step 2 — Install dependencies
bashpip install -r requirements.txt

Step 3 — Run the agent
bashpython agent.py
```

You should see this:
```
🖥️  PC Controller Agent — MVP
========================================
Commands you can try:
  → Open Chrome
  → Open Notepad and type Hello World
  ...
🎤 Your command:

Step 4 — Test in this exact order (simple → complex)
Test #Command to typeExpected result1Open NotepadNotepad opens2Open Notepad and type Hello WorldNotepad opens + types3Open ChromeChrome opens4Open Chrome and go to youtube.comChrome opens YouTube5Press ctrl+sSave dialog appears
Start with Test 1 only. Don't jump to Test 4 until the earlier ones work. This way if something breaks, you know exactly where.

Common errors you might hit:
ModuleNotFoundError: langchain_community
bashpip install langchain-community
Connection refused from Ollama
bash# Make sure ollama serve is running in another terminal
ollama serve
