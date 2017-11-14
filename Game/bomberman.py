from enemy import *


class Bomberman(Person):
    # bman is an array of size two containing the row and column of leftmost point of bomberman

    def moveRight(self, bman, score, lives):
        if((bman[1] + 4) < 72 and (arr[bman[0]][bman[1] + 4] == 0)):
            w = bman[1]
            bman[1] = bman[1] + 4
            self.mak(bman[0], w, bman)
            return -1
        elif((bman[1] + 4) < 72 and ([bman[0], bman[1] + 4] in en)):
            w = bman[1]
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

        elif((bman[1] - 4) >= 4 and ([bman[0], bman[1] - 4] in en)):

            w = bman[1]
            self.mak(bman[0], w, bman)
            lives = lives - 1
            return lives
        else:
            return -1

    def moveDown(self, bman, score, lives):
        if((bman[0] + 2) < 38 and (arr[bman[0] + 2][bman[1]] == 0)):
            x = bman[0]
            bman[0] = bman[0] + 2
            self.mak(x, bman[1], bman)
            return -1

        elif((bman[0] + 2) < 38 and ([bman[0] + 2, bman[1]] in en)):
            x = bman[0]
            self.mak(x, bman[1], bman)
            lives = lives - 1
            return lives
        else:
            return -1

    def moveUp(self, bman, score, lives):
        if((bman[0] - 2) >= 0 and(arr[bman[0] - 2][bman[1]] == 0)):
            w = bman[0]
            bman[0] = bman[0] - 2
            self.mak(w, bman[1], bman)
            return -1

        elif((bman[0] - 2) >= 0 and ([bman[0] - 2, bman[1]] in en)):
            w = bman[0]
            self.mak(w, bman[1], bman)
            lives = lives - 1
            return lives
        else:
            return -1


bbm = Bomberman()
