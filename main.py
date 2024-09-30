# main.py
import tkinter as tk
from tkinter import ttk
from audio_mastering import AudioMasteringTab
from waveform_plotting import WaveformPlottingTab

class MasteringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Mastering App")

        # Create a Notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        # Mastering Tab
        self.mastering_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.mastering_frame, text='Mastering')

        # Additional Tab
        self.additional_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.additional_frame, text='Additional Features')

        # Initialize the tab classes
        AudioMasteringTab(self.mastering_frame)
        WaveformPlottingTab(self.additional_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = MasteringApp(root)
    root.mainloop()
