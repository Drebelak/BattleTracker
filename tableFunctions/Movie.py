__author__ = 'dylan'
from json import dumps
from urllib import quote
from Connection import connect


def add_movie(title, year, rating, battle_ranking):
    database = connect()
    cursor = database.cursor()
    cursor.execute("INSERT INTO movie (title, year_produced, rating, battle_ranking) VALUES(%s, %s, %s, %s)",
                   (title, year, rating, battle_ranking))
    database.commit()


def delete_movie(title):
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM movie WHERE title = %s", title)
    database.commit()


def edit_movie(title, new_year, new_rating):
    database = connect()
    cursor = database.cursor()
    cursor.execute("UPDATE movie SET year_produced = %s, rating = %s WHERE title = %s", (new_year, new_rating, title))
    database.commit()


def get_movie_list():
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM movie GROUP BY battle_ranking")
    rows = cursor.fetchall()
    print("battle_ranking\tyear\trating\ttitle")
    data = {}
    for row in rows:
        print(str(row[3]) + "\t\t\t\t" + str(row[1]) + "\t" + str(row[2]) + "\t\t" + str(row[0]))
        data[str(row[0])] = {'year': str(row[1]), 'rating': str(row[2]), 'battle_ranking': str(row[3])}
    return quote(dumps(data, sort_keys=True))


def query_movie_by_title(title):
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM movie WHERE title = %s GROUP BY battle_ranking", title)
    rows = cursor.fetchall()
    print("battle_ranking\tyear\trating\ttitle")
    data = {}
    for row in rows:
        print(str(row[3]) + "\t\t\t\t" + str(row[1]) + "\t" + str(row[2]) + "\t\t" + str(row[0]))
        data[str(row[0])] = {'year': str(row[1]), 'rating': str(row[2]), 'battle_ranking': str(row[3])}
    return quote(dumps(data, sort_keys=True))


def query_movie_by_year(year):
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM movie WHERE year_produced = %s GROUP BY battle_ranking", year)
    rows = cursor.fetchall()
    print("battle_ranking\tyear\trating\ttitle")
    data = {}
    for row in rows:
        print(str(row[3]) + "\t\t\t\t" + str(row[1]) + "\t" + str(row[2]) + "\t\t" + str(row[0]))
        data[str(row[0])] = {'year': str(row[1]), 'rating': str(row[2]), 'battle_ranking': str(row[3])}
    return quote(dumps(data, sort_keys=True))