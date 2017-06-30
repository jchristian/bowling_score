from numpy.random import choice
from random import randint
import bowler_profiles as bp

#Main functions
#generate a ten frame game using weighted first ball values
#spares are also weighted
#Tenth frame is next on the agenda


class BowlingScores(object):

    def __init__(self, profile):
        # self.num_of_games = num_of_games
        self.profile = profile

    def get_games(self):
        game = self.onegame(10)
        return game

    def get_weighted_random_first_ball(self):
        l = []
        for i in range(0,11):
            l.append(i)
        return (choice(l, p=self.profile['sw']))

    def get_single_pin(self):
        l = [True, False]
        return (choice(l, p=self.profile['spw']))

    def get_multi_pin(self):
        l = [True, False]
        return (choice(l, p=self.profile['mpw']))

    def onegame(self, frames):
        game = []
        for i in range(frames):
            if i != 9:
                self.first_nine_frames(game)
            if i == 9:
                self.frame_ten(game)
        return game

    def first_nine_frames(self, game):
        first_ball = self.get_weighted_random_first_ball()
        if first_ball == 10:
            game.append('X')
        elif first_ball == 9:
            if self.get_single_pin():
                game.append(str(first_ball) + "/")
            else:
                game.append(str(first_ball) + "-0")
        else:
            if self.get_multi_pin():
                game.append(str(first_ball) + "/")
            else:
                game.append(str(first_ball) + "-" + str(randint(0, (10 - first_ball))))
        return game

    def frame_ten(self, game):
        box_one = self.get_weighted_random_first_ball()
        if box_one == 10:
            box_two = self.get_weighted_random_first_ball()
            if box_two == 10:
                box_three = self.get_weighted_random_first_ball()
                if box_three == 10:
                    game.append('XXX')
                else:
                    game.append('XX' + str(box_three))
            else:
                if box_two == 9:
                    if self.get_single_pin():
                        game.append('X ' + str(box_two) + "/")
                    else:
                        game.append('X ' + str(box_two) + "0")
                else:
                    if self.get_multi_pin():
                        game.append('X ' + str(box_two) + "/")
                    else:
                        game.append('X ' + str(box_two) + "-" + str(randint(0, (10 - box_two))))
        elif box_one == 9:
            if self.get_single_pin():
                game.append(str(box_one) + "/ " + str(self.get_weighted_random_first_ball()))
            else:
                game.append(str(box_one) + "-0")

        else:
            if self.get_multi_pin():
                game.append(str(box_one) + "/ " + str(self.get_weighted_random_first_ball()))
            else:
                game.append(str(box_one) + "-" + str(randint(0, (10 - box_one))))
        return game

    def print_series(self):
        print(self.get_games())
    #
    # def get_series(self):
    #     for i in range(self.num_of_games):
    #         return(self.get_games())

class Score(object):

    def __init__(self, game):
        self.game = game

    def get_score(self):
        return self.calculate_score(self.game)

    def calculate_score(self, game):
        score = 0
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
        return score