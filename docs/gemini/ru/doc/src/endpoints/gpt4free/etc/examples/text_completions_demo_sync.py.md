# Модуль для демонстрации синхронного текстового завершения с использованием g4f

## Обзор

Этот модуль демонстрирует, как использовать клиент `g4f` для выполнения синхронного запроса на завершение текста с использованием модели "gpt-4o".

## Подробней

Модуль создает экземпляр клиента `g4f.client.Client`, а затем использует его для отправки запроса на завершение чата к модели "gpt-4o". Запрос содержит системное сообщение, определяющее роль помощника, и пользовательское сообщение с вопросом. Ответ модели выводится на консоль.

## Функции

### `Client`

```python
from g4f.client import Client
```

**Описание**: Класс `Client` используется для взаимодействия с API g4f.

**Принцип работы**:
1. Создается экземпляр класса `Client`.
2. Используется метод `chat.completions.create` для отправки запроса на завершение чата.
3. Ответ модели выводится на консоль.

## Пример использования

```python
from g4f.client import Client

client = Client()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "how does a court case get to the Supreme Court?"}
    ],
)

print(response.choices[0].message.content)