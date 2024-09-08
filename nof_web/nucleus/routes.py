from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from nucleus.decorators import is_admin
from sqlalchemy import desc


from nucleus import app, db
from nucleus.models import Post, Post_Games, User, UserEvent

@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('index.html', posts=posts, title='Новости', status1='active')

@app.route('/games')
@login_required 
def games():    
    posts = Post_Games.query.all()
    return render_template('games.html', posts=posts, title='Игры', status2='active')

@app.route('/participate/<int:event_id>', methods=['POST'])
@login_required
def participate(event_id):
    event = Post_Games.query.get_or_404(event_id)
    existing_participation = UserEvent.query.filter_by(user_id=current_user.id, event_id=event_id).first()

    if not existing_participation:
        participation = UserEvent(user_id=current_user.id, event_id=event_id)
        db.session.add(participation)
        db.session.commit()
        flash("Спасибо за участие!", "success")
    else:
        flash("Вы уже участвуете в этом мероприятии.", "warning")

    return redirect(url_for('games'))


@app.route('/news/<int:news_id>')
def news(news_id):
    post = Post.query.filter_by(id=news_id).one()
    return render_template('news.html', post=post, title='Новости', status1='active')

@app.route('/raiting')
def rating():
    users = User.query.order_by(desc(User.rating)).all()
    return render_template('user/userRating.html', users=users, title='Рейтинг', status5='active')
