from random import randint
from board import arr
brick = []


class Brick:
    def __init__(self):

        for k in range(1, 20):
            i = randint(1, 19)
            j = randint(1, 17)
            if arr[i][j] == 0:
                brick.append([2 * i, 4 * j])

        for x in brick:
            for i in range(x[0], x[0] + 2):
                for j in range(x[1], x[1] + 4):
                    arr[i][j] = 'b'


br = Brick()
