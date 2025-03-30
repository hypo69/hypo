# Модуль для работы с Mega.nz
## Обзор
Модуль `mega.py` предоставляет класс `Mega` для взаимодействия с сервисом Mega.nz. Он включает в себя функции для аутентификации, скачивания и загрузки файлов, а также для работы с публичными ссылками.

## Подробней

Этот модуль позволяет выполнять различные операции с Mega.nz, такие как вход в систему с использованием email и пароля, создание эфемерных сессий, получение списка файлов, скачивание файлов по URL и загрузка файлов на сервер. Он использует криптографические методы для обеспечения безопасности передаваемых данных.

## Классы

### `Mega`

**Описание**: Класс для взаимодействия с API Mega.nz.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Mega`.
- `from_credentials`: Создает экземпляр класса `Mega` с использованием email и пароля.
- `from_ephemeral`: Создает экземпляр класса `Mega` для эфемерной сессии.
- `api_req`: Выполняет API-запрос к серверу Mega.nz.
- `login_user`: Выполняет вход в систему с использованием email и пароля.
- `login_ephemeral`: Выполняет вход в систему для эфемерной сессии.
- `_login_common`: Общий метод для обработки результатов входа в систему.
- `get_files`: Получает список файлов и папок из облачного хранилища.
- `download_from_url`: Скачивает файл по публичной ссылке.
- `download_file`: Скачивает файл из Mega.nz.
- `get_public_url`: Получает публичную ссылку на файл.
- `uploadfile`: Загружает файл на Mega.nz.

**Параметры**:
- `seqno` (int): Уникальный идентификатор запроса.
- `sid` (str): Идентификатор сессии.
- `master_key` (list[int]): Главный ключ для шифрования данных.
- `rsa_priv_key` (list[int]): Приватный RSA-ключ для расшифровки данных.
- `root_id` (str): Идентификатор корневой папки.
- `inbox_id` (str): Идентификатор папки входящих сообщений.
- `trashbin_id` (str): Идентификатор корзины.

**Примеры**
```python
# Пример создания экземпляра класса Mega и входа в систему с использованием email и пароля
mega = Mega.from_credentials('email@example.com', 'password')

# Пример получения списка файлов
files = mega.get_files()

# Пример скачивания файла по публичной ссылке
file_name = mega.download_from_url('https://mega.nz/#!file_id!file_key')

