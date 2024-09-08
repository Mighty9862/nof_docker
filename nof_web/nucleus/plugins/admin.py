from flask import render_template, request, redirect, url_for
from nucleus.decorators import is_admin

from werkzeug.utils import secure_filename
import os

from nucleus import app, db
from nucleus.models import Post, Post_Games, User, UserEvent

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Модуль создания Новостей и Мероприятий

@app.route('/admin/create_news', methods=['POST', 'GET'])
@is_admin
def create_news():
    if request.method == 'POST':
        upload_folder = 'nucleus/static/images/news/'

        title = request.form['title']
        short_body = request.form['short_body']
        full_body = request.form['full_body']
        status = request.form['flexRadioDefault']
        
        if ((request.files.get('img')).content_type in ['image/jpeg','image/png','image/jpg']):
            file = request.files['img']

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(upload_folder + filename)
                
                img = (upload_folder.replace('nucleus', '..')) + filename

                post = Post(title=title, short_body=short_body, full_body=full_body, img=img, status=status)

                try:
                    db.session.add(post)
                    db.session.commit()
                    return redirect('/')
                except:
                    return 'При добавлении записи произошла ошибка'
        
        else:
            img = ''
            post = Post(title=title, short_body=short_body, full_body=full_body, img=img, status=status)

            try:
                db.session.add(post)
                db.session.commit()
                return redirect('/')
            except:
                return 'При добавлении записи произошла ошибка'

    else:
        return render_template('admin/adminNews.html', status3='active')


@app.route('/admin/create_games', methods=['POST', 'GET'])
@is_admin
def create_games():
    if request.method == 'POST':
        upload_folder = 'nucleus/static/images/games/'

        title = request.form['title']
        body = request.form['body']

        if ((request.files.get('img')).content_type in ['image/jpeg','image/png','image/jpg']):
            file = request.files['img']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(upload_folder + filename)
                
                img = (upload_folder.replace('nucleus', '..')) + filename

                game = Post_Games(title=title, body=body, img=img)

                try:
                    db.session.add(game)
                    db.session.commit()
                    return redirect('/')
                except:
                    return 'При добавлении записи произошла ошибка'
        else:
            img = ''
            game = Post_Games(title=title, body=body, img=img)

            try:
                db.session.add(game)
                db.session.commit()
                return redirect('/')
            except:
                return 'При добавлении записи произошла ошибка'

    else:
        
        return render_template('admin/adminGames.html', status3='active')
    


# Модуль создания списка Новостей, Мероприятий и Пользователей
    
@app.route('/admin/NewsList')
@is_admin
def news_list():
    posts = Post.query.all()
    return render_template('admin/adminNewsList.html', posts=posts, title='Список новостей', status3='active')

@app.route('/admin/GamesList')
@is_admin
def games_list():
    games = Post_Games.query.all()
    return render_template('admin/adminGamesList.html', games=games, title='Список мероприятий', status3='active')

@app.route('/admin/UsersList', methods=['GET', 'POST'])
@is_admin
def users_list():
    users = User.query.all()
    if (request.method == 'POST'):
        last_name = request.form['last_name']
        return search_users(last_name)

    return render_template('admin/adminUsersList.html', users=users, title='Список пользователей', status3='active')


# Модуль обновления данных внутри Новостей, Мероприятий и Пользовательской информации

@app.route('/update_news/<int:news_id>', methods=['GET', 'POST'])
@is_admin
def update_news(news_id):
    post = Post.query.get_or_404(news_id)

    if request.method == 'POST':
        upload_folder = 'nucleus/static/images/news/'

        post.title = request.form['title']
        post.short_body = request.form['short_body']
        post.full_body = request.form['full_body']
        post.status = request.form['flexRadioDefault']
        
        if ((request.files.get('img')).content_type in ['image/jpeg','image/png','image/jpg']):
            file = request.files['img']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(upload_folder + filename)
                
                post.img = (upload_folder.replace('nucleus', '..')) + filename

                try:
                    db.session.commit()
                    return redirect('/admin/NewsList')
                except:
                    return "There was a problem updating data."
        else:
            post.img = post.img
            try:
                db.session.commit()
                return redirect('/admin/NewsList')
            except:
                return "There was a problem updating data."

    else:
        title = "Update Data"
        shrot_body = "Update Data"
        full_body = "Update Data"
        img = "Update Data"
        cover = "Update Data"
        return render_template('admin/update_news.html', title=title, shrot_body=shrot_body, full_body=full_body, img=img, cover=cover, post=post)
    
