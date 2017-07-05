from numpy.random import choice
from random import randint
import bowler_profiles as bp


# Main functions
# generate a ten frame game using weighted first ball values
# spares are also weighted
# Tenth frame is next on the agenda


class BowlingScores(object):
    def __init__(self, profile):
        # self.num_of_games = num_of_games
        self.profile = profile

    def get_games(self):
        game = self.onegame(10)
        return game

    def get_weighted_random_first_ball(self):
        l = []
        for i in range(0, 11):
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
                        game.append('X ' + str(box_two) + "-0")
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

class Frame(object):
    def __init__(self, data):
        self.data = data

    def is_strike(self):
        return self.data[0] == 'X'

    def is_spare(self):
        return len(self.data) == 2 and self.data[1] == '/'

    def is_open(self):
        return not (self.is_spare() or self.is_strike())

    def get_first_ball_count(self):
        return 10 if self.is_strike() else self._get_count(self.data[0])

    def get_second_ball_count(self):
        return self._get_count(self.data[2])

    def _get_count(self, character_data):
        return int(character_data)

class Score(object):
    def __init__(self, game):
        self.game = game

    def get_score(self):
        return self.calculate_score(self.game)

    def calculate_score(self, game):
        score = 0
        frame_index = 1
        for i in game:
            # frames 1-8
            if frame_index < 9:
                current_frame = Frame(i)
                if current_frame.is_strike():
                    next_frame = Frame(game[frame_index])

                    # if next frame is a strike
                    if next_frame.is_strike():
                        # turkey
                        two_frames_ahead = Frame(game[frame_index + 1])
                        if two_frames_ahead.is_strike():
                            score += 30
                        else:
                            score += (20 + two_frames_ahead.get_first_ball_count())

                    # if next frame is a spare
                    elif next_frame.is_spare():
                        score += 20

                    # if next frame is an open
                    else:
                        score += (10 + next_frame.get_first_ball_count() + next_frame.get_second_ball_count())
                    frame_index += 1

                # open
                elif current_frame.is_open():
                    score += (current_frame.get_first_ball_count() + current_frame.get_second_ball_count())
                    frame_index += 1

                # spare
                elif current_frame.is_spare():
                    next_frame = Frame(game[frame_index])
                    if next_frame.is_strike():
                        score += 20
                    else:
                        score += (10 + next_frame.get_first_ball_count())
                    frame_index += 1

            # frame 9. must account for tenth frame
            elif frame_index == 9:
                ball_one = i[0]
                if i[0] == 'X':
                    next_frame = game[frame_index]
                    # 10th frame
                    if next_frame[0] == 'X':
                        if next_frame[1] == 'X':
                            score += 30
                        else:
                            score += (20 + int(next_frame[2]))
                    else:
                        if next_frame[1] == '/':
                            score += 20
                        elif next_frame[1] == '-':
                            score += (10 + int(next_frame[0]) + int(next_frame[2]))
                # open
                elif i[1] == '-':
                    ball_two = i[2]
                    score += (int(ball_one) + int(ball_two))
                    frame_index += 1
                # spare
                elif i[1] == '/':
                    ball_one = i[0]
                    next_frame = game[frame_index]
                    if next_frame[0] == 'X':
                        score += 20
                    else:
                        score += (10 + int(next_frame[0]))
                frame_index += 1

            # frame 10
            elif frame_index == 10:
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
