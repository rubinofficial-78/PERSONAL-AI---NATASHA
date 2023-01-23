import speech_recognition as sr 

def getInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        aud = r.listen(source)
        said = ""
    try:
        said = r.recognize_google(aud)
        return(str(said).lower())
    except Exception as e:
        return 