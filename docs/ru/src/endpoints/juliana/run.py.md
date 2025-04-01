# Модуль запуска приложения Juliana

## Обзор

Модуль `run.py` является точкой входа для запуска веб-приложения Juliana. Он отвечает за загрузку конфигурации, настройку маршрутов для веб-сайта и бэкенд API, а также запуск Flask-сервера.

## Подробней

Этот модуль инициализирует и запускает веб-приложение Juliana. Он загружает конфигурацию из файла `config.json`, настраивает маршруты для веб-сайта и бэкенд API, используя классы `Website` и `Backend_Api` соответственно. После настройки маршрутов Flask-сервер запускается с параметрами, указанными в конфигурации сайта.

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

**Назначение**: Основная функция, которая запускает веб-приложение Juliana.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Как работает функция**:

1.  **Загрузка конфигурации**: Загружает конфигурацию из файла `config.json`.
2.  **Настройка маршрутов веб-сайта**: Создает экземпляр класса `Website` и добавляет маршруты для веб-сайта, используя метод `app.add_url_rule`.
3.  **Настройка маршрутов бэкенд API**: Создает экземпляр класса `Backend_Api` и добавляет маршруты для бэкенд API, используя метод `app.add_url_rule`.
4.  **Запуск Flask-сервера**: Запускает Flask-сервер с параметрами, указанными в конфигурации сайта.

**ASCII Flowchart**:

```
Загрузка конфигурации из config.json
│
Создание экземпляра Website
│
Добавление маршрутов веб-сайта
│
Создание экземпляра Backend_Api
│
Добавление маршрутов бэкенд API
│
Запуск Flask-сервера
│
Вывод сообщения о закрытии порта
```

**Примеры**:

```python
# Пример запуска приложения
# Для запуска приложения необходимо выполнить этот модуль
# с помощью интерпретатора Python.
# python hypotez/src/endpoints/juliana/run.py