from exceptions import GameOver, EnemyDown
from models import Player, Enemy


def play():
    player = Player()
    enemy = Enemy()

    while player.lives != 0:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown:
            player.score += 5
        except GameOver as err:
            err.write_score_to_file(player)


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye")
