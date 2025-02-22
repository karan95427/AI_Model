import speech_recognition as sr
import win32com.client
import webbrowser
import time

def say(text):
   speaker =win32com.client.Dispatch("SAPI.SpVoice")
   speaker.Rate= -2
   text = " " + text
   speaker.Speak(text)
   time.sleep(0.2)

def takeCommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
          r.pause_threshold = 1
          r.dynamic_energy_threshold = True
          print("listening.....")
          r.adjust_for_ambient_noise(source)
          audio =r.listen(source,timeout=5, phrase_time_limit=8)
          query =r.recognize_google(audio , language="eng-In")
          print(f"user said: {query}")
          return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        say("Sorry, I couldn't understand what you said.")
        return 0
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        say("Could not request results, check your internet connection.")
        return 0
if __name__ == '__main__':
    while True:
      query = takeCommand()
      query = query.lower()
      site=[["youtube" , "https://www.youtube.com/"],["google" , "https://www.google.com/"],["wikipedia","https://en.wikipedia.org/wiki/Main_Page" ,["hotstar","https://jiohotstar.com/"]]]
      if query:
        for site in site:
             if f"open {site[0]} " in query:
                say(f"opening {site[0]}  sir...")
                webbrowser.open(site[1])
                break
             else:
                 say("sorry sir, i can't open that site")
                 break

        if "ok" in query:
            say("  " + "ok have a nice day sir, bye")
            break
        else:
            say(query)

