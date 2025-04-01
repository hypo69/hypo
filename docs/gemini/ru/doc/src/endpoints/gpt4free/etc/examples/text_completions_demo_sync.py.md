# Документация для `text_completions_demo_sync.py`

## Обзор

Этот скрипт демонстрирует, как использовать клиент `g4f.client.Client` для взаимодействия с моделью `gpt-4o` и получения текстовых ответов. В примере отправляется запрос к модели с вопросом о том, как судебное дело попадает в Верховный суд, и выводится полученный ответ.

## Подробней

Скрипт предназначен для демонстрации простого способа использования библиотеки `g4f` для выполнения текстовых завершений. Он показывает, как создать клиент, отправить запрос к модели и получить ответ. Этот код может быть полезен для тестирования и понимания работы библиотеки `g4f` перед использованием в более сложных сценариях.

## Функции

### `Client`

```python
from g4f.client import Client
```

Класс для взаимодействия с API g4f. В данном скрипте используется для создания клиента, через который отправляется запрос к модели `gpt-4o`.

**Методы**:

- `chat.completions.create()`: Отправляет запрос на создание текстового завершения.

**Примеры**:

```python
from g4f.client import Client

client = Client()
```

### `response.choices[0].message.content`

Получение контента ответа.
```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "how does a court case get to the Supreme Court?"}
    ],
)

print(response.choices[0].message.content)
```

**Параметры**:

- `model` (str): Указывает используемую модель, в данном случае "gpt-4o".
- `messages` (list): Список сообщений, формирующих контекст запроса.

**Как работает функция**:

1. **Создание клиента**: Инициализируется клиент `Client` для взаимодействия с API.
2. **Формирование запроса**: Создается запрос к модели `gpt-4o` с указанием роли "system" и "user".
3. **Отправка запроса**: Запрос отправляется с помощью метода `client.chat.completions.create()`.
4. **Получение ответа**: Полученный ответ извлекается из объекта `response` и выводится на экран.

**ASCII flowchart**:

```
A: Создание клиента
|
B: Формирование запроса с ролями "system" и "user"
|
C: Отправка запроса к gpt-4o
|
D: Получение ответа
|
E: Вывод контента ответа
```

**Примеры**:

```python
from g4f.client import Client

client = Client()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "how does a court case get to the Supreme Court?"}
    ],
)

print(response.choices[0].message.content)
```

```python
from g4f.client import Client

client = Client()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Как создать веб-приложение на Python?"}
    ],
)

print(response.choices[0].message.content)