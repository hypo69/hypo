# Модуль для обработки изображений с использованием GPT4Free Vision
=================================================================

Модуль демонстрирует использование GPT4Free для анализа изображений, как локальных, так и удаленных. 
Он использует `g4f.client.Client` для взаимодействия с API и выполняет запросы на анализ содержимого изображений.

## Обзор

Этот модуль предоставляет примеры кода для отправки изображений в модель GPT4Free Vision и получения ответов о том, что изображено на этих изображениях. 
Он показывает, как работать с удаленными изображениями, получаемыми через HTTP-запросы, и с локальными изображениями, загружаемыми из файлов.

## Подробнее

Модуль демонстрирует, как отправлять запросы к API GPT4Free Vision с использованием библиотеки `g4f`. Он использует клиент `g4f.client.Client` для создания и отправки запросов на анализ изображений. Модуль показывает, как обрабатывать как удаленные изображения, полученные с использованием библиотеки `requests`, так и локальные изображения, открытые из файлов. Основная цель модуля - продемонстрировать, как использовать GPT4Free для анализа содержимого изображений.

## Функции

### `Client`

```python
client = Client()
```

**Назначение**: Создание экземпляра класса `Client` из библиотеки `g4f.client`.

**Как работает функция**:
1. Создается экземпляр класса `Client`.
2. Этот экземпляр используется для дальнейшего взаимодействия с API `g4f`.

**Примеры**:

```python
from g4f.client import Client
client = Client()
```

### Обработка удаленного изображения

```python
remote_image = requests.get("https://raw.githubusercontent.com/xtekky/gpt4free/refs/heads/main/docs/images/cat.jpeg", stream=True).content
response_remote = client.chat.completions.create(
    model=g4f.models.default_vision,
    messages=[
        {"role": "user", "content": "What are on this image?"}
    ],
    image=remote_image
)
print("Response for remote image:")
print(response_remote.choices[0].message.content)
```

**Назначение**: Получение удаленного изображения, отправка его в модель GPT4Free Vision и вывод ответа.

**Как работает функция**:

1.  **Получение изображения**: Функция `requests.get` используется для отправки HTTP-запроса к URL-адресу удаленного изображения. Параметр `stream=True` указывает, что содержимое должно быть получено в потоковом режиме. Атрибут `.content` используется для получения содержимого изображения в виде байтов.

2.  **Отправка запроса в GPT4Free**:
    *   Метод `client.chat.completions.create` используется для отправки запроса в модель GPT4Free Vision.
    *   Параметр `model` указывает используемую модель, в данном случае `g4f.models.default_vision`.
    *   Параметр `messages` содержит список сообщений. В данном случае список содержит одно сообщение с ролью "user" и содержанием "What are on this image?".
    *   Параметр `image` содержит содержимое удаленного изображения, полученное ранее.

3.  **Вывод ответа**:
    *   Извлекается содержимое первого сообщения из ответа, полученного от GPT4Free.
    *   Выводится в консоль.

**Примеры**:

```python
import requests
import g4f

from g4f.client import Client

client = Client()

remote_image = requests.get("https://raw.githubusercontent.com/xtekky/gpt4free/refs/heads/main/docs/images/cat.jpeg", stream=True).content
response_remote = client.chat.completions.create(
    model=g4f.models.default_vision,
    messages=[
        {"role": "user", "content": "What are on this image?"}
    ],
    image=remote_image
)
print("Response for remote image:")
print(response_remote.choices[0].message.content)
```

### Обработка локального изображения

```python
local_image = open("docs/images/cat.jpeg", "rb")
response_local = client.chat.completions.create(
    model=g4f.models.default_vision,
    messages=[
        {"role": "user", "content": "What are on this image?"}
    ],
    image=local_image
)
print("Response for local image:")
print(response_local.choices[0].message.content)
local_image.close()  # Close file after use
```

**Назначение**: Открытие локального изображения, отправка его в модель GPT4Free Vision и вывод ответа.

**Как работает функция**:

1.  **Открытие изображения**: Функция `open` используется для открытия локального изображения в двоичном режиме чтения (`"rb"`).
2.  **Отправка запроса в GPT4Free**:
    *   Метод `client.chat.completions.create` используется для отправки запроса в модель GPT4Free Vision.
    *   Параметр `model` указывает используемую модель, в данном случае `g4f.models.default_vision`.
    *   Параметр `messages` содержит список сообщений. В данном случае список содержит одно сообщение с ролью `"user"` и содержанием `"What are on this image?"`.
    *   Параметр `image` содержит открытый файл локального изображения.
3.  **Вывод ответа**:
    *   Извлекается содержимое первого сообщения из ответа, полученного от GPT4Free.
    *   Выводится в консоль.
4.  **Закрытие файла**:
    *   Метод `local_image.close()` используется для закрытия файла изображения после использования, чтобы освободить ресурсы.

**Примеры**:

```python
import g4f

from g4f.client import Client

client = Client()
local_image = open("docs/images/cat.jpeg", "rb")
response_local = client.chat.completions.create(
    model=g4f.models.default_vision,
    messages=[
        {"role": "user", "content": "What are on this image?"}
    ],
    image=local_image
)
print("Response for local image:")
print(response_local.choices[0].message.content)
local_image.close()