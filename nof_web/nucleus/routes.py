from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from nucleus.decorators import is_admin
from sqlalchemy import desc


from nucleus import app, db
from nucleus.models import Post, Post_Games, User, UserEvent, Departmen_Model

@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('index.html', posts=posts, title='Новости', status1='active')


@app.route('/games')
@login_required 
def games():    
    posts = Post_Games.query.all()
    user_events = {event.event_id for event in UserEvent.query.filter_by(user_id=current_user.id).all()}
    return render_template('games.html', posts=posts, user_events=user_events, title='Игры', status2='active')

@app.route('/departments')
@login_required 
def departments():    
    #posts = Post_Games.query.all()
    deps = Departmen_Model.query.all()
    #user_events = {event.event_id for event in UserEvent.query.filter_by(user_id=current_user.id).all()}
    return render_template('departmentList.html', title='Кружки кафедр', status3='active', deps=deps)

@app.route('/departments/<int:dep_id>')
@login_required 
def department(dep_id):    
    deps = Departmen_Model.query.all()
    #user_events = {event.event_id for event in UserEvent.query.filter_by(user_id=current_user.id).all()}
    return render_template('department.html', title='Кружки кафедр', status3='active', deps=deps)


@app.route('/join_event/<int:event_id>')
@login_required
def join_event(event_id):
    # Проверка, не участвует ли уже пользователь
    if not UserEvent.query.filter_by(user_id=current_user.id, event_id=event_id).first():
        participation = UserEvent(user_id=current_user.id, event_id=event_id)
        db.session.add(participation)
        db.session.commit()
    return redirect(url_for('games'))

@app.route('/leave_event/<int:event_id>')
@login_required
def leave_event(event_id):
    # Найти запись об участии
    participation = UserEvent.query.filter_by(user_id=current_user.id, event_id=event_id).first()
    if participation:
        db.session.delete(participation)
        db.session.commit()
    return redirect(url_for('games'))


@app.route('/news/<int:news_id>')
def news(news_id):
    post = Post.query.filter_by(id=news_id).one()
    return render_template('news.html', post=post, title='Новости', status1='active')

@app.route('/raiting')
def rating():
    users = User.query.order_by(desc(User.rating)).all()
    return render_template('user/userRating.html', users=users, title='Рейтинг', status5='active')
