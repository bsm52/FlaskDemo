import flask
from flask import render_template, request

app = flask.Flask(__name__, template_folder='templates')

@app.route('/login')
def index():
    return render_template('base.html', title='Login')


@app.route('/')
def main():
    return render_template('index.html', title='Home')

@app.route('/hello', methods=['GET'])
def hello():
    if 'name' in request.args:
        name = request.args['name']
        return f"Thanks for stopping by, {name}"
    else:
        return "Please enter your name"


app.run(debug=True)
