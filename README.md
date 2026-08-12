# NIK/OS — персональный сайт

Одностраничный сайт-визитка начинающего DevOps / системного инженера. Интерфейс оформлен как собственная цифровая среда: системный профиль, файловый браузер навыков, журнал опыта и небольшой интерактивный терминал.

На этом этапе проект содержит только Flask-приложение и vanilla frontend. База данных и инфраструктурные инструменты намеренно не добавлены.

## Что внутри

- Python + Flask;
- Jinja-шаблон;
- HTML, CSS и JavaScript без frontend-фреймворков;
- скачивание PDF-резюме через Flask;
- healthcheck `GET /health`;
- адаптивная вёрстка;
- поддержка `prefers-reduced-motion`;
- базовые тесты маршрутов.

## Локальный запуск

Требуется Python 3.10 или новее.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python run.py
```

После запуска сайт будет доступен по адресу `http://127.0.0.1:5000`.

## Проверка

```bash
python -m unittest discover -s tests
```

Проверить healthcheck:

```bash
curl http://127.0.0.1:5000/health
```

Ожидаемый ответ:

```json
{"status":"ok"}
```

## Структура

```text
.
├── app/
│   ├── static/
│   │   ├── css/portfolio.css
│   │   ├── js/main.js
│   │   └── resume/nikita-kirilenko-resume.pdf
│   ├── templates/index.html
│   ├── __init__.py
│   └── routes.py
├── tests/test_app.py
├── requirements.txt
└── run.py
```
