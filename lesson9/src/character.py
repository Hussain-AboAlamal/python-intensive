"""
Contains classes for our future MMORPG
"""
from logging import Logger


class Character:

    def __init__(self, name: str, hp: int, dmg: int, logger: Logger):
        self.name = name
        self.hit_point = hp
        self.damage = dmg
        self.logger = logger

    def is_alive(self) -> bool:
        """Checks if the caracter have positive health points

        Returns:
            bool: _description_
        """
        alive = self.hit_point > 0
        if not alive:
            print('dead')
            self.logger.info(f'{self.name} is Defeated')
        return alive

    def attack(self, enemy: "Character") -> None:
        """Reduces the hitpoint of an enemy

        Args:
            enemy (Character): Enemy to reduce hitpoints

        Raises:
            ValueError: Raises when enemy is not passed
        """
        if not enemy:
            raise ValueError("Missing enemy Character")
        
        enemy.hit_point -= self.damage
        self.logger.info(f"{self.name} attacked {enemy.name}")
