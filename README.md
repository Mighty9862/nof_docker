1. git clone https://github.com/Mighty9862/nof_docker.git
2. cd nof_docker
3. docker-compose up / docker compose up


1. При каждом запуске срабатывает юнит-тест и все данные из бд обнуляются, чтобы это убрать необходимо в файле nof_web/nucleus/__init__.py убрать строку create_data_from_bd()
2. Загрузка изображений для новостей и мероприятий работает только если проект запущен через Docker, через IDE работать не будет
