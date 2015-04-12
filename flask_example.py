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
    if category == "Battle Ranking":
        response = Battle.query_battle_by_ranking(search_value)
    print search_value + " and " + category
    return render_template('home.html', res=response)


@app.route('/map')
def test_api_flask():
    battles = Battle.get_battle_list()
    return render_template('test.html', b=battles)


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