import pyautogui;
import time;
import random;
while True:
    time.sleep(random.randint(40,180))
    # pyautogui.write('Hello world!')
    pyautogui.moveTo(random.randint(1, 800),120)
    time.sleep(1)
    pyautogui.click()

print(random.randint(1, 800))
