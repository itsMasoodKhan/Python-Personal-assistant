import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyautogui
import time
import pyfirmata

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Masood !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Masood ! ")
    else:
        speak("Good Evening Masood !")

    speak("Hello Masood i am Masood junior your assisstant how may i help you " )

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        ("recognizing...")
        query = r.recognize_google(audio , language= 'en-pk')
        print(f"user said : {query}\n")

    
    except Exception as e :
        print("Say that again please...")
        return "none"
    return query

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query :
            speak('searching Wikipedia...')
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query , sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak('ok sir')
            webbrowser.open('https://www.youtube.com/')

        elif "what's my name" in query:
            speak('Sir your name is masood')

        elif 'open google' in query:
            speak('ok sir')
            webbrowser.open('google.com')

        elif 'play nasheed' in query:
            speak('ok sir')
            webbrowser.open('https://www.youtube.com/watch?v=6t1k2W_sxtU')
        
        
        elif 'close ' in query:
            speak('ok sir')
            pyautogui.hotkey('ctrl','w')
        
        elif 'stop' in query:
            speak('ok sir')
            pyautogui.hotkey('space')
        elif 'continue' in query:
            speak('ok sir')
            pyautogui.hotkey('space')

        elif 'red face' in query:
            speak('Ummiya is one of your sisters who has a red face')

        elif 'babashka' in query:
            speak('qadira is babashka babar sari with puzzle hair ')

        elif 'paper doll' in query:
            speak('ok sir')
            webbrowser.open('https://www.youtube.com/watch?v=qf32hINUTkQ')

        elif 'haroon' in query:
            speak('he is your brother')
        elif 'who is mehmood' in query:
            speak('he is your brother')
        elif 'musa' in query:
            speak('musa is your cousin')
        elif 'eisa' in query:
            speak('he is your cousin')
        elif 'sameem' in query:
            speak('he is your cousin')
        elif 'saleem' in query:
            speak('he is your cousin')
        elif 'Halima' in query:
            speak('She is your cousin and your upcoming aunt')
        elif 'aisha' in query:
            speak('she is your cousin')
        elif 'nawab' in query:
            speak('he is your cousin')
        elif 'asif' in query:
            speak('he is your cousin')
        elif 'saima' in query:
            speak('she is your cousin')
        elif 'qaima' in query:
            speak('she is your cousin')
        elif 'fahima' in query:
            speak('she is your cousin')
        elif 'wajida' in query:
            speak('she is your cousin')
        elif 'hamidullah' in query:
            speak('he is your cousin')
        elif 'faridoon' in query:
            speak('Fareedun Muhammad rostai is your uncle')
        elif 'hamayoon' in query:
            speak('Hammayoun rostai is your uncle')
        elif 'hammasa' in query:
            speak('Hammasa rostai is your aunt ')
        elif 'nazia' in query:
            speak('she is your cousine')


        elif 'haj' in query:
            speak('wahaj is an employee of sveston watches and an executive of HR')
        elif 'sameer' in query:
            speak('Sameer bhai is CFO at sveston watches')
        elif 'mussab' in query:
            speak('mussab bhai is an employee of sveston watches and an executive of accounts')
        elif 'break' in query:
            speak('what is your name')
            result = takeCommand().lower()
            if 'masood' in result:
                speak('ok sir as you wish')
                exit()
            else:
                speak('i only hear to my boss')
        elif 'play nice song' in query:
            speak('ok sir')
            webbrowser.open('https://www.youtube.com/watch?v=npmY3DBXtds&list=RDnpmY3DBXtds&start_radio=1')
        elif 'close tab ' in query:
            speak ('ok sir')
            pyautogui.hotkey('ctrl','w')
        elif 'hey junior' in query:
            speak('hmm sir how may i help you')
        elif 'open facebook' in query:
            speak('ok sir as you wish')
            webbrowser.open('https://www.facebook.com/')
        elif 'thank you' in query:
            speak('i am glad to work for you')
        elif 'mute' in query:
            speak('ok sir')
            pyautogui.hotkey('m')
        elif 'unmute' in query:
            speak('ok sir')
            pyautogui.hotkey('m')
        elif 'joke about mehmood' in query:
            speak('ok sir')
            speak('with mehmoods mostaches you can tie up a giant')
        elif ' tab forward' in query:
            speak ('ok sir')
            pyautogui.hotkey('ctrl','tab')
        elif 'tab backward' in query:
            speak('ok sir')
            pyautogui.hotkey('ctrl','shift','tab')
        elif 'go to facebook tab' in query:
            speak('ok sir')
            webbrowser.open_new_tab('https://www.facebook.com/')
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir the time is{strTime}")
        elif 'maths teacher' in query:
            speak('Muhammad yamin is your maths teacher')
        elif 'nice song' in query:
            speak('ok sir')
            webbrowser.open('https://www.youtube.com/watch?v=FzG4uDgje3M')
        elif 'basit' in query:
            speak('basit is your cousin')
        elif 'farida' in query:
            speak('farida is your cousin')
           
            
        


        
    



        
        


        

        
            

        

        




