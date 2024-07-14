from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from nucleus.decorators import is_admin


from nucleus import app, db
from nucleus.models import Post, Post_Games, User

@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('index.html', posts=posts, title='Новости', status1='active')

@app.route('/games')
@login_required 
def games():    
    posts = Post_Games.query.all()
    return render_template('games.html', posts=posts, title='Игры', status2='active')

@app.route('/news/<int:news_id>')
def news(news_id):
    post = Post.query.filter_by(id=news_id).one()
    return render_template('news.html', post=post, title='Новости', status1='active')

