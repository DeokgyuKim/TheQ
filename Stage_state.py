import game_framework
import Title_State
import Main_Game_State
import Main_Game_State_Hard
from pico2d import *

name = "StageState"
TitleImage = None
EasyButtonImageOn = None
NormalButtonImageOn = None
HardButtonImageOn = None
SoundButtonImageOn = None
ScoreButtonImageOn = None
TipButtonImageOn = None

EasyButtonImageClick = None
NormalButtonImageClick = None
HardButtonImageClcik = None
SoundButtonImageClick = None
ScoreButtonImageClick = None
TipButtonImageClick = None

x = None
y = None
EasyButton_Click = False
NormalButton_Click = False
HardButton_Click = False
SoundButton_Click = False
ScoreButton_Click = False
TipButton_Click = False

EasyButton_On = False
NormalButton_On = False
HardButton_On = False
SoundButton_On = False
ScoreButton_On = False
TipButton_On = False

Easy = False
Normal = False
Hard = False
Score = False
Tip = False
Count = 0

def enter():
    global TitleImage
    global EasyButtonImageOn
    global NormalButtonImageOn
    global HardButtonImageOn
    global SoundButtonImageOn
    global ScoreButtonImageOn
    global TipButtonImageOn

    global EasyButtonImageClick
    global NormalButtonImageClick
    global HardButtonImageClick
    global SoundButtonImageClick
    global ScoreButtonImageClick
    global TipButtonImageClick

    global x
    global y
    global EasyButton_Click
    global NormalButton_Click
    global HardButton_Click
    global SoundButton_Click
    global ScoreButton_Click
    global TipButton_Click
    global EasyButton_On
    global NormalButton_On
    global HardButton_On
    global SoundButton_On
    global ScoreButton_On
    global TipButton_On
    global Easy
    global Normal
    global Hard
    global Score
    global Tip
    global Count

    x = None
    y = None
    EasyButton_Click = False
    NormalButton_Click = False
    HardButton_Click = False
    SoundButton_Click = False
    ScoreButton_Click = False
    TipButton_Click = False
    EasyButton_On = False
    NormalButton_On = False
    HardButton_On = False
    SoundButton_On = False
    ScoreButton_On = False
    TipButton_On = False
    Easy = False
    Normal = False
    Hard = False
    Score = False
    Tip = False
    Count = 0

    TitleImage = load_image('stage_title.png')
    EasyButtonImageOn = load_image('icon_easy_on.png')
    NormalButtonImageOn = load_image('icon_normal_on.png')
    HardButtonImageOn = load_image('icon_hard_on.png')
    SoundButtonImageOn = load_image('icon_sound_on.png')
    ScoreButtonImageOn = load_image('icon_score_on.png')
    TipButtonImageOn = load_image('icon_tip_on.png')

    EasyButtonImageClick = load_image('icon_easy_click.png')
    NormalButtonImageClick = load_image('icon_normal_click.png')
    HardButtonImageClick = load_image('icon_hard_click.png')
    SoundButtonImageClick = load_image('icon_sound_click.png')
    ScoreButtonImageClick = load_image('icon_score_click.png')
    TipButtonImageClick = load_image('icon_tip_click.png')

def exit():
    global TitleImage
    global EasyButtonImageOn
    global NormalButtonImageOn
    global HardButtonImageOn
    global SoundButtonImageOn
    global ScoreButtonImageOn
    global TipButtonImageOn

    global EasyButtonImageClick
    global NormalButtonImageClick
    global HardButtonImageClick
    global SoundButtonImageClick
    global ScoreButtonImageClick
    global TipButtonImageClick

    del(TitleImage)
    del(EasyButtonImageOn)
    del(NormalButtonImageOn)
    del(HardButtonImageOn)
    del(SoundButtonImageOn)
    del(ScoreButtonImageOn)
    del(TipButtonImageOn)

    del(EasyButtonImageClick)
    del(NormalButtonImageClick)
    del(HardButtonImageClick)
    del(SoundButtonImageClick)
    del(ScoreButtonImageClick)
    del(TipButtonImageClick)

