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
        self.X1, self.Y1 = 0, 0
        self.X2, self.Y2 = 0, 0
        self.X3, self.Y3 = 0, 0
        self.X4, self.Y4 = 0, 0
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
class Boxs:
    RED, BLUE = 3, 4
    def __init__(self, kind):
        self.left, self.top, self.right, self.bottom = 0, 0, 0, 0
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
        if self.CY <= 0:
            self.CX = 0
            self.CY = 0

    def draw(self):
        self.image.draw(self.CX, self.CY)


class Circles:
    RED, BLUE = 3, 4
    def __init__(self, kind):
        self.radian = 21
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
        if self.CY <= 0:
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


    del(TitleImage)
    del(RedCar)
    del(BlueCar)

    del(RedCircle)
    del(BlueCircle)
    del(RedBox)
    del(BlueBox)

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
            RBC += 1
            BBC += 1
        elif Rand == 1:
            RedBox[RBC].CX = 56
            RedBox[RBC].CY = 750
            BlueBox[BBC].CX = 389
            BlueBox[BBC].CY = 750
            RBC += 1
            BBC += 1
        elif Rand == 2:
            RedBox[RBC].CX = 56
            RedBox[RBC].CY = 750
            BlueCircle[BCC].CX = 278
            BlueCircle[BCC].CY = 750
            RBC += 1
            BCC += 1
        elif Rand == 3:
            RedBox[RBC].CX = 56
            RedBox[RBC].CY = 750
            BlueCircle[BCC].CX = 389
            BlueCircle[BCC].CY = 750
            RBC += 1
            BCC += 1
        elif Rand == 4:
            RedBox[RBC].CX = 167
            RedBox[RBC].CY = 750
            BlueBox[BBC].CX = 278
            BlueBox[BBC].CY = 750
            RBC += 1
            BBC += 1
        elif Rand == 5:
            RedBox[RBC].CX = 167
            RedBox[RBC].CY = 750
            BlueBox[BBC].CX = 389
            BlueBox[BBC].CY = 750
            RBC += 1
            BBC += 1
        elif Rand == 6:
            RedBox[RBC].CX = 167
            RedBox[RBC].CY = 750
            BlueCircle[BCC].CX = 278
            BlueCircle[BCC].CY = 750
            RBC += 1
            BCC += 1
        elif Rand == 7:
            RedBox[RBC].CX = 167
            RedBox[RBC].CY = 750
            BlueCircle[BCC].CX = 389
            BlueCircle[BCC].CY = 750
            RBC += 1
            BCC += 1
        elif Rand == 8:
            RedCircle[RCC].CX = 56
            RedCircle[RCC].CY = 750
            BlueBox[BBC].CX = 278
            BlueBox[BBC].CY = 750
            RCC += 1
            BBC += 1
        elif Rand == 9:
            RedCircle[RCC].CX = 56
            RedCircle[RCC].CY = 750
            BlueBox[BBC].CX = 389
            BlueBox[BBC].CY = 750
            RCC += 1
            BBC += 1
        elif Rand == 10:
            RedCircle[RCC].CX = 56
            RedCircle[RCC].CY = 750
            BlueCircle[BCC].CX = 278
            BlueCircle[BCC].CY = 750
            RCC += 1
            BCC += 1
        elif Rand == 11:
            RedCircle[RCC].CX = 56
            RedCircle[RCC].CY = 750
            BlueCircle[BCC].CX = 389
            BlueCircle[BCC].CY = 750
            RCC += 1
            BCC += 1
        elif Rand == 12:
            RedCircle[RCC].CX = 167
            RedCircle[RCC].CY = 750
            BlueBox[BBC].CX = 278
            BlueBox[BBC].CY = 750
            RCC += 1
            BBC += 1
        elif Rand == 13:
            RedCircle[RCC].CX = 167
            RedCircle[RCC].CY = 750
            BlueBox[BBC].CX = 389
            BlueBox[BBC].CY = 750
            RCC += 1
            BBC += 1
        elif Rand == 14:
            RedCircle[RCC].CX = 167
            RedCircle[RCC].CY = 750
            BlueCircle[BCC].CX = 278
            BlueCircle[BCC].CY = 750
            RCC += 1
            BCC += 1
        elif Rand == 15:
            RedCircle[RCC].CX = 167
            RedCircle[RCC].CY = 750
            BlueCircle[BCC].CX = 389
            BlueCircle[BCC].CY = 750
            RCC += 1
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


def pause():
    pass


def resume():
    pass