
Настройка зависимостей:
pip install -r requirements.txt

Запуск приложения (выполнять из корневой директории):
uvicorn app.main:app

Для остановки приложения нажать CTRL+C

Запуск приложения в режиме отладки:
uvicorn app.main:app --reload

Обновление версии библиотеки json_db_lite до современной:
pip install --upgrade json_db_lite

Работа с postgres из терминала:

Вход с использованием superuser:
psql -U postgres
(ввести пароль от суперюзера)

Создание своего юзера для базы данных.
В данном случае команда выглядит так:
create user zlayazayaz with password 'zlayazayaz';

Создание базы данных под данного юзера:
create database fast_api with owner zlayazayaz;

Запуск базы данных PostgreSQL:
docker-compose up -d