__author__ = 'dylan'
from Connection import connect
from tableFunctions.Battle import get_battle_list
from tableFunctions.Character import get_movie_character_list
from tableFunctions.Movie import get_movie_list


def get_all():
    get_battle_list()
    get_movie_list()
    get_movie_character_list()


def reset_battle():
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM battle")
    database.commit()


def reset_movie():
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM movie")
    database.commit()


def reset_movie_character():
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM movie_character")
    database.commit()


def reset():
    reset_movie()
    reset_movie_character()
    reset_battle()
