import game_framework
import Title_State
import Main_Game_State
import Main_Game_State_Hard
from pico2d import *

name = "RankingState"
TitleImage = None
font = None
score_data_normal = [
    {"REDCAR_SCORE": 0, "BLUECAR_SCORE": 0, "TOTAL_SCORE": 0}
]
score_data_hard = None

def enter():
    global TitleImage, font, score_data_normal, score_data_hard

    TitleImage = load_image('ranking_title.png')
    font = load_font('NEXON Football Gothic L.otf', 17)
    f = open('save_normal.txt', 'r')
    score_data_normal = json.load(f)
    f.close()

    f = open('save_hard.txt', 'r')
    score_data_hard = json.load(f)
    f.close()
def exit():
    global TitleImage, font
    del(font)
    del(TitleImage)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(Title_State)

def bubble_sort_normal(data_list):
    for i in range(0, len(data_list)):
        for j in range(i + 1, len(data_list)):
            if data_list[i]['TOTAL_SCORE'] < data_list[j]['TOTAL_SCORE']:
                data_list[i], data_list[j] = data_list[j], data_list[i]

def bubble_sort_hard(data_list):
    for i in range(0, len(data_list)):
        for j in range(i + 1, len(data_list)):
            if data_list[i]['TOTAL_TIME'] < data_list[j]['TOTAL_TIME']:
                data_list[i], data_list[j] = data_list[j], data_list[i]

def print_score_normal(score, y):
    global font
    if y == 0:
        font.draw(70, 700 - 205, '(RED: %5d, BLUE: %5d, TOTAL: %5d)' % (score['REDCAR_SCORE'], score['BLUECAR_SCORE'], score['TOTAL_SCORE']),
            (3, 4, 36))
    if y == 1:
        font.draw(70, 700 - 243, '(RED: %5d, BLUE: %5d, TOTAL: %5d)' % (score['REDCAR_SCORE'], score['BLUECAR_SCORE'], score['TOTAL_SCORE']),
            (3, 4, 36))
    if y == 2:
        font.draw(70, 700 - 282, '(RED: %5d, BLUE: %5d, TOTAL: %5d)' % (score['REDCAR_SCORE'], score['BLUECAR_SCORE'], score['TOTAL_SCORE']),
            (3, 4, 36))
    if y == 3:
        font.draw(70, 700 - 320, '(RED: %5d, BLUE: %5d, TOTAL: %5d)' % (score['REDCAR_SCORE'], score['BLUECAR_SCORE'], score['TOTAL_SCORE']),
            (3, 4, 36))
    if y == 4:
        font.draw(70, 700 - 358, '(RED: %5d, BLUE: %5d, TOTAL: %5d)' % (score['REDCAR_SCORE'], score['BLUECAR_SCORE'], score['TOTAL_SCORE']),
            (3, 4, 36))

def print_score_hard(score, y):
    global font
    if y == 0:
        font.draw(70, 700 - 503, '(RED: %4.2f, BLUE: %4.2f, TOTAL: %4.2f)' % (score['REDCAR_TIME'], score['BLUECAR_TIME'], score['TOTAL_TIME']),
            (3, 4, 36))
    if y == 1:
        font.draw(70, 700 - 540, '(RED: %4.2f, BLUE: %4.2f, TOTAL: %4.2f)' % (score['REDCAR_TIME'], score['BLUECAR_TIME'], score['TOTAL_TIME']),
            (3, 4, 36))
    if y == 2:
        font.draw(70, 700 - 578, '(RED: %4.2f, BLUE: %4.2f, TOTAL: %4.2f)' % (score['REDCAR_TIME'], score['BLUECAR_TIME'], score['TOTAL_TIME']),
            (3, 4, 36))
    if y == 3:
        font.draw(70, 700 - 616, '(RED: %4.2f, BLUE: %4.2f, TOTAL: %4.2f)' % (score['REDCAR_TIME'], score['BLUECAR_TIME'], score['TOTAL_TIME']),
            (3, 4, 36))
    if y == 4:
        font.draw(70, 700 - 654, '(RED: %4.2f, BLUE: %4.2f, TOTAL: %4.2f)' % (score['REDCAR_TIME'], score['BLUECAR_TIME'], score['TOTAL_TIME']),
            (3, 4, 36))

def draw(frame_time):
    global TitleImage, font, score_data_normal, score_data_hard
    clear_canvas()
    TitleImage.draw(222, 350)

    bubble_sort_normal(score_data_normal)
    bubble_sort_hard(score_data_hard)

    score_data_normal = score_data_normal[:5]
    score_data_hard = score_data_hard[:5]

    for y in range(0, len(score_data_normal)):
        print_score_normal(score_data_normal[y], y)
    for y in range(0, len(score_data_hard)):
        print_score_hard(score_data_hard[y], y)

    update_canvas()

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass