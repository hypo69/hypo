# `api_generations_image.py`

## Обзор

Данный код представляет собой пример запроса к API для генерации изображений. Он отправляет POST-запрос на указанный URL (`http://localhost:1337/v1/images/generations`) с параметрами модели, запроса и формата ответа, после чего выводит полученные данные в формате JSON.

## Подробней

Этот фрагмент кода демонстрирует, как взаимодействовать с локальным сервером, который предоставляет API для генерации изображений. Он использует библиотеку `requests` для отправки HTTP-запроса и обрабатывает ответ в формате JSON. Этот код может быть частью системы, которая позволяет пользователям создавать изображения на основе текстовых запросов.

## Функции

### Отправка запроса на генерацию изображения

```python
import requests
url = "http://localhost:1337/v1/images/generations"
body = {
    "model": "flux",
    "prompt": "hello world user",
    "response_format": None,
    #"response_format": "url",
    #"response_format": "b64_json",
}
data = requests.post(url, json=body, stream=True).json()
print(data)
```

**Назначение**: Отправка POST-запроса к API для генерации изображения и вывод результата.

**Параметры**:
- `url` (str): URL-адрес API для генерации изображений.
- `body` (dict): Тело запроса в формате JSON, содержащее параметры генерации изображения, такие как модель, запрос и формат ответа.

**Возвращает**:
- `data` (dict): JSON-ответ от API.

**Как работает функция**:

1. **Определение URL**: Задание URL-адреса API для генерации изображений.
2. **Формирование тела запроса**: Создание словаря `body` с параметрами запроса, включая модель, текстовый запрос (`prompt`) и формат ответа.
3. **Отправка POST-запроса**: Отправка POST-запроса на указанный URL с телом запроса в формате JSON. Используется `stream=True` для потоковой передачи данных.
4. **Обработка ответа**: Получение JSON-ответа от API и вывод его на экран.

```
Начало
↓
Определение URL для API генерации изображений
↓
Формирование тела запроса с параметрами: модель, запрос, формат ответа
↓
Отправка POST-запроса на URL с телом запроса в формате JSON (stream=True)
↓
Получение JSON-ответа от API
↓
Вывод JSON-ответа на экран
Конец
```

**Примеры**:

Пример 1: Базовый запрос с моделью "flux" и запросом "hello world user".

```python
import requests
url = "http://localhost:1337/v1/images/generations"
body = {
    "model": "flux",
    "prompt": "hello world user",
    "response_format": None,
}
data = requests.post(url, json=body, stream=True).json()
print(data)
```

Пример 2: Запрос с указанием формата ответа в виде URL.

```python
import requests
url = "http://localhost:1337/v1/images/generations"
body = {
    "model": "flux",
    "prompt": "hello world user",
    "response_format": "url",
}
data = requests.post(url, json=body, stream=True).json()
print(data)
```

Пример 3: Запрос с указанием формата ответа в виде base64 JSON.

```python
import requests
url = "http://localhost:1337/v1/images/generations"
body = {
    "model": "flux",
    "prompt": "hello world user",
    "response_format": "b64_json",
}
data = requests.post(url, json=body, stream=True).json()
print(data)