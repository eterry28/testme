import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import sys
import imdb
import python_weather
import asyncio

print('starting...')

listener = sr.Recognizer()
engine = pyttsx3.init()

global continueProgram
continueProgram = True

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = 'exit'
    try:    
        with sr.Microphone() as source:            
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'james' in command:
                command = command.replace('james', '')
                print(command)  
            else:
                print(command)                                     
    except:
        print("Something went wrong")
    return command

async def run_james():
    try:    
        command = take_command()
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('The current time is ' + time)
        elif 'what is the weather in' in command:
            weather_client = python_weather.Client(format=python_weather.IMPERIAL)
            city = command.replace('what is the weather in', '')
            weather = await weather_client.find(city)
            talk('The current temperature in ' + city + ' is ' + str(weather.current.temperature))
            talk('The forecast')
            for forecast in weather.forecasts:
                fc_string = "The forecast for {} is {} and {} degrees.".format(forecast.date, forecast.sky_text, str(forecast.temperature))
                talk(fc_string)
            await weather_client.close()
        elif 'what is' in command:
            term = command.replace('what is','')
            info = pywhatkit.info(term, 3, True)
            talk(info)
        elif 'who is' in command:
            person = command.replace('who is','')
            info = pywhatkit.info(person, 3, True)
            talk('searching wikipedia for ' + person)
            talk(info)
        elif 'search' in command:
            search_term = command.replace('search', '')
            talk('searching ' + search_term)
            pywhatkit.search(search_term)
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
        elif 'close' in command:
            continueProgram = False
        else:
            talk("I did not understand you.")
    except:
        talk("Something went wrong. Try again.")
        pass

talk("Hello. My name is James. How can I help you?")
while continueProgram:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_james())

talk("see you on the other side")
print('other side...')


"""
Here are more things to add:
Call contact - Call [Name]
Text contact - Tell [Name] I am on my way
Email contact - Send email to [Name] about [subject] and say [message]
Timer - Set the timer for [X] minutes
Alarm - Set an alarm for [time]
Date - What's the date
Weather - What's the weather like today?
Stocks - What's [X] stock price
Conversions - How many inches in 2 feet
Calculations - What is 20 percent of 75
Picture - Take a picture
Selfie - Take a selfie
Open [App]
Holidays - When is Easter
Time - What time is it in Mumbai
Define [word]
What is a synonym for [word]
Where is [business name]
Where is the nearest [business type]
Sports - Did the Chiefs win
Flip a coin
Roll a die
Show me the trailer for [movie]
Show me [X] from [website]
Movie - 
"""
