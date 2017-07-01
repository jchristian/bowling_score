from random import randint

score = 0
counter = 0
halfcounter = 0
highgame = 0
highgamenum = 0
actualgame = []
while True:
    if score < 220:
        game = []
        frame = 1
        score = 0
        while frame < 11:
            # frames 1-9
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
            # filling the weird frame 10
            elif frame == 10:
                ball_one = randint(0, 10)
                ball_two = randint(0, (10 - ball_one))
                # first show is strike
                if ball_one == 10:
                    box_two = randint(0, 10)
                    # if shot two is a strike
                    if box_two == 10:
                        box_three = randint(0, 10)
                        if box_three == 10:
                            game.append('XXX')
                        else:
                            game.append('XX' + str(box_three))
                    # if shot two is not a strike
                    else:
                        box_three = randint(0, (10 - box_two))
                        if box_two + box_three == 10:
                            game.append('X ' + str(box_two) + '/')
                        else:
                            game.append('X ' + str(box_two) + '-' + str(box_three))
                elif ball_one + ball_two == 10:
                    box_three = randint(0, 10)
                    game.append(str(ball_one) + '/ ' + str(box_three))
                else:
                    game.append(str(ball_one) + '-' + str(ball_two))
                frame += 1

        # calculate the score of the game
        frame = 1
        for i in game:
            # frames 1-8
            if frame < 9:
                ball_one = i[0]
                if i[0] == 'X':
                    next = game[frame]

                    # if next frame is a strike
                    if next[0] == 'X':
                        # turkey
                        turkey = game[frame + 1]
                        if turkey[0] == 'X':
                            score += 30
                        else:
                            nexttwo = game[frame + 1]
                            score += (20 + int(nexttwo[0]))

                    # if next frame is a spare
                    elif next[1] == '/':
                        score += 20

                    # if next frame is an open
                    else:
                        score += (10 + int(next[0]) + int(next[2]))
                    frame += 1

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

            # frame 9. must account for tenth frame
            elif frame == 9:
                ball_one = i[0]
                if i[0] == 'X':
                    next = game[frame]
                    # 10th frame
                    if next[0] == 'X':
                        if next[1] == 'X':
                            score += 30
                        else:
                            score += (20 + int(next[2]))
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
                    elif i[3] == '/':
                        score += 20
                    else:
                        score += (10 + int(i[2]) + int(i[4]))
                elif i[1] == '/':
                    if i[3] == 'X':
                        score += 20
                    else:
                        score += (10 + int(i[3]))
                elif i[1] == '-':
                    score += (int(i[0]) + int(i[2]))

        if score > 150:
            halfcounter += 1
        if score > highgame:
            highgame = score
            highgamenum = counter + 1
            actualgame = game
        counter += 1
        print("game " + str(counter) + " is " + str(score))

    else:
        # print("It took bitch kenny " + str(counter) + " games to bowl above 250 you suck")
        # print("There were " + str(halfcounter) + " games over 150.")
        # print(score)
        print("high game of " + str(highgame) + " in game " + str(highgamenum))
        print(actualgame)
        break

        # print the total game score
        # print(score)
