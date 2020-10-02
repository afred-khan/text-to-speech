from gtts import gTTS

myText = input("Type what you want me to speak \n")

language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")
