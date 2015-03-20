from flask import Flask
import Database
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test_page():
    Database.get_all()
    return 'This is a test'

if __name__ == '__main__':
    app.run()
