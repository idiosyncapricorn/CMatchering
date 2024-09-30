# waveform_plotting.py
import tkinter as tk
from tkinter import filedialog, messagebox
import librosa
import librosa.display
import matplotlib.pyplot as plt

class WaveformPlottingTab:
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # Label for additional features
        tk.Label(self.parent, text="Load an audio file to display its waveform:").pack(pady=20)

        # Button to load audio and plot waveform
        tk.Button(self.parent, text="Load and Plot Waveform", command=self.load_and_plot_waveform).pack(pady=10)

    def load_and_plot_waveform(self):
        # Open file dialog to select audio file
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if not file_path:
            return  # User canceled the dialog

        try:
            # Load the audio file
            audio, sample_rate = librosa.load(file_path, sr=None)

            # Plotting the waveform
            plt.figure(figsize=(12, 4))
            librosa.display.waveshow(audio, sr=sample_rate, alpha=0.5)
            plt.title('Waveform of ' + file_path)
            plt.xlabel('Time (s)')
            plt.ylabel('Amplitude')
            plt.grid()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading the audio file:\n{e}")
