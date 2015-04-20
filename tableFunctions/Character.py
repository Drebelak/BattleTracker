__author__ = 'dylan'
from json import dumps
from urllib import quote
from Connection import connect


def add_character(name, role, battle_ranking, actor):
    database = connect()
    cursor = database.cursor()
    cursor.execute("INSERT INTO movie_character (name, role, battle_ranking, actor) VALUES(%s, %s, %s, %s)",
                   (name, role, battle_ranking, actor))
    database.commit()


def delete_character(name, battle_ranking):
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM movie_character WHERE name = %s and battle_ranking = %s", (name, battle_ranking))
    database.commit()


def edit_movie_character(name, new_role, battle_rank, new_actor):
    database = connect()
    cursor = database.cursor()
    cursor.execute("UPDATE movie_character SET role = %s, actor = %s WHERE name = %s and battle_ranking = %s",
                   (new_role, new_actor, name, battle_rank))
    database.commit()


def get_movie_character_list():
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM movie_character ORDER BY battle_ranking ASC")
    rows = cursor.fetchall()
    data = {}
    for row in rows:
        data[str(row[0])] = {'role': str(row[1]), 'battle_ranking': str(row[2]), 'actor': str(row[3])}
    return quote(dumps(data, sort_keys=True))


def query_movie_character_by_name(name):
    database = connect()
    cursor = database.cursor()
    sql = "SELECT * FROM movie_character WHERE name LIKE %s"
    args = ['%'+name+'%']
    cursor.execute(sql, args)
    rows = cursor.fetchall()
    data = {}
    for row in rows:
        data[str(row[0])] = {'role': str(row[1]), 'battle_ranking': str(row[2]), 'actor': str(row[3])}
    return quote(dumps(data, sort_keys=True))


def query_movie_character_by_movie(title):
    database = connect()
    cursor = database.cursor()
    sql = "SELECT name, role, title, movie.battle_ranking FROM (movie INNER JOIN movie_character ON movie.battle_ranking=movie_character.battle_ranking) WHERE title LIKE %s"
    args = ['%'+title+'%']
    cursor.execute(sql, args)
    rows = cursor.fetchall()
    data = {}
    for row in rows:
        data[str(row[0])] = {'role': str(row[1]), 'title': str(row[2]), 'battle_ranking': str(row[3])}
    return quote(dumps(data, sort_keys=True))

#query_movie_character_by_movie('Pirates of the Caribbean : At World\'s End')
