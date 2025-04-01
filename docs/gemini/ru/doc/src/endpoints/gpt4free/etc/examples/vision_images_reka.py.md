# Модуль для работы с Image Chat Reka

## Обзор

Модуль демонстрирует пример использования библиотеки `g4f` для взаимодействия с моделью Reka с целью анализа изображений. Он показывает, как загрузить изображение и отправить запрос к модели для получения описания содержимого изображения.

## Подробней

Этот код предназначен для демонстрации работы с моделью Reka через библиотеку `g4f`.  Для успешной работы требуется наличие cookies и авторизация на chat.reka.ai.  Код загружает изображение (в данном случае, "docs/images/cat.jpeg") и отправляет его вместе с текстовым запросом к модели Reka, чтобы получить описание содержимого изображения.  Результат выводится в консоль.

## Функции

### `chat.completions.create`

```python
completion = client.chat.completions.create(
    model = "reka-core",
    messages = [
        {
            "role": "user",
            "content": "What can you see in the image ?"
        }
    ],
    stream = True,
    image = open("docs/images/cat.jpeg", "rb") # open("path", "rb"), do not use .read(), etc. it must be a file object
)
```

**Назначение**: Отправляет запрос к модели Reka для анализа изображения и получения текстового ответа.

**Параметры**:

- `model` (str): Имя используемой модели ("reka-core").
- `messages` (list): Список сообщений, содержащих запрос пользователя. В данном случае, содержит один элемент - запрос "What can you see in the image ?".
- `stream` (bool): Указывает, что ответ должен быть получен в режиме потока (stream).
- `image` (file object): Файловый объект изображения, которое необходимо проанализировать. Важно передавать именно файловый объект, а не содержимое файла, считанное в строку или байты.

**Возвращает**:

- `completion`: Объект, содержащий ответ модели.

**Как работает функция**:

1.  Функция `chat.completions.create` отправляет запрос к модели `reka-core` для анализа изображения.
2.  Внутри функции происходят следующие действия и преобразования:
    A. Формируется запрос к API Reka, включающий модель, текстовый запрос и изображение.
    |
    -- B. Запрос отправляется на сервер Reka.
    |
    C. Полученный ответ от сервера Reka передается в режиме потока (stream).
    |
    D. Ответ обрабатывается для извлечения содержимого.

**Примеры**:

```python
from g4f.client import Client
from g4f.Provider import Reka

client = Client(provider=Reka)

completion = client.chat.completions.create(
    model="reka-core",
    messages=[{"role": "user", "content": "What can you see in the image ?"}],
    stream=True,
    image=open("docs/images/cat.jpeg", "rb")
)

for message in completion:
    print(message.choices[0].delta.content or "")
```

### Вывод содержимого сообщений

```python
for message in completion:
    print(message.choices[0].delta.content or "")
```

**Назначение**: Выводит полученные от модели сообщения в консоль.

**Параметры**:

- `message` (object): Объект сообщения, полученный от модели.

**Как работает функция**:

1.  Цикл перебирает сообщения, полученные от модели.
2.  Внутри цикла происходят следующие действия и преобразования:
    A. Извлекается содержимое сообщения из объекта `message.choices[0].delta.content`.
    |
    -- B. Если содержимое отсутствует, используется пустая строка.
    |
    C. Содержимое сообщения выводится в консоль.

**Примеры**:

```python
for message in completion:
    print(message.choices[0].delta.content or "")