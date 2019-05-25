import speech_recognition as sr
import sys
# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class SpeechRecognition():
    stemmer = None
    audio = None
    credentials_json = None
    def __init__(self):
        # create stemmer
        factory = StemmerFactory()
        global stemmer
        global credentials_json
        stemmer = factory.create_stemmer()
        
        # recognize speech using Google Cloud Speech
        with open(r"/home/pi/Transibi-9098c60b00f8.json", "r") as f:
            credentials_json = f.read()

    def listen(self):
        result = None
        # obtain audio from the microphone
        r = sr.Recognizer()
        r.energy_threshold = 7000
        r.operation_timeout = 7  # in second
        global audio
        with sr.Microphone() as source:
            print("Mulai mendengarkan...")
            # audio = r.record(source,  duration = 4)
            audio = r.listen(source)
        try:
            speech_result = r.recognize_google_cloud(audio, language = "id-ID", credentials_json=credentials_json)
            stemmed_word = stemmer.stem(speech_result)
            result = stemmed_word
            
        except sr.UnknownValueError:
            result = "Google Cloud Speech could not understand audio"
        except sr.RequestError as e:
            result = "Could not request results from Google Cloud Speech service; {0}".format(e)
        
        print("speech response: " + result) 
        return result

