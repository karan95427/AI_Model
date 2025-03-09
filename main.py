import speech_recognition as sr
import win32com.client
import webbrowser
import os
import time
import random
import urllib.parse
import google.generativeai as genai
from config import API_KEY

chatStr =""
def chat(query):
  global chatStr
  print(chatStr)
  api_key = API_KEY 
  if api_key is None:
    raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")


  genai.configure(api_key=api_key)


  model = genai.GenerativeModel("gemini-1.5-pro")


  response = model.generate_content(query)
  if response and hasattr(response, "text"):
     say(response.text)
     print(f"Jarvis: {response.text}") 
     return response.text
  else:
        say("I couldn't generate a response.")
        return None

def google_search(query):
   
   base_url="https://www.google.com/search?q="
   search_url=base_url+urllib.parse.quote(query)
   webbrowser.open(search_url)

   say(f"Searching Google for {query}")
   print(f"Opening Google search: {search_url}")

 
def ai(prompt):
  api_key = API_KEY
  text=f"Response for pormpt: {prompt} \n ****************************\n\n"
  if api_key is None:
     raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")

  genai.configure(api_key=api_key)

  model = genai.GenerativeModel("gemini-1.5-pro")
  try:
    response = model.generate_content(prompt)
    text += response.text
    
    if not os.path.exists("ai"):
      os.makedirs("ai")
    file_path=f"ai/prompt-{random.randint(1,999999999999)}.txt"
    with open(file_path,"w") as f:
     f.write(text)

    return response.text
  
  except AttributeError:
    print("Error: Response object has no attribute 'text'")
    return None

  

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
          query =r.recognize_google(audio , language="en-In")
          print(f"user said: {query}")
          return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        say("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        say("Could not request results, check your internet connection.")
        return None
if __name__ == '__main__':
    say("Hello sir, how may i help you?")
    while True:
      query = takeCommand()
      if query:
        if "ok" in query:
            exit()
             
        elif f"open music" in query:
                 path="\\Desktop\\flute-traditional-v1-251387.mp3"
                 say(f"opening music sir...")
                 os.startfile(path)
                 
        elif f"the time" in query:
                 realtime=time.strftime("%H:%M:%S")
                 say(f" Sir the time is {realtime}")
                 
        elif f"using ai" in query:
                 say("what do you want to know about?")
                 prompt = takeCommand()
                 if prompt: 
                    say("Processing...") 
                    ai_response = ai(prompt)
                    if ai_response: 
                        say("Here's the AI's response:")
                        print(ai_response)
                    else:
                        say("AI response was empty.")
                 else:
                    say("I didn't hear a prompt.")
        elif "reset chat".lower() in query.lower():
            chatStr = ""
        
        elif "search for" in query or "google" in query:
          search_term=query.replace("search for","").replace("google","").strip()
          if search_term:
            google_search(search_term)
          else:
            say("What do you want me to search for?")
            new_query = takeCommand()
            if new_query:
              google_search(new_query)
            else:
              say("I didn't hear a search term.")
                 
        else:
            print("chatting...")
            chat(query)
