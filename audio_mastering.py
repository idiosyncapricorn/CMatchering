# audio_mastering.py
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from mastering import process_mastering

class AudioMasteringTab:
    def __init__(self, parent):
        self.parent = parent
        self.target_path = ""

        self.create_widgets()

    def create_widgets(self):
        # Label for target file
        tk.Label(self.parent, text="Target File:").pack(pady=5)

        # Entry for target file path
        self.target_entry = tk.Entry(self.parent, width=50)
        self.target_entry.pack(pady=5)

        # Browse button for target file
        tk.Button(self.parent, text="Browse", command=self.browse_target).pack(pady=5)

        # Master button
        tk.Button(self.parent, text="Master Audio", command=self.master_audio).pack(pady=20)

    def browse_target(self):
        # Open file dialog to select target file
        self.target_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        self.target_entry.delete(0, tk.END)  # Clear previous entry
        self.target_entry.insert(0, self.target_path)  # Insert selected file path

    def master_audio(self):
        if not self.target_path:
            messagebox.showerror("Error", "Please select a target file.")
            return

        try:
            # Call the Cython process_mastering function
            process_mastering(self.target_path)
            messagebox.showinfo("Success", "Mastering completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during mastering:\n{e}")
