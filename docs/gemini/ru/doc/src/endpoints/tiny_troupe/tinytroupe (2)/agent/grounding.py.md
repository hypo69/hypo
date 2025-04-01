# Модуль для работы с коннекторами заземления (Grounding)
===========================================================

Модуль содержит классы для подключения к различным источникам знаний, таким как локальные файлы и веб-страницы,
с целью расширения возможностей агента по обоснованию своих ответов на основе внешних данных.

## Обзор

В данном модуле определены классы, обеспечивающие подключение агента к различным источникам информации для расширения его знаний.
Основная идея заключается в создании коннекторов, которые позволяют агенту "заземлять" свои знания на внешние источники,
такие как файлы, веб-страницы и базы данных. Это позволяет агенту получать релевантную информацию из этих источников и использовать ее
для обоснования своих ответов.

## Подробнее

Модуль предоставляет абстрактный класс `GroundingConnector`, который служит базовым классом для всех коннекторов заземления.
Он определяет основные методы, которые должны быть реализованы в подклассах, такие как `retrieve_relevant`, `retrieve_by_name` и `list_sources`.

Также в модуле реализованы классы `BaseSemanticGroundingConnector`, `LocalFilesGroundingConnector` и `WebPagesGroundingConnector`,
которые предоставляют конкретные реализации коннекторов для семантического поиска, локальных файлов и веб-страниц соответственно.

## Классы

### `GroundingConnector`

**Описание**:
Абстрактный класс, представляющий коннектор заземления. Коннектор заземления - это компонент, который позволяет агенту заземлять свои знания во внешних источниках, таких как файлы, веб-страницы, базы данных и т.д.

**Атрибуты**:
- `name` (str): Имя коннектора заземления.

**Методы**:
- `__init__(name: str) -> None`:
    Инициализирует экземпляр класса `GroundingConnector`.
- `retrieve_relevant(self, relevance_target: str, source: str, top_k: int = 20) -> list`:
    Извлекает релевантные данные из источника на основе цели релевантности.
    Вызывает исключение `NotImplementedError`, если метод не реализован в подклассе.
- `retrieve_by_name(self, name: str) -> str`:
    Извлекает источник контента по его имени.
    Вызывает исключение `NotImplementedError`, если метод не реализован в подклассе.
- `list_sources(self) -> list`:
    Перечисляет имена доступных источников контента.
    Вызывает исключение `NotImplementedError`, если метод не реализован в подклассе.

### `BaseSemanticGroundingConnector`

**Описание**:
Базовый класс для коннекторов семантического заземления. Коннектор семантического заземления - это компонент, который индексирует и извлекает документы на основе так называемого "семантического поиска" (т.е. поиска на основе вложений). Эта конкретная реализация основана на классе `VectorStoreIndex` из библиотеки `LLaMa-Index`. Здесь "документы" относятся к структуре данных `llama-index`, которая хранит единицу контента, не обязательно файл.

**Наследует**:
- `GroundingConnector`: Наследует атрибуты и методы класса `GroundingConnector`.

**Атрибуты**:
- `documents` (list): Список документов, используемых для семантического поиска.
- `name_to_document` (dict): Словарь, сопоставляющий имена документов со списками документов.
- `index` (VectorStoreIndex): Индекс для семантического поиска.

**Методы**:
- `__init__(self, name: str = "Semantic Grounding") -> None`:
    Инициализирует экземпляр класса `BaseSemanticGroundingConnector`.
- `_post_init(self)`:
    Выполняется после `__init__`, так как класс имеет декоратор `@post_init`.
    Удобно разделять некоторые процессы инициализации, чтобы упростить десериализацию.
- `retrieve_relevant(self, relevance_target: str, top_k: int = 20) -> list`:
    Извлекает все значения из памяти, которые релевантны данной цели.
- `retrieve_by_name(self, name: str) -> list`:
    Извлекает источник контента по его имени.
- `list_sources(self) -> list`:
    Перечисляет имена доступных источников контента.
- `add_document(self, document, doc_to_name_func=None) -> None`:
    Индексирует документ для семантического поиска.
- `add_documents(self, new_documents, doc_to_name_func=None) -> list`:
    Индексирует документы для семантического поиска.

