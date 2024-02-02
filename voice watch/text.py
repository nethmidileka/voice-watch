import gtts


from tkinter import Tk, Button
from gtts import gTTS
import os
from datetime import datetime

def speak_in_sinhala(text):
    tts = gTTS(text, lang='si')  # 'si' is the code for Sinhala
    tts.save("output.mp3")
    os.system("start output.mp3")

def get_current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}"

def on_button_click():
    time_message = get_current_time()
    speak_in_sinhala(time_message)

# Create the main window
window = Tk()
window.title("Sinhala Time Teller")

# Create a button
button = Button(window, text="Tell Time in Sinhala", command=on_button_click)
button.pack(pady=20)

# Run the application
window.mainloop()
