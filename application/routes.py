from flask import render_template, flash, redirect
from application import app
from application.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'The Lomb'}
    posts = [
        {
            'author': {'username': 'Bob'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for {form.username.data}, {form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