# Пример загрузки файла на сервер
data = mega.uploadfile('filename')
```

## Функции

### `__init__`

```python
def __init__(self):
    """
    Args:
        self (Mega): Экземпляр класса `Mega`.
    
    Returns:
        None
    
    Raises:
        None
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `Mega`, устанавливая начальные значения для `seqno` и `sid`.

**Параметры**:
- `self` (Mega): Экземпляр класса `Mega`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
mega = Mega()
```

### `from_credentials`

```python
def from_credentials(cls, email: str, password: str) -> Mega:
    """
    Args:
        cls (Mega): Класс `Mega`.
        email (str): Email пользователя.
        password (str): Пароль пользователя.
    
    Returns:
        Mega: Экземпляр класса `Mega`.
    
    Raises:
        None
    """
    ...
```

**Описание**: Создает экземпляр класса `Mega` и выполняет вход в систему с использованием предоставленных email и пароля.

**Параметры**:
- `cls` (Mega): Класс `Mega`.
- `email` (str): Email пользователя.
- `password` (str): Пароль пользователя.

**Возвращает**:
- `Mega`: Экземпляр класса `Mega`.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
mega = Mega.from_credentials('email@example.com', 'password')
```

### `from_ephemeral`

```python
def from_ephemeral(cls) -> Mega:
    """
    Args:
        cls (Mega): Класс `Mega`.
    
    Returns:
        Mega: Экземпляр класса `Mega`.
    
    Raises:
        None
    """
    ...
```

**Описание**: Создает экземпляр класса `Mega` для эфемерной сессии (без использования email и пароля).

**Параметры**:
- `cls` (Mega): Класс `Mega`.

**Возвращает**:
- `Mega`: Экземпляр класса `Mega`.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
mega = Mega.from_ephemeral()
```

### `api_req`

```python
def api_req(self, data: dict) -> dict:
    """
    Args:
        self (Mega): Экземпляр класса `Mega`.
        data (dict): Словарь с данными для отправки в API-запросе.
    
    Returns:
        dict: Ответ от API в формате словаря.
    
    Raises:
        MegaRequestException: Если API возвращает код ошибки.
    """
    ...
```

**Описание**: Отправляет API-запрос к серверу Mega.nz и возвращает ответ в формате словаря.

**Параметры**:
- `self` (Mega): Экземпляр класса `Mega`.
- `data` (dict): Словарь с данными для отправки в API-запросе.

**Возвращает**:
- `dict`: Ответ от API в формате словаря.

**Вызывает исключения**:
- `MegaRequestException`: Если API возвращает код ошибки.

**Примеры**:
```python
data = mega.api_req({'a': 'f', 'c': 1})
```

### `login_user`

```python
def login_user(self, email: str, password: str) -> None:
    """
    Args:
        self (Mega): Экземпляр класса `Mega`.
        email (str): Email пользователя.
        password (str): Пароль пользователя.
    
    Returns:
        None
    
    Raises:
        MegaIncorrectPasswordExcetion: Если указан неверный email или пароль.
    """
    ...
```

**Описание**: Выполняет вход в систему с использованием предоставленных email и пароля.

**Параметры**:
- `self` (Mega): Экземпляр класса `Mega`.
- `email` (str): Email пользователя.
- `password` (str): Пароль пользователя.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `MegaIncorrectPasswordExcetion`: Если указан неверный email или пароль.

**Примеры**:
```python
mega = Mega()
mega.login_user('email@example.com', 'password')
```

### `login_ephemeral`

```python
def login_ephemeral(self) -> None:
    """
    Args:
        self (Mega): Экземпляр класса `Mega`.
    
    Returns:
        None
    
    Raises:
        None
    """
    ...
```

**Описание**: Выполняет вход в систему для эфемерной сессии (без использования email и пароля).

**Параметры**:
- `self` (Mega): Экземпляр класса `Mega`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
mega = Mega()
mega.login_ephemeral()
```

### `_login_common`

```python
def _login_common(self, res: dict, password: list[int]) -> None:
    """
    Args:
        self (Mega): Экземпляр класса `Mega`.
        res (dict): Ответ от API с данными для входа.
        password (list[int]): Ключ пароля.
    
    Returns:
        None
    
    Raises:
        MegaIncorrectPasswordExcetion: Если указан неверный email или пароль.
    """
    ...
```

**Описание**: Общий метод для обработки результатов входа в систему, расшифровки ключей и установки идентификатора сессии.

**Параметры**:
- `self` (Mega): Экземпляр класса `Mega`.
- `res` (dict): Ответ от API с данными для входа.
- `password` (list[int]): Ключ пароля.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `MegaIncorrectPasswordExcetion`: Если указан неверный email или пароль.

**Примеры**:
```python
# Пример использования внутри методов login_user и login_ephemeral
```

### `get_files`

```python
def get_files(self) -> dict:
    """
    Args:
        self (Mega): Экземпляр класса `Mega`.
    
    Returns:
        dict: Данные о файлах.
    
    Raises:
        None
    """
    ...
```

**Описание**: Получает список файлов и папок из облачного хранилища.

**Параметры**:
- `self` (Mega): Экземпляр класса `Mega`.

**Возвращает**:
- `dict`: Словарь с данными о файлах и папках.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
files = mega.get_files()
```

### `download_from_url`

```python
def download_from_url(self, url: str) -> str:
    """
    Args:
        self (Mega): Экземпляр класса `Mega`.
        url (str): URL файла для скачивания.
    
    Returns:
        str: Имя скаченного файла.
    
    Raises:
        None
    """
    ...
```

**Описание**: Скачивает файл по публичной ссылке.

**Параметры**:
- `self` (Mega): Экземпляр класса `Mega`.
- `url` (str): URL файла для скачивания.

**Возвращает**:
- `str`: Имя скаченного файла.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
file_name = mega.download_from_url('https://mega.nz/#!file_id!file_key')
```

### `download_file`

```python
def download_file(self, file_id: str, file_key: str, public: bool = False, store_path: Optional[str] = None) -> str:
    """
    Args:
        self (Mega): Экземпляр класса `Mega`.
        file_id (str): ID файла для скачивания.
        file_key (str): Ключ файла для скачивания.
        public (bool): Является ли файл публичным. По умолчанию `False`.
        store_path (Optional[str]): Путь для сохранения файла. По умолчанию `None`.
    
    Returns:
        str: Имя скаченного файла.
    
    Raises:
        ValueError: Если MAC не совпадает.
    """
    ...
```

**Описание**: Скачивает файл из Mega.nz.

**Параметры**:
- `self` (Mega): Экземпляр класса `Mega`.
- `file_id` (str): ID файла для скачивания.
- `file_key` (str): Ключ файла для скачивания.
- `public` (bool): Является ли файл публичным. По умолчанию `False`.
- `store_path` (Optional[str]): Путь для сохранения файла. По умолчанию `None`.

**Возвращает**:
- `str`: Имя скаченного файла.

**Вызывает исключения**:
- `ValueError`: Если MAC не совпадает.

**Примеры**:
```python
file_name = mega.download_file('file_id', 'file_key', public=True, store_path='/path/to/store')
```

### `get_public_url`

```python
def get_public_url(self, file_id: str, file_key: list[int]) -> str:
    """
    Args:
        self (Mega): Экземпляр класса `Mega`.
        file_id (str): ID файла.
        file_key (list[int]): Ключ файла.
    
    Returns:
        str: Публичный URL файла.
    
    Raises:
        None
    """
    ...
```

**Описание**: Получает публичную ссылку на файл.

**Параметры**:
- `self` (Mega): Экземпляр класса `Mega`.
- `file_id` (str): ID файла.
- `file_key` (list[int]): Ключ файла.

**Возвращает**:
- `str`: Публичный URL файла.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
public_url = mega.get_public_url('file_id', [1, 2, 3, 4, 5, 6, 7, 8])
```

### `uploadfile`

```python
def uploadfile(self, filename: str, dst: Optional[str] = None) -> dict:
    """
    Args:
        self (Mega): Экземпляр класса `Mega`.
        filename (str): Имя файла для загрузки.
        dst (Optional[str]): ID папки назначения. По умолчанию `None`.
    
    Returns:
        dict: Данные о загруженном файле.
    
    Raises:
        None
    """
    ...
```

**Описание**: Загружает файл на Mega.nz.

**Параметры**:
- `self` (Mega): Экземпляр класса `Mega`.
- `filename` (str): Имя файла для загрузки.
- `dst` (Optional[str]): ID папки назначения. По умолчанию `None`.

**Возвращает**:
- `dict`: Данные о загруженном файле.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
data = mega.uploadfile('filename', dst='destination_folder_id')