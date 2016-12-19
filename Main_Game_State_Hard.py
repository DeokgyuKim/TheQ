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
GageRedImage = None
GageBlueImage = None
EmptyGageRedImage = None
EmptyGageBlueImage = None
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
Max_Object = 20
font = None
BGM = None
playerCount = 0


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
    global BGM
    global playerCount
    global EmptyGageRedImage
    global EmptyGageBlueImage


    font = load_font('NEXON Football Gothic L.otf', 35)
    RBC = 0
    BBC = 0
    RCC = 0
    BCC = 0
    playerCount = 2

    GageRedImage = load_image('icon_gage_red.png')
    GageBlueImage = load_image('icon_gage_blue.png')
    EmptyGageRedImage = load_image('icon_empty_gage_red.png')
    EmptyGageBlueImage = load_image('icon_empty_gage_blue.png')

    TitleImage = load_image('main_game_title.png')
    Pause = False
    Count = 0
    RedCar = Cars(3)
    BlueCar = Cars(4)

    RedCircle = [Circles(3) for i in range(Max_Object)]
    BlueCircle = [Circles(4) for i in range(Max_Object)]
    RedBox = [Boxs(3) for i in range(Max_Object)]
    BlueBox = [Boxs(4) for i in range(Max_Object)]

    f = open('Sound.txt', 'r')
    Sound_data = json.load(f)
    f.close()

    if Sound_data[0]['SOUND'] == 1:
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

    f = open('save_hard.txt', 'r')
    score_data = json.load(f)
    f.close()

    score_data.append({"REDCAR_TIME": RedCar.Die_time, "BLUECAR_TIME": BlueCar.Die_time, "TOTAL_TIME": RedCar.Die_time + BlueCar.Die_time})
    f = open('save_hard.txt', 'w')
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
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(Title_State)
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


def draw(frame_time):
    global RedCar
    global BlueCar

    global RedCircle
    global BlueCircle
    global RedBox
    global BlueBox
    global GageRedImage
    global GageBlueImage
    global EmptyGageRedImage
    global EmptyGageBlueImage

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
    if RedCar.Die == False:
        RedCar.draw(frame_time)
    if BlueCar.Die == False:
        BlueCar.draw(frame_time)

    GageRedImage.clip_draw(0, 0, RedCar.Gage, 37, RedCar.Gage / 2, 681)
    GageBlueImage.clip_draw(150 - BlueCar.Gage, 0, BlueCar.Gage, 37, 450 - (BlueCar.Gage / 2), 681)
    EmptyGageRedImage.draw(75, 681)
    EmptyGageBlueImage.draw(450 - 75, 681)


    if BlueCar.Die == False:
        font.draw(225, 670, '%4.2f' % BlueCar.life_frame, (255, 255, 255))
    elif RedCar.Die == False:
        font.draw(225, 670, '%4.2f' % RedCar.life_frame, (255, 255, 255))
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

    if (BlueCar.Object_time >= (1 / BlueCar.level) and BlueCar.Die == False) or (RedCar.Object_time >= (1 / RedCar.level) and RedCar.Die == False):
        BlueCar.Object_time = 0.0
        RedCar.Object_time = 0.0

        Rand = random.randint(0, 3)
        Rand_Red_or_Blue_Circle = random.randint(0, 4)
        if Rand == 0:
            RedBox[RBC].CX = 56
            RedBox[RBC].CY = 750
            BlueBox[BBC].CX = 278
            BlueBox[BBC].CY = 750
            RBC = (RBC + 1) % Max_Object
            BBC = (BBC + 1) % Max_Object
            if Rand_Red_or_Blue_Circle == 0:
                RedCircle[RCC].CX = 167
                RedCircle[RCC].CY = 750
                RCC = (RCC + 1) % Max_Object
            elif Rand_Red_or_Blue_Circle == 1:
                BlueCircle[BCC].CX = 389
                BlueCircle[BCC].CY = 750
                BCC = (BCC + 1) % Max_Object
        elif Rand == 1:
            RedBox[RBC].CX = 56
            RedBox[RBC].CY = 750
            BlueBox[BBC].CX = 389
            BlueBox[BBC].CY = 750
            RBC = (RBC + 1) % Max_Object
            BBC = (BBC + 1) % Max_Object
            if Rand_Red_or_Blue_Circle == 0:
                RedCircle[RCC].CX = 167
                RedCircle[RCC].CY = 750
                RCC = (RCC + 1) % Max_Object
            elif Rand_Red_or_Blue_Circle == 1:
                BlueCircle[BCC].CX = 278
                BlueCircle[BCC].CY = 750
                BCC = (BCC + 1) % Max_Object
        elif Rand == 2:
            RedBox[RBC].CX = 167
            RedBox[RBC].CY = 750
            BlueBox[BBC].CX = 278
            BlueBox[BBC].CY = 750
            RBC = (RBC + 1) % Max_Object
            BBC = (BBC + 1) % Max_Object
            if Rand_Red_or_Blue_Circle == 0:
                RedCircle[RCC].CX = 56
                RedCircle[RCC].CY = 750
                RCC = (RCC + 1) % Max_Object
            elif Rand_Red_or_Blue_Circle == 1:
                BlueCircle[BCC].CX = 389
                BlueCircle[BCC].CY = 750
                BCC = (BCC + 1) % Max_Object

        elif Rand == 3:
            RedBox[RBC].CX = 167
            RedBox[RBC].CY = 750
            BlueBox[BBC].CX = 389
            BlueBox[BBC].CY = 750
            RBC = (RBC + 1) % Max_Object
            BBC = (BBC + 1) % Max_Object
            if Rand_Red_or_Blue_Circle == 0:
                RedCircle[RCC].CX = 56
                RedCircle[RCC].CY = 750
                RCC = (RCC + 1) % Max_Object
            elif Rand_Red_or_Blue_Circle == 1:
                BlueCircle[BCC].CX = 278
                BlueCircle[BCC].CY = 750
                BCC = (BCC + 1) % Max_Object

def Collision(frame_time):
    global RedCar
    global BlueCar

    global RedCircle
    global BlueCircle
    global RedBox
    global BlueBox
    global playerCount
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
    if BlueCar.Die == False:
        if BlueCar.Gage <= 0:
            BlueCar.Die_time = BlueCar.life_frame
            BlueCar.Die = True
            playerCount -= 1
    if RedCar.Die == False:
        if RedCar.Gage <= 0:
            RedCar.Die_time = RedCar.life_frame
            RedCar.Die = True
            playerCount -= 1

def update(frame_time):

    global RedCar
    global BlueCar

    global RedCircle
    global BlueCircle
    global RedBox
    global BlueBox

    MakeObject(frame_time)

    RedCar.update(frame_time, playerCount)
    BlueCar.update(frame_time, playerCount)


    if RedCar.Die == False:
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
    elif BlueCar.Die == False:
        for redbox in RedBox:
            if redbox.CX != 0 and redbox.CY != 0:
                redbox.update(frame_time, BlueCar.level)
        for bluebox in BlueBox:
            if bluebox.CX != 0 and bluebox.CY != 0:
                bluebox.update(frame_time, BlueCar.level)
        for redcircle in RedCircle:
            if redcircle.CX != 0 and redcircle.CY != 0:
                redcircle.update(frame_time, BlueCar.level)
        for bluecircle in BlueCircle:
            if bluecircle.CX != 0 and bluecircle.CY != 0:
                bluecircle.update(frame_time, BlueCar.level)
    Collision(frame_time)

    if BlueCar.Die == True and RedCar.Die == True:
        game_framework.change_state(Title_State)
def pause():
    pass


def resume():
    pass