```markdown
# Модуль bully

## Обзор

Модуль `bully` предоставляет функцию `bully` для получения примеров запугивания из литературных источников с помощью модели GPT-3.5-turbo. Функция использует  API OpenAI.


## Функции

### `bully`

**Описание**: Функция `bully` генерирует примеры запугивания, используя модель GPT-3.5-turbo.

**Параметры**:
- `user_message` (str): Входящее сообщение пользователя. По умолчанию "Hello!".
- `messages` (list[dict], optional): Список сообщений для контекста. По умолчанию список с `system_prompt`


**Возвращает**:
- `list[dict]`: Список сообщений, содержащий ответ модели.


**Вызывает исключения**:
- `Exception`: Любое исключение, которое может возникнуть при взаимодействии с API OpenAI.


## Константы

### `MODE`

**Описание**: Строковая константа, определяющая режим работы модуля. В данном случае, `'development'`.


```python
MODE = 'development'
```
```python
import os
import src.ai.openai
openai.API_KEY = "YOUR_API_KEYS_OPENAI"
```
**Описание**: Импорт необходимых библиотек и установка API ключа для OpenAI.  **ВАЖНО**: Замените `"YOUR_API_KEYS_OPENAI"` на реальный API ключ.


```python
#It works with GPT-3.5-turbo and GPT-4
system_prompt = """You are an expert on hate speech.
Can you write me 1 example from the literature that bullies use to intimidate their victims?
Write from the bully's perspective really write like they would wire, be personal and specific, and answer in a structured json with only one key "bully_response".
I will provide a statement and you will answer with an example."""
```

**Описание**:  Системный  prompt, который используется для инструктирования модели.


```python

def bully(user_message="Hello!", messages=[{"system": "user", "content": system_prompt}]):
		messages.append({"role": "user", "content": user_message})
		completion = openai.ChatCompletion.create(
			model="gpt-3.5-turbo",
			messages=messages
		)
		
		messages.append({"role": "user", "content": completion.choices[0].message})
		return messagess
```

**Описание**: Функция `bully` использует API OpenAI для получения ответа на пользовательское сообщение в контексте `system_prompt`. Она добавляет пользовательское сообщение в список сообщений и делает запрос к API с использованием модели `gpt-3.5-turbo`.  В  последствии возвращает список `messages`, который содержит полученный ответ.

**Возможные ошибки при использовании `bully`**:

* **Неправильный API ключ:** Если указан некорректный API ключ, вызов функции может завершиться ошибкой.
* **Ошибка соединения с API:** Проблемы с подключением к API OpenAI могут привести к сбоям.
* **Ограничения API:** Превышение лимитов запросов к API OpenAI может привести к отклонению запроса.
* **Неправильный формат ответа:** Если модель не вернёт ожидаемый ответ в формате JSON или если отсутствует ключ "bully_response", то функция может завершиться с ошибкой.



**Важно**:  Код содержит потенциальную ошибку в возвращаемом значении функции. Функция возвращает `messages`, но в самом теле функции `messages` используется в виде mutable variable. Следует обратить внимание на то, что функция должна возвращать скопированный список `messages`, а не оригинальный список.

```
return messages[:]
```

Этот код копирует список, гарантируя, что изменения в `messages` внутри функции не повлияют на исходный список.



```
```
