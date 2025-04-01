# Модуль для синхронной демонстрации text completions с использованием g4f

## Обзор

Этот модуль демонстрирует, как использовать библиотеку `g4f` для выполнения синхронных text completions с помощью модели `gpt-4o`. Он создает клиент, отправляет запрос с системным и пользовательским сообщением и печатает результат.

## Подробнее

Этот код является примером использования библиотеки `g4f` для получения текстовых завершений от модели `gpt-4o`. Он показывает, как создать клиент, определить сообщения для модели и распечатать полученный ответ.

## Функции

### `client.chat.completions.create`

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "how does a court case get to the Supreme Court?"}
    ],
)
```

**Назначение**: Отправляет запрос на создание text completion к модели `gpt-4o`.

**Параметры**:
- `model` (str): Идентификатор модели, используемой для завершения текста. В данном случае, `"gpt-4o"`.
- `messages` (list): Список сообщений, определяющих контекст и запрос. Каждый элемент списка представляет собой словарь с ключами `"role"` и `"content"`.
    - `"role"` (str): Роль сообщения (например, `"system"` или `"user"`).
    - `"content"` (str): Текст сообщения.

**Возвращает**:
- `response`: Объект ответа, содержащий сгенерированный текст.

**Как работает функция**:

1.  Функция `client.chat.completions.create` принимает в качестве аргументов модель и список сообщений.
2.  Внутри функции происходит отправка запроса к API g4f с указанными параметрами.
3.  API g4f обрабатывает запрос и возвращает ответ с сгенерированным текстом.

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