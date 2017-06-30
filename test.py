import pytest
from scoring_functions import Score

class TestYeah:

    def test_game(self):
        game = ['X', '8/', 'X', '90', '9/', '9/', 'X', '9/', 'X', 'X 7-1']
        assert(Score.get_score(self, game) == 192)

