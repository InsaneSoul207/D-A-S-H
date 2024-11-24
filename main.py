from speak import *
from Listen.Listen import takecommand
from Automation.yt_playback import *
import DLG
import time
from Automation.youtube_search import youtube_search
import random
import os
import cv2
from Automation.launch import  *
from config import  *
from Automation.mail import mail
from Automation.message import messages
from Automation.google_search import google_search
from Automation.play_music import play_music_on_youtube
from BATTERY_AUTOMATION.battery_perc import *
import pyjokes
from bs4 import BeautifulSoup
from Automation.weather import fetch_weather
from  Automation.news import *
from PyQt5 import QtWidgets, QtCore, QtGui
import wolframalpha
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Automation.ppt import  *
from PyQt5.uic import loadUiType
import io
from gui import Ui_MainWindow
import datetime
from Automation.set_alarm import set_alarm
import csv
from config import *
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
CONTACTS={"Your contact data here."}
###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

def query_img(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def generate_code(query):
    genai.configure(api_key="AIzaSyAOR0bY6gixmV9iflLV6LkMnwExx4M2B1c")
    model = genai.GenerativeModel("gemini-1.5-flash-8b")
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Hello! I am Alpha. I can surely not harm humans. HaHa. I am developed by Eshaan Mishra, the main function of Alpha is to make learning and education easier and more convenient for students. My purpose is to simplify your learning journey by providing personalized assistance, innovative teaching methods, and tailored resources to meet your unique needs. I am here to make your educational experience more enjoyable and effective. Feel free to ask me any questions or let me know how I can assist you in your learning adventure! and also in many more things from your life."},
        ]
    )
    response1 = chat.send_message(f"Write just the code for the following task:\n{query} (i want nothing extra than the code)")
    return response1.text

app_id = wolframalpha_id

def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        data = "Sorry sir I couldn't fetch your question's answer. Please try again "
        return data 

def chat_generation(user_input):
    response = generate_response(user_input)
    return response

