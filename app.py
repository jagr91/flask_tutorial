from flask import Flask, render_template, url_for
import random

app = Flask(__name__)


@app.route('/')
def index():
    first_name = "Grzegorz"
    some_list = [random.randint(0, 100) for i in range(10)]
    return render_template('index.html',
                           first_name=first_name,
                           some_list=some_list)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

# invalid URL - custom page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# internal server eror
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500