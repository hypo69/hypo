# Документация для модуля xAI API Client

## Обзор

Этот модуль предоставляет Python-клиент для взаимодействия с xAI API. Клиент упрощает процесс отправки запросов к xAI API, включая стандартные и потоковые запросы.

## Подробнее

Этот модуль предназначен для упрощения интеграции с API xAI. Он предоставляет удобные методы для аутентификации, создания запросов на завершение чата и получения потоковых ответов.

## Функциональность

- **Аутентификация**: Безопасная аутентификация запросов с использованием вашего ключа API xAI.
- **Завершение чата**: Генерация ответов от моделей xAI с помощью метода `chat_completion`.
- **Потоковые ответы**: Получение потоковых ответов от моделей xAI с помощью метода `stream_chat_completion`.

## Установка

Для использования этого клиента необходимо установить Python. Вы можете установить необходимые зависимости с помощью pip:

```bash
pip install requests
```

## Использование

### Инициализация

Сначала инициализируйте класс `XAI` своим ключом API:

```python
from xai import XAI

api_key = "your_api_key_here"  # Замените на свой фактический ключ API
xai = XAI(api_key)
```

### Завершение чата

Чтобы сгенерировать ответ от модели xAI, используйте метод `chat_completion`:

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

### Потоковое завершение чата

Чтобы получать потоковые ответы от модели xAI, используйте метод `stream_chat_completion`:

```python
stream_response = xai.stream_chat_completion(messages)
print("Streaming response:")
for line in stream_response:
    if line.strip():
        print(json.loads(line))
```

## Пример

Ниже приведен полный пример использования клиента `XAI`:

```python
import json
from xai import XAI

api_key = "your_api_key_here"  # Замените на свой фактический ключ API
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

Приветствуются вклады! Пожалуйста, не стесняйтесь отправлять pull request или открывать issue, если вы столкнетесь с какими-либо проблемами или у вас есть предложения по улучшению.

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

## Благодарности

- Спасибо xAI за предоставление API, который поддерживает этот клиент.
- Вдохновлен необходимостью простого и эффективного способа взаимодействия с мощными моделями xAI.

---

Для получения дополнительной информации, пожалуйста, обратитесь к [документации xAI API](https://api.x.ai/docs).

https://console.x.ai/team/4cd3d20f-f1d9-4389-9ffb-87c855e5ffac
https://docs.x.ai/docs