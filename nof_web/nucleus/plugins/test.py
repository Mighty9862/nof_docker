from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from nucleus.decorators import is_admin


from nucleus import app, db
from nucleus.models import Post, Post_Games, User

def create_data_from_bd():
    hash_pwd = generate_password_hash('admin')
    new_user = User(login='admin', password=hash_pwd, role='admin')
    post = Post(title='TEST', short_body='TEST', full_body='TEST', img='', status='Внешнее мероприятие')
    game = Post_Games(title='TEST', body='TEST', img='')

    User.query.delete()
    Post.query.delete()
    Post_Games.query.delete()

    db.session.add(new_user)
    db.session.add(post)
    db.session.add(game)
    db.session.commit()