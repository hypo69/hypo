# Модуль `website.py`

## Обзор

Модуль `website.py` отвечает за настройку маршрутов веб-сайта и отображение соответствующих шаблонов. Он использует Flask для определения эндпоинтов и рендеринга HTML-страниц.

## Подробнее

Этот модуль является частью веб-интерфейса `gpt4free`, созданного с использованием Flask. Он определяет различные маршруты, такие как главная страница, страница чата, страница настроек и страница фона. Каждый маршрут связан с определенной функцией, которая обрабатывает запрос и возвращает соответствующий шаблон HTML.

## Классы

### `Website`

**Описание**: Класс `Website` управляет маршрутами веб-сайта и связывает их с соответствующими функциями отображения.

**Принцип работы**:
Класс инициализируется с экземпляром Flask-приложения. Он определяет словарь `routes`, который содержит маршруты веб-сайта и связанные с ними функции и методы.

**Атрибуты**:
- `app`: Экземпляр Flask-приложения.
- `routes`: Словарь, содержащий маршруты веб-сайта и связанные с ними функции и методы.

**Методы**:
- `__init__(self, app) -> None`: Инициализирует экземпляр класса `Website` с Flask-приложением.
- `_chat(self, conversation_id)`: Отображает страницу чата для указанного `conversation_id`.
- `_share_id(self, share_id, conversation_id: str = "")`: Отображает страницу общего доступа с заданными `share_id` и `conversation_id`.
- `_index(self)`: Отображает главную страницу с новым `conversation_id`.
- `_settings(self)`: Отображает страницу настроек с новым `conversation_id`.
- `_background(self)`: Отображает страницу фона.

## Функции

### `redirect_home()`

**Назначение**: Выполняет перенаправление на страницу `/chat`.

**Как работает функция**:
Функция просто возвращает результат вызова `redirect('/chat')`, что приводит к перенаправлению пользователя на главную страницу чата.

```
A[Вызов redirect('/chat')]
|
B[Перенаправление на '/chat']
```

**Примеры**:
```python
from flask import Flask
from unittest.mock import MagicMock

app = Flask(__name__)
with app.test_request_context():
    result = redirect_home()
    print(result.location)  # Вывод: /chat
```

### `Website.__init__(self, app) -> None`

**Назначение**: Инициализирует экземпляр класса `Website` и настраивает маршруты приложения.

**Параметры**:
- `app`: Экземпляр Flask-приложения.

**Как работает функция**:
1.  Принимает экземпляр Flask-приложения в качестве аргумента.
2.  Сохраняет ссылку на приложение в атрибуте `self.app`.
3.  Определяет словарь `self.routes`, содержащий маршруты и связанные с ними функции и методы.

```
A[Инициализация экземпляра Website]
|
B[Сохранение ссылки на Flask-приложение]
|
C[Определение маршрутов]
```

### `Website._chat(self, conversation_id)`

**Назначение**: Отображает страницу чата для указанного `conversation_id`.

**Параметры**:
- `conversation_id`: Идентификатор разговора.

**Как работает функция**:
1.  Проверяет, является ли `conversation_id` равным "share".
2.  Если `conversation_id` равен "share", отображает шаблон `index.html` с новым `conversation_id`, сгенерированным с помощью `uuid.uuid4()`.
3.  В противном случае отображает шаблон `index.html` с предоставленным `conversation_id`.

```
A[Проверка conversation_id == "share"]
|
B[Если да: Генерация нового conversation_id]
|
C[Отображение шаблона index.html с conversation_id]
```

**Примеры**:
```python
from flask import Flask
from unittest.mock import MagicMock

app = Flask(__name__)
app.template_folder = 'templates'  # Укажите путь к вашей папке с шаблонами

@app.route('/chat/<conversation_id>')
def chat(conversation_id):
    website = Website(app)
    # Mock render_template для тестирования
    website.render_template = MagicMock(return_value='Template Rendered')
    result = website._chat(conversation_id)
    return result

# Создаем фиктивный шаблон index.html
with open('templates/index.html', 'w') as f:
    f.write('<h1>Hello, World!</h1>')

with app.test_request_context():
    result1 = chat('123')
    print(result1)
    #website.render_template.assert_called_with('index.html', conversation_id='123')

    result2 = chat('share')
    print(result2)
    #assert website.render_template.call_args[0][0] == 'index.html'
    #assert 'conversation_id' in website.render_template.call_args[1]
```

### `Website._share_id(self, share_id, conversation_id: str = "")`

**Назначение**: Отображает страницу общего доступа с заданными `share_id` и `conversation_id`.

**Параметры**:
- `share_id`: Идентификатор общего доступа.
- `conversation_id` (optional): Идентификатор разговора. По умолчанию пустая строка.

