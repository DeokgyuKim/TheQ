from pico2d import *

class Circles():
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 40.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    RED, BLUE = 3, 4
    def __init__(self, kind):
        self.Radian = 20
        self.CX, self.CY = 0, 0
        if kind == 3:
            self.kind = self.RED
        else:
            self.kind = self.BLUE
        if kind == 3:
            self.image = load_image('icon_circle_red.png')
        else:
            self.image = load_image('icon_circle_blue.png')

    def update(self, frame_time, level):
        distance = Circles.RUN_SPEED_PPS * frame_time * level
        self.CY -= distance
        if self.CY <= -10:
            self.CX = 0
            self.CY = 0
            #game_framework.change_state(Score_State)

    def draw(self, frame_time):
        self.image.draw(self.CX, self.CY)