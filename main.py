import os
import sys

if len(sys.argv) > 1: m = sys.argv[1]
else: m = "empty"

appdir = os.path.abspath(os.path.dirname(__file__))
os.chdir(appdir)
for d in ((appdir, 'src'), (appdir, 'data/games/')):
    if d not in sys.path:
        sys.path.insert(0, os.path.join(*d))

from main import GameApp
app = GameApp(m)
