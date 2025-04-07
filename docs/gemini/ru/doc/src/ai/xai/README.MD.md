# Документация для модуля xAI API Client

## Обзор

Этот репозиторий содержит Python-клиент для взаимодействия с xAI API. Клиент разработан для упрощения процесса отправки запросов к xAI API, включая как стандартные, так и потоковые запросы.

## Подробнее

Этот модуль предоставляет интерфейс для взаимодействия с API xAI, позволяя генерировать ответы от моделей xAI и обрабатывать потоковые ответы. Он включает в себя функции аутентификации и упрощает процесс выполнения запросов к API.

## Функции

- **Аутентификация**: Безопасная аутентификация запросов с использованием ключа API xAI.
- **Chat Completion**: Генерация ответов от моделей xAI с использованием метода `chat_completion`.
- **Streaming Responses**: Потоковая передача ответов от моделей xAI с использованием метода `stream_chat_completion`.

## Установка

Чтобы использовать этот клиент, на вашей системе должен быть установлен Python. Вы можете установить необходимые зависимости с помощью pip:

```bash
pip install requests
```

## Использование

### Инициализация

Сначала инициализируйте класс `XAI` своим ключом API:

```python
from xai import XAI

api_key = "your_api_key_here"  # Замените своим фактическим ключом API
xai = XAI(api_key)
```

### Chat Completion

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

Ниже приведен полный пример использования клиента `XAI`:

```python
import json
from xai import XAI

api_key = "your_api_key_here"  # Замените своим фактическим ключом API
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

## Вклад

Вклад приветствуется! Пожалуйста, не стесняйтесь отправлять pull request или открывать issue, если вы столкнетесь с какими-либо проблемами или у вас есть предложения по улучшению.

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

## Благодарности

- Спасибо xAI за предоставление API, на котором работает этот клиент.
- Вдохновлен потребностью в простом и эффективном способе взаимодействия с мощными моделями xAI.

---

Для получения дополнительной информации обратитесь к [документации xAI API](https://api.x.ai/docs).

https://console.x.ai/team/4cd3d20f-f1d9-4389-9ffb-87c855e5ffac
https://docs.x.ai/docs