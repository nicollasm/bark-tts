# Import necessary modules
from IPython.display import Audio
from scipy.io.wavfile import write

class AudioUtils:
    # Static method for playing audio
    @staticmethod
    def play_audio(model, speech_values):
        # Get the sampling rate
        sampling_rate = model.generation_config.sample_rate
        # Create an Audio object and display it
        audio = Audio(speech_values.cpu().numpy().squeeze(), rate=sampling_rate)
        return audio

    # Static method for saving audio
    @staticmethod
    def save_audio(model, file_path, speech_values):
        # Get the sampling rate
        sampling_rate = model.generation_config.sample_rate
        # Save the speech_values as a .wav file
        write(file_path, rate=sampling_rate, data=speech_values.cpu().numpy().squeeze())
