# config root dir, library path
import os, sys
__script_path=os.path.abspath(globals().get('__file__','.'))
__script_dir = os.path.dirname(__script_path)
root_dir = os.path.abspath(f'{__script_dir}/../../../..')
print(root_dir)
src_dir    = os.path.join(root_dir, "src").replace("\\", "/")
include_dirs  = [src_dir]
for lib in include_dirs:
    if lib not in sys.path: sys.path.insert(0, lib)
assets_dir = os.path.join(root_dir, "assets").replace("\\", "/")
IS_FULLSCREEN = False
WIDTH = 480
HEIGHT = 416
HAND_GESTURES = ["Open", "Closed"]
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
ORANGE = (0,128,255)
YELLOW = (0,255,255)
MAGENTA = (255,0,255)
CYAN = (255,255,0)
PURPLE = (128,0,128)