# Install an external module and use it to perform an operation of your interest. 

import pyttsx3 # type: ignore
engine = pyttsx3.init()
engine.say("Harry is a good boy")
engine.runAndWait()