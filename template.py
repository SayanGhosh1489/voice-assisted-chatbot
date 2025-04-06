import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]: %(message)s:')

list_of_files = [
    "voice_chat/constants/__init__.py",
    "voice_chat/components/__init__.py",
    "voice_chat/components/speech_recognizer.py",
    "voice_chat/components/tts_engine.py",
    "voice_chat/components/spotify_controller.py",
    "voice_chat/components/camera_controller.py",
    "voice_chat/entity/__init__.py",
    "voice_chat/entity/config.py",
    "voice_chat/entity/artifact.py",
    "voice_chat/pipeline/__init__.py",
    "voice_chat/pipeline/assistant.py",
    "Notebooks/experiment.ipynb",
    "main.py",
    "voice_chat/logger.py",
    "voice_chat/exceptions.py",
]

def file_creator(list_of_files):
    for file in list_of_files:
        filepath = Path(file)
        filedir, filename = os.path.split(filepath)

        if filedir:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory; {filedir} for the file {filename}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, 'w') as f:
                pass
                logging.info(f"Creating empty file: {filepath}")

        else:
            logging.info(f"{filename} is already created")

    logging.info("All files are created successfully")

if __name__ == "__main__":
    file_creator(list_of_files)
