# Клиент API xAI

## Обзор

Этот репозиторий содержит Python-клиент для взаимодействия с API xAI. Клиент разработан для упрощения процесса отправки запросов к API xAI, включая как стандартные, так и потоковые запросы.

## Оглавление

- [Обзор](#обзор)
- [Возможности](#возможности)
- [Установка](#установка)
- [Использование](#использование)
    - [Инициализация](#инициализация)
    - [Завершение чата](#завершение-чата)
    - [Потоковая передача ответов](#потоковая-передача-ответов)
- [Пример](#пример)
- [Вклад](#вклад)
- [Лицензия](#лицензия)
- [Благодарности](#благодарности)


## Возможности

- **Аутентификация**: Безопасная аутентификация ваших запросов с использованием ключа API xAI.
- **Завершение чата**: Генерация ответов от моделей xAI с использованием метода `chat_completion`.
- **Потоковая передача ответов**: Потоковая передача ответов от моделей xAI с использованием метода `stream_chat_completion`.


## Установка

Для использования этого клиента вам необходимо установить Python на вашей системе. Вы можете установить необходимые зависимости с помощью pip:

```bash
pip install requests
```


## Использование

### Инициализация

Сначала инициализируйте класс `XAI` с вашим ключом API:

```python
from xai import XAI

api_key = "your_api_key_here"  # Замените на ваш реальный ключ API
xai = XAI(api_key)
```

### Завершение чата

Для генерации ответа от модели xAI используйте метод `chat_completion`:

```python
from typing import List, Dict, Optional
import json

def chat_completion(messages: List[Dict[str, str]]) -> Dict[str, str] | None:
    """
    Args:
        messages (List[Dict[str, str]]): Список сообщений для чата в формате [{'role': str, 'content': str}].

    Returns:
        Dict[str, str] | None: Ответ от модели xAI в формате JSON или None, если произошла ошибка.

    Raises:
        requests.exceptions.RequestException: Возникает при проблемах с запросом к API.
    """
    # ... (Реализация метода chat_completion)
    pass
```

### Потоковая передача ответов

Для потоковой передачи ответов от модели xAI используйте метод `stream_chat_completion`:

```python
from typing import Generator, List, Dict, Optional
import json


def stream_chat_completion(messages: List[Dict[str, str]]) -> Generator[str, None, None]:
    """
    Args:
        messages (List[Dict[str, str]]): Список сообщений для чата в формате [{'role': str, 'content': str}].

    Returns:
        Generator[str, None, None]: Потоковая генерация ответов от модели xAI в формате JSON.

    Raises:
        requests.exceptions.RequestException: Возникает при проблемах с запросом к API.
    """
    # ... (Реализация метода stream_chat_completion)
    pass
```



## Пример

Вот полный пример использования клиента `XAI`:

```python
import json
from xai import XAI

api_key = "your_api_key_here"  # Замените на ваш реальный ключ API
xai = XAI(api_key)

messages = [
    {"role": "system", "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."},
    {"role": "user", "content": "What is the answer to life and universe?"}
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

Вклад приветствуется! Не стесняйтесь отправлять pull request или открывать issue, если вы столкнулись с какими-либо проблемами или имеете предложения по улучшению.


## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](../../LICENSE).


## Благодарности

- Спасибо xAI за предоставление API, которое делает возможным работу этого клиента.
- Вдохновлен необходимостью простого и эффективного способа взаимодействия с мощными моделями xAI.