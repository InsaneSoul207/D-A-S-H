import pyautogui
import time
import subprocess

def launch_application(app_name):
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.typewrite(app_name)
    pyautogui.press('enter') 
    time.sleep(2)  