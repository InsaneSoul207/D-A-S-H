import random
import pyautogui as ui
from speak import speak
import webbrowser
import time
from DLG import yt_search, search_comp
def youtube_search(text):
  
  time.sleep(2)
  web= "https://www.youtube.com/results?search_query="+text
  webbrowser.open(web)
