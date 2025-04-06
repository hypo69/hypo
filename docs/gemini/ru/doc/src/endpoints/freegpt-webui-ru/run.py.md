# Модуль запуска веб-приложения `freegpt-webui-ru`

## Обзор

Модуль `run.py` является точкой входа для веб-приложения `freegpt-webui-ru`. Он отвечает за настройку маршрутов для веб-сайта и бэкенд API, а также за запуск Flask-сервера.

## Подробнее

Этот модуль загружает конфигурацию из файла `config.json`, инициализирует объекты `Website` и `Backend_Api`, добавляет маршруты из этих объектов в Flask-приложение и, наконец, запускает сервер Flask с использованием конфигурации, загруженной из `config.json`.

## Функции

### `__main__`

```python
if __name__ == '__main__':
    # Load configuration from config.json
    config = load(open('config.json', 'r'))
    site_config = config['site_config']

    # Set up the website routes
    site = Website(app)
    for route in site.routes:
        app.add_url_rule(
            route,
            view_func=site.routes[route]['function'],
            methods=site.routes[route]['methods'],
        )

    # Set up the backend API routes
    backend_api = Backend_Api(app, config)
    for route in backend_api.routes:
        app.add_url_rule(
            route,
            view_func=backend_api.routes[route]['function'],
            methods=backend_api.routes[route]['methods'],
        )

    # Run the Flask server
    print(f"Running on port {site_config['port']}")
    app.run(**site_config)
    print(f"Closing port {site_config['port']}")
```

**Назначение**: Главная функция модуля, которая выполняется при запуске скрипта.

**Параметры**: Отсутствуют.

**Возвращает**: Отсутствует.

**Вызывает исключения**: Отсутствуют.

**Как работает функция**:

1.  **Загрузка конфигурации**: Загружает конфигурацию из файла `config.json` с помощью `load(open('config.json', 'r'))`. Извлечение конфигурации веб-сайта `site_config = config['site_config']`.
2.  **Настройка маршрутов веб-сайта**:
    *   Создает экземпляр класса `Website`, передавая ему объект `app` (Flask-приложение). `site = Website(app)`.
    *   Проходит по всем маршрутам, определенным в `site.routes`, и добавляет каждый маршрут в Flask-приложение с помощью `app.add_url_rule()`.
        Для каждого маршрута указывается URL, функция-обработчик (`view_func`) и HTTP-методы (`methods`).
3.  **Настройка маршрутов бэкенд API**:
    *   Создает экземпляр класса `Backend_Api`, передавая ему объект `app` и объект `config`. `backend_api = Backend_Api(app, config)`.
    *   Проходит по всем маршрутам, определенным в `backend_api.routes`, и добавляет каждый маршрут в Flask-приложение, используя `app.add_url_rule()`, аналогично маршрутам веб-сайта.
4.  **Запуск Flask-сервера**:
    *   Выводит в консоль сообщение о запуске сервера на определенном порту: `print(f"Running on port {site_config['port']}")`.
    *   Запускает Flask-сервер с использованием конфигурации, определенной в `site_config`: `app.run(**site_config)`.
    *   Выводит в консоль сообщение о закрытии порта: `print(f"Closing port {site_config['port']}")`.

**ASCII flowchart функции `__main__`**:

```
Загрузка конфигурации из config.json
|
|
Создание экземпляра Website и добавление маршрутов
|
|
Создание экземпляра Backend_Api и добавление маршрутов
|
|
Запуск Flask-сервера
```

**Примеры**:

Пример запуска приложения:

```python
# Допустим, config.json содержит:
# {
#   "site_config": {
#     "port": 5000,
#     "debug": true
#   }
# }

# После запуска скрипта в консоли будет выведено:
# Running on port 5000
# ... (запуск Flask-сервера)
# Closing port 5000