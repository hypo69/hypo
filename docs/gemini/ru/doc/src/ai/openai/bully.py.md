# Модуль `src.ai.openai.bully`

## Обзор

Этот модуль предоставляет функциональность для генерации примеров грубостей и запугиваний с использованием модели OpenAI. Он предназначен для демонстрации того, как можно использовать модель для создания таких текстов с точки зрения обидчика.

## Содержание

1. [Функции](#Функции)
    - [`bully`](#bully)

## Функции

### `bully`

**Описание**: 
Генерирует пример грубости и запугивания на основе запроса пользователя, используя модель OpenAI.

**Параметры**:
- `user_message` (str, optional): Сообщение пользователя, которое будет использоваться для генерации примера. По умолчанию `"Hello!"`.
- `messages` (list, optional): Список сообщений для диалога с моделью, включая системное сообщение. По умолчанию `[{"system": "user", "content": system_prompt}]`.

**Возвращает**:
- `list`: Обновленный список сообщений с ответом модели.

**Пример использования:**
```python
messages = [{"system": "user", "content": system_prompt}]
result = bully(user_message="You are stupid!", messages=messages)
print(result)
```

**Код:**
```python
def bully(user_message="Hello!", messages=[{"system": "user", "content": system_prompt}]):
		messages.append({"role": "user", "content": user_message})
		completion = openai.ChatCompletion.create(
			model="gpt-3.5-turbo",
			messages=messages
		)
		
		messages.append({"role": "user", "content": completion.choices[0].message})
		return messages
```