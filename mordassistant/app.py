import os

import speech_recognition

from mordassistant.initializations import recognizer


def run():
    while True:
        try:
            audio_text = recognizer.get_text()
            recognizer.commands.get(audio_text.lower(), lambda: print("Команда не распознана."))()
        except speech_recognition.UnknownValueError:
            pass


if __name__ == "__main__":
    run()