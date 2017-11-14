from random import randint
from brick import *
from person import *
en = []


class Enemy(Person):
    def __init__(self):
        count = 1
        while(count != 10):
            i = randint(1, 19)
            j = randint(1, 17)
            if ([i, j] not in brick) and ([i, j] not in en) and arr[i][j] == 0:
                en.append([i * 2, j * 4])
                count += 1

    def __enemymove(self, bman, score, lives):
        for x in en:

            lif = 5
            c = randint(1, 4)
            print(c)

            if(c == 1):
                lif = self.moveRight(x, score, lives)
            elif(c == 2):
                lif = self.moveLeft(x, score, lives)
            elif(c == 3):
                lif = self.moveDown(x, score, lives)
            else:
                lif = self.moveUp(x, score, lives)

            if (lif >= 0):
                lives = lif
                bman[0] = 0
                bman[1] = 4

        for a in en:
            for x in range(a[0], a[0] + 2):
                for y in range(a[1], a[1] + 4):
                    arr[x][y] = 'E'
        return lives

    def moveRight(self, bman, score, lives):
        if((bman[1] + 4) < 72 and (arr[bman[0]][bman[1] + 4] == 0)):
            w = bman[1]
            bman[1] = bman[1] + 4
            self.mak(bman[0], w, bman)
            return -1

        elif((bman[1] + 4) < 72 and (arr[bman[0]][bman[1] + 4] == 'B')):
            w = bman[1]
            bman[1] = bman[1] + 4
            self.mak(bman[0], w, bman)
            lives = lives - 1
            return lives
        else:
            return -1

    def moveLeft(self, bman, score, lives):
        if((bman[1] - 4) >= 4 and (arr[bman[0]][bman[1] - 4] == 0)):
            w = bman[1]
            bman[1] = bman[1] - 4
            self.mak(bman[0], w, bman)
            return -1

        elif((bman[1] - 4) >= 4 and (arr[bman[0]][bman[1] - 4] == 'B')):
            w = bman[1]
            bman[1] = bman[1] - 4
            self.mak(bman[0], w, bman)
            lives = lives - 1
            return lives
        else:
            return -1

    def moveDown(self, bman, score, lives):
        if((bman[0] + 2) < 37 and (arr[bman[0] + 2][bman[1]] == 0)):
            x = bman[0]
            bman[0] = bman[0] + 2
            self.mak(x, bman[1], bman)
            return -1

        elif((bman[0] + 2) < 37 and (arr[bman[0] + 2][bman[1]] == 'B')):
            x = bman[0]
            bman[0] = bman[0] + 2
            self.mak(x, bman[1], bman)
            lives = lives - 1
            return lives
        else:
            return -1

    def moveUp(self, bman, score, lives):
        if((bman[0] - 2) >= 0 and (arr[bman[0] - 2][bman[1]] == 0)):
            w = bman[0]
            bman[0] = bman[0] - 2
            self.mak(w, bman[1], bman)
            return -1
        elif((bman[0] - 2) >= 0 and (arr[bman[0] - 2][bman[1]] == 'B')):
            w = bman[0]
            bman[0] = bman[0] - 2
            self.mak(w, bman[1], bman)
            lives = lives - 1
            return lives
        else:
            return -1


e = Enemy()
