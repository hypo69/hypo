# Модуль для работы с веб-сайтом

## Обзор

Модуль `website.py` предоставляет класс `Website`, который отвечает за настройку и обработку маршрутов веб-сайта, включая перенаправления, рендеринг шаблонов и обслуживание статических ресурсов. Он использует Flask для определения конечных точек и обработки запросов.

## Подробнее

Этот модуль является частью веб-интерфейса `freegpt-webui-ru` и отвечает за маршрутизацию запросов к различным частям веб-приложения. Он определяет, какие функции должны быть вызваны при обращении к определенным URL-адресам.

## Классы

### `Website`

**Описание**:
Класс `Website` инициализирует веб-приложение Flask, определяет маршруты и связывает их с соответствующими функциями обработки.

**Принцип работы**:
Класс принимает экземпляр приложения Flask в качестве аргумента при инициализации. Он определяет словарь `routes`, который содержит соответствия между URL-адресами и функциями, которые должны быть вызваны при обращении к этим URL-адресам. Методы класса обрабатывают различные маршруты, такие как главная страница, страница чата и статические ресурсы.

**Атрибуты**:
- `app`: Экземпляр приложения Flask.
- `routes` (dict): Словарь, содержащий соответствия между URL-адресами и функциями обработки.

**Методы**:
- `__init__(self, app)`: Инициализирует класс `Website`, сохраняя экземпляр приложения Flask и определяя маршруты.
- `_chat(self, conversation_id)`: Обрабатывает маршрут `/chat/<conversation_id>`, перенаправляя на страницу чата с указанным идентификатором разговора.
- `_index(self)`: Обрабатывает маршрут `/chat/`, генерируя уникальный идентификатор разговора и отображая страницу чата.
- `_assets(self, folder: str, file: str)`: Обрабатывает маршрут `/assets/<folder>/<file>`, отправляя запрошенный статический файл.

## Функции

### `__init__`

```python
def __init__(self, app) -> None:
    """
    Инициализирует класс Website, связывая приложение Flask с маршрутами.

    Args:
        app: Экземпляр приложения Flask.

    Returns:
        None

    Raises:
        None
    """
```

**Назначение**:
Инициализирует экземпляр класса `Website`, сохраняя переданное приложение Flask и определяя маршруты веб-сайта.

**Параметры**:
- `app`: Экземпляр приложения Flask, который будет использоваться для маршрутизации.

**Возвращает**:
- `None`

**Как работает функция**:

1.  Сохраняет переданный экземпляр приложения Flask в атрибуте `app`.
2.  Определяет словарь `routes`, который связывает URL-адреса с функциями, которые должны обрабатывать эти URL-адреса.

```
A: Сохранение приложения Flask
|
B: Определение маршрутов
```

**Примеры**:
```python
from flask import Flask
app = Flask(__name__)
website = Website(app)
```

### `_chat`

```python
def _chat(self, conversation_id):
    """
    Обрабатывает маршрут `/chat/<conversation_id>`, отображая страницу чата с указанным ID.

    Args:
        conversation_id: Идентификатор разговора.

    Returns:
        response: Ответ Flask, отображающий страницу `index.html` с указанным `chat_id`.

    Raises:
        None
    """
```

**Назначение**:
Функция обрабатывает URL-адрес `/chat/<conversation_id>` и отображает страницу чата с заданным идентификатором разговора.

**Параметры**:
- `conversation_id`: Идентификатор разговора, который будет передан в шаблон `index.html`.

**Возвращает**:
- Ответ Flask, отображающий страницу `index.html` с указанным `chat_id`. Если `conversation_id` не содержит символ '-', происходит перенаправление на `/chat`.

**Как работает функция**:

1.  Проверяет, содержит ли `conversation_id` символ `-`.
2.  Если символ отсутствует, выполняет перенаправление на маршрут `/chat`.
3.  Если символ присутствует, отображает шаблон `index.html`, передавая `conversation_id` в качестве параметра `chat_id`.

```
A: Проверка наличия '-' в conversation_id
|
B: Если '-' отсутствует -> Перенаправление на '/chat'
|
C: Если '-' присутствует -> Отображение шаблона index.html с chat_id=conversation_id
```

