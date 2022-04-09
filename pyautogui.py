import pyautogui
import time
pyautogui.hotkey("win")
time.sleep(0.3)
pyautogui.typewrite("https://139-162-198-43.ip.linodeusercontent.com:3000/demos/butcher/index.html", interval=0.02)
time.sleep(0.3)
pyautogui.hotkey("enter")
