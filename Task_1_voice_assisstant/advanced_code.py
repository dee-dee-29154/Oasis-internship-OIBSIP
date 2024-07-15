import speech_recognition as sr
import pyttsx3
from datetime import datetime
import requests  # For making API requests (e.g., for weather)
import smtplib    # For sending emails (if you want that feature)

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
    elif 'time' in command:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}.")
    elif 'date' in command:
        current_date = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}.")
    elif 'weather' in command:
        get_weather()  # Placeholder function, you need to implement it
    elif 'email' in command:
        send_email()  # Placeholder function, you need to implement it
    elif 'exit' in command or 'stop' in command:
        speak("Goodbye!")
        exit()  # Terminate the program
    else:
        speak("Sorry, I didn't understand that.")

def get_weather():
    """Fetch and speak the weather information."""
    # You would need to implement this using a weather API
    speak("Fetching weather information is not implemented yet.")

def send_email():
    """Send an email (requires additional setup)."""
    speak("Sending email is not implemented yet.")

if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            respond(command)
