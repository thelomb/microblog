from flask import render_template, flash, redirect, url_for
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
        username = form.username.data
        remember = form.remember_me.data
        flash_text = (
            'Login requested for {}, {}'
            .format(username, remember)
        )
        flash(flash_text)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
