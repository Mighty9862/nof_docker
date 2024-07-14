from flask import render_template
from flask_login import login_required

from nucleus import app, db
from nucleus.models import Post, Post_Games, User

@app.route('/profile/<string:user_id>')
@login_required 
def profile(user_id):
    user = User.query.filter_by(login=user_id).first()
    
    return render_template('user/userProfile.html', user=user, title='Личный кабинет', status4='active')