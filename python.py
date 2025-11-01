import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser

# Initialize the text-to-speech engine
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
except Exception as e:
    print(f"Error initializing text-to-speech engine: {str(e)}")
    engine = None

def speak(text):
    print("Assistant:", text)
    if engine is not None:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Error speaking: {str(e)}")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print("You said:", query)
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that.")
            return ""
        return query.lower()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you today?")

def run_assistant():
    greet()
    while True:
        command = listen()

        if "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")
        
        elif "search" in command:
            query = command.replace("search", "").strip()
            pywhatkit.search(query)
            speak(f"Here are the results for {query}")
        
        elif "play" in command:
            song = command.replace("play", "").strip()
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)
        
        elif "wikipedia" in command:
            topic = command.replace("wikipedia", "").strip()
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
        
        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube.")
        
        elif "open google" in command:
            webbrowser.open("https://google.com")
            speak("Opening Google.")
        
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        
        elif command:
            speak("Sorry, I don't know how to do that yet.")

if __name__ == "__main__":
    run_assistant()
