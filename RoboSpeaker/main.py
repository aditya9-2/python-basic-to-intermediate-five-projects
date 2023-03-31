import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1, Created by Aditya\n")
    while True:
        x = input("Enter what you want me to speak (press 'q' to quit): ")
        if x.lower() == "q":
            speak("Bye my dear friend")
            break
        else:
            speak(x)
