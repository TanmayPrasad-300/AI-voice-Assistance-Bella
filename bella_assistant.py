import tkinter as tk
from tkinter import messagebox
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia as wik
import random
import pyautogui
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)      
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon")
    elif hour >= 16 and hour < 21:
        speak("Good evening")
    else:
        speak("Good night")

def get_current_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    speak("The current time is " + current_time)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for your command...")
        r.pause_threshold = 1
        r.energy_threshold = 300      
        audio = r.listen(source, timeout=5)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results from the service.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def Google(query):
    query = query.replace("google search", "").replace("google", "").strip()
    speak("This is what I found on Google")
    try:
        speak("Processing...")
        pywhatkit.search(query)
        result = wik.summary(query, sentences=1)
        speak(result)
    except:
        speak("Sorry, I couldn't find anything.")

def Youtube(query):
    query = query.replace("youtube search", "").replace("youtube", "").strip()
    speak("This is what I found for your search!")
    web = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done.")

def classroom():
    webbrowser.open("https://classroom.google.com")

def Searchwiki(query):
    query = query.replace("wikipedia search", "").replace("wikipedia", "").strip()
    speak("This is what I found on Wikipedia")
    try:
        speak("Processing...")
        result = wik.summary(query, sentences=1)
        speak(result)
    except:
        speak("Sorry, I couldn't find anything.")

def start_voice_input():
    query = take_command()
    if query:
        if "wake up" in query:
            greet()
            speak("I am Bella, how can I help you?")
            while True:
                query = take_command()
                if query is None:
                    continue
                elif "open wikipedia" in query:
                    speak("Searching Wikipedia...")
                    Searchwiki(query)
                elif 'search google' in query:
                    Google(query)
                elif 'youtube' in query:
                    Youtube(query)
                elif "open" in query:
                   from dictapp import openappweb
                   openappweb(query)
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                     pywhatkit.press("k")
                     speak("video played")
                elif "mute" in query:
                      pyautogui.press("m")
                      speak("video muted")
                elif "volume up" in query:
                      from keyboard import volumeup
                      speak("Turning volume up,sir")
                      volumeup()
                elif "volume down" in query:
                      from keyboard import volumedown
                      speak("Turning volume down, sir")
                      volumedown()        
                elif "close" in query:
                    from dictapp import closeappweb
                    closeappweb(query)
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3,4,5,6,7) 
                    b = random.choice(a)
                    if b==1:
                       webbrowser.open("https://youtu.be/Oextk-If8HQ?si=5phG9gze-ZntLg7N")
                    elif b==2:
                        webbrowser.open("https://youtu.be/HIbzXaBdwZw?si=hUUzH1F5nIqf76Tg")
                    elif b==3:
                      webbrowser.open("https://youtu.be/mbGNF4QXaEE?si=TWzebVPRBkvExAH9")
                    elif b==4:
                     webbrowser.open("https://youtu.be/W-TE_Ys4iwM")
                    elif  b==5:
                     webbrowser.open("https://youtu.be/zDtvoZAHVTY")
                    elif b==6:
                     webbrowser.open("https://youtu.be/t7wSjy9Lv-o")
                    else:
                     webbrowser.open("https://youtu.be/fdubeMFwuGs")
                elif 'sleep' in query:
                   speak("Call me when you need me.")
                   break
    
              

def create_voice_window():
    voice_window = tk.Toplevel()
    voice_window.title("Bella")
    voice_window.geometry("300x100+1000+700")  

    label = tk.Label(voice_window, text="start", font=("Arial", 14))
    label.pack(pady=10)

    start_button = tk.Button(voice_window, text="say wake up", command=start_voice_input)
    start_button.pack(pady=10)

root = tk.Tk()
root.title("Main Window")
root.geometry("200x100")  

button = tk.Button(root, text="bella", command=create_voice_window)
button.pack(pady=20)

root.mainloop()