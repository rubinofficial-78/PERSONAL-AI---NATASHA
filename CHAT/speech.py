import speech_recognition as sr 

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something")
    aud = r.listen(source)
    said = ""
    try:
        said = r.recognize_google(aud)
        print("You said:",said)
    except Exception as e:
        print(e)