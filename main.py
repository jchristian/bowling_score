from random import randint
from time import sleep
import scoring_functions as sf


# frame = 1
# score = 0
# while frame < 10:
#     ball_one = randint(0,10)
#     sleep(1)
#     if ball_one == 10:
#         print("you got a strike!")
#         score += ball_one
#         print("your score after frame " + str(frame) + " is " + str(score) + ".")
#         frame += 1
#         sleep(1)
#     else:
#         print("you knocked down " + str(ball_one) + " pins.")
#         sleep(1)
#         ball_two = randint(0, (10 - ball_one))
#         print("you knocked down " + str(ball_two) + " pins on the second try.")
#         sleep(1)
#         if ball_one + ball_two == 10:
#             score += ball_one + ball_two
#             print("you got a spare")
#             print("your score after frame " + str(frame) + " is " + str(score) + ".")
#             sleep(1)
#         else:
#             print("your score after frame " + str(frame) + " is " + str(score) + ".")
#             sleep(1)
#         frame += 1


#initialize a full game with random inputs
game = []
frame = 1
score = 0
while frame < 11:
    #frames 1-9
    if frame != 10:
        ball_one = randint(0, 10)
        ball_two = randint(0, (10 - ball_one))
        if ball_one == 10:
            game.append('X')
        elif ball_one + ball_two == 10:
            game.append(str(ball_one) + '/')
        else:
            game.append(str(ball_one) + '-' + str(ball_two))
        frame += 1
    #filling the weird frame 10
    elif frame == 10:
        # ball_one = randint(0,10)
        ball_one = 10
        ball_two = randint(0, (10 - ball_one))
        #first show is strike
        if ball_one == 10:
            box_two = randint(0,10)
            #if shot two is a strike
            if box_two == 10:
                box_three = randint(0,10)
                game.append('XX'+ str(box_three))
            #if shot two is not a strike
            else:
                box_three = randint(0, (10 - box_two))
                if box_two + box_three == 10:
                    game.append('X ' + str(box_two) + '/')
                else:
                    game.append('X ' + str(box_two) + '-' + str(box_three))
        elif ball_one + ball_two == 10:
            box_three = randint(0,10)
            game.append(str(ball_one) + '/' + str(box_three))
        else:
            game.append(str(ball_one) + '-' + str(ball_two))
        frame += 1



#shows the game
print(game)

#calculate the score of the game
frame = 0
for i in game:
    #frames 1-9
    if frame < 9:
        ball_one = i[0]
        #open
        if len(i) == 3:
            ball_two = i[2]
            score += (int(ball_one) + int(ball_two))
            frame += 1
        #spare
        elif len(i) == 2:
            ball_one = i[0]
            next = game[frame + 1]
            score += (10 + int(next[0]))
            frame += 1
        #strike
        else:
            next = game[frame + 1]
            if len(next) == 2:
                score += 20
            else:
                score += (10 + int(next[0]) + int(next[2]))
            frame += 1
    #frame 10
    # else:
    #     if len(i) == 3:
    #         ball_two = i[2]
    #         score += (int(ball_one) + int(ball_two))
    #     elif len(i) == 2:
    #         ball_one = i[0]
    #         next = game[frame + 1]
    #         score += (10 + int(next[0]))
print(score)