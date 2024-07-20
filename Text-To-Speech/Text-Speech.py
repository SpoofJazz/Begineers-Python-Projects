import pyttsx3 
engine = pyttsx3.init()

text=input("Enter the words you want to listen: ")
engine.say(text)

print("The words you just listened are: ", text)
engine.runAndWait()