### `LocalFilesGroundingConnector`

**Описание**:
Класс для подключения к локальным файлам для заземления.

**Наследует**:
- `BaseSemanticGroundingConnector`: Наследует атрибуты и методы класса `BaseSemanticGroundingConnector`.

**Атрибуты**:
- `folders_paths` (list): Список путей к папкам с файлами для заземления.
- `loaded_folders_paths` (list): Список путей к уже загруженным папкам.

**Методы**:
- `__init__(self, name: str = "Local Files", folders_paths: list | None = None) -> None`:
    Инициализирует экземпляр класса `LocalFilesGroundingConnector`.
- `_post_init(self)`:
    Выполняется после `__init__`, так как класс имеет декоратор `@post_init`.
    Удобно разделять некоторые процессы инициализации, чтобы упростить десериализацию.
- `add_folders(self, folders_paths: list | None) -> None`:
    Добавляет путь к папке с файлами, используемыми для заземления.
- `add_folder(self, folder_path: str) -> None`:
    Добавляет путь к папке с файлами, используемыми для заземления.
- `add_file_path(self, file_path: str) -> None`:
    Добавляет путь к файлу, используемому для заземления.
- `_mark_folder_as_loaded(self, folder_path: str) -> None`:
    Помечает папку как загруженную.

### `WebPagesGroundingConnector`

**Описание**:
Класс для подключения к веб-страницам для заземления.

**Наследует**:
- `BaseSemanticGroundingConnector`: Наследует атрибуты и методы класса `BaseSemanticGroundingConnector`.

**Атрибуты**:
- `web_urls` (list): Список URL-адресов веб-страниц для заземления.
- `loaded_web_urls` (list): Список уже загруженных URL-адресов веб-страниц.

**Методы**:
- `__init__(self, name: str = "Web Pages", web_urls: list | None = None) -> None`:
    Инициализирует экземпляр класса `WebPagesGroundingConnector`.
- `_post_init(self)`:
    Выполняется после `__init__`, так как класс имеет декоратор `@post_init`.
- `add_web_urls(self, web_urls: list | None) -> None`:
    Добавляет данные, полученные с указанных URL-адресов, к заземлению.
- `add_web_url(self, web_url: str) -> None`:
    Добавляет данные, полученные с указанного URL-адреса, к заземлению.
- `_mark_web_url_as_loaded(self, web_url: str) -> None`:
    Помечает URL-адрес веб-страницы как загруженный.

## Функции

### `GroundingConnector.retrieve_relevant`

```python
def retrieve_relevant(self, relevance_target: str, source: str, top_k: int = 20) -> list:
    """
    Извлекает релевантные данные из источника на основе цели релевантности.
    """
    ...
```

**Назначение**:
Извлекает релевантные данные из внешнего источника, основываясь на заданной цели релевантности и конкретном источнике. Этот метод предназначен для поиска информации, которая наиболее соответствует запросу пользователя в контексте определенного источника данных.

**Параметры**:
- `relevance_target` (str): Цель релевантности, представляющая собой запрос или вопрос, на который нужно найти ответ.
- `source` (str): Источник данных, из которого необходимо извлечь релевантную информацию.
- `top_k` (int, optional): Максимальное количество релевантных результатов, которые необходимо извлечь. По умолчанию равно 20.

**Возвращает**:
- `list`: Список релевантных данных, извлеченных из источника.

**Вызывает исключения**:
- `NotImplementedError`: Вызывается, если метод не реализован в подклассе.

**Как работает функция**:
1. Функция принимает цель релевантности (`relevance_target`), источник данных (`source`) и количество результатов (`top_k`) в качестве входных параметров.
2. Поскольку `GroundingConnector` является абстрактным классом, этот метод не имеет конкретной реализации и предназначен для переопределения в подклассах.
3. Если метод не переопределен в подклассе, он вызывает исключение `NotImplementedError`, указывающее на необходимость реализации метода в подклассе.

**ASCII flowchart**:

```
Начало
  ↓
Вызов исключения NotImplementedError
  ↓
Конец
```

