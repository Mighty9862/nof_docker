from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from nucleus.decorators import is_admin


from nucleus import app, db
from nucleus.models import Post, Post_Games, User, UserEvent, Departmen_Model



def create_data_from_bd():
    giga_text = '''Курсанты университета приняли участие в открытой технологической
              конференции "GIGA CONF", проводимой ПАО "Сбербанк".

            Члены научного кружка при кафедре информационной безопаности
            посетили открытую технологическую конференцию "GIGA CONF",
            проводимую ПАО "Сбербанк", которая стала площадкой для обмена
            опытом и обсуждения актуальных вопросов представителями
            международных организаций, бизнеса, научных и экспертных кругов,
            профессиональных ассоциаций из разных стран.
            <br />
            Наши курсанты в рамках данного мероприятия ознакомились с интересующими их докладами на различные тематики,
            подчерпнув для себя что-то новое, а также изучив представленные на конференции новые технологии в области
            разработки и искусственного интеллекта.'''
    
    hash_pwd = generate_password_hash('admin')
    hash_pwd2 = generate_password_hash('test')
    new_user = User(login='admin', password=hash_pwd, role='admin', first_name='Никита', last_name='Рожков', middle_name='Игоревич', faculty='ФПСОИБ', course='3', rating=100)
    new_user2 = User(login='test', password=hash_pwd2, role='user', first_name='Станислав', last_name='Помещиков', middle_name='Евгеньевич', faculty='ФПСОИБ', course='2', rating='0')
    
    post1 = Post(title='GIGA CONF', short_body='Посетили открытую технологическую конференцию "GIGA CONF", проводимую ПАО "Сбербанк".', 
                full_body=giga_text, img='../static/images/news/gigaconf.jpg', status='Внешнее мероприятие')
    post2 = Post(title='Tinkoff CTF', short_body='Cостоялись ежегодные международные соревнования по спортивному хакингу для ИТ-специалистов TinkoffCTF в формате оффлайн', 
                full_body='Cостоялись ежегодные международные соревнования по спортивному хакингу для ИТ-специалистов TinkoffCTF в формате оффлайн', img='../static/images/news/TinkoffCTF.jpg', status='Внешнее мероприятие')
    post3 = Post(title='GIGA CONF', short_body='Состоялась масштабная ИТ-конференция True Tech Day 2.0, проводимая ПАО «МТС», ключевой темой которой стала связь науки и технологий', 
                full_body='Состоялась масштабная ИТ-конференция True Tech Day 2.0, проводимая ПАО «МТС», ключевой темой которой стала связь науки и технологий', img='../static/images/news/MTSTrueTech.jpg', status='Внешнее мероприятие')
    
    game1 = Post_Games(title='Codeby CTF', body='Открыта регистрация на всероссийские CTF-соревнования по информационной безопансности, основная задача - нахождение уязвимостей в приложениях и нахождение там соответствующего "флага"',
                       img='../static/images/games/codeby.png')
    game2 = Post_Games(title='Научные открытия', body='Каждый участник готовит короткую презентацию о важном научном открытии. Презентации оцениваются по креативности, глубине исследования и ясности изложения',
                       img='../static/images/games/image.png')
    game3 = Post_Games(title='Киберполицейские', body='Игра строится в формате «своей игры», где команды, состоящие из 5 человек должны ответить на ряд вопросов по различным направлениям ИБ, таким как криптография, социальная инженерия, всё про IT и многие другие.',
                       img='../static/images/games/cyberpolice.jpg')
    
    dep1 = Departmen_Model(title='Информационной безопасности УНК ИТ', img='../static/images/departments/logo.png', small_title='ИБ УНК ИТ',
                          name_krug='Ad opus!', nach_krug = 'Начальник кафедры ИБ УНК ИТ Гончар В.В.', prepod_krug='Старший преподаватель кафедры ИБ УНК ИТ Полянская Е.П.')
    
    dep2 = Departmen_Model(title='Естественнонаучных дисциплин УНК ИТ', img='../static/images/departments/logo.png', small_title='ЕНД УНК ИТ',
                          name_krug='', nach_krug = 'Начальник кафедры Булгаков В.Г.', prepod_krug='Преподаватель кафедры Таранина Е.И.')

    User.query.delete()
    Post.query.delete()
    Post_Games.query.delete()
    UserEvent.query.delete()
    Departmen_Model.query.delete()

    db.session.add(new_user)
    db.session.add(new_user2)

    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    
    db.session.add(game1)
    db.session.add(game2)
    db.session.add(game3)

    db.session.add(dep1)
    db.session.add(dep2)

    db.session.commit()