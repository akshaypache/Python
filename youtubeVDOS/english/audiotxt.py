from gtts import gTTS

def tts(data):   
    myobj = gTTS(text=data, lang='en', slow=False,)
    myobj.save(f"SQLUnit1.mp3")

file = open("Data.txt","r")
data = file.read()
file.close()

tts(data)