**Примеры**:
```python
# Пример вызова метода retrieve_relevant (невозможно, так как метод абстрактный)
# connector = GroundingConnector(name="example")
# results = connector.retrieve_relevant(relevance_target="example target", source="example source", top_k=10)
```

### `GroundingConnector.retrieve_by_name`

```python
def retrieve_by_name(self, name: str) -> str:
    """
    Извлекает источник контента по его имени.
    """
    ...
```

**Назначение**:
Извлекает контент из источника данных по указанному имени. Этот метод позволяет получить доступ к конкретному источнику информации, идентифицированному по его уникальному имени.

**Параметры**:
- `name` (str): Имя источника контента, который необходимо извлечь.

**Возвращает**:
- `str`: Контент, извлеченный из источника данных.

**Вызывает исключения**:
- `NotImplementedError`: Вызывается, если метод не реализован в подклассе.

**Как работает функция**:
1. Функция принимает имя источника контента (`name`) в качестве входного параметра.
2. Поскольку `GroundingConnector` является абстрактным классом, этот метод не имеет конкретной реализации и предназначен для переопределения в подклассах.
3. Если метод не переопределен в подклассе, он вызывает исключение `NotImplementedError`, указывающее на необходимость реализации метода в подклассе.

**ASCII flowchart**:

```
Начало
  ↓
Вызов исключения NotImplementedError
  ↓
Конец
```

**Примеры**:
```python
# Пример вызова метода retrieve_by_name (невозможно, так как метод абстрактный)
# connector = GroundingConnector(name="example")
# content = connector.retrieve_by_name(name="example name")
```

### `GroundingConnector.list_sources`

```python
def list_sources(self) -> list:
    """
    Перечисляет имена доступных источников контента.
    """
    ...
```

**Назначение**:
Предоставляет список имен всех доступных источников контента, к которым может подключиться коннектор.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `list`: Список имен доступных источников контента.

**Вызывает исключения**:
- `NotImplementedError`: Вызывается, если метод не реализован в подклассе.

**Как работает функция**:
1. Функция не принимает входных параметров.
2. Поскольку `GroundingConnector` является абстрактным классом, этот метод не имеет конкретной реализации и предназначен для переопределения в подклассах.
3. Если метод не переопределен в подклассе, он вызывает исключение `NotImplementedError`, указывающее на необходимость реализации метода в подклассе.

**ASCII flowchart**:

```
Начало
  ↓
Вызов исключения NotImplementedError
  ↓
Конец
```

**Примеры**:
```python
# Пример вызова метода list_sources (невозможно, так как метод абстрактный)
# connector = GroundingConnector(name="example")
# sources = connector.list_sources()
```

### `BaseSemanticGroundingConnector._post_init`

```python
def _post_init(self):
    """
    Эта функция будет запущена после __init__, поскольку класс имеет декоратор @post_init.
    Удобно разделять некоторые процессы инициализации, чтобы упростить десериализацию.
    """
    ...
```

**Назначение**:
Выполняет постобработку инициализации экземпляра класса `BaseSemanticGroundingConnector`. Этот метод вызывается автоматически после завершения `__init__` благодаря декоратору `@post_init`. Он предназначен для выполнения задач инициализации, которые зависят от завершения основных этапов инициализации, таких как десериализация объектов.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

**Как работает функция**:
1. Функция не принимает входных параметров.
2. Инициализирует атрибут `self.index` значением `None`.
3. Проверяет наличие атрибута `self.documents` и, если он отсутствует или равен `None`, инициализирует его пустым списком.
4. Проверяет наличие атрибута `self.name_to_document` и, если он отсутствует или равен `None`, инициализирует его пустым словарем.
5. Вызывает метод `self.add_documents` с аргументом `self.documents` для индексации документов.

**ASCII flowchart**:

```
Начало
  ↓
Инициализация self.index = None
  ↓
Проверка наличия self.documents и его инициализация, если отсутствует
  ↓
Проверка наличия self.name_to_document и его инициализация, если отсутствует
  ↓
Вызов self.add_documents(self.documents)
  ↓
Конец
```

**Примеры**:
```python
# Пример вызова метода _post_init (вызывается автоматически декоратором @post_init)
# connector = BaseSemanticGroundingConnector(name="example")
# connector._post_init()
```

