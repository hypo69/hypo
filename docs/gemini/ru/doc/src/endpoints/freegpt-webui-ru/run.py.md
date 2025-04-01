# Модуль запуска веб-приложения FreeGPT WebUI (run.py)

## Обзор

Модуль `run.py` является точкой входа для веб-приложения FreeGPT WebUI. Он отвечает за загрузку конфигурации, настройку маршрутов для веб-сайта и backend API, а также запуск Flask-сервера.

## Подробней

Этот модуль играет важную роль в инициализации и запуске всего приложения. Он использует конфигурацию из файла `config.json` для настройки веб-сайта и API, а также запускает Flask-сервер на указанном порту. Без этого модуля приложение не сможет функционировать.

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

**Назначение**: Главная функция, которая запускает веб-приложение.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

**Как работает функция**:

1.  **Загрузка конфигурации**:
    -   Извлекает конфигурацию из файла `config.json`.
    -   Использует стандартную библиотеку `json` для десериализации JSON-файла.
    -   Получает конфигурацию веб-сайта из ключа `site_config`.
2.  **Настройка маршрутов веб-сайта**:
    -   Создает экземпляр класса `Website`, передавая ему экземпляр Flask-приложения (`app`).
    -   Добавляет маршруты веб-сайта, итерируясь по словарю `site.routes` и используя метод `app.add_url_rule` для каждого маршрута.
    -   `route`: URL маршрута.
    -   `view_func`: Функция, которая будет обрабатывать запросы к этому маршруту.
    -   `methods`: Список HTTP-методов, которые поддерживает маршрут (например, `['GET', 'POST']`).
3.  **Настройка маршрутов backend API**:
    -   Создает экземпляр класса `Backend_Api`, передавая ему экземпляр Flask-приложения (`app`) и полную конфигурацию (`config`).
    -   Добавляет маршруты API, итерируясь по словарю `backend_api.routes` и используя метод `app.add_url_rule` для каждого маршрута.
    -   `route`: URL маршрута.
    -   `view_func`: Функция, которая будет обрабатывать запросы к этому маршруту.
    -   `methods`: Список HTTP-методов, которые поддерживает маршрут (например, `['GET', 'POST']`).
4.  **Запуск Flask-сервера**:
    -   Выводит сообщение в консоль, указывающее на каком порту запущен сервер.
    -   Запускает Flask-сервер с использованием параметров из `site_config`.
    -   Выводит сообщение в консоль после остановки сервера.

**Примеры**:

```python
# Пример запуска веб-приложения
# (Предполагается, что config.json настроен правильно и классы Website и Backend_Api определены)
# В данном случае функция __main__ вызывается автоматически при запуске скрипта