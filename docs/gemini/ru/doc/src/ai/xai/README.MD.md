# xAI API Client

## Оглавление
1. [Обзор](#Обзор)
2. [Возможности](#Возможности)
3. [Установка](#Установка)
4. [Использование](#Использование)
   - [Инициализация](#Инициализация)
   - [Chat Completion](#Chat-Completion)
   - [Streaming Chat Completion](#Streaming-Chat-Completion)
5. [Пример](#Пример)
6. [Вклад](#Вклад)
7. [Лицензия](#Лицензия)
8. [Благодарности](#Благодарности)

## Обзор

Этот репозиторий содержит Python-клиент для взаимодействия с xAI API. Клиент разработан для упрощения процесса отправки запросов к xAI API, включая как стандартные, так и потоковые запросы.

## Возможности

-   **Аутентификация**: Безопасная аутентификация ваших запросов с использованием вашего API-ключа xAI.
-   **Chat Completion**: Генерация ответов от моделей xAI с использованием метода `chat_completion`.
-   **Streaming Responses**: Потоковая передача ответов от моделей xAI с использованием метода `stream_chat_completion`.

## Установка

Для использования этого клиента на вашей системе должен быть установлен Python. Вы можете установить необходимые зависимости с помощью pip:

```bash
pip install requests
```

## Использование

### Инициализация

Сначала инициализируйте класс `XAI` с вашим API-ключом:

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
        "content": "Вы Grok, чат-бот, вдохновленный «Путеводителем по галактике»."
    },
    {
        "role": "user",
        "content": "Какой ответ на жизнь, вселенную и все остальное?"
    }
]

completion_response = xai.chat_completion(messages)
print("Непотоковый ответ:", completion_response)
```

### Streaming Chat Completion

Чтобы получить потоковые ответы от модели xAI, используйте метод `stream_chat_completion`:

```python
stream_response = xai.stream_chat_completion(messages)
print("Потоковый ответ:")
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
        "content": "Вы Grok, чат-бот, вдохновленный «Путеводителем по галактике»."
    },
    {
        "role": "user",
        "content": "Какой ответ на жизнь, вселенную и все остальное?"
    }
]

# Непотоковый запрос
completion_response = xai.chat_completion(messages)
print("Непотоковый ответ:", completion_response)

# Потоковый запрос
stream_response = xai.stream_chat_completion(messages)
print("Потоковый ответ:")
for line in stream_response:
    if line.strip():
        print(json.loads(line))
```

## Вклад

Вклад приветствуется! Пожалуйста, не стесняйтесь отправлять pull request или открывать issue, если вы столкнетесь с какими-либо проблемами или у вас есть предложения по улучшению.

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

## Благодарности

-   Спасибо xAI за предоставление API, которое поддерживает этот клиент.
-   Вдохновлено необходимостью простого и эффективного способа взаимодействия с мощными моделями xAI.

---

Для получения дополнительной информации, пожалуйста, обратитесь к [документации xAI API](https://api.x.ai/docs).

https://console.x.ai/team/4cd3d20f-f1d9-4389-9ffb-87c855e5ffac
https://docs.x.ai/docs