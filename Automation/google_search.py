import random
import pyautogui as ui
from speak import speak
import webbrowser
import time
def google_search(text):
  time.sleep(2)
  text = text.replace(" ",  "+")
  web= "https://www.google.com/search?q="+text
  webbrowser.open(web)
