import keyboard
import time
import random
import string
import subprocess
from datetime import datetime
import webbrowser
import pyautogui

def generate_gibberish():
    length = random.randint(8, 16)
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

print("Press SPACE to start spamming. Press ESC to stop.")
keyboard.wait("space")
print("Opening Notepad and starting spam...")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"spam_{timestamp}.txt"

with open(filename, "w") as f:
    pass

subprocess.Popen(["notepad.exe", filename])
time.sleep(2)
 
while True:
    if keyboard.is_pressed("esc"):
        print("Stopped spamming.")
        break
    keyboard.write(generate_gibberish())
    keyboard.send("enter")
    time.sleep(0.3)

print("Opening YouTube...")
webbrowser.open("https://www.youtube.com")
time.sleep(7)

pyautogui.press('/')
time.sleep(0.5)
pyautogui.write("DDos Attack")
pyautogui.press("enter")
time.sleep(5)

pyautogui.moveTo(640, 361)
pyautogui.click()