import logging
import os
from character import Character

import pytest

LOG_FILE_NAME = os.getcwd() + os.sep + "log.txt"
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = "%(levelname)s %(asctime)s | %(filename)s | %(message)s"

LEVEL = os.environ.get("LOGLEVEL", DEFAULT_LOG_LEVEL)

# Config default logging
logging.basicConfig(filename=LOG_FILE_NAME, level=LEVEL, filemode='a', format=DEFAULT_LOG_FORMAT)


@pytest.fixture
def logger():
    yield logging.getLogger()


@pytest.fixture
def char1(logger):
    yield Character(name='Char1', hp=100, dmg=35, logger=logger)


@pytest.fixture
def char2(logger):
    yield Character(name='Char2', hp=100, dmg=52, logger=logger)


def test_character_hp_decreased_after_attack_return_true(char1: Character, char2: Character):
    char1.attack(char2)
    assert char2.hit_point == 65


def test_character_alive_after_attack_return_false(char1: Character, char2: Character):
    char2.attack(char1)
    char2.attack(char1)
    assert not char1.is_alive()


def test_character_alive_after_attack_return_true(char1: Character, char2: Character):
    char2.attack(char1)
    assert char1.is_alive()


def test_attack_empty_character_exception(char1: Character):
    with pytest.raises(ValueError):
        char1.attack(None)


def test_dead_character_attack_another_character_exception(char1: Character, char2: Character):
    char2.attack(char1)
    char2.attack(char1)
    with pytest.raises(ValueError):
        char1.attack(char2)
