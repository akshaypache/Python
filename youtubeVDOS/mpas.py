from mutagen.mp3 import MP3
audio = MP3("hello.mp3")
print(audio.info.length)