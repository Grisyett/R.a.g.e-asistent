from vosk import Model, KaldiRecognizer
import pyaudio
import requests
import json

#Modulo de reconocimiento de voz v.1

modelo = Model(r"C:\Users\yaewa\OneDrive\Desktop\Rage asistent\vosk-model-small-es-0.42") #cargando modelo de reconocimiento
sample_rate = 16000 #frecuencia
chunk = 8192

reconocedor = KaldiRecognizer(modelo,sample_rate)

#manejando el microfono
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=chunk)
stream.start_stream()

print("Escuchando....")

while True:
    data = stream.read(4096)

    if len(data) == 0:
        break

    if reconocedor.AcceptWaveform(data):
        text = reconocedor.Result()
        print(text[14:-3]) #recorta para que solo se vea las palabras reconocidas

