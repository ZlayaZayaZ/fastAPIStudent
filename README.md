
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

Для создания миграций нам нужно зайти в папку «app» через консоль (cd app) и там выполнить команду:
alembic init -t async migration
после чего сгенерированный файл alembic.ini вынести в корень репозитория

Команда для создании миграции базы данных:
alembic revision --autogenerate -m "Initial revision"

Чтобы применить сгенерированные миграции:
alembic upgrade head

Чтобы откатить изменения:
alembic downgrade -1