from enum import Enum


class Player(Enum):
    """
    Fixed life constants
    """
    lives: int = 1


class Enemy(Enum):
    """
    Fixed level constants
    """
    level: int = 1


class Score:

    @staticmethod
    def show_scores():
        """this static method to show scores from file"""
        with open('scores.txt') as file:
            scores = [string for string in file]
            scores_array = [string.split(' ') for string in scores]
            scores_array = sorted(scores_array, key=lambda x: x[-1])
            for score_idx in range(len(scores_array)):
                scores_array[score_idx][0] = score_idx + 1
            return scores_array

