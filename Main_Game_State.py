import random
import game_framework
import Title_State
from pico2d import *

name = "MainGameState"
TitleImage = None
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
Max_Object = 7
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
        self.Radian = 32
        self.Die = False
        self.Score = 0
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
        if self.CY < -10:
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

    font = load_font('koverwatch.ttf', 40)
    RBC = 0
    BBC = 0
    RCC = 0
    BCC = 0

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


    del(TitleImage)
    del(RedCar)
    del(BlueCar)

    del(RedCircle)
    del(BlueCircle)
    del(RedBox)
    del(BlueBox)
    del(font)

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
                if BlueCar.state == BlueCar.STAND:
                    BlueCar.state = BlueCar.RIGHT
            elif event.key == SDLK_LEFT:
                if BlueCar.state == BlueCar.STAND:
                    BlueCar.state = BlueCar.LEFT
            if event.key == SDLK_LALT:
                if RedCar.state == RedCar.STAND:
                    RedCar.state = RedCar.RIGHT
            elif event.key == SDLK_LCTRL:
                if RedCar.state == RedCar.STAND:
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
    RedCar.draw()
    BlueCar.draw()
    font.draw(380, 670, '%5d' % (BlueCar.Score + RedCar.Score), (255, 255, 255))
    update_canvas()

def MakeObject():
    global RedCircle
    global BlueCircle
    global RedBox
    global BlueBox

    global RBC
    global BBC
    global RCC
    global BCC
    global Count
    Count += 1

    if Count == 400:
        Count = 0
        if RBC >= Max_Object:
            RBC = 0
        if BBC >= Max_Object:
            BBC = 0
        if RCC >= Max_Object:
            RCC = 0
        if BCC >= Max_Object:
            BCC = 0
        Rand = random.randint(0, 15)
        if Rand == 0:
            RedBox[RBC].CX = 56
            RedBox[RBC].CY = 750
            BlueBox[BBC].CX = 278
            BlueBox[BBC].CY = 750
            RBC += 1 % Max_Object
            BBC += 1 % Max_Object
        elif Rand == 1:
            RedBox[RBC].CX = 56
            RedBox[RBC].CY = 750
            BlueBox[BBC].CX = 389
            BlueBox[BBC].CY = 750
            RBC += 1 % Max_Object
            BBC += 1 % Max_Object
        elif Rand == 2:
            RedBox[RBC].CX = 56
            RedBox[RBC].CY = 750
            BlueCircle[BCC].CX = 278
            BlueCircle[BCC].CY = 750
            RBC += 1 % Max_Object
            BCC += 1 % Max_Object
        elif Rand == 3:
            RedBox[RBC].CX = 56
            RedBox[RBC].CY = 750
            BlueCircle[BCC].CX = 389
            BlueCircle[BCC].CY = 750
            RBC += 1 % Max_Object
            BCC += 1 % Max_Object
        elif Rand == 4:
            RedBox[RBC].CX = 167
            RedBox[RBC].CY = 750
            BlueBox[BBC].CX = 278
            BlueBox[BBC].CY = 750
            RBC += 1 % Max_Object
            BBC += 1 % Max_Object
        elif Rand == 5:
            RedBox[RBC].CX = 167
            RedBox[RBC].CY = 750
            BlueBox[BBC].CX = 389
            BlueBox[BBC].CY = 750
            RBC += 1 % Max_Object
            BBC += 1 % Max_Object
        elif Rand == 6:
            RedBox[RBC].CX = 167
            RedBox[RBC].CY = 750
            BlueCircle[BCC].CX = 278
            BlueCircle[BCC].CY = 750
            RBC += 1 % Max_Object
            BCC += 1 % Max_Object
        elif Rand == 7:
            RedBox[RBC].CX = 167
            RedBox[RBC].CY = 750
            BlueCircle[BCC].CX = 389
            BlueCircle[BCC].CY = 750
            RBC += 1 % Max_Object
            BCC += 1 % Max_Object
        elif Rand == 8:
            RedCircle[RCC].CX = 56
            RedCircle[RCC].CY = 750
            BlueBox[BBC].CX = 278
            BlueBox[BBC].CY = 750
            RCC += 1 % Max_Object
            BBC += 1 % Max_Object
        elif Rand == 9:
            RedCircle[RCC].CX = 56
            RedCircle[RCC].CY = 750
            BlueBox[BBC].CX = 389
            BlueBox[BBC].CY = 750
            RCC += 1 % Max_Object
            BBC += 1 % Max_Object
        elif Rand == 10:
            RedCircle[RCC].CX = 56
            RedCircle[RCC].CY = 750
            BlueCircle[BCC].CX = 278
            BlueCircle[BCC].CY = 750
            RCC += 1 % Max_Object
            BCC += 1 % Max_Object
        elif Rand == 11:
            RedCircle[RCC].CX = 56
            RedCircle[RCC].CY = 750
            BlueCircle[BCC].CX = 389
            BlueCircle[BCC].CY = 750
            RCC += 1 % Max_Object
            BCC += 1 % Max_Object
        elif Rand == 12:
            RedCircle[RCC].CX = 167
            RedCircle[RCC].CY = 750
            BlueBox[BBC].CX = 278
            BlueBox[BBC].CY = 750
            RCC += 1 % Max_Object
            BBC += 1 % Max_Object
        elif Rand == 13:
            RedCircle[RCC].CX = 167
            RedCircle[RCC].CY = 750
            BlueBox[BBC].CX = 389
            BlueBox[BBC].CY = 750
            RCC += 1 % Max_Object
            BBC += 1 % Max_Object
        elif Rand == 14:
            RedCircle[RCC].CX = 167
            RedCircle[RCC].CY = 750
            BlueCircle[BCC].CX = 278
            BlueCircle[BCC].CY = 750
            RCC += 1 % Max_Object
            BCC += 1 % Max_Object
        elif Rand == 15:
            RedCircle[RCC].CX = 167
            RedCircle[RCC].CY = 750
            BlueCircle[BCC].CX = 389
            BlueCircle[BCC].CY = 750
            RCC += 1 % Max_Object
            BCC += 1 % Max_Object

