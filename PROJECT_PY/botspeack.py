# import speech_recognition as sr


# rec =sr.Recognizer()
# with sr.Microphone() as src:
#     print('..........')
#     audio = rec.listen(src)
#     text = rec.recognize_bing(audio)
# if text == 'hello':
#     print('good morning')
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
rec = sr.Recognizer()
helo = AudioSegment.from_wav("sound/1.wav")
sick = AudioSegment.from_wav('sound/2.wav')
play(helo)
with sr.Microphone() as src:
    print('🎤 انتظر... جارٍ الاستماع')
    audio = rec.listen(src)


    text = rec.recognize_google(audio)
    print("📣 أنت قلت:", text)

    if text.lower() == 'hello':
        print('🌞 Good morning!')
    elif text.lower() == 'time':
        
        play(sick)

