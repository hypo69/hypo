# Модуль для взаимодействия с Reka API для анализа изображений
## Обзор
Модуль предоставляет пример кода для взаимодействия с API Reka, используемого для анализа изображений. Он демонстрирует, как отправлять изображения в Reka API и получать текстовое описание содержимого изображения.

## Подробнее
Этот код предназначен для демонстрации функциональности анализа изображений с использованием модели "reka-core" через библиотеку `g4f`. Для его работы требуется быть залогиненым на `chat.reka.ai` и иметь cookies.  Основная цель - показать, как можно отправить изображение и получить описание того, что на нем изображено.  Он использует класс `Client` из библиотеки `g4f` для взаимодействия с API. Файл  `cat.jpeg` должен лежать в папке `docs/images/`. Путь до картинки указывается при инициализации.

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

**Назначение**: Создает запрос к API Reka для анализа изображения и получения текстового описания.

**Параметры**:

- `model` (str): Указывает используемую модель, в данном случае "reka-core".
- `messages` (list): Список сообщений, содержащих запрос пользователя.
- `stream` (bool): Указывает, следует ли использовать потоковую передачу данных.
- `image` (file object): Открытый файл изображения, который необходимо проанализировать. Важно передавать именно файловый объект, а не содержимое файла.

**Возвращает**:

- `completion`: Объект, представляющий собой потоковый ответ от API Reka.

**Вызывает исключения**:

- Возможные исключения, связанные с сетевыми запросами и обработкой данных от API.

**Как работает функция**:

1.  Формирует запрос к API Reka, указывая модель, сообщение пользователя и изображение для анализа.
2.  Отправляет запрос к API и получает потоковый ответ.
3.  Обрабатывает каждый фрагмент ответа, извлекая текстовое описание.

```
Запрос к API Reka с параметрами:
model="reka-core",
messages=[{"role": "user", "content": "What can you see in the image ?"}]
stream=True, image=<_io.BufferedReader name='docs/images/cat.jpeg'>]
|
Отправка запроса к API Reka
|
Получение потокового ответа
|
Извлечение текстового описания из каждого фрагмента ответа
```

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

### Цикл for для обработки ответа

```python
for message in completion:
    print(message.choices[0].delta.content or "")
```

**Назначение**: Обрабатывает потоковый ответ от API Reka и выводит полученное описание изображения.

**Параметры**:

- `message`: Каждый фрагмент ответа, полученный из потока `completion`.

**Как работает функция**:

1.  Итерируется по каждому фрагменту ответа, полученного из потока `completion`.
2.  Извлекает текстовое содержимое из каждого фрагмента (`message.choices[0].delta.content`).
3.  Выводит извлеченное содержимое в консоль.

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