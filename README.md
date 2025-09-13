
Настройка зависимостей:
pip install -r req.txt

Запуск приложения (выполнять из корневой директории):
uvicorn app.main:app

Для остановки приложения нажать CTRL+C

Запуск приложения в режиме отладки:
uvicorn app.main:app --reload

Обновление версии библиотеки json_db_lite до современной:
pip install --upgrade json_db_lite
