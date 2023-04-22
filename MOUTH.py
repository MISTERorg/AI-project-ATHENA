import datetime
import random
import pyttsx3

# speech settings
engine = pyttsx3.init()
voice_speed = 130
tone = 2
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[tone].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', voice_speed)
calls = 0


# greetings function
def greeting():
    global calls
    if calls == 0:
        x = datetime.datetime.now()
        if "5" <= str(x.hour) < "12":
            day_period = "bonjour"
        elif "12" <= str(x.hour) <= "23":
            day_period = "bonsoir "
        else:
            hour = x.hour
            if hour == 0:
                hour = "minuit"
            elif hour == 1:
                hour = "une heure"
            elif hour == 2:
                hour = "deux heure"
            elif hour == 3:
                hour = "trois heure"
            elif hour == 4:
                hour = "quatre heure"

            day_period = "j'espère que tu sais qu'il est " + str(hour) + " et  " + x.strftime(
                "%M") + " minute mais-bon  "
        text = " {} , comment puis-je t'aider"
        calls += 1
        return text.format(day_period)

    else:
        greet = ["oui oui", "je te suis", "parle je t'écoute", "je suis la parle", "oui a ton service", "parle"]
        return random.choice(greet)

# open conversation function
# def common_words(text):
