import pytest
from scoring_functions import Score
from scoring_functions import Frame

class TestFrame:

    def test_when_getting_is_strike_and_it_is_a_strike_it_should_return_true(self):
        assert(Frame(['X']).is_strike() == True)

    def test_when_getting_is_strike_and_it_is_a_spare_it_should_return_false(self):
        assert(Frame(['9/']).is_strike() == False)

    def test_when_getting_is_strike_and_it_is_an_open_it_should_return_false(self):
        assert(Frame(['9', '0']).is_strike() == False)

    def test_when_getting_is_spare_and_it_is_a_spare_it_should_return_true(self):
        assert(Frame(['9', '/']).is_spare() == True)

    def test_when_getting_is_spare_and_it_is_a_strike_it_should_return_false(self):
        assert(Frame(['X']).is_spare() == False)

    def test_when_getting_is_spare_and_it_is_an_open_it_should_return_false(self):
        assert(Frame(['9', '0']).is_spare() == False)

class TestScore:

    def test_game(self):
        game = ['X', '8/', 'X', '90', '9/', '9/', 'X', '9/', 'X', 'X71']
        assert(Score(game).get_score() == 202)

    def test_when_there_is_a_spare_strike_it_should_count_the_spare_as_twenty(self):
        game = self.fill_zeroes(['0-0', '8/', 'X'])
        assert(Score(game).get_score() == 30)

    def test_when_there_is_a_spare_then_spare_it_should_only_count_the_first_ball_for_the_first_spare(self):
        game = self.fill_zeroes(['0-0', '8/', '7/'])
        assert(Score(game).get_score() == 27)

    def test_when_there_are_three_consecutive_strikes_the_first_should_count_as_thirty(self):
        game = self.fill_zeroes(['0-0', 'X', 'X', 'X'])
        assert(Score(game).get_score() == 60)

    def test_when_there_are_two_consecutive_strikes_and_a_spare_the_first_should_only_count_the_second_strike_and_first_ball_of_the_spare(self):
        game = self.fill_zeroes(['0-0', 'X', 'X', '8/'])
        assert(Score(game).get_score() == 58)

    def test_when_there_is_a_strike_spare_it_should_count_the_strike_as_twenty(self):
        game = self.fill_zeroes(['0-0', 'X', '8/'])
        assert(Score(game).get_score() == 30)

    def test_when_there_are_three_strikes_in_the_tenth_it_should_count_as_thirty(self):
        game = ['0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', 'XXX']
        assert(Score(game).get_score() == 30)

    def test_when_there_is_a_spare_strike_in_the_tenth_it_should_count_as_twenty(self):
        game = ['0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '9/ X']
        assert(Score(game).get_score() == 20)

    def test_when_there_is_a_strike_spare_in_the_tenth_it_should_count_as_twenty(self):
        game = ['0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '9/ X']
        assert(Score(game).get_score() == 20)

    def test_when_there_is_an_open_in_the_tenth_it_should_not_count_any_extra_pins(self):
        game = ['0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '7-2']
        assert(Score(game).get_score() == 9)

    def test_when_there_is_a_spare_in_the_ninth_and_a_strike_in_the_tenth_it_should_count_the_spare_as_twenty(self):
        game = ['0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '9/', 'X 0-0']
        assert(Score(game).get_score() == 30)

    def test_when_there_is_a_spare_in_the_ninth_and_a_spare_in_the_tenth_should_only_count_the_first_ball_in_the_tenth_towards_the_spare_in_the_ninth(self):
        game = ['0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '9/', '8/ 5']
        assert(Score(game).get_score() == 33)

    def test_when_there_is_a_strike_in_the_ninth_and_two_strikes_in_the_tenth_it_should_count_the_strike_as_thirty(self):
        game = ['0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', 'X', 'X X 0']
        assert(Score(game).get_score() == 50)

    def test_when_there_is_a_strike_in_the_ninth_and_strike_spare_in_the_tenth_it_should_only_count_the_first_two_balls_in_the_tenth_on_the_first_strike(self):
        game = ['0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', 'X', 'X 9/']
        assert(Score(game).get_score() == 50)

    def test_when_there_is_a_strike_in_the_ninth_and_a_spare_in_the_tenth_it_should_count_the_strike_as_twenty(self):
        game = ['0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', 'X', '9/ X']
        assert(Score(game).get_score() == 40)

    def test_when_there_are_all_strike_it_should_count_as_three_hundred(self):
        game = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'XXX']
        assert(Score(game).get_score() == 300)

    def test_when_there_are_all_gutters_it_should_count_as_zero(self):
        game = self.fill_zeroes([])
        assert(Score(game).get_score() == 0)

    def test_fill_zero(self):
        assert(self.fill_zeroes(['9/']) == ['9/', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0', '0-0'])

    def fill_zeroes(self, partial_score):
        return partial_score + list(map(lambda x: '0-0', range(0, 10 - len(partial_score))))