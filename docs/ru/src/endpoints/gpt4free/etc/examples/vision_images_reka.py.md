# Модуль для работы с Image Chat Reka

## Обзор

Этот модуль демонстрирует, как использовать библиотеку `g4f` для взаимодействия с моделью `reka-core` для анализа изображений. Он включает в себя пример отправки изображения коту и запроса на описание того, что видно на изображении.

## Подробнее

Модуль предназначен для демонстрации базового функционала отправки изображений и получения текстового ответа от модели Reka. Для работы модуля требуется наличие файла изображения `cat.jpeg` в директории `docs/images/` проекта, а также активная сессия пользователя (наличие cookies) для `chat.reka.ai`.

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

**Назначение**: Отправляет запрос на анализ изображения модели `reka-core` и возвращает ответ в режиме стриминга.

**Параметры**:
- `model` (str): Имя модели для использования, в данном случае `reka-core`.
- `messages` (list): Список сообщений, содержащих запрос пользователя.
- `stream` (bool): Флаг, указывающий на необходимость стриминга ответа.
- `image` (file object): Объект файла изображения для анализа.

**Возвращает**:
- `Generator[str, None, None]`: Генератор, выдающий части ответа модели.

**Вызывает исключения**:
- `Exception`: В случае ошибки при отправке запроса или получении ответа от модели.

**Как работает функция**:

1.  **Инициализация запроса**: Создается запрос к модели `reka-core` через метод `client.chat.completions.create`.
2.  **Формирование сообщения**: Формируется сообщение с ролью `user`, содержащее текстовый запрос "What can you see in the image ?".
3.  **Открытие изображения**: Открывается файл изображения `cat.jpeg` в бинарном режиме чтения (`"rb"`). Важно отметить, что передается именно объект файла, а не его содержимое.
4.  **Отправка запроса**: Запрос отправляется с указанием модели, сообщения, флага стриминга и объекта изображения.
5.  **Получение ответа**: Ответ возвращается в виде генератора, который выдает части ответа модели в режиме реального времени.

```
Инициализация запроса
      │
      ▼
Формирование сообщения
      │
      ▼
  Открытие изображения
      │
      ▼
    Отправка запроса
      │
      ▼
   Получение ответа
```

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
    image = open("docs/images/cat.jpeg", "rb") # open("path", "rb"), do not use .read(), etc. it must be a file object
)

for message in completion:
    print(message.choices[0].delta.content or "")
```

### `print`

```python
for message in completion:
    print(message.choices[0].delta.content or "")
```

**Назначение**: Выводит в консоль содержимое ответа от модели Reka.

**Параметры**:
- `message` (str): Сообщение, полученное от модели.

**Как работает функция**:

1.  **Итерация по ответу**: Цикл `for` итерируется по каждой части ответа, возвращаемого генератором `completion`.
2.  **Извлечение содержимого**: Извлекается содержимое ответа из объекта `message.choices[0].delta.content`.
3.  **Вывод в консоль**: Содержимое выводится в консоль. Если содержимое отсутствует, выводится пустая строка.

**Примеры**:

```python
for message in completion:
    print(message.choices[0].delta.content or "")