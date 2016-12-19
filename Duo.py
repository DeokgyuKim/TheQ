from pico2d import *
import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

import game_framework
import Title_State

open_canvas(450, 700)

game_framework.run(Title_State)

close_canvas()