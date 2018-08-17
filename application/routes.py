from flask import render_template
from application import app


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
