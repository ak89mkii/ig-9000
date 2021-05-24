import speech_recognition as sr;
import webbrowser;
import random;
import os;
import playsound;
from gtts import gTTS;
from flask import Flask, redirect, url_for, render_template, request;
from time import ctime;

app = Flask(__name__)

r = sr.Recognizer()

@app.route("/")
def home():
    sayings_list = ['hello', 'whats up', 'good day', 'do you have a question', 'how may i be of assistance']
    mom_9000_speak(random.choice(sayings_list))
    voice_data = record_audio()
    respond(voice_data)
    return render_template('index.html')

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            mom_9000_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            mom_9000_speak('im sorry my responses are limited. you must ask the right questions')
        except sr.RequestError:
            mom_9000_speak('Sorry, speech service down.')
        return voice_data

def mom_9000_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        mom_9000_speak('My name is  ig 9000.')
    if 'what time is it' in voice_data:
        mom_9000_speak(ctime())
    if 'who is the best' in voice_data:
        mom_9000_speak('Bender is the best.')
    if 'say something' in voice_data:
        sayings_list = ['Ha', 'do or do not, there is no try, except in javascript', 'shut the explitive deleted up']
        mom_9000_speak(random.choice(sayings_list))
    if 'cook' in voice_data:
        mom_9000_speak('jesus mary and joseph.')


# @app.route('/activate', methods=['POST'])
# def activate(mom_9000_speak):
#     mom_9000_speak('How may I be of service?')
#     voice_data = record_audio()
#     respond(voice_data)

if __name__=="__main__":
    app.run(port=5000, debug=True, threaded=True)