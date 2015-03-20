__author__ = 'dylan'
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
    print("rank\turl\t\t\tcity\t\t\t\tdesc")
    for row in rows:
        print(str(row[3]) + "\t\t" + str(row[2]) + "\t\t" + str(row[1]) + "\t\t\t" + str(row[0]))


def query_battle_by_city(city):
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM battle WHERE city = %s GROUP BY battle_ranking", city)
    rows = cursor.fetchall()
    print("rank\turl\t\t\tcity\t\t\t\tdesc")
    for row in rows:
        print(str(row[3]) + "\t\t" + str(row[2]) + "\t\t" + str(row[1]) + "\t\t\t" + str(row[0]))