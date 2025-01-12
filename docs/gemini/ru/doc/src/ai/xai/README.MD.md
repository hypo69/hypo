# xAI API Client

## Оглавление
1. [Обзор](#обзор)
2. [Возможности](#возможности)
3. [Установка](#установка)
4. [Использование](#использование)
    - [Инициализация](#инициализация)
    - [Chat Completion](#chat-completion)
    - [Streaming Chat Completion](#streaming-chat-completion)
5. [Пример](#пример)
6. [Участие](#участие)
7. [Лицензия](#лицензия)
8. [Благодарности](#благодарности)
    
## Обзор

Этот репозиторий содержит Python-клиент для взаимодействия с xAI API. Клиент предназначен для упрощения процесса отправки запросов к xAI API, включая как стандартные, так и потоковые запросы.

## Возможности

- **Аутентификация**: Безопасная аутентификация ваших запросов с использованием вашего API-ключа xAI.
- **Chat Completion**: Генерация ответов от моделей xAI с использованием метода `chat_completion`.
- **Streaming Responses**: Потоковая передача ответов от моделей xAI с использованием метода `stream_chat_completion`.

## Установка

Для использования этого клиента необходимо установить Python на вашей системе. Вы можете установить необходимые зависимости, используя pip:

```bash
pip install requests
```

## Использование

### Инициализация

Сначала инициализируйте класс `XAI` вашим API-ключом:

```python
from xai import XAI

api_key = "your_api_key_here"  # Замените на ваш фактический API-ключ
xai = XAI(api_key)
```

### Chat Completion

Чтобы сгенерировать ответ от модели xAI, используйте метод `chat_completion`:

```python
messages = [
    {
        "role": "system",
        "content": "Вы Грок, чат-бот, вдохновленный Путеводителем по Галактике."
    },
    {
        "role": "user",
        "content": "Какой ответ на жизнь и вселенную?"
    }
]

completion_response = xai.chat_completion(messages)
print("Non-streaming response:", completion_response)
```

### Streaming Chat Completion

Чтобы получать потоковые ответы от модели xAI, используйте метод `stream_chat_completion`:

```python
stream_response = xai.stream_chat_completion(messages)
print("Streaming response:")
for line in stream_response:
    if line.strip():
        print(json.loads(line))
```

## Пример

Вот полный пример того, как использовать клиент `XAI`:

```python
import json
from xai import XAI

api_key = "your_api_key_here"  # Замените на ваш фактический API-ключ
xai = XAI(api_key)

messages = [
    {
        "role": "system",
        "content": "Вы Грок, чат-бот, вдохновленный Путеводителем по Галактике."
    },
    {
        "role": "user",
        "content": "Какой ответ на жизнь и вселенную?"
    }
]

# Non-streaming request
completion_response = xai.chat_completion(messages)
print("Non-streaming response:", completion_response)

# Streaming request
stream_response = xai.stream_chat_completion(messages)
print("Streaming response:")
for line in stream_response:
    if line.strip():
        print(json.loads(line))
```

## Участие

Вклад приветствуется! Пожалуйста, не стесняйтесь отправлять pull request или открывать issue, если у вас возникнут какие-либо проблемы или есть предложения по улучшению.

## Лицензия

Этот проект лицензирован по MIT License. Подробности смотрите в файле [LICENSE](LICENSE).

## Благодарности

- Спасибо xAI за предоставление API, который поддерживает этот клиент.
- Вдохновлено необходимостью простого и эффективного способа взаимодействия с мощными моделями xAI.

---

Для получения дополнительной информации, пожалуйста, обратитесь к [документации xAI API](https://api.x.ai/docs).

https://console.x.ai/team/4cd3d20f-f1d9-4389-9ffb-87c855e5ffac
https://docs.x.ai/docs