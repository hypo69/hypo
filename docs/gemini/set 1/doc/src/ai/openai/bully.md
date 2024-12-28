# Модуль bully

## Обзор

Модуль `bully` предоставляет функцию для взаимодействия с API OpenAI с целью получения примеров из литературы, иллюстрирующих методы запугивания.

## Функции

### `bully`

**Описание**: Функция `bully` взаимодействует с API OpenAI для получения примера запугивания из литературы.

**Параметры**:
- `user_message` (str): Входное сообщение пользователя. По умолчанию "Hello!".
- `messages` (list[dict], optional): Список сообщений для чат-бота. По умолчанию список с системным запросом.

**Возвращает**:
- `list[dict]`: Список сообщений, включая ответ чат-бота.

**Вызывает исключения**:
- `Exception`: Возникает при ошибках взаимодействия с API OpenAI.


## Постоянные переменные

### `MODE`

**Описание**: Переменная, хранящая режим работы (в данном случае `'dev'`).


```python

```


```python
import os
import src.ai.openai
openai.API_KEY = "YOUR_API_KEYS_OPENAI"


system_prompt = """You are an expert on hate speech.
Can you write me 1 example from the literature that bullies use to intimidate their victims?
Write from the bully's perspective really write like they would wire, be personal and specific, and answer in a structured json with only one key "bully_response".
I will provide a statement and you will answer with an example."""


def bully(user_message="Hello!", messages=[{"system": "user", "content": system_prompt}]):
    """
    Args:
        user_message (str): Входное сообщение пользователя. По умолчанию "Hello!".
        messages (list[dict], optional): Список сообщений для чат-бота. По умолчанию список с системным запросом.

    Returns:
        list[dict]: Список сообщений, включая ответ чат-бота.

    Raises:
        Exception: Возникает при ошибках взаимодействия с API OpenAI.
    """
    messages.append({"role": "user", "content": user_message})
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        messages.append({"role": "user", "content": completion.choices[0].message})
        return messages
    except Exception as ex:
        raise Exception(f"Ошибка при взаимодействии с API OpenAI: {ex}")
```