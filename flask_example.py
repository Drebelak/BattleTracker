from flask import Flask, jsonify, render_template, request
import Database
import tableFunctions.Battle as Battle
import tableFunctions.Character as Character
import tableFunctions.Movie as Movie

app = Flask(__name__)


@app.route('/test')
def test_page():
    return 'This is a Test'


@app.route('/')
def test_flask():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def search_form():
    search_value = request.form['sbox']
    category = request.form['category']
    response = ""
    search_type = ""
    if category == "Battle Ranking":
        response = Battle.query_battle_by_ranking(search_value)
        search_type = "battle"
    if category == "City":
        response = Battle.query_battle_by_city(search_value)
        search_type = "battle"
    if category == "Character":
        response = Character.query_movie_character_by_name(search_value)
        search_type = "character"
    if category == "Movie Title":
        response = Movie.query_movie_by_title(search_value)
        search_type = "movie"
    if category == "Movie Year":
        response = Movie.query_movie_by_year(search_value)
        search_type = "movie"
    if category == "All Battles":
        response = Battle.get_battle_list()
        search_type = "battle"
    if category == "All Characters":
        response = Character.get_movie_character_list()
        search_type = "character"
    if category == "All Movies":
        response = Movie.get_movie_list()
        search_type = "movie"

    print search_value + " and " + category
    return render_template('home.html', res=response, type=search_type)


@app.route('/map')
def test_api_flask():
    battles = Battle.get_battle_list()
    return render_template('test.html', b=battles)


@app.route('/records')
def login():
    return render_template('login.html')


@app.route('/records', methods=['POST'])
def records_page():
    user = request.form['user']
    password = request.form['password']
    if user == 'admin@admin' and password == 'test':
        attr1 = request.form.get('attr1', None)
        attr2 = request.form.get('attr2', None)
        attr3 = request.form.get('attr3', None)
        attr4 = request.form.get('attr4', None)
        operation = request.form.get('operation', None)
        table = request.form.get('type', None)

        print attr1, attr2, attr3, attr4, table, operation

        if table == 'movie':
            if operation == "Add":
                Movie.add_movie(attr1, attr2, attr3, attr4)
            elif operation == "Edit":
                Movie.edit_movie(attr1, attr2, attr3)
            elif operation == "Delete":
                Movie.delete_movie(attr1)
        elif table == 'character':
            if operation == "Add":
                Character.add_character(attr1, attr2, attr3)
            elif operation == "Edit":
                Character.edit_movie_character(attr1, attr2, attr3)
            elif operation == "Delete":
                Character.delete_character(attr1, attr3)
        elif table == 'battle':
            if operation == "Add":
                Battle.add_battle(attr1, attr2, attr3, attr4)
            elif operation == "Edit":
                Battle.edit_battle(attr1, attr2, attr3, attr4)
            elif operation == "Delete":
                Battle.delete_battle(attr1)

        return render_template('records.html', user=user, password=password)
    else:
        return render_template('login.html')


@app.route('/api/battles', methods=['GET'])
def get_all_battles():
    return jsonify({'battles': Battle.get_battle_list()})


@app.route('/api/battles', methods=['GET'])
def add_battle_to_db(ranking, city, description, video_link):
    return jsonify({'battles': Battle.add_battle(ranking, city, description, video_link)})


@app.route('/api/battles/<city>', methods=['GET'])
def get_query_battle(city):
    print(city)
    return jsonify({'battles': Battle.query_battle_by_city(city)})


@app.route('/api/characters', methods=['GET'])
def get_all_characters():
    return jsonify({'characters': Character.get_movie_character_list()})


@app.route('/api/characters/<name>', methods=['GET'])
def get_character_by_name(name):
    return jsonify({'character': Character.query_movie_character_by_name(name)})


@app.route('/api/movies', methods=['GET'])
def get_all_movies():
    return jsonify({'movies': Movie.get_movie_list()})


@app.route('/api/movies/<year>', methods=['GET'])
def get_movies_by_year(year):
    return jsonify({'movies': Movie.query_movie_by_year(year)})


@app.route('/api/movies/<title>', methods=['GET'])
def get_movies_by_title(title):
    return jsonify({'movies': Movie.query_movie_by_title(title)})

if __name__ == '__main__':
    app.run()