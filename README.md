# Описание
Небольшой Django-проект, сделанный в рамках тестового задания. Представляет собой "онлайн-библиотеку" с возможностью брать и возвращать книги.
# Инструкции по развёртыванию
1. Создать переменную среду Python (`python -m venv venv`)
2. Активировать переменную среду (`venv\scripts\activate` для Windows или (`source venv/bin/activate`) для Linux
3. Установить зависимости проекта (`pip install -r requirements.txt`)
4. Перейти в директорию src (`cd src`)
5. Применить миграции (`python manage.py migrate`)
6. При необходимости, установить переменные окружения (`SET NAME=VALUE` для Windows и `export NAME="VALUE"` для Linux): `DJANGO_SECRET_KEY` для указания секретного ключа Django и `DEBUG` для выбора debug-режима
7. Создать аккаунт администратора (`python manage.py createsuperuser`)
8. Собрать static-файлы (`python manage.py collectstatic`)
9. Запустить dev-сервер (`python manage.py runserver`)
# Инструкции по использованию
- Админ-панель доступна по адресу `/admin`, с ёё помощью можно наполнить сайт книгами и пользователями. Для авторизации можно использовать аккаунт созданный в ходе развёртывания (шаг **7**)
- Главная страница `/` для читателей и неавторизованных пользователей представляет собой список книг, а для библиотекарей - список владельцев книг
- Страница `/books/my` доступна только читателям и представляет собой список книг на руках у пользователя
- API доступно по адресу `/api`
  - Схема drf-spectacular доступна по адресу `api/schema`, а документация swagger - `/api/schema/swagger-ui`
  - JWT аутентификация доступна по адресу `/api/auth/jwt/create`, `/api/auth/jwt/refresh` и `/api/auth/jwt/blacklist`
  - API-книг доступно по адресу `/api/books`, `/api/books/my`, `/api/books/take` и `/api/books/return`
    - Методы `/books/my`, `/books/take` и `/books/return` доступны только читателям
