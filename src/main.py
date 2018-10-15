import os, sys
try:
    import __builtin__ as builtins
    py = 2
except:
    import builtins
    py = 3

print("Loading pygame.")
with open(os.devnull, "w") as f:
    oldstdout=sys.stdout; sys.stdout=f; import pygame; sys.stdout=oldstdout
from dagoo import Dagooberd

class GameApp():
    def __init__(self, game):
        # WARNING FOLLOWING VARS ARE IN BUILTIN SCOPE.
        # WARNING WATCH OUT DANGEROUS ROADS AHEAD.
        builtins.python_version = py
        builtins.pygame = pygame
        builtins.dagooberd  = Dagooberd()

if __name__ == "__main__":
    app = GameApp("empty")
