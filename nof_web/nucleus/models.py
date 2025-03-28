from flask_login import UserMixin

from nucleus import db,manager


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    short_body = db.Column(db.Text, nullable=False)
    full_body = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=False)
    status = db.Column(db.Text, nullable=False)


class Post_Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=False)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    
    first_name = db.Column(db.String(128), nullable=True)
    last_name = db.Column(db.String(128), nullable=True)
    middle_name = db.Column(db.String(128), nullable=True)
    faculty = db.Column(db.String(128), nullable=True)
    course = db.Column(db.String(128), nullable=True)
    rating = db.Column(db.Integer, nullable=False, default=0)

    role = db.Column(db.String(128), nullable=False, default='user')


class UserEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('post__games.id'))
    
    user = db.relationship('User', backref=db.backref('events', lazy=True))
    event = db.relationship('Post_Games', backref=db.backref('participants', lazy=True))



@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)