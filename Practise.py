import speech_recognition as sr
from gtts import gTTS
import os
# Initialize the recognizer
recognizer = sr.Recognizer()
# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Adjusting for background noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source, duration=2)
    print("Listening... Speak something!")
    audio = recognizer.listen(source)
# Convert speech to text using Google Speech Recognition
print("Recognizing...")
text1 = recognizer.recognize_google(audio)
print("You said:", text1)
# Input text
text = text1
# Convert text to audio
tts = gTTS(text=text, lang='en')
# Save the audio file
output_file = "output.mp3"
tts.save(output_file)
# Play the audio (optional, requires an audio player installed)
os.system(f"start {output_file}")  # For Windows
# os.system(f"open {output_file}")  # For macOS
# os.system(f"xdg-open {output_file}")  # For Linux
print(f"Audio saved as {output_file}")