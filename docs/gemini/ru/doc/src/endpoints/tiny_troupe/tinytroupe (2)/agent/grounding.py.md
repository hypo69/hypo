# Модуль для работы с коннекторами заземления (grounding connectors)
=================================================================

Модуль содержит классы для подключения к различным источникам знаний, таким как файлы, веб-страницы и т.д., чтобы агент мог обосновывать свои знания на основе этих внешних источников.

## Обзор

Этот модуль предоставляет абстрактный класс `GroundingConnector` и его реализации для семантического поиска `BaseSemanticGroundingConnector`, локальных файлов `LocalFilesGroundingConnector` и веб-страниц `WebPagesGroundingConnector`. Он использует библиотеку `llama_index` для индексации и поиска документов.

## Подробней

Модуль предназначен для расширения возможностей агента, позволяя ему извлекать информацию из различных источников и использовать её для обоснования своих ответов и действий. Это достигается путем создания коннекторов, которые индексируют и извлекают документы на основе семантического поиска или других методов.

## Классы

### `GroundingConnector`

**Описание**: Абстрактный класс, представляющий коннектор заземления. Коннектор заземления - это компонент, который позволяет агенту обосновывать свои знания во внешних источниках, таких как файлы, веб-страницы, базы данных и т.д.

**Атрибуты**:
- `name` (str): Имя коннектора заземления.

**Методы**:
- `retrieve_relevant(relevance_target: str, source: str, top_k: int = 20) -> list`: Извлекает релевантные значения из источника на основе цели релевантности.
- `retrieve_by_name(name: str) -> str`: Извлекает источник контента по его имени.
- `list_sources() -> list`: Перечисляет имена доступных источников контента.

### `BaseSemanticGroundingConnector(GroundingConnector)`

**Описание**: Базовый класс для семантических коннекторов заземления. Семантический коннектор заземления - это компонент, который индексирует и извлекает документы на основе так называемого "семантического поиска" (т.е. поиска на основе вложений). Эта конкретная реализация основана на классе `VectorStoreIndex` из библиотеки `LLaMa-Index`. Здесь "документы" относятся к структуре данных llama-index, которая хранит единицу контента, не обязательно файл.

**Наследует**:
- `GroundingConnector`: Наследует атрибуты и методы класса `GroundingConnector`.

**Атрибуты**:
- `documents` (list): Список документов для индексации.
- `name_to_document` (dict): Словарь, отображающий имена документов на сами документы.
- `index`: Индекс для семантического поиска.

**Методы**:

- `__init__(self, name: str = "Semantic Grounding") -> None`:
    ```python
    def __init__(self, name: str = "Semantic Grounding") -> None:
        """
        Args:
            name (str, optional): Имя коннектора заземления. По умолчанию "Semantic Grounding".
        """
    ```
- `_post_init(self) -> None`:
    ```python
    def _post_init(self) -> None:
        """
        Выполняется после __init__, так как у класса есть декоратор @post_init.
        Удобно разделять некоторые процессы инициализации, чтобы упростить десериализацию.
        """
    ```
- `retrieve_relevant(self, relevance_target: str, top_k: int = 20) -> list`:
    ```python
    def retrieve_relevant(self, relevance_target: str, top_k: int = 20) -> list:
        """
        Извлекает все значения из памяти, которые релевантны данной цели.

        Args:
            relevance_target (str): Цель релевантности.
            top_k (int, optional): Количество извлекаемых результатов. По умолчанию 20.

        Returns:
            list: Список извлеченных контентов.
        """
    ```

    **Как работает функция**:
     1. Проверяет, инициализирован ли индекс (`self.index`).
     2. Если индекс существует, создает объект `retriever` на основе индекса с указанием количества извлекаемых результатов (`top_k`).
     3. Выполняет поиск по индексу, используя `relevance_target` в качестве запроса. Результаты поиска сохраняются в переменной `nodes`.
     4. Если индекс не существует, `nodes` инициализируется пустым списком.
     5. Итерируется по каждому узлу (`node`) в `nodes`.
     6. Для каждого `node` формирует строку `content`, включающую источник (`file_name`), оценку схожести (`score`) и релевантный контент (`text`).
     7. Добавляет `content` в список `retrieved`.
     8. Логирует первые 200 символов извлеченного контента с использованием `logger.debug`.
     9. Возвращает список `retrieved`.

    ```
    Начало
    │
    ├── Проверка: self.index is not None
    │   ├── Да: Создание retriever
    │   │   │
    │   │   └── Поиск: retriever.retrieve(relevance_target)
    │   │       │
    │   │       └── Сохранение результатов в nodes
    │   │
    │   └── Нет: nodes = []
    │
    └── Итерация по nodes
        │
        └── Формирование content для каждого node
            │
            └── Добавление content в retrieved
                │
                └── Логирование content
                    │
                    └── Возврат retrieved
                        │
                        Конец
    ```

    **Примеры**:

    ```python
    # Пример вызова функции retrieve_relevant
    connector = BaseSemanticGroundingConnector()
    connector._post_init()  # Необходимо вызвать для инициализации index
    connector.add_document(Document(text="Example document", metadata={"file_name": "example.txt"}))
    relevant_content = connector.retrieve_relevant("example", top_k=1)
    print(relevant_content)  # Вывод: ['SOURCE: example.txt\nSIMILARITY SCORE:...\nRELEVANT CONTENT:Example document']
    ```
