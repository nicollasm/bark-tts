# Import necessary modules
import tkinter as tk
from tkinter import filedialog
from model import TextToSpeechModel
from audio_utils import AudioUtils

class App:
    def __init__(self, master):
        # Create main frame
        self.master = master
        # Load model
        self.text_to_speech_model = TextToSpeechModel("suno/bark-small")
        # Create and set text input variable
        self.text_input = tk.StringVar()
        # Create and place text input field
        self.text_input_field = tk.Entry(master, textvariable=self.text_input)
        self.text_input_field.pack()
        # Create and place 'Generate Speech' button
        self.generate_button = tk.Button(master, text="Generate Speech", command=self.generate_speech)
        self.generate_button.pack()
        # Create and place 'Save Audio' button
        self.save_button = tk.Button(master, text="Save Audio", command=self.save_audio)
        self.save_button.pack()

    def generate_speech(self):
        # Get the text input
        text = self.text_input.get()
        # Convert the text to speech
        self.speech_values = self.text_to_speech_model.text_to_speech(text)
        # Play the audio
        AudioUtils.play_audio(self.speech_values)

    def save_audio(self):
        # Ask the user for the file location
        file_path = filedialog.asksaveasfilename(defaultextension=".wav")
        # Save the audio
        AudioUtils.save_audio(file_path, self.speech_values)