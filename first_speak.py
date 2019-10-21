import speech_recognition as sr
import speechd,datetime
r= sr.Recognizer()
tts_d = speechd.SSIPClient('test')
tts_d.set_output_module('rhvoice')

with sr.Microphone(device_index=12) as source:
    tts_d.speak("Как вас зовут?")
    r.adjust_for_ambient_noise(source, duration = 1)
    
    a=r.listen(source)
    
query = r.recognize_google(a, language="ru-Ru")




tts_d.set_punctuation(speechd.PunctuationMode.SOME)
tts_d.speak("Вы сказали:" +query.lower())

print("Вы сказали:" +query.lower())

