from functools import wraps
from flask import render_template
from flask_login import current_user

from nucleus.models import User

def is_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # проверка на админа
        if current_user.role != 'admin' or current_user == None:
            return render_template('errors/404.html')
        return f(*args, **kwargs)
    return decorated_function