### `BaseSemanticGroundingConnector.retrieve_relevant`

```python
def retrieve_relevant(self, relevance_target: str, top_k: int = 20) -> list:
    """
    Извлекает все значения из памяти, которые релевантны данной цели.
    """
    ...
```

**Назначение**:
Извлекает из индекса VectorStoreIndex наиболее релевантные узлы (nodes) на основе переданной цели (`relevance_target`).

**Параметры**:
- `relevance_target` (str): Цель релевантности, запрос или вопрос, на который нужно найти ответ.
- `top_k` (int, optional): Количество наиболее релевантных узлов, которые нужно извлечь. По умолчанию равно 20.

**Возвращает**:
- `list`: Список строк, представляющих извлеченный контент, отформатированный с информацией об источнике, оценке сходства и релевантном содержимом.

**Как работает функция**:
1. Проверяет, инициализирован ли индекс (`self.index is not None`).
2. Если индекс существует, создает объект `retriever` с помощью метода `self.index.as_retriever(similarity_top_k=top_k)`, который позволяет извлекать `top_k` наиболее похожих узлов.
3. Вызывает метод `retriever.retrieve(relevance_target)` для получения списка узлов, релевантных цели.
4. Если индекс не существует, возвращает пустой список `nodes = []`.
5. Инициализирует пустой список `retrieved = []` для хранения извлеченного контента.
6. Перебирает узлы в списке `nodes` и для каждого узла формирует строку `content`, содержащую информацию об источнике (имя файла), оценке сходства и релевантном содержимом.
7. Добавляет отформатированную строку `content` в список `retrieved`.
8. Логирует извлеченный контент с использованием `logger.debug(f"Content retrieved: {content[:200]}")`.
9. Возвращает список `retrieved`, содержащий извлеченный контент.

**ASCII flowchart**:

```
Начало
  ↓
Проверка: self.index is not None
  ├── True:
  │   ↓
  │   Создание retriever: retriever = self.index.as_retriever(similarity_top_k=top_k)
  │   ↓
  │   Извлечение узлов: nodes = retriever.retrieve(relevance_target)
  │   ↓
  └── False:
      ↓
      nodes = []
  ↓
retrieved = []
  ↓
Перебор узлов в nodes
  │
  └──Для каждого узла:
      ↓
      Формирование content: "SOURCE: ... SIMILARITY SCORE: ... RELEVANT CONTENT: ..."
      ↓
      Добавление content в retrieved
      ↓
      Логирование: logger.debug(f"Content retrieved: {content[:200]}")
  ↓
Возврат retrieved
  ↓
Конец
```

**Примеры**:
```python
#Пример вызова функции
#connector = BaseSemanticGroundingConnector(name="example")
#result = connector.retrieve_relevant(relevance_target="example target", top_k=10)
```

### `BaseSemanticGroundingConnector.retrieve_by_name`

```python
def retrieve_by_name(self, name: str) -> list:
    """
    Извлекает источник контента по его имени.
    """
    ...
```

**Назначение**:
Извлекает содержимое документов по их именам, предоставляя информацию об источнике, странице и содержании каждого документа.

**Параметры**:
- `name` (str): Имя документа, который нужно извлечь.

**Возвращает**:
- `list`: Список строк, представляющих извлеченное содержимое документов, с информацией об источнике, странице и содержании.

**Как работает функция**:
1. Инициализирует пустой список `results = []` для хранения результатов.
2. Проверяет, существует ли `self.name_to_document` и содержится ли `name` в `self.name_to_document`.
3. Если `name` содержится в `self.name_to_document`, получает список документов `docs` для этого имени.
4. Перебирает документы `docs` в цикле с индексом `i`.
5. Для каждого документа формирует строку `content`, содержащую информацию об источнике (имя), странице (индекс) и содержании документа (первые 10000 символов).
6. Добавляет строку `content` в список `results`.
7. Возвращает список `results`, содержащий извлеченное содержимое документов.

**ASCII flowchart**:

