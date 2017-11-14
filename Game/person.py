from board import arr


class Person():
    def mak(self, x, y, bman):
        for i in range(x, x + 2):
            for j in range(y, y + 4):
                arr[i][j] = 0
        return 0

    def moveRight(self, bman, score, lives):
        raise NotImplementedError("Subclass should implement it")

    def moveRight(self, bman, score, lives):
        raise NotImplementedError("Subclass should implement it")

    def moveDown(self, bman, score, lives):
        raise NotImplementedError("Subclass should implement it")

    def moveUp(self, bman, score, lives):
        raise NotImplementedError("Subclass should implement it")
