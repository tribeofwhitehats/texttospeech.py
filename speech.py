from gtts import gTTS  
import os  
mytext = 'i am saying what you wrote' 
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
os.system("mpg321 welcome.mp3") 
