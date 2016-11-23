import random
import game_framework
import Title_State
from pico2d import *

name = "MainGameState"
TitleImage = None
GageRedImage = None
GageBlueImage = None
x = None
y = None
Pause = False
Count = 0
RedCar = None
BlueCar = None
RedCircle = None
BlueCircle = None
RedBox = None
BlueBox = None
RBC = 0
BBC = 0
RCC = 0
BCC = 0
Count = 0
CountCircle = 0
Max_Object = 20
font = None


class Cars:
    LEFT, RIGHT, STAND = 0, 1, 2
    RED, BLUE = 3, 4

    def handle_left(self):
        if self.kind == self.RED:
            if self.CX <= 56:
                self.CX = 56
                self.state = self.STAND
            else:
                self.CX -= 1
        elif self.kind == self.BLUE:
            if self.CX <= 278:
                self.CX = 278
                self.state = self.STAND
            else:
                self.CX -= 1
    def handle_right(self):
        if self.kind == self.RED:
            if self.CX >= 167:
                self.CX = 167
                self.state = self.STAND
            else:
                self.CX += 1
        elif self.kind == self.BLUE:
            if self.CX >= 389:
                self.CX = 389
                self.state = self.STAND
            else:
                self.CX += 1
    def handle_stand(self):
        pass

    handle_state = {
        LEFT: handle_left,
        RIGHT: handle_right,
        STAND: handle_stand
    }

    def update(self):
        self.handle_state[self.state](self)


    def __init__(self, kind):
        if kind == 3:
            self.CX, self.CY = 56, 100
        else:
            self.CX, self.CY = 389, 100
        self.Radian = 22
        self.Die = False
        self.Score = 0
        self.Gage = 150
        self.state = self.STAND
        if kind == 3:
            self.kind = self.RED
        else:
            self.kind = self.BLUE
        if kind == 3:
            self.image = load_image('icon_car_red.png')
        else:
            self.image = load_image('icon_car_blue.png')

    def draw(self):
        self.image.draw(self.CX, self.CY)
class Object:
    def __init__(self, kind):
        self.Radian = 20
        self.CX, self.CY = 0, 0
class Boxs(Object):
    RED, BLUE = 3, 4
    def __init__(self, kind):
        self.Radian = 20
        self.CX, self.CY = 0, 0
        if kind == 3:
            self.kind = self.RED
        else:
            self.kind = self.BLUE
        if kind == 3:
            self.image = load_image('icon_box_red.png')
        else:
            self.image = load_image('icon_box_blue.png')

    def update(self):
        self.CY -= 1
        if self.CY <= -10:
            self.CX = 0
            self.CY = 0

    def draw(self):
        self.image.draw(self.CX, self.CY)
class Circles(Object):
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

    def update(self):
        self.CY -= 1
        if self.CY <= -10:
            self.CX = 0
            self.CY = 0
            #game_framework.change_state(Score_State)

    def draw(self):
        self.image.draw(self.CX, self.CY)

def enter():
    global GageRedImage
    global GageBlueImage
    global TitleImage
    global Pause, Count
    global RedCar
    global BlueCar
    global RedCircle
    global BlueCircle
    global RedBox
    global BlueBox
    global RBC
    global BBC
    global RCC
    global BCC
    global Max_Object
    global font
    global CountCircle

    font = load_font('koverwatch.ttf', 40)
    RBC = 0
    BBC = 0
    RCC = 0
    BCC = 0
    CountCircle = 0

    GageRedImage = load_image('icon_gage_red.png')
    GageBlueImage = load_image('icon_gage_blue.png')

    TitleImage = load_image('main_game_title.png')
    Pause = False
    Count = 0
    RedCar = Cars(3)
    BlueCar = Cars(4)

    RedCircle = [Circles(3) for i in range(Max_Object)]
    BlueCircle = [Circles(4) for i in range(Max_Object)]
    RedBox = [Boxs(3) for i in range(Max_Object)]
    BlueBox = [Boxs(4) for i in range(Max_Object)]

def exit():
    global TitleImage
    global RedCar
    global BlueCar

    global RedCircle
    global BlueCircle
    global RedBox
    global BlueBox
    global font


    #del(TitleImage)
    #del(RedCar)
    #del(BlueCar)

    #del(RedCircle)
    #del(BlueCircle)
    #del(RedBox)
    #del(BlueBox)
    #del(font)

def handle_events():
    global x, y, Pause
    global Count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                Pause = True
            if event.key == SDLK_RIGHT:
                #if BlueCar.state == BlueCar.STAND:
                BlueCar.state = BlueCar.RIGHT
            elif event.key == SDLK_LEFT:
                #if BlueCar.state == BlueCar.STAND:
                BlueCar.state = BlueCar.LEFT
            if event.key == SDLK_LALT:
                #if RedCar.state == RedCar.STAND:
                RedCar.state = RedCar.RIGHT
            elif event.key == SDLK_LCTRL:
                #if RedCar.state == RedCar.STAND:
                RedCar.state = RedCar.LEFT


        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, 599 - event.y
            pass
        if Pause != True:
            if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                x, y = event.x, 599 - event.y
                pass
        else:
            Count += 1
            if(Count == 10):
                if(Pause == True):
                    #game_framework.push_state(Pause_state)
                    pass
            game_framework.change_state(Title_State)


