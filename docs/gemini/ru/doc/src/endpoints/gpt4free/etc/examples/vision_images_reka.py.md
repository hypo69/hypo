# Модуль для работы с Image Chat Reka

## Обзор

Модуль предназначен для взаимодействия с моделью Reka для анализа изображений. Он использует клиент `g4f.client.Client` для отправки запросов к модели Reka и получения ответов на вопросы об изображениях.

## Подробней

Этот код демонстрирует пример использования модели `reka-core` для анализа изображений. Для работы с этим кодом необходимо быть залогиненым в `chat.reka.ai` и иметь сохраненные cookies. Также, необходимо иметь изображение `cat.jpeg` в папке `docs/images`. Этот модуль можно использовать для анализа изображений и получения информации об объектах, присутствующих на них.

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

**Назначение**: Отправляет запрос к модели `reka-core` для анализа изображения и получения ответа на вопрос.

**Параметры**:

- `model` (str): Имя модели для использования. В данном случае, `"reka-core"`.
- `messages` (list): Список сообщений для отправки модели. Содержит сообщение пользователя с вопросом об изображении.
- `stream` (bool): Определяет, должен ли ответ быть получен в потоковом режиме. В данном случае, `True`.
- `image` (file object): Объект файла изображения, открытый в бинарном режиме чтения (`"rb"`).

**Возвращает**:

- `completion`: Объект, представляющий собой потоковый ответ от модели.

**Как работает функция**:

1. Создается запрос к модели `reka-core` через метод `client.chat.completions.create`.
2. В запросе передается вопрос пользователя `"What can you see in the image ?"` и объект файла изображения `cat.jpeg`.
3. Запрос отправляется в потоковом режиме, что позволяет получать ответ частями.

**Примеры**:

```python
from g4f.client import Client
from g4f.Provider import Reka

client = Client(provider=Reka)

completion = client.chat.completions.create(
    model="reka-core",
    messages=[
        {
            "role": "user",
            "content": "What can you see in the image?"
        }
    ],
    stream=True,
    image=open("docs/images/cat.jpeg", "rb")
)
```

### Цикл `for message in completion`

```python
for message in completion:
    print(message.choices[0].delta.content or "")
```

**Назначение**: Обрабатывает потоковый ответ от модели и выводит его в консоль.

**Параметры**:

- `message`: Объект, представляющий собой часть потокового ответа от модели.

**Как работает функция**:

1.  **Цикл обработки ответа**: Цикл `for message in completion:` итерируется по каждой части потокового ответа, возвращаемого методом `create`. Каждая итерация представляет собой отдельное сообщение от модели.
2.  **Извлечение содержимого**: `message.choices[0].delta.content or ""` извлекает содержимое из текущего сообщения. `message.choices` представляет собой список возможных вариантов ответа, где `[0]` выбирает первый вариант. `delta.content` содержит фактический текст ответа. Если `delta.content` равно `None` или пусто, то `or ""` обеспечивает вывод пустой строки, чтобы избежать ошибок.
3.  **Вывод в консоль**: `print(message.choices[0].delta.content or "")` выводит извлеченное содержимое в консоль. Это позволяет видеть ответ модели в реальном времени по мере его генерации.

**Примеры**:

```python
from g4f.client import Client
from g4f.Provider import Reka

client = Client(provider=Reka)

completion = client.chat.completions.create(
    model="reka-core",
    messages=[
        {
            "role": "user",
            "content": "What can you see in the image?"
        }
    ],
    stream=True,
    image=open("docs/images/cat.jpeg", "rb")
)

for message in completion:
    print(message.choices[0].delta.content or "")