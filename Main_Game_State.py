import random
import game_framework
import Title_State
from Car import Cars
from Box import Boxs
from Circle import Circles
from Sound import Sounds
from pico2d import *

name = "MainGameState"
TitleImage = None
x = None
y = None
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
Max_Object = 7
font = None
BGM = None

def enter():
    global TitleImage
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
    global BGM

    font = load_font('koverwatch.ttf', 40)
    RBC = 0
    BBC = 0
    RCC = 0
    BCC = 0

    TitleImage = load_image('main_game_title.png')
    RedCar = Cars(3)
    BlueCar = Cars(4)

    RedCircle = [Circles(3) for i in range(Max_Object)]
    BlueCircle = [Circles(4) for i in range(Max_Object)]
    RedBox = [Boxs(3) for i in range(Max_Object)]
    BlueBox = [Boxs(4) for i in range(Max_Object)]

    f = open('Sound.txt', 'r')
    Sound_data = json.load(f)
    f.close()

    if Sound_data[0]['SOUND'] != 0:
        BGM = Sounds()

    game_framework.reset_time()
def exit():
    global TitleImage
    global RedCar
    global BlueCar

    global RedCircle
    global BlueCircle
    global RedBox
    global BlueBox
    global font
    global BGM

    f = open('save_normal.txt', 'r')
    score_data = json.load(f)
    f.close()

    score_data.append({"REDCAR_SCORE": RedCar.Score, "BLUECAR_SCORE": BlueCar.Score, "TOTAL_SCORE": RedCar.Score + BlueCar.Score})
    f = open('save_normal.txt', 'w')
    json.dump(score_data, f)
    f.close()

    del(TitleImage)
    del(RedCar)
    del(BlueCar)

    del(RedCircle)
    del(BlueCircle)
    del(RedBox)
    del(BlueBox)
    del(font)
    del(BGM)
def handle_events(frame_time):
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(Title_State)
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
def draw(frame_time):
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
            redbox.draw(frame_time)
    for bluebox in BlueBox:
        if bluebox.CX != 0 and bluebox.CY != 0:
            bluebox.draw(frame_time)
    for redcircle in RedCircle:
        if redcircle.CX != 0 and redcircle.CY != 0:
            redcircle.draw(frame_time)
    for bluecircle in BlueCircle:
        if bluecircle.CX != 0 and bluecircle.CY != 0:
            bluecircle.draw(frame_time)
    RedCar.draw(frame_time)
    BlueCar.draw(frame_time)
    font.draw(380, 670, '%5d' % (BlueCar.Score + RedCar.Score), (255, 255, 255))
    update_canvas()
def MakeObject(frame_time):
    global RedCircle
    global BlueCircle
    global RedBox
    global BlueBox
    global RedCar
    global BlueCar

    global RBC
    global BBC
    global RCC
    global BCC
    global Count

    if (BlueCar.Object_time >= (2 / BlueCar.level) and BlueCar.Die == False) or (RedCar.Object_time >= (2 / RedCar.level) and RedCar.Die == False):
        BlueCar.Object_time = 0.0
        RedCar.Object_time = 0.0

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
def Collision(frame_time):
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
            RedCar.Die_time = RedCar.life_frame
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
            BlueCar.Die_time = BlueCar.life_frame
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
def update(frame_time):

    global RedCar
    global BlueCar

    global RedCircle
    global BlueCircle
    global RedBox
    global BlueBox

    MakeObject(frame_time)

    RedCar.update(frame_time)
    BlueCar.update(frame_time)

    for redbox in RedBox:
        if redbox.CX != 0 and redbox.CY != 0:
            redbox.update(frame_time, RedCar.level)
    for bluebox in BlueBox:
        if bluebox.CX != 0 and bluebox.CY != 0:
            bluebox.update(frame_time, RedCar.level)
    for redcircle in RedCircle:
        if redcircle.CX != 0 and redcircle.CY != 0:
            redcircle.update(frame_time, RedCar.level)
    for bluecircle in BlueCircle:
        if bluecircle.CX != 0 and bluecircle.CY != 0:
            bluecircle.update(frame_time, RedCar.level)

    Collision(frame_time)

    if BlueCar.Die == True or RedCar.Die == True:
        game_framework.push_state(Title_State)
def pause():
    pass


def resume():
    pass