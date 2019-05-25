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
        global audio
        with sr.Microphone() as source:
            sys.stdout.write("Mulai mendengarkan...")
            audio = r.listen(source)
            
        try:
            speech_result = r.recognize_google_cloud(audio, language = "id-ID", credentials_json=credentials_json)
            stemmed_word = stemmer.stem(speech_result)
            result = stemmed_word
            
        except sr.UnknownValueError:
            result = "Google Cloud Speech could not understand audio"
        except sr.RequestError as e:
            result = "Could not request results from Google Cloud Speech service; {0}".format(e)
        
        sys.stdout.write(result) 
        return result

