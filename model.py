# model.py

from transformers import AutoProcessor, AutoModel
import torch

class TextToSpeechModel:
    def __init__(self, model_name, device="cpu"):
        self.device = device
        # Load the model and processor on the specified device
        self.model, self.processor = self.load_model_and_processor(model_name, device=device)

    # Static method for loading model and processor
    @staticmethod
    def load_model_and_processor(model_name, device="cpu"):
        # Load the model on the specified device
        model = AutoModel.from_pretrained(model_name).to(device)
        # Load the processor on the specified device
        processor = AutoProcessor.from_pretrained(model_name)
        return model, processor

    # Method for converting text to speech
    def text_to_speech(self, text):
        # Process the input text
        inputs = self.processor(text=[text], return_tensors="pt")
        # Generate the speech on the specified device
        speech_values = self.model.generate(**inputs, do_sample=True).to(self.device)
        return speech_values
