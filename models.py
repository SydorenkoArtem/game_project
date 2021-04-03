import random

from settings import Player as ConstantPlayer, Enemy as ConstantEnemy
from exceptions import GameOver, EnemyDown


class Enemy:
    """
    Class include method random select attack and decrease lives
    """

    def __init__(self):
        self. level: int = ConstantEnemy.level.value
        self.lives: int = self.level

    @staticmethod
    def select_attack():
        """
        This method select random attack from 1 to 3
        :return: int
        """

        return random.randint(1, 3)

    def decrease_lives(self):
        """
        in this method, life is taken from the enemy in case of a failed defense.
        If the enemy ran out of lives, the enemy's level rises and the life level
        is equal to the enemy's level
        :return: int
        """

        self.lives -= 1
        if self.lives == 0:
            self.level += 1
            self.lives = self.level
            raise EnemyDown


class Player:
    """
    Has properties: name, lives, score, allowed_attacks.
    The constructor takes the name of the player.
    The number of lives is indicated from the settings. The score is zero.
    """

    def __init__(self):
        self.score = 0
        self.name: str = self.create_name()
        self.start: str = self.start_game()
        self.lives: int = ConstantPlayer.lives.value

    @classmethod
    def create_name(cls):
        """
        In this method, the player's name is created and the input is checked for correctness.
        :return: str
        """

        name = input("Введите свое имя: ")
        while not name.isalpha():
            if not name.isalpha():
                name = input("Похоже вы ввели не имя. Введите свое имя: ")
        return name

    @classmethod
    def start_game(cls):
        """
        the user enters "start" to start the game.
        :return: str
        """
        start = input("Введите start для начала игры: ")

        while start != 'start':
            if start != 'start':
                start = input("Вы не ввели start. Введите start для начала игры: ")

    @staticmethod
    def fight(attack, defense):
        """
        returns the result of the round - 0 if there is a draw, -1 if the attack is unsuccessful,
        1 if the attack is successful.
        :param attack: int
        :param defense: int
        :return: int
        """

        if attack == 1 and defense == 2 or attack == 3 and defense == 1 or attack == 2 and defense == 3:
            return 1
        elif attack == defense:
            return 0
        else:
            return -1

    def decrease_lives(self):
        """
        in this method, the player's life is taken away in the event of an unsuccessful defense.
        When the lives are 0, the game ends.
        :return: int
        """

        self.lives -= 1
        if self.lives == 0:
            raise GameOver

    def attack(self, enemy_obj: Enemy):
        """
        receives input from user (1, 2, 3), selects enemy attack from enemy_obj object;
        calls the fight () method; If the result of the battle is 0, print "It's a draw!",
        If 1 = "You attacked successfully!"
        and reduces the number of lives of the enemy by 1, if -1 = "You missed!"
        :param enemy_obj: int
        :return: str
        """

        hero = int(input("Выберите героя: 1 - волшебник, 2 - воин, 3 - разбойник: "))

        while hero not in (1, 2, 3):
            if hero != 1 or hero != 2 or hero != 3:
                hero = int(input(
                    "Вы ввели некорректную атаку.\nВыберите героя: 1 - волшебник, 2 - воин, 3 - разбойник: "))

        fight_score = Player.fight(hero, enemy_obj.select_attack())

        if fight_score == 0:
            print("It's a draw!")
        elif fight_score == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
            self.score += 1
        else:
            print("You missed!")

    def defence(self, enemy_obj: Enemy):
        """
        We receive input from the enemy (1, 2, 3), the user chooses the attack;
        calls the fight () method; If the result of the battle is 0, print "It's a draw!",
        If 1 = "Enemy attacked successfully!" and decreases the number of lives of the user by 1,
        if -1 = "Enemy missed!"
        :param enemy_obj: int
        :return: str
        """
        hero = int(input("Выберите героя: 1 - волшебник, 2 - воин, 3 - разбойник: "))
        fight_score = Player.fight(enemy_obj.select_attack(), hero)

        if fight_score == 0:
            print("It's a draw!")
        elif fight_score == 1:
            print("Enemy attacked successfully!")
            self.decrease_lives()
        else:
            print("Enemy missed!")
