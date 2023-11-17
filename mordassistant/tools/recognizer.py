import speech_recognition
from .command import Command


class Recognizer(speech_recognition.Recognizer, Command):
    def __init__(self):
        # Здесь я использовал явный вызов конструктора, потому что super()
        # перекрывал всё
        speech_recognition.Recognizer.__init__(self)
        Command.__init__(self)

        self.pause_threshold = .5

    def get_text(self):
        with speech_recognition.Microphone(device_index=23) as mic:
            self.adjust_for_ambient_noise(source=mic, duration=.5)
            print("> Произнесите команду")
            audio = self.listen(source=mic)
            query = self.recognize_google(audio_data=audio, language="ru-RU")
            print(f"> Реагирую на \"{query}\"")

        return query.lower()

    def load_command(self, command: Command):
        for keyword, func in command.commands.items():
            self.commands[keyword] = func
