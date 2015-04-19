from flask import Flask, render_template, request
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

    if category == "Battle by Ranking":
        response = Battle.query_battle_by_ranking(search_value)
        search_type = "battle"
    if category == "Battles by City":
        response = Battle.query_battle_by_city(search_value)
        search_type = "battle"
    if category == "Characters by Name":
        response = Character.query_movie_character_by_name(search_value)
        search_type = "character"
    if category == "Characters by Movie":
        response = Character.query_movie_character_by_movie(search_value)
        search_type = "mov_char"
    if category == "Movies by Title":
        response = Movie.query_movie_by_title(search_value)
        search_type = "movie"
    if category == "Movies by Year":
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


if __name__ == '__main__':
    app.run()