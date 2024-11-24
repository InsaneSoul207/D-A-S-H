import speech_recognition as sr
from mtranslate import translate 
from colorama import Fore, Style, init 

def Trans_hindi_to_english (txt):
    english_txt= translate(txt, to_language= "en-us")
    return english_txt 

def takecommand():
    recognizer = sr. Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source,0,8)  
        rec_txt =recognizer.recognize_google(audio).lower()
        if rec_txt:
            trans_txt = Trans_hindi_to_english(rec_txt)
            print("\r"+ Fore.LIGHTBLUE_EX + "User : "+ trans_txt)
            return trans_txt
        else:
            return ""  
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en')
        print(f"User said: {query} ")
    except Exception as e:
        print("Say that again please...\n")

        return "None"
    return query