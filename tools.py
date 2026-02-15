import subprocess
import time
import webbrowser
import pyautogui
from langchain.tools import tool

# ── App paths — update these if needed ──────────────────────────────
APPS = {
    "chrome":   "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "notepad":  "notepad.exe",
    "vscode":   "code",
    "explorer": "explorer.exe",
    "calculator": "calc.exe",
}

# ────────────────────────────────────────────────────────────────────

@tool
def open_application(app_name: str) -> str:
    """Opens an application on the PC. Use app names like chrome, notepad, vscode, calculator."""
    name = app_name.lower().strip()
    path = APPS.get(name)

    if path:
        try:
            subprocess.Popen(path)
            time.sleep(2)  # Wait for app to open
            return f"✅ Opened {app_name} successfully."
        except Exception as e:
            return f"❌ Failed to open {app_name}: {str(e)}"
    else:
        return f"❌ App '{app_name}' not found. Available: {', '.join(APPS.keys())}"


@tool
def type_text(text: str) -> str:
    """Types the given text at the current cursor position on screen."""
    try:
        time.sleep(1)  # Small delay so focus is set
        pyautogui.typewrite(text, interval=0.05)
        return f"✅ Typed: '{text}'"
    except Exception as e:
        return f"❌ Failed to type text: {str(e)}"


@tool
def open_url(url: str) -> str:
    """Opens a URL in the default browser. Example: open_url('https://youtube.com')"""
    try:
        if not url.startswith("http"):
            url = "https://" + url
        webbrowser.open(url)
        time.sleep(2)
        return f"✅ Opened URL: {url}"
    except Exception as e:
        return f"❌ Failed to open URL: {str(e)}"


@tool
def press_key(key: str) -> str:
    """Presses a keyboard key or shortcut. Examples: enter, ctrl+t, alt+f4, win"""
    try:
        keys = key.lower().strip().split("+")
        if len(keys) == 1:
            pyautogui.press(keys[0])
        else:
            pyautogui.hotkey(*keys)
        return f"✅ Pressed key: {key}"
    except Exception as e:
        return f"❌ Failed to press key: {str(e)}"


# All tools in one list — import this in agent.py
ALL_TOOLS = [open_application, type_text, open_url, press_key]