def Collision():
    global RedCar
    global BlueCar

    global RedCircle
    global BlueCircle
    global RedBox
    global BlueBox
    for redbox in RedBox:
        if((RedCar.CX - redbox.CX) * (RedCar.CX - redbox.CX) + (RedCar.CY - redbox.CY) * (RedCar.CY - redbox.CY) <= (
            RedCar.Radian + redbox.Radian) * (RedCar.Radian + redbox.Radian)):
            redbox.CX = 0
            redbox.CY = 0
            RedCar.Die = True
    for redcircle in RedCircle:
        if ((RedCar.CX - redcircle.CX) * (RedCar.CX - redcircle.CX) + (RedCar.CY - redcircle.CY) * (RedCar.CY - redcircle.CY) <= (
            RedCar.Radian + redcircle.Radian) * (RedCar.Radian + redcircle.Radian)):
            redcircle.CX = 0
            redcircle.CY = 0
            RedCar.Score += 1

    for bluebox in BlueBox:
        if((BlueCar.CX - bluebox.CX) * (BlueCar.CX - bluebox.CX) + (BlueCar.CY - bluebox.CY) * (BlueCar.CY - bluebox.CY) <= (
            BlueCar.Radian + bluebox.Radian) * (BlueCar.Radian + bluebox.Radian)):
            bluebox.CX = 0
            bluebox.CY = 0
            BlueCar.Die = True
    for bluecircle in BlueCircle:
        if ((BlueCar.CX - bluecircle.CX) * (BlueCar.CX - bluecircle.CX) + (BlueCar.CY - bluecircle.CY) * (BlueCar.CY - bluecircle.CY) <= (
            BlueCar.Radian + bluecircle.Radian) * (BlueCar.Radian + bluecircle.Radian)):
            bluecircle.CX = 0
            bluecircle.CY = 0
            BlueCar.Score += 1

    for redcircle in RedCircle:
        if redcircle.CX != 0:
            if redcircle.CY <= 0:
                RedCar.Die = True
    for bluecircle in BlueCircle:
        if bluecircle.CX != 0:
            if bluecircle.CY <= 0:
                BlueCar.Die = True

def update():

    global RedCar
    global BlueCar

    global RedCircle
    global BlueCircle
    global RedBox
    global BlueBox

    MakeObject()

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

    Collision()

    if BlueCar.Die == True or RedCar.Die == True:
        game_framework.push_state(Title_State)
def pause():
    pass


def resume():
    pass