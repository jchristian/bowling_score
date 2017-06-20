from random import randint
from time import sleep
import scoring_functions as sf

#IGNORE THIS.
# -----------------------------------
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
# -------------------------------------------------


#MAIN SCORING
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
        ball_one = randint(0,10)
        ball_two = randint(0, (10 - ball_one))
        #first show is strike
        if ball_one == 10:
            box_two = randint(0,10)
            #if shot two is a strike
            if box_two == 10:
                box_three = randint(0,10)
                if box_three == 10:
                    game.append('XXX')
                else:
                    game.append('XX'+ str(box_three))
            #if shot two is not a strike
            else:
                box_three = randint(0, (10 - box_two))
                if box_two + box_three == 10:
                    game.append('X ' + str(box_two) + '/ ')
                else:
                    game.append('X ' + str(box_two) + '-' + str(box_three))
        elif ball_one + ball_two == 10:
            box_three = randint(0,10)
            game.append(str(ball_one) + '/ ' + str(box_three))
        else:
            game.append(str(ball_one) + '-' + str(ball_two))
        frame += 1



#shows the game
print(game)
#159
# game = ['5-3','9/','X','9-0','X','9/','7-2','X','X','9-0']
# game = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'XXX']


#calculate the score of the game
frame = 1
for i in game:
    #frames 1-8
    if frame < 9:
        ball_one = i[0]
        if i[0] == 'X':
            next = game[frame]

            # if next frame is a strike
            if next[0] == 'X':
                #turkey
                turkey = game[frame + 1]
                if turkey[0] == 'X':
                    score += 30
                else:
                    nexttwo = game[frame + 1]
                    score += (20 + int(nexttwo[0]))

            #if next frame is a spare
            elif next[1] == '/':
                score += 20

            #if next frame is an open
            else:
                score += (10 + int(next[0]) + int(next[2]))
            frame += 1

        #open
        elif i[1] == '-':
            ball_two = i[2]
            score += (int(ball_one) + int(ball_two))
            frame += 1

        #spare
        elif i[1] == '/':
            ball_one = i[0]
            next = game[frame]
            if next[0] == 'X':
                score += 20
            else:
                score += (10 + int(next[0]))
            frame += 1

    #frame 9. must account for tenth frame
    elif frame == 9:
        ball_one = i[0]
        if i[0] == 'X':
            next = game[frame]
            #10th frame
            if next[0] == 'X':
                if next[1] == 'X':
                    score += 30
                else:
                    score += (20 + int(next[1]))
            else:
                if next[1] == '/':
                    score += 20
                elif next[1] == '-':
                    score += (10 + int(next[0]) + int(next[2]))
        # open
        elif i[1] == '-':
            ball_two = i[2]
            score += (int(ball_one) + int(ball_two))
            frame += 1
        # spare
        elif i[1] == '/':
            ball_one = i[0]
            next = game[frame]
            if next[0] == 'X':
                score += 20
            else:
                score += (10 + int(next[0]))
        frame += 1

    # frame 10
    elif frame == 10:
        if i == 'XXX':
            score += 30
        elif i[0] == 'X':
            if i[1] == 'X':
                score += (20 + int(i[2]))
            elif i[2] == '/':
                score += 20
            else:
                score += (10 + int(i[1]) + int(i[4]))
        elif i[1] == '/':
            if i[3] == 'X':
                score += 20
            else:
                score += (10 + int(i[3]))
        elif i[1] == '-':
            score += (int(i[0]) + int(i[2]))

# print the total game score
print(score)