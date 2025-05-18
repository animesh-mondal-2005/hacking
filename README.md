# Notepad Spammer Bot (Educational Tool)

This Python script demonstrates basic keyboard automation using popular libraries such as `keyboard`, `pyautogui`, and `subprocess`. It opens Notepad, writes random gibberish repeatedly, and optionally opens a web browser for demonstration purposes.

> ⚠️ **Disclaimer**: This tool is intended for educational use only. Do not use it to interfere with systems or software without permission. Misuse of automation tools can violate terms of service or local laws.

---

## 🔧 Features

- Opens Notepad and writes random alphanumeric strings.
- Writes to a timestamped file.
- Uses keyboard simulation to type and hit Enter repeatedly.
- Optional automation to open a web browser and simulate search.

---

## 📁 File Description

### `spammer.py`
This is the main script. Here's what it does:

1. **Waits for the SPACE key** to begin.
2. **Creates a text file** with a timestamped name (e.g., `spam_20250518_153012.txt`).
3. **Opens Notepad** and loads the new file.
4. **Types random gibberish** strings into the file every 0.3 seconds using the keyboard.
5. **Continues spamming** until the user presses the ESC key.
6. **Opens YouTube** in a browser (optional, included as a demonstration).
7. **Simulates a search** on YouTube using PyAutoGUI (customizable).

> ⚠️ The typing is fully automated and real keystrokes are sent. Make sure to save work and close other windows before running.

---

## 📦 Requirements

Install the dependencies with:

```bash
pip install keyboard pyautogui
