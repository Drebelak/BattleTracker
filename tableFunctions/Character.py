__author__ = 'dylan'
from Connection import connect


def add_character(name, role, battle_ranking):
    database = connect()
    cursor = database.cursor()
    cursor.execute("INSERT INTO movie_character (name, role, battle_ranking) VALUES(%s, %s, %s)",
                   (name, role, battle_ranking))
    database.commit()


def delete_character(name, battle_ranking):
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM movie_character WHERE name = %s and battle_ranking = %s", (name, battle_ranking))
    database.commit()


def edit_movie_character(name, battle_rank, new_role):
    database = connect()
    cursor = database.cursor()
    cursor.execute("UPDATE movie_character SET role = %s WHERE name = %s and battle_ranking = %s" , (new_role, name, battle_rank))
    database.commit()


def get_movie_character_list():
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM movie_character GROUP BY battle_ranking")
    rows = cursor.fetchall()
    print("name\t\t\trole\t\t\tbattle_ranking")
    for row in rows:
        print(str(row[0]) + "\t\t" + str(row[1]) + "\t\t\t" + str(row[2]))


def query_movie_character_by_name(name):
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM movie_character WHERE name = %s GROUP BY battle_ranking", name)
    rows = cursor.fetchall()
    print("name\t\t\trole\t\t\tbattle_ranking")
    for row in rows:
        print(str(row[0]) + "\t\t" + str(row[1]) + "\t\t\t" + str(row[2]))