**Примеры**:
```python
from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

class Website():
  def __init__(self, app) -> None:
    self.app = app
    self.routes = {
        '/chat/<conversation_id>': {
            'function': self._chat,
            'methods': ['GET', 'POST']
        },
    }

  def _chat(self, conversation_id):
    if '-' not in conversation_id:
      return redirect('/chat')

    return render_template('index.html', chat_id=conversation_id)


@app.route('/chat')
def chat_index():
    return "Страница выбора чата"

@app.route('/chat/<conversation_id>')
def chat_route(conversation_id):
  website = Website(app)
  return website._chat(conversation_id)

@app.route('/')
def index():
    return render_template('index.html', chat_id="123")

if __name__ == '__main__':
    app.run(debug=True)
```

### `_index`

```python
def _index(self):
    """
    Обрабатывает маршрут `/chat/`, перенаправляя на страницу чата с новым сгенерированным ID.

    Args:
        None

    Returns:
        response: Ответ Flask, отображающий страницу `index.html` с новым `chat_id`.

    Raises:
        None
    """
```

**Назначение**:
Функция обрабатывает URL-адрес `/chat/` и отображает страницу чата с новым уникальным идентификатором разговора.

**Параметры**:
- Отсутствуют

**Возвращает**:
- Ответ Flask, отображающий страницу `index.html` с новым `chat_id`. Идентификатор генерируется случайным образом и включает текущее время.

**Как работает функция**:

1.  Генерирует случайный идентификатор разговора, используя `urandom` и `time`.
2.  Отображает шаблон `index.html`, передавая сгенерированный идентификатор в качестве параметра `chat_id`.

```
A: Генерация случайного chat_id
|
B: Отображение шаблона index.html с chat_id
```

**Примеры**:
```python
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = True

class Website():
  def __init__(self, app) -> None:
    self.app = app
    self.routes = {
        '/chat/': {
            'function': self._index,
            'methods': ['GET', 'POST']
        },
    }

  def _index(self):
    return render_template('index.html', chat_id=f'test-test-test')


@app.route('/')
def index():
    return render_template('index.html', chat_id="123")

@app.route('/chat/')
def chat_route():
  website = Website(app)
  return website._index()

if __name__ == '__main__':
    app.run(debug=True)
```

### `_assets`

```python
def _assets(self, folder: str, file: str):
    """
    Обрабатывает маршрут `/assets/<folder>/<file>`, отправляя запрошенный файл из указанной папки.

    Args:
        folder (str): Папка, содержащая запрошенный файл.
        file (str): Имя запрошенного файла.

    Returns:
        response: Ответ Flask, содержащий запрошенный файл.
        404: Если файл не найден, возвращает сообщение "File not found" и код 404.

    Raises:
        None
    """
```

**Назначение**:
Функция обслуживает статические ресурсы, такие как CSS, JavaScript и изображения, отправляя запрошенный файл из указанной папки.

**Параметры**:
- `folder` (str): Имя папки, содержащей запрошенный файл.
- `file` (str): Имя запрошенного файла.

**Возвращает**:
- Ответ Flask, содержащий запрошенный файл, или сообщение "File not found" с кодом 404, если файл не найден.

**Как работает функция**:

1.  Пытается отправить запрошенный файл из папки `../client/{folder}/{file}`.
2.  Если файл найден, он отправляется в качестве ответа.
3.  Если файл не найден, возвращается сообщение "File not found" с кодом 404.

```
A: Попытка отправить файл из папки ../client/{folder}/{file}
|
B: Если файл найден -> Отправка файла в качестве ответа
|
C: Если файл не найден -> Возврат сообщения "File not found" с кодом 404
```

**Примеры**:
```python
from flask import Flask
from flask import send_file

app = Flask(__name__)
app.config['DEBUG'] = True

class Website():
  def __init__(self, app) -> None:
    self.app = app
    self.routes = {
        '/assets/<folder>/<file>': {
            'function': self._assets,
            'methods': ['GET', 'POST']
        },
    }

  def _assets(self, folder: str, file: str):
    try:
      return send_file(f"./client/{folder}/{file}", as_attachment=False)
    except:
      return "File not found", 404


@app.route('/assets/<folder>/<file>')
def assets_route(folder, file):
  website = Website(app)
  return website._assets(folder, file)


if __name__ == '__main__':
    app.run(debug=True)