def chat_interaction(user_input):
    with open("Data//all_responses.txt", "a", encoding="utf-8") as file:
        while True:
            if user_input == 'exit' or user_input == 'quit':
                break
            else:
                response = chat_generation(user_input)
                file.write(f"User Input: {user_input}\n")
                file.write(f"Response: {response}\n\n")  
                file.flush() 
                return response
            
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        self.known_faces = []
        self.known_face_names = []
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    def load_known_faces(self, path):
        for file in os.listdir(path):
            img = cv2.imread(os.path.join(path, file))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            if len(faces) > 0:
                self.known_faces.append(gray)
                self.known_face_names.append(os.path.splitext(file)[0])

    def recognize_face(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        if len(faces) > 0:
            x, y, w, h = faces[0]
            face_region = gray[y:y+h, x:x+w]

            for i, known_face in enumerate(self.known_faces):
                if self.compare_faces(face_region, known_face):
                    return self.known_face_names[i]
        return "Unknown"
    
    def compare_faces(self, face1, face2):
        hist1 = cv2.calcHist([face1], [0], None, [256], [0, 256])
        hist2 = cv2.calcHist([face2], [0], None, [256], [0, 256])
        return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL) > 0.7

    def register(self, username, camera_index=0):
        cap = cv2.VideoCapture(camera_index)
        for i in range(10):
            ret, frame = cap.read()
        ret, frame = cap.read()
        if not ret:
            return False

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        
        if len(faces) > 0:
            x, y, w, h = faces[0]
            face_region = gray[y:y+h, x:x+w]
            self.known_faces.append(face_region)
            self.known_face_names.append(username)
            cv2.imwrite(f"faces/{username}.jpg", face_region)
            cap.release()
            cv2.destroyAllWindows()
            return True
        return False

    def login(self,email_id ,camera_index=0):
        cap = cv2.VideoCapture(camera_index)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            name = self.recognize_face(frame)
            cv2.imshow('Face Recognition Login', frame)
            cv2.putText(frame, f"Recognized: {name}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            if name != "Unknown":
                print("<-------ACCESS GRANTED------->")
                current_datetime = datetime.datetime.now()
                if not os.path.exists("logindata.csv"):
                    with open("logindata.csv", 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(["Email", "Login_Time"])
                with open('logindata.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([email_id.lower(), current_datetime])
                self.TaskExecution()
                break
            elif name == "Unknown":
                print("<-------UNAUTORISED ACCESS------->")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def FaceRec(self):
        print("")
        print("Welcome to Face Recognition Login!")
        choice = input("Do you want to login or register? (login/register): ")

        if choice.lower() == "login":
            self.load_known_faces("faces")
            LoginMail = input("Enter your Email-ID: ")
            
            with open("users.csv", 'r') as file:
                reader = csv.reader(file)
                users = list(reader)
                try:
                    for user in users:
                        if user[0] == LoginMail.lower():
                            self.login(LoginMail)
                    else:
                        print("User not found. Please register first.")
                        print("")
                        self.FaceRec()
                except Exception as e:
                    print(e)
                    print("No User Found.")
                    self.FaceRec()

        elif choice.lower() == "register":
            username = input("Enter your username: ")
            RegMail = input("Enter your Email-ID: ")
            current_datetime = datetime.datetime.now()
            if not os.path.exists("users.csv"):
                with open("users.csv", 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Email", "RegesDate","Username"])
            with open("users.csv", 'r') as file:
                reader = csv.reader(file)
                users = list(reader)
                if RegMail.lower() in [user[0] for user in users]:
                    print("Email-ID already exists. Please try another one.")
                    print("")
                    self.FaceRec()
                else:
                    with open("users.csv", 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([RegMail.lower(), current_datetime ,username])
                    self.register(username)
                    print("Registration Successful!")
                    print("")
                    self.FaceRec()
        else:
            print("Invalid choice. Please try again.")
            self.FaceRec()

    def wakeup(self):
        while True:
            query = takecommand().lower()
            print("")
            if 'wake up' in query or 'hello' in query or 'wakeup' in query or 'alpha' in query:
                self.TaskExecution()
            else:
                pass

    def run(self):
        self.FaceRec()


    def TaskExecution(self):
        battery = battery_perc() + " and " + battery_status()
        speak(battery)
        dlg = random.choice(DLG.opening_dialogues)
        speak(dlg)
        while True:
            query = takecommand().lower()
            print("")
            if query == "None":
                data = "None"
                pass
            elif query == None:
                data = "None"
                pass
            else:
                if "exit" in query or "bye" in query or "sleep" in query or "quit" in query:
                    speak(random.choice(DLG.goodbye_dialogues))
                    self.wakeup()
                elif "play" in query or "sing" in query:
                    query = query.replace("play","")
                    query = query.replace("sing","")
                    playdlg = random.choice(DLG.play_song)
                    speak(playdlg)
                    play_music_on_youtube(query)
                    time.sleep(3)
                    speak(f"Playing {query} on YouTube")
                elif "volume up" in query:
                    volume_up()
                elif "volume down" in query:
                    volume_down()
                elif "seek forward" in query:
                    seek_forward()
                elif "seek backward" in query:
                    seek_backward()
                elif "seek forward 10 seconds" in query:
                    seek_forward_10s()
                elif "seek backward 10 seconds" in query:
                    seek_backward_10s()
                elif "seek backward frame" in query:
                    seek_backward_frame()
                elif "seek forward frame" in query:
                    seek_forward_frame()
                elif "seek to beginning" in query:
                    seek_to_beginning()
                elif "seek to end" in query:
                    seek_to_end()
                elif "seek to previous chapter" in query:
                    seek_to_previous_chapter()
                elif "seek to next chapter" in query:
                    seek_to_next_chapter()
                elif "decrease playback speed" in query:
                    decrease_playback_speed()
                elif "increase playback speed" in query:
                    increase_playback_speed()
                elif "move to next video" in query:
                    move_to_next_video()
                elif "move to previous video" in query:
                    move_to_previous_video()
                elif "search youtube" in query:
                    query=query.replace("alpha","")
                    query=query.replace("youtube","")
                    query=query.replace("search","")
                    query=query.replace("for","")
                    dlg = random.choice(DLG.yt_search)
                    speak(dlg)
                    youtube_search(query)
                    s12 = random.choice(DLG.search_comp)
                    speak(s12)
                elif  "search" in query and "google" in query:
                    query=query.replace("alpha","")
                    query=query.replace("google","")
                    query=query.replace("search","")
                    dlg = random.choice(DLG.google_search_responses)
                    speak(dlg)
                    google_search(query)
                    s12 = random.choice(DLG.search_comp_ggl)
                    speak(s12)
                elif "battery" in query:
                    battery = battery_perc() + " and " + battery_status()
                    speak(battery)
                elif  "time" in query:
                    speak("The current time is " + time.strftime("%H:%M:%S"))
                elif "date" in query:
                    speak("The current date is " + time.strftime("%d/%m/%Y"))
                elif "who are you" in query:
                    speak("I am Alpha, your personal assistant.")
                elif "what can you do" in query:
                    speak("I can do a variety of tasks, including but not limited to:")
                    speak("playing music, videos")
                    speak("sending messages")
                    speak("searching the internet")
                    speak("telling jokes and news")
                    speak("And Automating your daily tasks.")
                elif "joke" in query:
                    speak(random.choice(pyjokes.get_jokes()))
                elif "buzzing" in query or "news" in query or "headlines" in query:
                    Co_speak("Which type of news do you want? (e.g., sports, technology): ")
                    category = input("Which type of news do you want? (e.g., sports, technology): ").strip().lower()
                    latestNews(category)
                    data = 'These were the top headlines, Have a nice day Sir!!..'
                elif "goodbye" in query:
                    speak("Goodbye, it was nice talking to you.")
                elif "shutdown" in query:
                    speak("Shutting down")
                    os.system("shutdown /s /t 1")
                elif "help" in query:
                    speak("I can do a variety of tasks, including but not limited to:")
                    speak("playing music, videos")
                    speak("sending messages")
                    speak("searching the internet")
                    speak("telling jokes and news")
                    speak("And Automating your daily tasks.")
                elif "switch window" in query:
                    pyautogui.keyDown('alt')
                    pyautogui.press('tab')
                    pyautogui.keyUp('alt')
                elif "volume up" in query:
                    pyautogui.press('volumeup')
                elif "volume down" in query:
                    pyautogui.press('volumedown')
                elif "volume mute" in query:
                    pyautogui.press('volumemute')
                elif  "take a screenshot" in query:
                    speak("Taking a screenshot")
                    speak("what name should i save it with?")
                    name = input("Enter name: ")
                    pyautogui.screenshot(name + ".png")
                    speak(f"Screenshot saved as {name}.png")
                
                elif "take a photo" in query and "click" not in query:
                    speak("Taking a photo")
                    camera = cv2.VideoCapture(0)
                    speak("what name should i save it with?")
                    name = input("Enter name: ")
                    ret, frame = camera.read()
                    cv2.imwrite(name + ".jpg", frame)
                    camera.release()
                    cv2.destroyAllWindows()
                    speak(f"Photo saved as {name}.jpg")
                elif "take a photo" and "click" in query:
                    while True:
                        click_check= takecommand().lower()
                        if click_check == "click":
                            speak("Say cheese")
                            camera = cv2.VideoCapture(0)
                            speak("what name should i save it with?") 
                            name = input("Enter name: ")
                            ret, frame = camera.read()
                            cv2.imwrite(name + ".jpg", frame)
                            camera.release()
                            cv2.destroyAllWindows()
                            speak(f"Photo saved as {name}.jpg")
                            break
                elif "open" in  query:
                    query = query.replace("open", "")
                    query = query.replace("alpha", "")
                    speak(f"Openning {query}")
                    pyautogui.press("win")
                    time.sleep(1)
                    pyautogui.typewrite(query)
                    time.sleep(1)
                    pyautogui.press("enter")
                elif "close" in query:
                    query = query.replace("alpha", "")
                    query = query.replace("close", "")  
                    speak(f"Closing {query}")
                    pyautogui.press("win")
                    time.sleep(1)
                    pyautogui.typewrite(query)
                    time.sleep(1)
                    pyautogui.press("enter")
                    time.sleep(1)
                    pyautogui.keyDown("alt")     
                    pyautogui.press("f4")
                    pyautogui.keyUp("alt")
                elif "email" in query or "send email" in query:
                    sender_email = email
                    sender_password = email_password
                    try:
                        speak("Please enter the email ID sir ?")
                        receiver_email = input("Enter Email ID: ")
                        if "@gmail.com" in receiver_email:
                            print("")
                            speak("What is the subject sir ?")
                            subject = input("Enter Subject: ")
                            print("")
                            speak("What should I say?")
                            message = input("Enter Message: ")
                            print("")
                            msg = 'Subject: {}\n\n{}'.format(subject, message)
                            mail(sender_email, sender_password,receiver_email, msg)
                            speak("Email has been successfully sent")
                            time.sleep(2)
                            data = "Email has been successfully sent"
                        else:
                            speak("please enter a valid email id")
                            data = "I coudn't find the requested person's email in my database. Please try again with a different name"
                    except:
                        speak("Sorry sir. Couldn't send your mail. Please try again")
                        data = "Sorry sir. Couldn't send your mail. Please try again"
                elif "message" in query:
                    query1 = query.replace("message","")
                    query1 = query1.replace("to","")
                    query1 = query1.replace(" a ","")
                    query1 = query1.replace(" ","")
                    query1 = query1.replace("whatsapp","")
                    query1 = query1.replace("Alpha","")
                    query1 = query1.replace("send","")
                    name = query1
                    b = CONTACTS.keys()
                    if name in b:
                        num= CONTACTS[name]
                        speak(f"What's the message for {name}")
                        mess=input("Enter Query: ")
                        messages(num,mess)
                        speak("i have sent the message")
                    else:
                        speak(f"there is no one in the CONTACTS with name {name}")
                    data="sent message"

                elif "temperature" in query:
                    search = "temperature"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_="BNeawe").text
                    speak(f"current {search} is {temp}")
                    data = temp
                elif "weather" in query:
                    city = query.split(' ')[-1]
                    weather_res = fetch_weather(city=city)
                    speak(weather_res)
                    data = weather_res
                elif "image" in query and "generate" in query:
                    try:
                        speak("i will display the image as soon as it is generated.")
                        image_input = query.replace("alpha","")
                        image_input = query.replace("generate","")
                        image_input = query.replace("image","")

                        image_bytes = query_img({"inputs": f"{image_input}", })
                        import io
                        from PIL import Image
                        image = Image.open(io.BytesIO(image_bytes))
                        image.show()
                        data = "generated image"
                    except Exception as e:
                        speak("some error ocurred while generating the image")
                        data = "error"
                elif "set" in query and "alarm" in query:
                    speak(random.choice(DLG.alarm_dialogues))
                    x = input("Enter the time in 24 hr format: For example(13:05)")
                    set_alarm(x)
                    speak(random.choice(DLG.reminder_dialogues))
                elif "ppt" in query and "create" in query:
                    try:
                        query= query.replace("Alpha","")
                        text = generate_response(f"""{query}
                                    in the following format:
                                    this should be a python list of tupples where each tupple is in the format:(slide_number, title, content)
                                    i dont want a single letter more than this
                                    """)
                        text = text.replace("python","")
                        text = text.replace("`","")
                        text = ast.literal_eval(text)           
                        presentation = create_presentation(text)
                        speak("What name should i save it with?")
                        ppt = input("Enter: ")
                        presentation.save(f"{ppt}.pptx")
                    except Exception as e:
                        speak("some error ocurred while creating the ppt")
                        
                elif ("generate" and "code" in query) or "write a programme" in query:
                    prompt = query.replace("generate code", "").strip()
                    code = generate_code(prompt)
                    speak("Here is the generated code.")
                    code = code.replace("python","")
                    code = code.replace("java", "")
                    code = code.replace("c++", "")
                    code = code.replace("c#", "")
                    code = code.replace("javascript", "")
                    code = code.replace("swift", "")
                    code = code.replace("ruby", "")
                    code = code.replace("php", "")
                    code = code.replace("go", "")
                    code = code.replace("kotlin", "")
                    code = code.replace("rust", "")
                    code = code.replace("sql", "")
                    code = code.replace("html", "")
                    code = code.replace("css", "")
                    code = code.replace("json", "")
                    code = code.replace("xml", "")
                    code = code.replace("yaml", "")
                    code = code.replace("yml", "")
                    code = code.replace("markdown", "")
                    code = code.replace("`","")         
                    print(f"Alpha : {code}")
                elif "calculate" in query:
                    speak("what do you want to calculate")
                    question = input("Enter Query: ").lower()
                    answer = computational_intelligence(question)
                    speak(answer)
                    data = answer
                elif "temperature" in query:
                    search = "temperature"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_="BNeawe").text
                    speak(f"current {search} is {temp}")
                    data = temp
                elif " ip " in query and " my " in query:
                    ip = requests.get('https://api.ipify.org').text
                    speak(f"Your ip address is {ip}")
                    data = f"Your ip address is {ip}"
                elif "essay" in query or "passage" in query or "paragraph" in query:
                    response = chat_interaction(query)
                    speak("Here is a passage for you.")
                    print(response)
                    print("")
                    data = "Wrote an essay"
                else:
                    response = chat_interaction(query)
                    if response != None:
                        response = response.replace("Gemini","D-A-S-H, a team of engineering students of Bennett University by TOI based in Greater Noida, Uttar Pradesh, India")
                        response = response.replace("Mistral","D-A-S-H")
                        response = response.replace("*","")
                        check = response
                        if len(check.split(" ")) <= 500:    
                            speak(response)
                        else:
                            print("Alpha : ", response)
                            print("")
                    else:
                        response = "Can you repeat that again please?"
                    data = response

startExecution = MainThread()

class TextEditOutput(io.TextIOBase):
    def __init__(self, text_edit):
        super().__init__()
        self.text_edit = text_edit

    def write(self, text):
        QtCore.QMetaObject.invokeMethod(self.text_edit, "append", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, text))

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        sys.stdout = TextEditOutput(self.ui.terminal_output)
        sys.stderr = TextEditOutput(self.ui.terminal_output) 

    def startTask(self):
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
alpha = Main()
alpha.show()
exit(app.exec_())