def handle_events():
    global x, y
    global Easy, Normal, Hard, Score, Tip, Count
    global EasyButton_Click
    global NormalButton_Click
    global HardButton_Click
    global SoundButton_Click
    global ScoreButton_Click
    global TipButton_Click

    global EasyButton_On
    global NormalButton_On
    global HardButton_On
    global SoundButton_On
    global ScoreButton_On
    global TipButton_On
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(Title_State)
        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, 599 - event.y
            if (x >= 134 and x <= 314 and y >= 225 and y <= 275 or ((x - 134.0) * (x - 134.0)) + ((y - 250.0) * (y - 250.0)) <= 25 * 25 or ((x - 314.0) * (x - 314.0)) + ((y - 250.0) * (y - 250.0)) <= 25 * 25):
                NormalButton_On = True
            elif (x >= 134 and x <= 314 and y >= 150 and y <= 200 or ((x - 134.0) * (x - 134.0)) + ((y - 175.0) * (y - 175.0)) <= 25 * 25 or ((x - 314.0) * (x - 314.0)) + ((y - 175.0) * (y - 175.0)) <= 25 * 25):
                HardButton_On = True
            elif(((x - 126.0) * (x - 126.0)) + ((y - 100.0) * (y - 100.0)) <= 25 * 25):
                ScoreButton_On = True
            elif (((x - 222.0) * (x - 222.0)) + ((y - 100.0) * (y - 100.0)) <= 25 * 25):
                SoundButton_On = True
            elif (((x - 318.0) * (x - 318.0)) + ((y - 100.0) * (y - 100.0)) <= 25 * 25):
                TipButton_On = True
            else:
                EasyButton_On = False
                NormalButton_On = False
                HardButton_On = False
                ScoreButton_On = False
                SoundButton_On = False
                TipButton_On = False
        if Easy != True and Normal != True and Hard != True and Score != True and Tip != True:
            if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                x, y = event.x, 599 - event.y
                if (x >= 134 and x <= 314 and y >= 225 and y <= 275 or ((x - 134.0) * (x - 134.0)) + (
                    (y - 250.0) * (y - 250.0)) <= 25 * 25 or ((x - 314.0) * (x - 314.0)) + (
                    (y - 250.0) * (y - 250.0)) <= 25 * 25):
                    if NormalButton_Click == True:
                        NormalButton_Click = False
                    else:
                        NormalButton_Click = True
                        Normal = True
                elif (x >= 134 and x <= 314 and y >= 150 and y <= 200 or ((x - 134.0) * (x - 134.0)) + (
                    (y - 175.0) * (y - 175.0)) <= 25 * 25 or ((x - 314.0) * (x - 314.0)) + (
                    (y - 175.0) * (y - 175.0)) <= 25 * 25):
                    if HardButton_Click == True:
                        HardButton_Click = False
                    else:
                        HardButton_Click = True
                        Hard = True
                if (((x - 126.0) * (x - 126.0)) + ((y - 100.0) * (y - 100.0)) <= 25 * 25):
                    if ScoreButton_Click == True:
                        ScoreButton_Click = False
                    else:
                        ScoreButton_Click = True
                        Score = True
                if (((x - 222.0) * (x - 222.0)) + ((y - 100.0) * (y - 100.0)) <= 25 * 25):
                    if SoundButton_Click == True:
                        SoundButton_Click = False
                    else:
                        SoundButton_Click = True
                if (((x - 318.0) * (x - 318.0)) + ((y - 100.0) * (y - 100.0)) <= 25 * 25):
                    if TipButton_Click == True:
                        TipButton_Click = False
                    else:
                        TipButton_Click = True
                        Tip = True
        else:
            Count += 1
            if(Count == 10):
                if(Normal == True):
                    game_framework.change_state(Main_Game_State)
                    pass
                elif(Hard == True):
                    game_framework.change_state(Main_Game_State_Hard)
                #elif(Score == True):
                    #Score_State
                    #pass
                #elif(Tip == True):
                    #Tip_State
                    #pass
            #game_framework.quit()


def draw():
    clear_canvas()
    TitleImage.draw(222, 350)
    if EasyButton_Click == True:
        EasyButtonImageClick.draw(221, 425)
    elif EasyButton_On == True:
        EasyButtonImageOn.draw(221, 425)
    if NormalButton_Click == True:
        NormalButtonImageClick.draw(222, 350)
    elif NormalButton_On == True:
        NormalButtonImageOn.draw(223, 350)
    if HardButton_Click == True:
        HardButtonImageClick.draw(222, 275)
    elif HardButton_On == True:
        HardButtonImageOn.draw(223, 275)
    if ScoreButton_Click == True:
        ScoreButtonImageClick.draw(123, 200)
    elif ScoreButton_On == True:
        ScoreButtonImageOn.draw(122, 200)
    if SoundButton_Click == True:
        SoundButtonImageClick.draw(219, 200)
    elif SoundButton_On == True:
        SoundButtonImageOn.draw(220, 200)
    if TipButton_Click == True:
        TipButtonImageClick.draw(315, 200)
    elif TipButton_On == True:
        TipButtonImageOn.draw(316, 200)
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass