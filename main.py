import EAR
import MOUTH

while True:
    data = EAR.stream.read(4000, exception_on_overflow=False)
    # if len(data) == 0:
    #   break
    if EAR.recognizer.AcceptWaveform(data):
        Text = EAR.recognizer.Result()
        text = Text[14:-3]
        print(text)
        count = len(text.split())
        if count <= 3:
            if text == "athènes" or text == "athéna" or text == "a demain" or text == "a peine" or text == "demain" or text == "abdellah" or text == "avenant" or text == "demain" or text == "ah benin":
                MOUTH.engine.say(MOUTH.greeting())
                MOUTH.engine.runAndWait()

        elif count > 3:
            MOUTH.engine.say("parlons vrai et clair")
            MOUTH.engine.runAndWait()
        elif count > 3:
            MOUTH.engine.say("je ne te suis pas")
            MOUTH.engine.runAndWait()



