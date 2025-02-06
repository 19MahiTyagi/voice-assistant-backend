from flask import Flask, request, jsonify
from flask_cors import CORS
import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser
import datetime

app = Flask(__name__)
CORS(app)  # Allow requests from the frontend


def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

@app.route('/process_voice', methods=['POST'])
def process_voice():
    data = request.get_json()
    command = data.get("command", "").lower()

    response_text = "I did not understand."

    if "hello" in command:
        response_text = "Hello!"
    elif "time" in command:
        response_text = f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}"
    elif "date" in command:
        response_text = f"Today's date is {datetime.datetime.now().strftime('%B %d, %Y')}"
    elif "open google" in command:
        response_text = "Opening Google"
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        response_text = "Opening YouTube"
        webbrowser.open("https://www.youtube.com")
    elif "open notepad" in command:
        response_text = "Opening Notepad"
        os.system("notepad")
    elif "stop" in command:
        response_text = "Goodbye!"
    
    speak(response_text)
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

