# Import the necessary modules
from transformers import AutoProcessor, AutoModel
import torch

class TextToSpeechModel:
    def __init__(self, model_name):
        # Load the model and processor
        self.model, self.processor = self.load_model_and_processor(model_name)

    # Static method for loading model and processor
    @staticmethod
    def load_model_and_processor(model_name):
        # Load the model
        model = AutoModel.from_pretrained(model_name)
        # Load the processor
        processor = AutoProcessor.from_pretrained(model_name)
        return model, processor

    # Method for converting text to speech
    def text_to_speech(self, text):
        # Process the input text
        inputs = self.processor(text=[text], return_tensors="pt")
        # Generate the speech
        speech_values = self.model.generate(**inputs, do_sample=True)
        return speech_values
