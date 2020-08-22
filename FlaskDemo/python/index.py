import flask
from flask import render_template

app = flask.Flask(__name__, template_folder='templates')

@app.route('/login')
def index():
    return render_template('base.html', title='Login')


@app.route('/')
def main():
    return render_template('index.html', title='Home')

app.run(debug=True)
