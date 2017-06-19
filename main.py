from random import randint
from time import sleep

frame = 1
score = 0
while frame < 10:
    ball_one = randint(0,10)
    sleep(1)
    if ball_one == 10:
        print("you got a strike!")
        score += ball_one
        print("your score after frame " + str(frame) + " is " + str(score) + ".")
        frame += 1
        sleep(1)
    else:
        print("you knocked down " + str(ball_one) + " pins.")
        sleep(1)
        ball_two = randint(0, (10 - ball_one))
        print("you knocked down " + str(ball_two) + " pins on the second try.")
        sleep(1)
        if ball_one + ball_two == 10:
            score += ball_one + ball_two
            print("you got a spare")
            print("your score after frame " + str(frame) + " is " + str(score) + ".")
            sleep(1)
        else:
            print("your score after frame " + str(frame) + " is " + str(score) + ".")
            sleep(1)
        frame += 1
