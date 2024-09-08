from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from nucleus import app, db
from nucleus.models import Post, Post_Games, User, UserEvent

@app.route('/profile/<string:user_id>')
@login_required 
def profile(user_id):
    user = User.query.filter_by(login=user_id).first()

    return render_template('user/userProfile.html', user=user, title='Личный кабинет', status4='active')


@app.route('/withdraw/<int:event_id>', methods=['POST'])
@login_required
def withdraw(event_id):
    participation = UserEvent.query.filter_by(user_id=current_user.id, event_id=event_id).first()

    if participation:
        db.session.delete(participation)
        db.session.commit()
        flash("Вы отказались от участия.", "success")
    else:
        flash("Вы не участвуете в этом мероприятии.", "warning")

    return redirect(url_for('profile', user_id=current_user.login))