def draw():
    global RedCar
    global BlueCar

    global RedCircle
    global BlueCircle
    global RedBox
    global BlueBox
    global GageRedImage
    global GageBlueImage

    clear_canvas()
    TitleImage.draw(222, 350)
    for redbox in RedBox:
        if redbox.CX != 0 and redbox.CY != 0:
            redbox.draw()
    for bluebox in BlueBox:
        if bluebox.CX != 0 and bluebox.CY != 0:
            bluebox.draw()
    for redcircle in RedCircle:
        if redcircle.CX != 0 and redcircle.CY != 0:
            redcircle.draw()
    for bluecircle in BlueCircle:
        if bluecircle.CX != 0 and bluecircle.CY != 0:
            bluecircle.draw()
    if RedCar.Die == False:
        RedCar.draw()
    if BlueCar.Die == False:
        BlueCar.draw()

    GageRedImage.clip_draw(0, 0, RedCar.Gage, 37, RedCar.Gage / 2, 681)
    GageBlueImage.clip_draw(150 - BlueCar.Gage, 0, BlueCar.Gage, 37, 450 - (BlueCar.Gage / 2), 681)

    font.draw(225, 670, '%5d' % (BlueCar.Score + RedCar.Score), (255, 255, 255))
    update_canvas()

def update():

    global RedCar
    global BlueCar

    global RedCircle
    global BlueCircle
    global RedBox
    global BlueBox

    global RBC
    global BBC
    global RCC
    global BCC
    global Count
    global CountCircle

    Count += 1
    CountCircle += 1

    if Count == 200:
        Count = 0
        if RBC >= Max_Object:
            RBC = 0
        if BBC >= Max_Object:
            BBC = 0
        if RCC >= Max_Object:
            RCC = 0
        if BCC >= Max_Object:
            BCC = 0
        Rand1 = random.randint(0, 2)
        Rand1_Pos = random.randint(56, 167)
        Rand2_Pos = random.randint(278, 389)
        Rand3_Pos = random.randint(56, 167)
        while (not(Rand1_Pos + 30 <= Rand3_Pos or Rand1_Pos - 30 >= Rand3_Pos)):
            Rand3_Pos = random.randint(56, 167)
        Rand4_Pos = random.randint(278, 389)
        while (not(Rand2_Pos + 30 <= Rand4_Pos or Rand2_Pos - 30 >= Rand4_Pos)):
            Rand4_Pos = random.randint(278, 389)


        RedBox[RBC].CX = Rand1_Pos
        RedBox[RBC].CY = 750
        RBC += 1
        if CountCircle == 600:
            RedCircle[RCC].CX = Rand3_Pos
            RedCircle[RCC].CY = 750
            RCC += 1

        BlueBox[BBC].CX = Rand2_Pos
        BlueBox[BBC].CY = 750
        BBC += 1
        if CountCircle == 600:
            CountCircle = 0
            BlueCircle[BCC].CX = Rand4_Pos
            BlueCircle[BCC].CY = 750
            BCC += 1



    RedCar.update()
    BlueCar.update()

    for redbox in RedBox:
        if redbox.CX != 0 and redbox.CY != 0:
            redbox.update()
    for bluebox in BlueBox:
        if bluebox.CX != 0 and bluebox.CY != 0:
            bluebox.update()
    for redcircle in RedCircle:
        if redcircle.CX != 0 and redcircle.CY != 0:
            redcircle.update()
    for bluecircle in BlueCircle:
        if bluecircle.CX != 0 and bluecircle.CY != 0:
            bluecircle.update()

    if RedCar.Die == False:
        for redbox in RedBox:
            if((RedCar.CX - redbox.CX) * (RedCar.CX - redbox.CX) + (RedCar.CY - redbox.CY) * (RedCar.CY - redbox.CY) <= (
                RedCar.Radian + redbox.Radian) * (RedCar.Radian + redbox.Radian)):
                if(redbox.CX != 0 and redbox.CY != 0):
                    redbox.CX = 0
                    redbox.CY = 0
                    RedCar.Gage -= 20
        for redcircle in RedCircle:
            if ((RedCar.CX - redcircle.CX) * (RedCar.CX - redcircle.CX) + (RedCar.CY - redcircle.CY) * (RedCar.CY - redcircle.CY) <= (
                RedCar.Radian + redcircle.Radian) * (RedCar.Radian + redcircle.Radian)):
                if (redcircle.CX != 0 and redcircle.CY != 0):
                    redcircle.CX = 0
                    redcircle.CY = 0
                    RedCar.Gage += 10
                    if(RedCar.Gage > 150):
                        RedCar.Gage = 150

    if BlueCar.Die == False:
        for bluecircle in BlueCircle:
            if ((BlueCar.CX - bluecircle.CX) * (BlueCar.CX - bluecircle.CX) + (BlueCar.CY - bluecircle.CY) * (BlueCar.CY - bluecircle.CY) <= (
                    BlueCar.Radian + bluecircle.Radian) * (BlueCar.Radian + bluecircle.Radian)):
                if (bluecircle.CX != 0 and bluecircle.CY != 0):
                    bluecircle.CX = 0
                    bluecircle.CY = 0
                    BlueCar.Gage += 10
                    if (BlueCar.Gage > 150):
                        BlueCar.Gage = 150
        for bluebox in BlueBox:
            if((BlueCar.CX - bluebox.CX) * (BlueCar.CX - bluebox.CX) + (BlueCar.CY - bluebox.CY) * (BlueCar.CY - bluebox.CY) <= (
                BlueCar.Radian + bluebox.Radian) * (BlueCar.Radian + bluebox.Radian)):
                if (bluebox.CX != 0 and bluebox.CY != 0):
                    bluebox.CX = 0
                    bluebox.CY = 0
                    BlueCar.Gage -= 20
    if BlueCar.Gage <= 0:
        BlueCar.Die = True
    elif RedCar.Gage <= 0:
        RedCar.Die = True

    if BlueCar.Die == True and RedCar.Die == True:
        game_framework.push_state(Title_State)
def pause():
    pass


def resume():
    pass