import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for a command from the user."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from the service.")
            return ""

def respond(command):
    """Respond to the user's command."""
    command = command.lower()
    if 'hello' in command:
        speak("Hello! How can I help you?")
        print(f"Hello! How can I help you?")
    elif 'time' in command:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}.")
        print(f"The current time is {current_time}.")

    elif 'date' in command:
        current_date = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}.")
        print(f"Today's date is {current_date}.")
    elif 'exit' in command or 'stop' in command:
        speak("Goodbye!")
        print("Goodbye")
        exit()  # Terminate the program
    else:
        speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            respond(command)


