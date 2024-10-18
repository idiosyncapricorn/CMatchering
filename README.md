# Audio Mastering App

This is a simple Audio Mastering desktop application built using Python's `Tkinter` library. The app provides a graphical interface for mastering audio and visualizing waveforms. It is based on the [Matchering](https://github.com/sergree/matchering) Python library for reference audio mastering, but it has been converted to **Cython** for improved performance and includes a basic UI built on `Tkinter`.

## Features
- **Mastering Tab:** Includes tools for basic audio mastering functionalities, leveraging the power of the Matchering library with support for mastering audio files via **URLs**.
- **Additional Features Tab:** Allows for waveform plotting and other audio-related functionalities.
- **Download as ZIP:** The app processes and downloads the mastered audio as a ZIP file, ensuring easy access and organization of the output files.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- `tkinter` (comes with most Python installations)
- Required Python libraries (install via `requirements.txt`)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/audio-mastering-app.git

	2.	Navigate to the project directory:

cd audio-mastering-app


	3.	Install the required Python packages:

pip install -r requirements.txt

Make sure to install any additional dependencies needed for audio_mastering and waveform_plotting.

Cython Conversion

The core mastering functionality from the Matchering library has been converted to Cython for performance optimization. Make sure Cython is installed:

pip install cython

You can compile the Cython modules by running:

python setup.py build_ext --inplace

Usage

	1.	Run the main.py script to launch the app:

python main.py


	2.	The application window will open with two tabs:
	•	Mastering: Tools for mastering audio from a URL. Simply input the URL of your target audio file, and the app will process it directly without needing to save files locally. Once the process is complete, the mastered audio files will be downloaded as a ZIP file.
	•	Additional Features: Tools for waveform plotting and other audio-related functionalities.