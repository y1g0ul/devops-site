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

## CI/CD

В проекте есть два GitHub Actions workflow.

- **CI** (`.github/workflows/ci.yml`) запускается при push в `main` и при pull
  request в `main`. Он устанавливает зависимости, запускает тесты, проверяет
  конфигурацию Compose и собирает Docker-образ. Запуски для устаревших коммитов
  одной ветки отменяются, поэтому при частых push полностью проверяется только
  актуальная версия кода.
- **Deploy production** (`.github/workflows/deploy.yml`) запускается только
  вручную из вкладки **Actions** в GitHub. Он подключается к VPS по SSH,
  обновляет ветку `main` и перезапускает контейнеры через Docker Compose.

Для ручного деплоя один раз настройте на VPS каталог с клоном репозитория и
доступ пользователя к Docker. Затем добавьте в **Settings → Secrets and
variables → Actions**:

| Тип | Имя | Значение |
| --- | --- | --- |
| Secret | `SSH_HOST` | IP-адрес или доменное имя VPS |
| Secret | `SSH_USER` | Пользователь для SSH на VPS |
| Secret | `SSH_PRIVATE_KEY` | Приватный ключ этого пользователя для GitHub Actions |
| Secret | `SSH_KNOWN_HOSTS` | Строка хоста из `~/.ssh/known_hosts` VPS |
| Variable | `DEPLOY_PATH` | Абсолютный путь к клону проекта на VPS, например `/opt/devops-site` |

Не добавляйте приватный ключ, IP или `known_hosts` в репозиторий. Публичный ключ
из пары `SSH_PRIVATE_KEY` должен быть добавлен на VPS в
`~/.ssh/authorized_keys` пользователя деплоя. Значение для `SSH_KNOWN_HOSTS`
можно получить на доверенном компьютере после первой проверенной SSH-сессии:

```bash
ssh-keyscan -H YOUR_VPS_HOST
```

Перед сохранением сверьте fingerprint ключа хоста с данными VPS-провайдера или
с уже известным ключом сервера. Workflow использует `StrictHostKeyChecking=yes`,
поэтому не будет молча доверять незнакомому серверу.

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
