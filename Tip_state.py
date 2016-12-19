import game_framework
import Title_State
import Main_Game_State
import Main_Game_State_Hard
from pico2d import *
import ranking_state

name = "TipState"
TitleImage = None

def enter():
    global TitleImage

    TitleImage = load_image('tip_title.png')

def exit():
    global TitleImage

    del(TitleImage)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(Title_State)
def draw(frame_time):
    clear_canvas()
    TitleImage.draw(222, 350)
    update_canvas()
def update(frame_time):
    pass
def pause():
    pass
def resume():
    pass