- `retrieve_by_name(self, name: str) -> list`:
    ```python
    def retrieve_by_name(self, name: str) -> list:
        """
        Извлекает источник контента по его имени.

        Args:
            name (str): Имя источника контента.

        Returns:
            list: Список извлеченных контентов.
        """
    ```
- `list_sources(self) -> list`:
    ```python
    def list_sources(self) -> list:
        """
        Перечисляет имена доступных источников контента.

        Returns:
            list: Список имен источников контента.
        """
    ```
- `add_document(self, document, doc_to_name_func=None) -> None`:
    ```python
    def add_document(self, document, doc_to_name_func=None) -> None:
        """
        Индексирует документ для семантического поиска.

        Args:
            document: Документ для индексации.
            doc_to_name_func: Функция для извлечения имени документа.
        """
    ```
- `add_documents(self, new_documents, doc_to_name_func=None) -> list`:
    ```python
    def add_documents(self, new_documents, doc_to_name_func=None) -> list:
        """
        Индексирует документы для семантического поиска.

        Args:
            new_documents: Список документов для индексации.
            doc_to_name_func: Функция для извлечения имени документа.

        Returns:
            list: Список добавленных документов.
        """
    ```

### `LocalFilesGroundingConnector(BaseSemanticGroundingConnector)`

**Описание**: Класс для подключения к локальным файлам в качестве источника знаний.

**Наследует**:
- `BaseSemanticGroundingConnector`: Наследует атрибуты и методы класса `BaseSemanticGroundingConnector`.

**Атрибуты**:
- `folders_paths` (list): Список путей к папкам с файлами.
- `loaded_folders_paths` (list): Список путей к уже загруженным папкам.

**Методы**:
- `__init__(self, name: str = "Local Files", folders_paths: list = None) -> None`:
    ```python
    def __init__(self, name: str = "Local Files", folders_paths: list = None) -> None:
        """
        Args:
            name (str, optional): Имя коннектора заземления. По умолчанию "Local Files".
            folders_paths (list, optional): Список путей к папкам с файлами. По умолчанию None.
        """
    ```
- `_post_init(self) -> None`:
    ```python
    def _post_init(self) -> None:
        """
        Выполняется после __init__, так как у класса есть декоратор @post_init.
        Удобно разделять некоторые процессы инициализации, чтобы упростить десериализацию.
        """
    ```
- `add_folders(self, folders_paths: list) -> None`:
    ```python
    def add_folders(self, folders_paths: list) -> None:
        """
        Добавляет путь к папке с файлами, используемыми для заземления.

        Args:
            folders_paths (list): Список путей к папкам.
        """
    ```
- `add_folder(self, folder_path: str) -> None`:
    ```python
    def add_folder(self, folder_path: str) -> None:
        """
        Добавляет путь к папке с файлами, используемыми для заземления.

        Args:
            folder_path (str): Путь к папке.
        """
    ```
- `add_file_path(self, file_path: str) -> None`:
    ```python
    def add_file_path(self, file_path: str) -> None:
        """
        Добавляет путь к файлу, используемому для заземления.

        Args:
            file_path (str): Путь к файлу.
        """
    ```
- `_mark_folder_as_loaded(self, folder_path: str) -> None`:
    ```python
    def _mark_folder_as_loaded(self, folder_path: str) -> None:
        """
        Помечает папку как загруженную.

        Args:
            folder_path (str): Путь к папке.
        """
    ```

### `WebPagesGroundingConnector(BaseSemanticGroundingConnector)`

**Описание**: Класс для подключения к веб-страницам в качестве источника знаний.

**Наследует**:
- `BaseSemanticGroundingConnector`: Наследует атрибуты и методы класса `BaseSemanticGroundingConnector`.

**Атрибуты**:
- `web_urls` (list): Список URL-адресов веб-страниц.
- `loaded_web_urls` (list): Список уже загруженных URL-адресов.

**Методы**:
- `__init__(self, name: str = "Web Pages", web_urls: list = None) -> None`:
    ```python
    def __init__(self, name: str = "Web Pages", web_urls: list = None) -> None:
        """
        Args:
            name (str, optional): Имя коннектора заземления. По умолчанию "Web Pages".
            web_urls (list, optional): Список URL-адресов веб-страниц. По умолчанию None.
        """
    ```
- `_post_init(self) -> None`:
    ```python
    def _post_init(self) -> None:
        """
        Выполняется после __init__, так как у класса есть декоратор @post_init.
        Удобно разделять некоторые процессы инициализации, чтобы упростить десериализацию.
        """
    ```
- `add_web_urls(self, web_urls: list) -> None`:
    ```python
    def add_web_urls(self, web_urls: list) -> None:
        """
        Добавляет данные, полученные с указанных URL-адресов, в заземление.

        Args:
            web_urls (list): Список URL-адресов.
        """
    ```
- `add_web_url(self, web_url: str) -> None`:
    ```python
    def add_web_url(self, web_url: str) -> None:
        """
        Добавляет данные, полученные с указанного URL-адреса, в заземление.

        Args:
            web_url (str): URL-адрес.
        """
    ```
- `_mark_web_url_as_loaded(self, web_url: str) -> None`:
    ```python
    def _mark_web_url_as_loaded(self, web_url: str) -> None:
        """
        Помечает URL-адрес как загруженный.

        Args:
            web_url (str): URL-адрес.
        """
    ```

## Функции

В модуле нет отдельных функций, все основные операции выполняются через методы классов.