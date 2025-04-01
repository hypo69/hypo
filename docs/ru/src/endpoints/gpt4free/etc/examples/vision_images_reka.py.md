# Модуль для работы с изображениями через Reka

## Обзор

Модуль демонстрирует пример взаимодействия с моделью `reka-core` для анализа изображений. Он использует клиент `g4f.client.Client` для отправки запроса с изображением и получения ответа с описанием содержимого изображения.  В примере используется изображение `cat.jpeg`, расположенное в директории `docs/images`.

## Подробней

Этот код предназначен для демонстрации возможности анализа изображений с использованием модели `reka-core` через API `g4f`. Для работы кода требуется быть залогиненным в `chat.reka.ai` и иметь сохраненные cookie. Модуль отправляет изображение кота и запрашивает у модели описание того, что она видит на изображении. Результат выводится в консоль.

## Функции

### `create`

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

**Назначение**: Отправляет запрос на анализ изображения к модели `reka-core`.

**Параметры**:

-   `model` (str): Имя модели, используемой для анализа ("reka-core").
-   `messages` (list): Список сообщений, содержащих запрос пользователя. В данном случае, запрос "What can you see in the image ?".
-   `stream` (bool): Указывает, будет ли ответ возвращаться потоком. В данном случае `True`.
-   `image` (file object): Объект файла изображения, которое необходимо проанализировать. Открывается с помощью `open("docs/images/cat.jpeg", "rb")`. Важно передавать именно файловый объект, а не содержимое файла, прочитанное с помощью `.read()`.

**Возвращает**:

-   `completion` (Generator): Генератор, возвращающий части ответа от модели.

**Как работает функция**:

1.  Функция `create` из `client.chat.completions` вызывается с параметрами, необходимыми для анализа изображения.
2.  Указывается модель `reka-core`, которая специализируется на анализе изображений.
3.  Формируется сообщение с запросом "What can you see in the image ?".
4.  Указывается, что ответ должен быть возвращен потоком (`stream = True`).
5.  Передается файловый объект изображения `cat.jpeg`.

**Примеры**:

```python
from g4f.client import Client
from g4f.Provider import Reka

client = Client(
    provider = Reka # Optional if you set model name to reka-core
)

completion = client.chat.completions.create(
    model = "reka-core",
    messages = [
        {
            "role": "user",
            "content": "What can you see in the image ?"
        }
    ],
    stream = True,
    image = open("docs/images/cat.jpeg", "rb")
)
```

### Вывод результата анализа

```python
for message in completion:
    print(message.choices[0].delta.content or "")
```

**Назначение**: Выводит результат анализа изображения в консоль.

**Параметры**:

-   `message` (object): Объект, возвращаемый генератором `completion`.

**Как работает функция**:

1.  Цикл `for` перебирает сообщения, возвращаемые генератором `completion`.
2.  Для каждого сообщения извлекается содержимое (`message.choices[0].delta.content`).
3.  Содержимое выводится в консоль.

**Примеры**:

```python
for message in completion:
    print(message.choices[0].delta.content or "")