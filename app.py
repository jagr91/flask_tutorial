from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = "mySecretKey"


class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


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
def server_error(e):
    return render_template('500.html'), 500

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    
    return render_template('name.html', name=name, form=form)
