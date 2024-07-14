# Выкачиваем из dockerhub образ с python версии 3.9
FROM python:3.9
# Устанавливаем рабочую директорию для проекта в контейнере
WORKDIR /nof_web
# Скачиваем/обновляем необходимые библиотеки для проекта 
COPY requirements.txt /nof_web
RUN pip3 install --upgrade pip -r requirements.txt
# |ВАЖНЫЙ МОМЕНТ| копируем содержимое папки, где находится Dockerfile, 
# в рабочую директорию контейнера
COPY . /nof_web
# Устанавливаем порт, который будет использоваться для сервера
EXPOSE 8000