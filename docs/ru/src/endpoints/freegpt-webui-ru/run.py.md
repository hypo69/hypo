# Модуль запуска веб-приложения

## Обзор

Данный модуль является точкой входа для запуска веб-приложения, основанного на Flask. Он загружает конфигурацию из файла `config.json`, настраивает маршруты для веб-сайта и бэкенд API, а затем запускает Flask-сервер.

## Подробней

Этот модуль выполняет следующие задачи:

1.  Загружает конфигурацию из `config.json`, которая содержит настройки для веб-сайта и бэкенд API.
2.  Инициализирует и настраивает маршруты для веб-сайта, используя класс `Website`.
3.  Инициализирует и настраивает маршруты для бэкенд API, используя класс `Backend_Api`.
4.  Запускает Flask-сервер с использованием конфигурации, загруженной из `config.json`.

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

**Назначение**: Главная функция, выполняющая запуск веб-приложения.

**Параметры**:
*   Нет параметров.

**Возвращает**:
*   Нет возвращаемого значения.

**Вызывает исключения**:
*   `FileNotFoundError`: Если файл `config.json` не найден.
*   `KeyError`: Если в файле `config.json` отсутствуют необходимые ключи.

**Как работает функция**:

1.  Загружает конфигурацию из файла `config.json` используя стандартную библиотеку `json.load`.
2.  Извлекает конфигурацию сайта из загруженной конфигурации.
3.  Создает экземпляр класса `Website`, передавая ему объект приложения Flask.
4.  Добавляет маршруты веб-сайта в приложение Flask, используя метод `add_url_rule`.
5.  Создает экземпляр класса `Backend_Api`, передавая ему объект приложения Flask и конфигурацию.
6.  Добавляет маршруты бэкенд API в приложение Flask, используя метод `add_url_rule`.
7.  Запускает Flask-сервер, используя конфигурацию сайта.
8.  После завершения работы сервера выводит сообщение о закрытии порта.

**Примеры**:

```python
# Запуск веб-приложения
# (Предполагается, что config.json существует и содержит корректные настройки)
python run.py
```

ASCII схема работы функции:

```
A: Загрузка конфигурации из config.json
|
B: Создание экземпляра Website и добавление маршрутов
|
C: Создание экземпляра Backend_Api и добавление маршрутов
|
D: Запуск Flask-сервера
|
E: Закрытие порта
```

### Пример содержимого `config.json`:

```json
{
  "site_config": {
    "host": "0.0.0.0",
    "port": 5000,
    "debug": true
  }
}