#Project Jarvis
import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import wmi
import osascript
import tkinter as tk
import smtplib
import requests


#Text To Speech\
  


url = 'http://api.openweathermap.org/data/2.5/weather?appid=API KEY&q=bengaluru'
json_data = requests.get(url).json()
format_add = json_data['weather'][0]['main']
fomat_add = json_data['main']['temp'] 


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremailid.com', 'password')
    server.sendmail('youremailid.com', to, content)
    server.close()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio):  #here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()



def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning sir i am virtual assistent Jarvis")
    elif hour>=12 and hour<18:
        speak("good afternoon sir i am virtual assistent Jarvis") 
    else:
        speak("good evening sir i am virtual assistent Jarvis")



def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        audio = r.listen(source, phrase_time_limit=4)
    try:
        print("Recognising...") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        return "none"
    return text

#for main function                               
def start():
    if __name__ == "__main__":
        wish()
        speak('The weather is ')
        speak(format_add)
        speak('And the temperature is ')
        speak(fomat_add)
        while True:
            query = takecom().lower()

            if 'github' in query:
                webbrowser.open("https://www.github.com")
                speak("opening github")  
            elif 'facebook' in query:
                webbrowser.open("https://www.facebook.com")
                speak("opening facebook")      
            elif 'instagram' in query:
                webbrowser.open("https://www.instagram.com")
                speak("opening instagram") 
            elif 'email to' in query:
                j = query.replace("email to", "")
                d = j.replace(" ", "")
                try:
                    speak("What should I say?")
                    content = takecom()
                    to = "{}@gmail.com".format(d)   
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry. I am not able to send this email")       
            elif 'google' in query:
                webbrowser.open("https://www.google.com")
                speak("opening google")
            elif 'volume' in query:
                repla = query.replace("volume", "")
                osascript.osascript("set volume output volume" + repla)    
            elif 'yahoo' in query:
                webbrowser.open("https://www.yahoo.com")
                speak("opening yahoo")
                
            elif 'gmail' in query:
                webbrowser.open("https://mail.google.com")
                speak("opening google mail") 
                
            elif 'snapdeal' in query:
                webbrowser.open("https://www.snapdeal.com") 
                speak("opening snapdeal")  
            elif 'amazon' in query or 'shop online' in query:
                webbrowser.open("https://www.amazon.com")
                speak("opening amazon")
            elif 'flipkart' in query:
                webbrowser.open("https://www.flipkart.com")
                speak("opening flipkart")   
            elif 'ebay' in query:
                webbrowser.open("https://www.ebay.com")
                speak("opening ebay")
            elif 'brightness' in query:
                zz = query.replace("brightness", "")
                brightness = zz
                c = wmi.WMI(namespace='wmi')
                methods = c.WmiMonitorBrightnessMethods()[0]    
                methods.WmiSetBrightness(brightness, 0)
            elif 'good bye' in query:
                speak("good bye")
                exit()
            elif "shutdown" in query:
                speak("shutting down")
                os.system('shutdown -s') 
            elif "what's up" in query or 'how are you' in query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
                ans_q = random.choice(stMsgs)
                speak(ans_q)  
                ans_take_from_user_how_are_you = takecom()
                if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                    speak('okey..')  
                elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                    speak('oh sorry..')  
            elif 'make you' in query or 'created you' in query or 'develop you' in query:
                ans_m = " I was made by the great Advaith S "
                print(ans_m)
                speak(ans_m)
            elif "who are you" in query or "about you" in query or "your details" in query:
                about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
                print(about)
                speak(about)
            elif "hello" in query or "hello Jarvis" in query:
                hel = "Hello! How May i Help you.."
                print(hel)
                speak(hel)
            elif "open" in query:
                f = query.replace("open ", "")
                os.startfile('C:\\Users\\Public\\Desktop\\{}.lnk'.format(f))
            elif 'prime' in query:
                e = query.replace("prime", "")
                webbrowser.open("https://www.primevideo.com/region/eu/search/ref=atv_nb_sr?phrase={}&ie=UTF8".format(e))
            elif "your name" in query or "sweat name" in query:
                na_me = "Thanks for Asking my name my self ! Jarvis"  
                print(na_me)
                speak(na_me)
            elif "you feeling" in query:
                print("feeling Very sweet after meeting you")
                speak("feeling Very sweet after meeting you") 
            elif query == 'none':
                continue 
            elif 'search youtube' in query:
                q = query.replace("search youtube", "")
                webbrowser.open("https://www.youtube.com/results?search_query={}".format(q))
            elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
                ex_exit = 'bye'
                speak(ex_exit)
                exit()
            elif 'product' in query:
                w = query.replace("product", "")   
                webbrowser.open("https://www.amazon.in/s?k={}&ref=nb_sb_noss_2".format(w))
            elif 'jarvis' in query:
                speak('yes')
            else:
                results = wikipedia.summary(query,sentences=2)
                print(results)
                speak(results)

if __name__ == "__main__":
    while True:
        qury = takecom().lower()
        if 'start' in qury:
            start()
            
