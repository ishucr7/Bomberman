from getchunix import *
from walls import *
bman = []
score = [0]
lives = 3


class Gameplay():
    def __init__(self):
        bman.append(0)
        bman.append(4)


b = Gameplay()
g.printboard(bman, score, lives)
r.mov(bman, score, lives)
