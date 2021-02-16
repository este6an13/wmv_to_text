# Diego Esteban Quintero Rey
# este6an13

import moviepy.editor as mp
import speech_recognition as sr
import json

wmv_file = mp.AudioFileClip(r"312620210212_080008.wmv")
duration = int(wmv_file.duration)

r = sr.Recognizer()

text = ""

for s in range(0, duration+1, 90):

    sc_wmv_file = wmv_file

    try:
        sc_wmv_file = wmv_file.subclip(s, s+89.99)
        sc_wmv_file.write_audiofile(r"312620210212_080008_{}.wav".format(s))
    except:
        print("Error while accessing a subclip")


    sc_wav_file = sr.AudioFile('312620210212_080008_{}.wav'.format(s))
    with sc_wav_file as source:
        audio = r.record(source)
        try:
            t = r.recognize_google(audio, language="es-ES")
            text += " "+t
            # print("Text: "+t)
        except Exception as e:
            print("Exception: "+str(e))


text_obj = {
    'name': '312620210212_080008.wmv',
    'text': text
}

with open('wmv_text.json', 'w', encoding='utf-8') as json_file:
    json.dump(text_obj, json_file, ensure_ascii=False)
