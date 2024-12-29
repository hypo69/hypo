# xAI API Client

## Оглавление
1. [Обзор](#Обзор)
2. [Возможности](#Возможности)
3. [Установка](#Установка)
4. [Использование](#Использование)
    - [Инициализация](#Инициализация)
    - [Завершение чата](#Завершение-чата)
    - [Потоковое завершение чата](#Потоковое-завершение-чата)
5. [Пример](#Пример)
6. [Вклад](#Вклад)
7. [Лицензия](#Лицензия)
8. [Благодарности](#Благодарности)

## Обзор

Этот репозиторий содержит Python-клиент для взаимодействия с xAI API. Клиент разработан для упрощения процесса отправки запросов к xAI API, включая как стандартные, так и потоковые запросы.

## Возможности

-   **Аутентификация**: Безопасная аутентификация ваших запросов с использованием вашего ключа API xAI.
-   **Завершение чата**: Генерация ответов от моделей xAI с использованием метода `chat_completion`.
-   **Потоковые ответы**: Потоковая передача ответов от моделей xAI с использованием метода `stream_chat_completion`.

## Установка

Для использования этого клиента на вашем компьютере должен быть установлен Python. Вы можете установить необходимые зависимости с помощью pip:

```bash
pip install requests
```

## Использование

### Инициализация

Сначала инициализируйте класс `XAI` вашим ключом API:

```python
from xai import XAI

api_key = "your_api_key_here"  # Замените на ваш фактический ключ API
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

### Потоковое завершение чата

Для получения потоковых ответов от модели xAI используйте метод `stream_chat_completion`:

```python
stream_response = xai.stream_chat_completion(messages)
print("Streaming response:")
for line in stream_response:
    if line.strip():
        print(json.loads(line))
```

## Пример

Вот полный пример использования клиента `XAI`:

```python
import json
from xai import XAI

api_key = "your_api_key_here"  # Замените на ваш фактический ключ API
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

Вклады приветствуются! Пожалуйста, не стесняйтесь отправлять pull request или открывать issue, если вы столкнулись с какими-либо проблемами или у вас есть предложения по улучшению.

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. См. файл [LICENSE](LICENSE) для получения более подробной информации.

## Благодарности

-   Спасибо xAI за предоставление API, на котором работает этот клиент.
-   Вдохновлено необходимостью простого и эффективного способа взаимодействия с мощными моделями xAI.

---

Для получения дополнительной информации, пожалуйста, обратитесь к [документации xAI API](https://api.x.ai/docs).

https://console.x.ai/team/4cd3d20f-f1d9-4389-9ffb-87c855e5ffac
https://docs.x.ai/docs