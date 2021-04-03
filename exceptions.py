import datetime


class GameOver(Exception):
    """
    Write score to file score.txt
    """

    @staticmethod
    def write_score_to_file(player):
        with open('scores.txt', 'a+') as file:
            file.write('Name: ' + player.name + ' ' + 'Score: ' + str(player.score) +
                       ' | ' + str(datetime.datetime.now()) + '\n')


class EnemyDown(Exception):
    pass
