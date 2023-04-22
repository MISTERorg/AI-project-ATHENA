from vosk import Model, KaldiRecognizer
import pyaudio


# hearing initialisation
model = Model(r"B:\Athene\vosk-model-small-fr-0.22")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()