**Как работает функция**:
1.  Получает значение переменной окружения `G4F_SHARE_URL`.
2.  Если `conversation_id` не предоставлен, генерирует новый `conversation_id` с помощью `uuid.uuid4()`.
3.  Отображает шаблон `index.html` с переменными `share_url`, `share_id` и `conversation_id`.

```
A[Получение G4F_SHARE_URL из окружения]
|
B[Проверка наличия conversation_id]
|
C[Если нет: Генерация нового conversation_id]
|
D[Отображение шаблона index.html с share_url, share_id и conversation_id]
```

**Примеры**:
```python
from flask import Flask
from unittest.mock import MagicMock
import os

app = Flask(__name__)
app.template_folder = 'templates'  # Укажите путь к вашей папке с шаблонами
os.environ["G4F_SHARE_URL"] = "http://example.com/share"

@app.route('/share/<share_id>/<conversation_id>')
def share_id(share_id, conversation_id):
    website = Website(app)
    # Mock render_template для тестирования
    website.render_template = MagicMock(return_value='Template Rendered')
    result = website._share_id(share_id, conversation_id)
    return result

# Создаем фиктивный шаблон index.html
with open('templates/index.html', 'w') as f:
    f.write('<h1>Hello, World!</h1>')

with app.test_request_context():
    result1 = share_id('abc', '123')
    print(result1)
    #website.render_template.assert_called_with('index.html', share_url="http://example.com/share", share_id='abc', conversation_id='123')

    result2 = share_id('abc', '')
    print(result2)
    #assert website.render_template.call_args[0][0] == 'index.html'
    #assert 'share_url' in website.render_template.call_args[1]
    #assert 'share_id' in website.render_template.call_args[1]
    #assert 'conversation_id' in website.render_template.call_args[1]
```

### `Website._index(self)`

**Назначение**: Отображает главную страницу с новым `conversation_id`.

**Как работает функция**:
1.  Генерирует новый `conversation_id` с помощью `uuid.uuid4()`.
2.  Отображает шаблон `index.html` с новым `conversation_id`.

```
A[Генерация нового conversation_id]
|
B[Отображение шаблона index.html с conversation_id]
```

**Примеры**:
```python
from flask import Flask
from unittest.mock import MagicMock

app = Flask(__name__)
app.template_folder = 'templates'  # Укажите путь к вашей папке с шаблонами

@app.route('/')
def index():
    website = Website(app)
    # Mock render_template для тестирования
    website.render_template = MagicMock(return_value='Template Rendered')
    result = website._index()
    return result

# Создаем фиктивный шаблон index.html
with open('templates/index.html', 'w') as f:
    f.write('<h1>Hello, World!</h1>')

with app.test_request_context():
    result = index()
    print(result)
    #assert website.render_template.call_args[0][0] == 'index.html'
    #assert 'conversation_id' in website.render_template.call_args[1]
```

### `Website._settings(self)`

**Назначение**: Отображает страницу настроек с новым `conversation_id`.

**Как работает функция**:
1.  Генерирует новый `conversation_id` с помощью `uuid.uuid4()`.
2.  Отображает шаблон `index.html` с новым `conversation_id`.

```
A[Генерация нового conversation_id]
|
B[Отображение шаблона index.html с conversation_id]
```

**Примеры**:
```python
from flask import Flask
from unittest.mock import MagicMock

app = Flask(__name__)
app.template_folder = 'templates'  # Укажите путь к вашей папке с шаблонами

@app.route('/settings')
def settings():
    website = Website(app)
    # Mock render_template для тестирования
    website.render_template = MagicMock(return_value='Template Rendered')
    result = website._settings()
    return result

# Создаем фиктивный шаблон index.html
with open('templates/index.html', 'w') as f:
    f.write('<h1>Hello, World!</h1>')

with app.test_request_context():
    result = settings()
    print(result)
    #assert website.render_template.call_args[0][0] == 'index.html'
    #assert 'conversation_id' in website.render_template.call_args[1]
```

### `Website._background(self)`

**Назначение**: Отображает страницу фона.

**Как работает функция**:
Функция отображает шаблон `background.html`.

```
A[Отображение шаблона background.html]
```

**Примеры**:
```python
from flask import Flask
from unittest.mock import MagicMock

app = Flask(__name__)
app.template_folder = 'templates'  # Укажите путь к вашей папке с шаблонами

@app.route('/background')
def background():
    website = Website(app)
    # Mock render_template для тестирования
    website.render_template = MagicMock(return_value='Template Rendered')
    result = website._background()
    return result

# Создаем фиктивный шаблон background.html
with open('templates/background.html', 'w') as f:
    f.write('<h1>Background</h1>')

with app.test_request_context():
    result = background()
    print(result)
    #website.render_template.assert_called_with('background.html')