```
Начало
  ↓
results = []
  ↓
Проверка: self.name_to_document is not None и name in self.name_to_document
  ├── True:
  │   ↓
  │   docs = self.name_to_document[name]
  │   ↓
  │   Перебор документов в docs с индексом i
  │   │
  │   └──Для каждого документа:
  │       ↓
  │       Формирование content: "SOURCE: ... PAGE: ... CONTENT: ..."
  │       ↓
  │       Добавление content в results
  │   ↓
  └── False:
      ↓
      (Пропуск цикла)
  ↓
Возврат results
  ↓
Конец
```

**Примеры**:
```python
#Пример вызова функции
#connector = BaseSemanticGroundingConnector(name="example")
#result = connector.retrieve_by_name(name="example_document")
```

### `BaseSemanticGroundingConnector.list_sources`

```python
def list_sources(self) -> list:
    """
    Перечисляет имена доступных источников контента.
    """
    ...
```

**Назначение**:
Предоставляет список имен всех доступных источников контента, которые хранятся в `self.name_to_document`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `list`: Список ключей (имен источников) из словаря `self.name_to_document`, если `self.name_to_document` существует. В противном случае возвращает пустой список.

**Как работает функция**:
1. Проверяет, существует ли `self.name_to_document`.
2. Если `self.name_to_document` существует, возвращает список его ключей (имен источников) с помощью `list(self.name_to_document.keys())`.
3. Если `self.name_to_document` не существует, возвращает пустой список `[]`.

**ASCII flowchart**:

```
Начало
  ↓
Проверка: self.name_to_document is not None
  ├── True:
  │   ↓
  │   Возврат list(self.name_to_document.keys())
  │   ↓
  └── False:
      ↓
      Возврат []
  ↓
Конец
```

**Примеры**:
```python
#Пример вызова функции
#connector = BaseSemanticGroundingConnector(name="example")
#sources = connector.list_sources()
```

### `BaseSemanticGroundingConnector.add_document`

```python
def add_document(self, document, doc_to_name_func=None) -> None:
    """
    Индексирует документ для семантического поиска.
    """
    ...
```

**Назначение**:
Добавляет один документ для семантического поиска.

**Параметры**:
- `document`: Документ, который нужно добавить.
- `doc_to_name_func` (function, optional): Функция, которая принимает документ и возвращает его имя. По умолчанию `None`.

**Возвращает**:
- Отсутствует.

**Как работает функция**:
1. Вызывает метод `self.add_documents` с передачей списка, содержащего только `document`, и функции `doc_to_name_func`.

**ASCII flowchart**:

```
Начало
  ↓
Вызов self.add_documents([document], doc_to_name_func)
  ↓
Конец
```

**Примеры**:
```python
#Пример вызова функции
#connector = BaseSemanticGroundingConnector(name="example")
#connector.add_document(document="example document", doc_to_name_func=lambda doc: "example_name")
```

### `BaseSemanticGroundingConnector.add_documents`

```python
def add_documents(self, new_documents, doc_to_name_func=None) -> list:
    """
    Индексирует документы для семантического поиска.
    """
    ...
```

**Назначение**:
Индексирует предоставленные документы для семантического поиска, обновляя индекс VectorStoreIndex.

**Параметры**:
- `new_documents` (list): Список документов, которые необходимо добавить в индекс.
- `doc_to_name_func` (function, optional): Функция, принимающая документ и возвращающая его имя. Используется для сопоставления документов с их именами. По умолчанию `None`.

**Возвращает**:
- Отсутствует.

**Как работает функция**:
1. Проверяет, есть ли новые документы для индексации (`len(new_documents) > 0`).
2. Если есть новые документы, добавляет их в список `self.documents`.
3. Перебирает новые документы в цикле.
4. Для каждого документа очищает текст с помощью `utils.sanitize_raw_string(document.text)`.
5. Если предоставлена функция `doc_to_name_func`, получает имя документа, вызвав `doc_to_name_func(document)`.
6. Если имя документа уже есть в `self.name_to_document`, добавляет документ в список документов для этого имени. В противном случае создает новую запись в `self.name_to_document` с именем документа в качестве ключа и списком, содержащим документ, в качестве значения.
7. После обработки всех новых документов проверяет, существует ли индекс (`self.index is None`).
8. Если индекс не существует, создает новый индекс `VectorStoreIndex` из всех документов `self.documents`.
9. Если индекс существует, обновляет его, используя все документы `self.documents`.

