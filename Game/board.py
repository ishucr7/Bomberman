arr = [[0 for i in range(78)] for i in range(78)]
boards = []


class Board():
    def makewalls(self):
        r = 2
        y = 0
        while(r < 38):
            y = y + 1
            c = 0
            x = 0
            while(x < 72):
                if(c != 4):
                    boards.append([r, x])
                    arr[r][x] = 'W'
                    c = c + 1
                    x = x + 1
                else:
                    x = x + 4
                    c = 0
            if(y != 2):
                r = r + 1
            else:
                r = r + 3
                y = 0


b = Board()
b.makewalls()
