import speech_recognition as sr
import pyttsx3
import random

# the code will read the lines from the saved text file
lines = []
dispfile = open("lines.txt", "r")
content = dispfile.read()
content = content.split("\n")
dispfile.close()
for i in content:
    lines.append(i)

# A random line is chosen from the text file
random_line = random.choice(lines)
print(random_line)
mytext = random_line
mytext2 = str(mytext)


# the function to say the line aloud by the program
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


r = sr.Recognizer()


def Listen():
    try:
        with sr.Microphone() as source2:
            SpeakText(mytext2)  # SpeakText is used to make the program say whatever we want

            while True:
                print("Say it now")

                # the code to ask the user to say the sentence
                r.adjust_for_ambient_noise(source2, duration=0.9)
                audio2 = r.listen(source2)
                Myvoice = r.recognize_google(audio2)
                Myvoice = Myvoice.lower()
                print(Myvoice)

                # checking whether the sentence matches what the user said
                if (Myvoice == mytext2):
                    SpeakText("it is correct")
                    break  # the code stops when the sentence matches
                else:
                    SpeakText(
                        "it is wrong. try again")  # the code repeats and the user tries again if the sentence does not match

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")

Listen()