**ASCII flowchart**:

```
Начало
  ↓
Проверка: len(new_documents) > 0
  ├── True:
  │   ↓
  │   self.documents += new_documents
  │   ↓
  │   Перебор документов в new_documents
  │   │
  │   └──Для каждого документа:
  │       ↓
  │       Очистка текста: document.text = utils.sanitize_raw_string(document.text)
  │       ↓
  │       Если doc_to_name_func is not None:
  │       │   ↓
  │       │   Получение имени: name = doc_to_name_func(document)
  │       │   ↓
  │       │   Если name in self.name_to_document:
  │       │   │   ↓
  │       │   │   Добавление документа в self.name_to_document[name]
  │       │   │   ↓
  │       │   Иначе:
  │       │   │   ↓
  │       │   │   self.name_to_document[name] = [document]
  │       │   ↓
  │       Конец цикла
  │   ↓
  │   Проверка: self.index is None
  │   ├── True:
  │   │   ↓
  │   │   Создание индекса: self.index = VectorStoreIndex.from_documents(self.documents)
  │   │   ↓
  │   └── False:
  │       ↓
  │       Обновление индекса: self.index.refresh(self.documents)
  │   ↓
  └── False:
      ↓
      (Пропуск обработки документов)
  ↓
Конец
```

**Примеры**:
```python
#Пример вызова функции
#connector = BaseSemanticGroundingConnector(name="example")
#connector.add_documents(new_documents=["example document"], doc_to_name_func=lambda doc: "example_name")
```

### `LocalFilesGroundingConnector._post_init`

```python
def _post_init(self):
    """
    Эта функция будет запущена после __init__, поскольку класс имеет декоратор @post_init.
    Удобно разделять некоторые процессы инициализации, чтобы упростить десериализацию.
    """
    ...
```

**Назначение**:
Выполняет постобработку инициализации экземпляра класса `LocalFilesGroundingConnector`. Этот метод вызывается автоматически после завершения `__init__` благодаря декоратору `@post_init`. Он предназначен для выполнения задач инициализации, таких как загрузка путей к папкам, которые используются для заземления.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

**Как работает функция**:
1. Инициализирует атрибут `self.loaded_folders_paths` пустым списком.
2. Проверяет, существует ли атрибут `self.folders_paths` и, если он отсутствует или равен `None`, инициализирует его пустым списком.
3. Вызывает метод `self.add_folders` с аргументом `self.folders_paths` для добавления папок.

**ASCII flowchart**:

```
Начало
  ↓
Инициализация self.loaded_folders_paths = []
  ↓
Проверка наличия self.folders_paths и его инициализация, если отсутствует
  ↓
Вызов self.add_folders(self.folders_paths)
  ↓
Конец
```

**Примеры**:
```python
# Пример вызова метода _post_init (вызывается автоматически декоратором @post_init)
# connector = LocalFilesGroundingConnector(name="example")
# connector._post_init()
```

### `LocalFilesGroundingConnector.add_folders`

```python
def add_folders(self, folders_paths: list | None) -> None:
    """
    Добавляет путь к папке с файлами, используемыми для заземления.
    """
    ...
```

**Назначение**:
Добавляет список путей к папкам, которые будут использоваться для загрузки файлов и последующего "заземления" (grounding).

**Параметры**:
- `folders_paths` (list | None): Список путей к папкам. Если `None`, функция ничего не делает.

**Возвращает**:
- Отсутствует.

**Как работает функция**:
1. Проверяет, не является ли `folders_paths` равным `None`. Если да, функция завершает свою работу.
2. Если `folders_paths` не равен `None`, функция перебирает каждый `folder_path` в списке `folders_paths`.
3. Для каждого `folder_path` функция пытается добавить папку, вызвав метод `self.add_folder(folder_path)`.
4. Если во время добавления папки возникает исключение `FileNotFoundError` или `ValueError`, функция перехватывает исключение и выводит сообщение об ошибке, включая текущую рабочую директорию и предоставленный путь.

**ASCII flowchart**:

