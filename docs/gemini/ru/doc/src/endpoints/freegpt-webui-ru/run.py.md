# Модуль запуска веб-приложения

## Обзор

Данный модуль является точкой входа для запуска веб-приложения, включающего в себя как пользовательский интерфейс (сайт), так и backend API. Он загружает конфигурацию из файла `config.json`, инициализирует маршруты для сайта и API, а затем запускает Flask-сервер.

## Подробнее

Модуль выполняет следующие действия:

1.  Загружает конфигурацию из файла `config.json`, который содержит параметры для настройки сайта и backend API.
2.  Инициализирует объект `Website` для настройки маршрутов сайта.
3.  Добавляет маршруты сайта в Flask-приложение.
4.  Инициализирует объект `Backend_Api` для настройки маршрутов API.
5.  Добавляет маршруты API в Flask-приложение.
6.  Запускает Flask-сервер с использованием параметров, указанных в конфигурации сайта.

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

**Назначение**: Главная функция, точка входа в приложение.

**Параметры**:
*   отсутствуют

**Возвращает**:
*   `None`

**Как работает функция**:

1.  **Загрузка конфигурации (`Load configuration`)**: Загружает конфигурацию из файла `config.json`.

2.  **Настройка маршрутов сайта (`Set up the website routes`)**: Создает экземпляр класса `Website`, передавая в него Flask-приложение `app`, и настраивает маршруты для веб-сайта.

3.  **Настройка маршрутов API (`Set up the backend API routes`)**: Создает экземпляр класса `Backend_Api`, передавая в него Flask-приложение `app` и конфигурацию `config`, и настраивает маршруты для backend API.

4.  **Запуск Flask-сервера (`Run the Flask server`)**: Запускает Flask-сервер с использованием конфигурации сайта, указывая порт и другие параметры.

5.  **Вывод сообщений в консоль**: Выводит сообщения о запуске и завершении работы сервера.

    ```text
    Загрузка конфигурации
    │
    ├── Создание экземпляра Website
    │   │
    │   └── Настройка маршрутов сайта
    │
    ├── Создание экземпляра Backend_Api
    │   │
    │   └── Настройка маршрутов API
    │
    └── Запуск Flask-сервера
    ```

**Примеры**:

Запуск приложения:

```python
python run.py