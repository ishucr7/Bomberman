from __future__ import print_function
from getchunix import *
import signal
import sys
import time
import os
from alarmexception import *
from board import *
from bomberman import *
from bomb import *
from termcolor import colored

getch = GetchUnix()


def alarmHandler(signum, frame):
    raise AlarmException


def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\nTimeout")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


class Walls():
    def printboard(self, bman, score, lives):
        for x in range(bman[0], bman[0] + 2):
            for y in range(bman[1], bman[1] + 4):
                arr[x][y] = 'B'

        # for making the inside walls
        b.makewalls()

        # for making bomb
        self.hit = []
        if bom:
            for i in range(0, 2):
                for j in range(0, 4):
                    self.hit.append([bom[0][0] + i, bom[0][1] + j])

        # for making bricks
        self.bri = []
        if brick:
            for x in brick:
                for i in range(0, 2):
                    for j in range(0, 4):
                        self.bri.append([x[0] + i, x[1] + j])

        for k in range(2):
            for i in range(77):
                if(i == 76):
                    print("")
                else:
                    print("X", end="")

        for r in range(38):
            for x in range(77):
                if((x < 4) or ((x < 76) and (x >= 72))):
                    print("X", end="")
                elif(arr[r][x] == 'W'):
                    print("X", end="")
                elif([r, x] in self.hit):
                    print(bom[1], end="")
                elif(around and [r, x] in around):
                    print(colored("e", 'red'), end="")
                elif([r, x] in self.bri):
                    print(colored('/', 'blue'), end="")
                elif(arr[r][x] == 'B'):
                    print (colored("B", 'green'), end="")
                elif(arr[r][x] == 'E'):
                    print (colored("E", 'red'), end="")
                else:
                    print(" ", end="")
            print("")

        # around array for spreading bomb around e
        if around and not bom:
            around[:] = []

        for k in range(2):
            for i in range(77):
                if(i == 76):
                    print("")
                else:
                    print("X", end="")
        print("Score " + str(score[0]) + " Lives Remaining " + str(lives))
        return 0


class run(Bomb, Walls):
    def __init__(self):
        self.finish = 0
        self.curr_time = time.time()
        self.curr_time2 = time.time()

    def mov(self, bman, score, lives):
        move = '0'
        while(1):
            while(move != 'q'):
                m = -3
                move = input_to()
                if(move == 'w'):
                    m = bbm.moveUp(bman, score, lives)
                elif(move == 's'):
                    m = bbm.moveDown(bman, score, lives)
                elif(move == 'a'):
                    m = bbm.moveLeft(bman, score, lives)
                elif(move == 'd'):
                    m = bbm.moveRight(bman, score, lives)
                elif(move == 'b'):
                    if not bom:
                        self.place(bman[0], bman[1])

                rem_time = time.time() - self.curr_time

                if bom and rem_time > 1:
                    self.finish = self.timer(score)
                    self.curr_time = time.time()
                    if(self.finish == 1):
                        print("Game Over")
                        sys.exit(0)

                if(m >= 0):
                    lives = m
                    bman[0] = 0
                    bman[1] = 4

                rem_time2 = time.time() - self.curr_time2
                if rem_time2 > 1:
                    lives = e._Enemy__enemymove(bman, score, lives)
                    self.curr_time2 = time.time()

                os.system("tput reset")
                self.printboard(bman, score, lives)
                if(lives == 0):
                    print("Game Over")
                    sys.exit(0)
                if not en:
                    print("You Win :-)")
                    sys.exit(0)
            sys.exit(0)


g = Walls()
r = run()
