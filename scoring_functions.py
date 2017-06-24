from numpy.random import choice
from random import randint

#Main functions
#generate a ten frame game using weighted first ball values
#Tenth frame is next on the agenda


def get_weighted_random_first_ball():
    l = []
    w = [0, 0.001, 0.0001, 0.001, 0.001, 0.005, 0.03, 0.07, 0.092, 0.22, 0.5799]
    for i in range(0,11):
        l.append(i)
    return (choice(l, p=w))

def get_single_pin():
    l = [True, False]
    sw = [.97, .03]
    return (choice(l, p=sw))

def get_multi_pin():
    l = [True, False]
    sw = [.75, .25]
    return (choice(l, p=sw))

def onegame(frames):
    game = []
    for i in range(frames):
        first_ball = get_weighted_random_first_ball()
        if first_ball == 10:
            game.append('X')
        elif first_ball == 9:
            if get_single_pin():
                game.append(str(first_ball) + "/")
            else:
                game.append(str(first_ball) + "0")
        else:
            if get_multi_pin():
                game.append(str(first_ball) + "/")
            else:
                game.append(str(first_ball) + "-" + str(randint(0, (10 - first_ball))))
    return game

for i in range(10):
    x = onegame(10)
    print(x)