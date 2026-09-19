# Пульт охраны банка

Учёт визитов в хранилище по пропускам. Серверная часть на Django.

## Запуск

Для запуска у вас уже должен быть установлен Python 3.8+ и PostgreSQL.

- Скачайте код
- Создайте и активируйте виртуальное окружение:
  - Windows: `python -m venv venv` затем `venv\Scripts\activate`
  - Linux/macOS: `python3 -m venv venv` затем `source venv/bin/activate`
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл `.env` рядом с `manage.py`
- Примените миграции командой `python manage.py migrate`
- Запустите сервер командой `python manage.py runserver`

После этого переходите по ссылке [127.0.0.1:8000](http://127.0.0.1:8000) — вы увидите список активных карт доступа.

### Пример запуска

```
> python -m venv venv
> venv\Scripts\activate
(venv) > pip install -r requirements.txt
(venv) > python manage.py migrate
Operations to perform:
  Apply all migrations: datacenter
Running migrations:
  Applying datacenter.0001_initial... OK
(venv) > python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 3.2.12, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

**Для запуска проекта эти настройки обязательны** — без них Django не стартует.

Доступны следующие переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.
- `ALLOWED_HOSTS` — список доменов через запятую, на которых разрешено обслуживать сайт. Например: `127.0.0.1,localhost`. См. [документацию Django](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts).
- `DB_HOST` — адрес сервера PostgreSQL. Например: `localhost`.
- `DB_PORT` — порт PostgreSQL. Например: `5432`.
- `DB_PASSWORD` — пароль пользователя БД.

База данных называется `checkpoint`, пользователь — `guard`.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).