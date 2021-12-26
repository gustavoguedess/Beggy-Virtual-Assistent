import speech_recognition as sr 

listener = sr.Recognizer()

with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
except:
    print('Ocorreu algum erro...')
    pass