```
Начало
  ↓
Проверка: folders_paths is not None
  ├── True:
  │   ↓
  │   Перебор folder_path в folders_paths
  │   │
  │   └──Для каждого folder_path:
  │       ↓
  │       Попытка добавить папку: self.add_folder(folder_path)
  │       │
  │       └──Если возникает FileNotFoundError или ValueError:
  │           ↓
  │           Вывод сообщения об ошибке
  │           ↓
  │       Конец цикла
  │   ↓
  └── False:
      ↓
      (Пропуск обработки папок)
  ↓
Конец
```

**Примеры**:
```python
#Пример вызова функции
#connector = LocalFilesGroundingConnector(name="example")
#connector.add_folders(folders_paths=["/path/to/folder1", "/path/to/folder2"])
```

### `LocalFilesGroundingConnector.add_folder`

```python
def add_folder(self, folder_path: str) -> None:
    """
    Добавляет путь к папке с файлами, используемыми для заземления.
    """
    ...
```

**Назначение**:
Добавляет указанную папку для индексации файлов, используемых для "заземления" (grounding).

**Параметры**:
- `folder_path` (str): Путь к папке, которую необходимо добавить.

**Возвращает**:
- Отсутствует.

**Как работает функция**:
1. Проверяет, была ли уже загружена папка (`folder_path not in self.loaded_folders_paths`).
2. Если папка еще не загружена, помечает ее как загруженную с помощью `self._mark_folder_as_loaded(folder_path)`.
3. Использует `SimpleDirectoryReader` для загрузки данных из папки.
4. Вызывает `self.add_documents` для добавления загруженных файлов в индекс, передавая функцию `lambda doc: doc.metadata["file_name"]` для извлечения имени файла из метаданных документа.

**ASCII flowchart**:

```
Начало
  ↓
Проверка: folder_path not in self.loaded_folders_paths
  ├── True:
  │   ↓
  │   self._mark_folder_as_loaded(folder_path)
  │   ↓
  │   new_files = SimpleDirectoryReader(folder_path).load_data()
  │   ↓
  │   self.add_documents(new_files, lambda doc: doc.metadata["file_name"])
  │   ↓
  └── False:
      ↓
      (Пропуск обработки папки)
  ↓
Конец
```

**Примеры**:
```python
#Пример вызова функции
#connector = LocalFilesGroundingConnector(name="example")
#connector.add_folder(folder_path="/path/to/folder")
```

### `LocalFilesGroundingConnector.add_file_path`

```python
def add_file_path(self, file_path: str) -> None:
    """
    Adds a path to a file used for grounding.
    """
    ...
```

**Назначение**:
Добавляет путь к файлу, используемому для заземления.

**Параметры**:
- `file_path` (str): Путь к файлу, который нужно добавить.

**Возвращает**:
- Отсутствует.

**Как работает функция**:
1. Использует `SimpleDirectoryReader` для загрузки данных из файла.
2. Логирует добавление файла в индекс заземления с помощью `logger.debug(f"Adding the following file to grounding index: {new_files}")`.
3. Вызывает `self.add_documents` для добавления загруженных файлов в индекс, передавая функцию `lambda doc: doc.metadata["file_name"]` для извлечения имени файла из метаданных документа.

**ASCII flowchart**:

```
Начало
  ↓
new_files = SimpleDirectoryReader(input_files=[file_path]).load_data()
  ↓
logger.debug(f"Adding the following file to grounding index: {new_files}")
  ↓
self.add_documents(new_files, lambda doc: doc.metadata["file_name"])
  ↓
Конец
```

**Примеры**:
```python
#Пример вызова функции
#connector = LocalFilesGroundingConnector(name="example")
#connector.add_file_path(file_path="/path/to/file.txt")
```

### `LocalFilesGroundingConnector._mark_folder_as_loaded`

```python
def _mark_folder_as_loaded(self, folder_path: str) -> None:
    """
    Помечает папку как загруженную.
    """
    ...
```

**Назначение**:
Помечает указанную папку как загруженную, добавляя ее в списки `self.loaded_folders_paths` и `self.folders_paths`, если ее там еще нет.

**Параметры**:
- `folder_path` (str): Путь к папке, которую необходимо пометить как