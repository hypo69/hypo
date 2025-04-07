# Документация для модуля xai (Клиент API xAI)

## Обзор

Данный модуль представляет собой Python-клиент для взаимодействия с API xAI. Он предоставляет инструменты для отправки запросов к API xAI, включая как обычные, так и потоковые запросы. Клиент упрощает процесс аутентификации и работы с API xAI.

## Подробнее

Этот клиент позволяет безопасно аутентифицировать запросы с использованием ключа API xAI, генерировать ответы от моделей xAI с использованием метода `chat_completion`, а также получать ответы в потоковом режиме с использованием метода `stream_chat_completion`.

## Установка

Для использования клиента необходимо установить Python и зависимости с помощью `pip`:

```bash
pip install requests
```

## Использование

### Инициализация

Инициализируйте класс `XAI` с вашим ключом API:

```python
from xai import XAI

api_key = "your_api_key_here"  # Замените на ваш реальный ключ API
xai = XAI(api_key)
```

### Завершение чата

Для генерации ответа от модели xAI используйте метод `chat_completion`:

```python
messages = [
    {
        "role": "system",
        "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
    },
    {
        "role": "user",
        "content": "What is the answer to life and universe?"
    }
]

completion_response = xai.chat_completion(messages)
print("Non-streaming response:", completion_response)
```

### Потоковая передача завершения чата

Для потоковой передачи ответов от модели xAI используйте метод `stream_chat_completion`:

```python
stream_response = xai.stream_chat_completion(messages)
print("Streaming response:")
for line in stream_response:
    if line.strip():
        print(json.loads(line))
```

## Пример

Полный пример использования клиента `XAI`:

```python
import json
from xai import XAI

api_key = "your_api_key_here"  # Замените на ваш реальный ключ API
xai = XAI(api_key)

messages = [
    {
        "role": "system",
        "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
    },
    {
        "role": "user",
        "content": "What is the answer to life and universe?"
    }
]

# Непотоковый запрос
completion_response = xai.chat_completion(messages)
print("Non-streaming response:", completion_response)

# Потоковый запрос
stream_response = xai.stream_chat_completion(messages)
print("Streaming response:")
for line in stream_response:
    if line.strip():
        print(json.loads(line))
```

## Вклад

Приветствуются любые вклады в проект. Вы можете отправлять pull request или открывать issue, если столкнулись с проблемами или у вас есть предложения по улучшению.

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](../../LICENSE).

## Благодарности

- Спасибо xAI за предоставление API, которое делает возможным работу этого клиента.
- Вдохновлен необходимостью простого и эффективного способа взаимодействия с мощными моделями xAI.

---

Для получения дополнительной информации, пожалуйста, обратитесь к [документации API xAI](https://api.x.ai/docs).