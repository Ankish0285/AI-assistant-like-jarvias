import os
import time
import subprocess
import pyttsx3
import speech_recognition as sr
import webbrowser
import pyautogui

# ------------------- TEXT TO SPEECH ENGINE -------------------
def speak(text):
    engine.say(text)
    engine.runAndWait()

engine = pyttsx3.init()

# ------------------- SPEECH RECOGNIZER ------------------------
listener = sr.Recognizer()

print("\n Jarvis Activated...\n")
speak("Jarvis activated and ready sir")

def done(text):
    speak(text)

WHATSAPP = r"C:/Users/ANKISH KUMAR/OneDrive/Desktop/WhatsApp.lnk"
YOUTUBE = "https://www.youtube.com/"


while True:
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)

        command = listener.recognize_google(voice, language="en-in").lower()
        print("You said:", command)

        # ---------------------------------------------------------
        # OPEN NOTEPAD
        if "open notepad" in command:
            os.system("notepad")
            done("Notepad opened boss")

        # ---------------------------------------------------------
        # OPEN WHATSAPP
        elif "open whatsapp" in command:
            os.startfile(WHATSAPP)
            time.sleep(5)
            done("WhatsApp opened boss")

        # ---------------------------------------------------------
        # WHATSAPP MESSAGE WITH CONTACT NAME
        elif "message" in command:
            os.startfile(WHATSAPP)
            time.sleep(5)

            parts = command.replace("message", "").strip().split()
            name = parts[0]                         # contact name
            msg = " ".join(parts[1:])               # message body

            pyautogui.write(name)
            time.sleep(2)
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.write(msg)
            pyautogui.press("enter")
            done("Message sent boss")

        # ---------------------------------------------------------
        # WHATSAPP CALL WITH CONTACT NAME
        elif "call" in command:
            os.startfile(WHATSAPP)
            time.sleep(5)

            name = command.replace("call", "").strip()
            pyautogui.write(name)
            time.sleep(2)
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.hotkey("ctrl", "shift", "s")      # voice call shortcut
            done("Calling boss")

        # ---------------------------------------------------------
        # OPEN YOUTUBE AND PLAY
        elif "open youtube" in command and "play" in command:
            webbrowser.open(YOUTUBE)
            time.sleep(5)

            query = command.replace("open youtube", "").replace("play", "").strip()
            pyautogui.write(query)
            pyautogui.press("enter")
            time.sleep(4)
            pyautogui.press("enter")
            done("Music played boss")
        elif "open youtube" in command:
            webbrowser.open(YOUTUBE)
            done("youtube opened boss")

    

        
        # GOOGLE SEARCH
        elif "search" in command or "google" in command:
            query = command.replace("search", "").replace("google", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            done("Searching on google boss")

    
        # OPEN WEBSITE
        elif "open website" in command:
            webbrowser.open("https://ankish0285.github.io/Neo-Gen-/")
            done("Website opened boss")

        # ---------------------------------------------------------
        # OPEN FILE
        elif "open file" in command:
            os.startfile("C:/Users/ANKISH KUMAR/OneDrive/Desktop/my code/AI BASED INTERNSHIP PROGRAM/.vscode")
            done("File opened boss")

        # ---------------------------------------------------------
        # OPEN CALCULATOR
        elif "open calculator" in command:
            os.system("calc")
            done("Calculator opened boss")

        # ---------------------------------------------------------
        # EXIT SYSTEM
        elif "exit" in command or "stop" in command or "shutdown" in command:
            speak("Goodbye sir, shutting down Jarvis")
            print(" Jarvis Stopped")
            break

        # ---------------------------------------------------------
        # UNKNOWN COMMAND
        else:
            speak("Sorry boss, I did not understand that")
            speak("Next command please")

    except Exception as e:
        print(" Error:", e)
        speak("Something went wrong boss")
