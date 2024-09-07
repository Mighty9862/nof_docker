from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from nucleus import app, db
from nucleus.models import User

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')
    
    if login and password:
        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user) 

            next_page = request.args.get('next')

            return redirect('games')    #TODO: редирект на профиль пользователя
        else:
            flash('Неверный логин или пароль')
    else:
        flash('Заполните все поля')

    return render_template('login_page.html', title='Вход')

@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('login2')
    password = request.form.get('password2')
    
    if request.method == 'POST':
        hash_pwd = generate_password_hash(password)
        
        new_user = User(login=login, password=hash_pwd)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login_page'))

        
    
    return render_template('register.html', title='Регистрация')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page'))
    return response