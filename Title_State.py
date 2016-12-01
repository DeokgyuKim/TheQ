import game_framework
import Stage_state
import ranking_state
from pico2d import *

name = "TitleState"
TitleImage = None
PlayButtonImageOn = None
SoundButtonImageOn = None
ScoreButtonImageOn = None
TipButtonImageOn = None

PlayButtonImageClick = None
SoundButtonImageClick = None
ScoreButtonImageClick = None
TipButtonImageClick = None

x = None
y = None
PlayButton_Click = False
SoundButton_Click = False
ScoreButton_Click = False
TipButton_Click = False

PlayButton_On = False
SoundButton_On = False
ScoreButton_On = False
TipButton_On = False

Play = False
Score = False
Tip = False
Count = 0

def enter():
    global TitleImage
    global PlayButtonImageOn
    global SoundButtonImageOn
    global ScoreButtonImageOn
    global TipButtonImageOn
    global PlayButtonImageClick
    global SoundButtonImageClick
    global ScoreButtonImageClick
    global TipButtonImageClick
    global TitleImage
    global PlayButtonImageOn
    global SoundButtonImageOn
    global ScoreButtonImageOn
    global TipButtonImageOn

    global PlayButtonImageClick
    global SoundButtonImageClick
    global ScoreButtonImageClick
    global TipButtonImageClick
    global x
    global y
    global PlayButton_Click
    global SoundButton_Click
    global ScoreButton_Click
    global TipButton_Click
    global PlayButton_On
    global SoundButton_On
    global ScoreButton_On
    global TipButton_On
    global Play
    global Score
    global Tip
    global Count

    TitleImage = None
    PlayButtonImageOn = None
    SoundButtonImageOn = None
    ScoreButtonImageOn = None
    TipButtonImageOn = None

    PlayButtonImageClick = None
    SoundButtonImageClick = None
    ScoreButtonImageClick = None
    TipButtonImageClick = None
    x = None
    y = None
    PlayButton_Click = False
    SoundButton_Click = False
    ScoreButton_Click = False
    TipButton_Click = False
    PlayButton_On = False
    SoundButton_On = False
    ScoreButton_On = False
    TipButton_On = False
    Play = False
    Score = False
    Tip = False
    Count = 0

    f = open('Sound.txt', 'r')
    Sound_data = json.load(f)
    f.close()

    if Sound_data[0]['SOUND'] == 1:
        SoundButton_Click = True

    TitleImage = load_image('title.png')
    PlayButtonImageOn = load_image('icon_play_on.png')
    SoundButtonImageOn = load_image('icon_sound_on.png')
    ScoreButtonImageOn = load_image('icon_score_on.png')
    TipButtonImageOn = load_image('icon_tip_on.png')
    PlayButtonImageClick = load_image('icon_play_click.png')
    SoundButtonImageClick = load_image('icon_sound_click.png')
    ScoreButtonImageClick = load_image('icon_score_click.png')
    TipButtonImageClick = load_image('icon_tip_click.png')

def exit():
    global TitleImage
    global PlayButtonImageOn
    global SoundButtonImageOn
    global ScoreButtonImageOn
    global TipButtonImageOn

    global PlayButtonImageClick
    global SoundButtonImageClick
    global ScoreButtonImageClick
    global TipButtonImageClick

    if SoundButton_Click == True:
        Sound_data = [{"SOUND": 1}]
    else:
        Sound_data = [{"SOUND": 0}]
    f = open('Sound.txt', 'w')
    json.dump(Sound_data, f)
    f.close()

    del(TitleImage)
    del(PlayButtonImageOn)
    del(SoundButtonImageOn)
    del(ScoreButtonImageOn)
    del(TipButtonImageOn)

    del(PlayButtonImageClick)
    del(SoundButtonImageClick)
    del(ScoreButtonImageClick)
    del(TipButtonImageClick)

def handle_events(frame_time):
    global x, y
    global Play, Score, Tip, Count
    global PlayButton_Click
    global SoundButton_Click
    global ScoreButton_Click
    global TipButton_Click

    global PlayButton_On
    global SoundButton_On
    global ScoreButton_On
    global TipButton_On
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, 599 - event.y
            if(((x - 222.0) * (x - 222.0)) + ((y - 250.0) * (y - 250.0)) <= 100 * 100):
                PlayButton_On = True
            elif(((x - 126.0) * (x - 126.0)) + ((y - 100.0) * (y - 100.0)) <= 25 * 25):
                ScoreButton_On = True
            elif (((x - 222.0) * (x - 222.0)) + ((y - 100.0) * (y - 100.0)) <= 25 * 25):
                SoundButton_On = True
            elif (((x - 318.0) * (x - 318.0)) + ((y - 100.0) * (y - 100.0)) <= 25 * 25):
                TipButton_On = True
            else:
                PlayButton_On = False
                ScoreButton_On = False
                SoundButton_On = False
                TipButton_On = False
        if Play != True and Score != True and Tip != True:
            if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                x, y = event.x, 599 - event.y
                if (((x - 222.0) * (x - 222.0)) + ((y - 250.0) * (y - 250.0)) <= 100 * 100):
                    if PlayButton_Click == True:
                        PlayButton_Click = False
                    else:
                        PlayButton_Click = True
                        Play = True
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
                if(Play == True):
                    game_framework.change_state(Stage_state)
                    pass
                elif(Score == True):
                    game_framework.change_state(ranking_state)
                    pass
                elif(Tip == True):
                    #Tip_State
                    pass
            #game_framework.quit()
def draw(frame_time):
    clear_canvas()
    TitleImage.draw(222, 350)
    if PlayButton_Click == True:
        PlayButtonImageClick.draw(225, 350)
    elif PlayButton_On == True:
        PlayButtonImageOn.draw(225, 350)
    if ScoreButton_Click == True:
        ScoreButtonImageClick.draw(123, 200)
    elif ScoreButton_On == True:
        ScoreButtonImageOn.draw(123, 200)
    if SoundButton_Click == True:
        SoundButtonImageClick.draw(219, 200)
    elif SoundButton_On == True:
        SoundButtonImageOn.draw(219, 200)
    if TipButton_Click == True:
        TipButtonImageClick.draw(315, 200)
    elif TipButton_On == True:
        TipButtonImageOn.draw(315, 200)
    update_canvas()
def update(frame_time):
    pass
def pause():
    pass
def resume():
    pass