import os
import time
import pyautogui
os.system("Spotify")
time.sleep(5)
pyautogui.keyDown('ctrl')
pyautogui.keyDown('l')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('l')
time.sleep(0.1)  # Adjust the delay as needed

pyautogui.write('Heya',interval=0.1)