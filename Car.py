from pico2d import *
import  game_framework

class Cars:
    LEFT, RIGHT, STAND = 0, 1, 2
    RED, BLUE = 3, 4
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 40.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def handle_left(self, frame_time):
        if self.kind == self.RED:
            if self.CX <= 56:
                self.CX = 56
                self.state = self.STAND
            else:
                distance = Cars.RUN_SPEED_PPS * frame_time
                self.CX -= distance
        elif self.kind == self.BLUE:
            if self.CX <= 278:
                self.CX = 278
                self.state = self.STAND
            else:
                distance = Cars.RUN_SPEED_PPS * frame_time
                self.CX -= distance
    def handle_right(self, frame_time):
        if self.kind == self.RED:
            if self.CX >= 167:
                self.CX = 167
                self.state = self.STAND
            else:
                distance = Cars.RUN_SPEED_PPS * frame_time
                self.CX += distance
        elif self.kind == self.BLUE:
            if self.CX >= 389:
                self.CX = 389
                self.state = self.STAND
            else:
                distance = Cars.RUN_SPEED_PPS * frame_time
                self.CX += distance
    def handle_stand(self, frame_time):
        pass

    handle_state = {
        LEFT: handle_left,
        RIGHT: handle_right,
        STAND: handle_stand
    }

    def update(self, frame_time):
        if self.Die == False:
            self.life_frame += frame_time
        self.Object_time += frame_time
        self.level_time += frame_time
        if int(self.life_frame * 100) % 100 == 0:
            self.Gage -= 1
        if self.level_time >= 5:
            self.level_time = 0.0
            self.level = min(self.level * 1.1, 2.5)
        self.handle_state[self.state](self, frame_time)


    def __init__(self, kind):
        if kind == 3:
            self.CX, self.CY = 56, 100
        else:
            self.CX, self.CY = 389, 100
        self.Radian = 22
        self.Die = False
        self.Score = 0
        self.Gage = 150
        self.life_frame = 0.0
        self.level_time = 0.0
        self.Object_time = 0.0
        self.state = self.STAND
        self.level = 1.0
        self.Die_time = 0.0
        if kind == 3:
            self.kind = self.RED
        else:
            self.kind = self.BLUE
        if kind == 3:
            self.image = load_image('icon_car_red.png')
            self.left_image = load_image('icon_car_red_left_animaition.png')
            self.right_image = load_image('icon_car_red_right_animaition.png')
        else:
            self.image = load_image('icon_car_blue.png')
            self.left_image = load_image('icon_car_blue_left_animaition.png')
            self.right_image = load_image('icon_car_blue_right_animaition.png')

    def draw(self, frame_time):
        if self.state == self.STAND:
            self.image.draw(self.CX, self.CY)
        elif self.state == self.LEFT:
            if self.kind == self.RED:
                if (self.CX - 56) / 14 > 0 and (self.CX - 56) / 14 <= 1:
                    self.left_image.clip_draw(0, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 1 and (self.CX - 56) / 14 <= 2:
                    self.left_image.clip_draw(84, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 2 and (self.CX - 56) / 14 <= 3:
                    self.left_image.clip_draw(84 * 2, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 3 and (self.CX - 56) / 14 <= 4:
                    self.left_image.clip_draw(84 * 3, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 4 and (self.CX - 56) / 14 <= 5:
                    self.left_image.clip_draw(84 * 4, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 5 and (self.CX - 56) / 14 <= 6:
                    self.left_image.clip_draw(84 * 5, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 6 and (self.CX - 56) / 14 <= 7:
                    self.left_image.clip_draw(84 * 6, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 7 and (self.CX - 56) / 14 <= 8:
                    self.left_image.clip_draw(84 * 7, 0, 84, 84, self.CX, self.CY)
            elif self.kind == self.BLUE:
                if (self.CX - 278) / 14 > 0 and (self.CX - 278) / 14 <= 1:
                    self.left_image.clip_draw(0, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 1 and (self.CX - 278) / 14 <= 2:
                    self.left_image.clip_draw(84, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 2 and (self.CX - 278) / 14 <= 3:
                    self.left_image.clip_draw(84 * 2, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 3 and (self.CX - 278) / 14 <= 4:
                    self.left_image.clip_draw(84 * 3, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 4 and (self.CX - 278) / 14 <= 5:
                    self.left_image.clip_draw(84 * 4, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 5 and (self.CX - 278) / 14 <= 6:
                    self.left_image.clip_draw(84 * 5, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 6 and (self.CX - 278) / 14 <= 7:
                    self.left_image.clip_draw(84 * 6, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 7 and (self.CX - 278) / 14 <= 8:
                    self.left_image.clip_draw(84 * 7, 0, 84, 84, self.CX, self.CY)
        elif self.state == self.RIGHT:
            if self.kind == self.RED:
                if (self.CX - 56) / 14 > 0 and (self.CX - 56) / 14 <= 1:
                    self.right_image.clip_draw(0, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 1 and (self.CX - 56) / 14 <= 2:
                    self.right_image.clip_draw(84, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 2 and (self.CX - 56) / 14 <= 3:
                    self.right_image.clip_draw(84 * 2, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 3 and (self.CX - 56) / 14 <= 4:
                    self.right_image.clip_draw(84 * 3, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 4 and (self.CX - 56) / 14 <= 5:
                    self.right_image.clip_draw(84 * 4, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 5 and (self.CX - 56) / 14 <= 6:
                    self.right_image.clip_draw(84 * 5, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 6 and (self.CX - 56) / 14 <= 7:
                    self.right_image.clip_draw(84 * 6, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 56) / 14 > 7 and (self.CX - 56) / 14 <= 8:
                    self.right_image.clip_draw(84 * 7, 0, 84, 84, self.CX, self.CY)
            elif self.kind == self.BLUE:
                if (self.CX - 278) / 14 > 0 and (self.CX - 278) / 14 <= 1:
                    self.right_image.clip_draw(0, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 1 and (self.CX - 278) / 14 <= 2:
                    self.right_image.clip_draw(84, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 2 and (self.CX - 278) / 14 <= 3:
                    self.right_image.clip_draw(84 * 2, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 3 and (self.CX - 278) / 14 <= 4:
                    self.right_image.clip_draw(84 * 3, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 4 and (self.CX - 278) / 14 <= 5:
                    self.right_image.clip_draw(84 * 4, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 5 and (self.CX - 278) / 14 <= 6:
                    self.right_image.clip_draw(84 * 5, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 6 and (self.CX - 278) / 14 <= 7:
                    self.right_image.clip_draw(84 * 6, 0, 84, 84, self.CX, self.CY)
                if (self.CX - 278) / 14 > 7 and (self.CX - 278) / 14 <= 8:
                    self.right_image.clip_draw(84 * 7, 0, 84, 84, self.CX, self.CY)