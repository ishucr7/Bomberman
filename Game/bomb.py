bom = []
around = []
from enemy import *


class Bomb:
    def place(self, locx, locy):
        bom.append([locx, locy])
        bom.append(3)

    def timer(self, score):
        self.finish = 0
        if(bom[1] == 0):

            self.general(score, bom[0][1] - 4, bom[0]
                         [1], bom[0][0], bom[0][0] + 2)
            self.general(score, bom[0][1] + 4, bom[0]
                         [1] + 8, bom[0][0], bom[0][0] + 2)
            self.general(score, bom[0][1], bom[0][1] +
                         4, bom[0][0] + 2, bom[0][0] + 4)
            self.general(score, bom[0][1], bom[0][1] +
                         4, bom[0][0] - 2, bom[0][0])

            bom[:] = []
            #list is emptied
        else:
            bom[1] = bom[1] - 1

        return self.finish

    def general(self, score, r1, r2, c1, c2):
        for j in range(r1, r2):
            for i in range(c1, c2):
                around.append(([i, j]))
                if(arr[i][j] == 'E'):
                    arr[i][j] = 0
                    if [i, j] in en:
                        en.remove([i, j])
                        score[0] = score[0] + 100
                elif [i, j] in brick:
                    arr[i][j] = 0
                    brick.remove([i, j])
                    score[0] = score[0] + 20

                elif(arr[i][j] == 'B'):
                    self.finish = 1
