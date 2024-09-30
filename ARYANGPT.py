import openai
import os
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
openai.api_key = os.getenv('sk-R93PCWBgn2usx_2fQpR38RsmqXRgcyr5lTCBZ0cFr5T3BlbkFJBiqNoNII9-zcMiTbxoBLotbMdHhNFFD4mnoSfj_UwA')

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input using speech recognition
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)

        try:
            # Recognize the speech using Google Speech Recognition
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand. Could you repeat that?")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the speech service.")
            return ""

# Function to query OpenAI's GPT model
def aryan_ask(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Main loop for interacting with ARYAN
while True:
    user_input = listen()  # Listen to the user's voice input
    if "exit" in user_input.lower():  # Exit command to stop the assistant
        speak("Goodbye!")
        break

    if user_input:  # If input is not empty, process it
        reply = aryan_ask(user_input)  # Get response from GPT model
        print(f"ARYAN: {reply}")
        speak(reply)  # Respond with voice
