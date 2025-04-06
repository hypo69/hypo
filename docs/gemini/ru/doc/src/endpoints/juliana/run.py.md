# Модуль запуска приложения Juliana

## Обзор

Модуль `run.py` предназначен для запуска веб-приложения Juliana. Он загружает конфигурацию из файла `config.json`, настраивает маршруты для веб-сайта и бэкенд API, а затем запускает Flask-сервер.

## Подробней

Этот файл является точкой входа для запуска веб-приложения. Он выполняет следующие действия:

1.  Загружает конфигурацию из файла `config.json`.
2.  Инициализирует классы `Website` и `Backend_Api`, передавая им инстанс приложения Flask.
3.  Добавляет маршруты из `site.routes` и `backend_api.routes` в приложение Flask, связывая URL с соответствующими функциями и методами.
4.  Запускает Flask-сервер с параметрами, указанными в конфигурации.

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

**Назначение**: Основная функция, запускающая веб-приложение.

**Как работает функция**:

1.  **Загрузка конфигурации**: Загружает конфигурацию из файла `config.json` с помощью функции `load` из модуля `json`.

2.  **Настройка маршрутов веб-сайта**: Создает экземпляр класса `Website`, передавая ему объект `app` (Flask-приложение). Затем добавляет маршруты веб-сайта, используя метод `add_url_rule` приложения Flask. Для каждого маршрута устанавливается функция обработки (`view_func`) и HTTP-методы (`methods`).

3.  **Настройка маршрутов API**: Создает экземпляр класса `Backend_Api`, передавая ему объект `app` и конфигурацию. Аналогично добавляет маршруты API, используя метод `add_url_rule` приложения Flask.

4.  **Запуск Flask-сервера**: Запускает Flask-сервер с использованием параметров, указанных в конфигурации (`site_config`). Выводит в консоль сообщение о запуске сервера на определенном порту и сообщение о закрытии порта после остановки сервера.

**ASCII Flowchart**:

```
Загрузка конфигурации из config.json (config = load(open('config.json', 'r')))
|
Создание экземпляра класса Website (site = Website(app))
|
Добавление маршрутов веб-сайта (app.add_url_rule)
|
Создание экземпляра класса Backend_Api (backend_api = Backend_Api(app, config))
|
Добавление маршрутов API (app.add_url_rule)
|
Запуск Flask-сервера (app.run(**site_config))
```

**Примеры**:

```python
# Пример запуска приложения (в данном случае пример не требуется, так как это основная функция)