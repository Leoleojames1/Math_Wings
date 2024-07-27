import speech_rec as sr

class speech_recognizer_class:
    def __init__(self, colors):
        self.auto_speech_flag = False

    def recognize_speech(self, audio):
        """ a method for calling the speech recognizer
            args: audio
            returns: speech_str
        """
        #TODO Realized current implementation calls google API, must replace with LOCAL SPEECH RECOGNITION MODEL WHISPER
        speech_str = self.recognizer.recognize_google(audio)
        print(self.colors["GREEN"] + f"<<<👂 SPEECH RECOGNIZED 👂 >>> " + self.colors["OKBLUE"] + f"{speech_str}")
        return speech_str