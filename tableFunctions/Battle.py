__author__ = 'dylan'
from json import dumps
from urllib import quote
from Connection import connect


def add_battle(ranking, city, description, video_link):
    database = connect()
    cursor = database.cursor()
    cursor.execute("INSERT INTO battle (ranking, city, description, video_link) VALUES(%s, %s, %s, %s)",
                   (ranking, city, description, video_link))
    database.commit()


def delete_battle(ranking):
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM battle WHERE ranking = %s", ranking)
    database.commit()


def edit_battle(rank, new_city, new_desc, new_link):
    database = connect()
    cursor = database.cursor()
    cursor.execute("UPDATE battle SET city = %s, description = %s, video_link = %s WHERE ranking = %s", (new_city, new_desc, new_link, rank))
    database.commit()


def get_battle_list():
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM battle GROUP BY ranking")
    rows = cursor.fetchall()
    data = {}
    for row in rows:
        data[str(row[3])] = {'urllink': str(row[2]), 'city': str(row[1]), 'desc': str(row[0])}
    return quote(dumps(data, sort_keys=True))


def query_battle_by_city(city):
    database = connect()
    cursor = database.cursor()
    sql = "SELECT * FROM battle WHERE city LIKE %s GROUP BY ranking"
    args = ['%'+city+'%']
    cursor.execute(sql, args)
    rows = cursor.fetchall()
    data = {}
    for row in rows:
        data[str(row[3])] = {'urllink': str(row[2]), 'city': str(row[1]), 'desc': str(row[0])}
    return quote(dumps(data, sort_keys=True))


def query_battle_by_ranking(ranking):
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM battle WHERE ranking = %s", ranking)
    rows = cursor.fetchall()
    data = {}
    for row in rows:
        data[str(row[3])] = {'urllink': str(row[2]), 'city': str(row[1]), 'desc': str(row[0])}
    return quote(dumps(data, sort_keys=True))