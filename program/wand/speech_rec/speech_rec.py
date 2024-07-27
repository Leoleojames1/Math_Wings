import speech_recognition as sr

class speech_rec:
    def __init__(self, colors):
        self.color_dict = colors
        self.auto_speech_flag = False

    def recognize_speech(self, audio):
        """ a method for calling the speech recognizer
            args: audio
            returns: speech_str
        """
        #TODO Realized current implementation calls google API, must replace with LOCAL SPEECH RECOGNITION MODEL WHISPER
        speech_str = self.recognizer.recognize_google(audio)
        print(self.color_dict["GREEN"] + f"<<<👂 SPEECH RECOGNIZED 👂 >>> " + self.color_dict["OKBLUE"] + f"{speech_str}")
        return speech_str