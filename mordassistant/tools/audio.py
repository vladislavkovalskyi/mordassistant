from speech_recognition import Microphone


class Audio:
    def __init__(self):
        ...

    def _decode(self, microphones: dict):
        for device_id, name in microphones.items():
            print(f"{device_id}\t| {name}")

    def get_audio_devices(self) -> list:
        self._decode(Microphone.list_working_microphones())
        return


audio = Audio()
audio.get_audio_devices()