@app.route('/update_games/<int:games_id>', methods=['GET', 'POST'])
@is_admin
def update_games(games_id):
    game = Post_Games.query.get_or_404(games_id)

    if request.method == 'POST':
        
        upload_folder = 'nucleus/static/images/games/'
        
        game.title = request.form['title']
        game.body = request.form['body']
        
        if ((request.files.get('img')).content_type in ['image/jpeg','image/png','image/jpg']):
            file = request.files['img']

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(upload_folder + filename)

                game.img = (upload_folder.replace('nucleus', '..')) + filename

                try:
                    db.session.commit()
                    return redirect('/admin/GamesList')
                except:
                    return "There was a problem updating data."
        else:
            game.img = game.img

            try:
                db.session.commit()
                return redirect('/admin/GamesList')
            except:
                return "There was a problem updating data."

    else:
        title = "Update Data"
        body = "Update Data"
        img = "Update Data"
        return render_template('admin/update_games.html', title=title, body=body, img=img, game=game)
    
@app.route('/update_users/<int:users_id>', methods=['GET', 'POST'])
@is_admin
def update_users(users_id):
    user = User.query.get_or_404(users_id)

    if request.method == 'POST':
    
        user.last_name = request.form['last_name']
        user.first_name = request.form['first_name']
        user.middle_name = request.form['middle_name']
        user.login = request.form['login']
        user.faculty = request.form['faculty']
        user.course = request.form['course']
        user.role = request.form['flexRadioDefault']
        user.rating += int(request.form['rating'])


        try:
            db.session.commit()
            return redirect('/admin/UsersList')
        except:
            return "There was a problem updating data."

    else:
        last_name = "Update Data"
        first_name = "Update Data"
        middle_name = "Update Data"
        login = "Update Data"
        faculty = "Update Data"
        course = "Update Data"
        role = "Update Data"
        rating = "Update Data"
        return render_template('admin/update_users.html', last_name=last_name, first_name=first_name, middle_name=middle_name,
                               login=login, faculty=faculty, course=course, role=role, rating=rating, user=user, title='Редактировать данные пользователя')


# Модуль для удаления Новостей, Мероприятий и Пользователей

@app.route('/delete_news/<int:news_id>')
@is_admin
def delete_news(news_id):
    post = Post.query.get_or_404(news_id)

    try:
        db.session.delete(post)
        db.session.commit()
        return redirect('/admin/NewsList')
    except:
        return "There was a problem deleting data."
    
@app.route('/delete_games/<int:games_id>')
@is_admin
def delete_games(games_id):
    game = Post_Games.query.get_or_404(games_id)

    try:
        db.session.delete(game)
        db.session.commit()
        return redirect('/admin/GamesList')
    except:
        return "There was a problem deleting data."
    
@app.route('/delete_users/<int:users_id>')
@is_admin
def delete_users(users_id):
    user = User.query.get_or_404(users_id)

    try:
        db.session.delete(user)
        db.session.commit()
        return redirect('/admin/UsersList')
    except:
        return "There was a problem deleting data."
    


@app.route('/admin/SearchUsers', methods=['GET', 'POST'])
@is_admin
def search_users(last_name):
    users = User.query.filter_by(last_name=last_name).all()
        
    return render_template('/admin/adminUserSearch.html', users=users, title='Поиск пользователей') 


@app.route('/participants/<int:games_id>')
@is_admin
def view_participants(games_id):
    game = Post_Games.query.get_or_404(games_id)
    participants = UserEvent.query.filter_by(event_id=games_id).all()

    users = [User.query.get(participant.user_id) for participant in participants]

    return render_template('/admin/participantsGames.html', game=game, participants=users, title='Список участников')


