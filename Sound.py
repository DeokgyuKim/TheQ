from pico2d import *

class Sounds():
    def __init__(self):
        self.bgm = load_wav('Main_Sound.wav')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

    def update(self, frame_time):
        pass

    def draw(self, frame_time):
        pass
    def __del__(self):
        del self.bgm