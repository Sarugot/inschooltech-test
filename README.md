# Проект inschooltech_test
## Автор:


[Sarugot](https://github.com/Sarugot)


## Описание:
### Проект inschooltech_test

Проект inschooltech_test является тестовым заданием для компании Inschooltech. Данное задание предстваляет собой API сервис для получения данных медицинских исследований с возможностью фильтрации по лабораториям, которые проводили исследования.


## Технологии

Python 3.11

Django 4.2

Docker 3.8


## Шаблон наполнения env-файла:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=inschooltech_test_db
POSTGRES_USER=inschooltech_test_user
POSTGRES_PASSWORD=inschooltech_test_password
DB_HOST=db
DB_PORT=5432
```


## Описание команд для запуска приложения в контейнерах:

Перейти в папку с файлом docker-compose:

```
cd infra
```

Запустить контейнеры:

```
docker compose up -d --build
```

Выполнить миграции:

```
docker compose exec api python manage.py migrate
```

Создать суперпользователя:

```
docker compose exec api python manage.py createsuperuser
```


### Примеры запросов:

# Получение рецептов

Получить список всех рецептов. При указании параметров limit и offset выдача разделена по страницам.

```
GET /api/results/

[
    {
        "id": "59bb8ba9-a3ea-4e37-ba59-a40498a9e987",
        "lab_id": "ab5ccf66-cf95-468f-b5b4-0ba62446f7fe",
        "duration_seconds": "10.0",
        "results": [
            {
                "id": "ef3b4f6c-791a-4816-aea3-ed6dc189c192",
                "score": "10.00",
                "indicator_name": "Ловкость",
                "metric_name": "Прыжки",
                "metric_unit": "метры",
                "is_within_normal_range": false
            },
            {
                "id": "b0d4a6c4-e716-4f65-934c-4528fe83f6fe",
                "score": "17.00",
                "indicator_name": "Сила",
                "metric_name": "Жим",
                "metric_unit": "кг",
                "is_within_normal_range": true
            }
        ]
    }
]
```

Responses

```
200 Удачное выполнение запроса.
```

```
401 Пользователь не авторизован.
```
