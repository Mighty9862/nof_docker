from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from nucleus.decorators import is_admin


from nucleus import app, db
from nucleus.models import Post, Post_Games, User, UserEvent, Departmen_Model

def create_data_from_bd():
    hash_pwd = generate_password_hash('admin')
    hash_pwd2 = generate_password_hash('test')
    new_user = User(login='admin', password=hash_pwd, role='admin', first_name='Никита', last_name='Рожков', middle_name='Игоревич', faculty='ФПСОИБ', course='3', rating=100)
    new_user2 = User(login='test', password=hash_pwd2, role='user', first_name='Станислав', last_name='Помещиков', middle_name='Евгеньевич', faculty='ФПСОИБ', course='2', rating='0')
    post = Post(title='TEST', short_body='TEST', full_body='TEST', img='../static/images/news/pink-red-nebula-space-cosmos-4k-7m-3840x2400.jpg', status='Внешнее мероприятие')
    game = Post_Games(title='TEST', body='TEST', img='../static/images/games/pink-red-nebula-space-cosmos-4k-7m-3840x2400.jpg')
    dep = Departmen_Model(title='Информационной безопасности УНК ИТ')

    User.query.delete()
    Post.query.delete()
    Post_Games.query.delete()
    UserEvent.query.delete()
    Departmen_Model.query.delete()

    db.session.add(new_user)
    db.session.add(new_user2)
    db.session.add(post)
    db.session.add(game)
    db.session.add(dep)
    db.session.commit()