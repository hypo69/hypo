# Модуль mega.py

## Обзор

Модуль `mega.py` предоставляет класс `Mega` для взаимодействия с сервисом Mega.co.nz. Он включает функциональность для входа в систему, получения списка файлов, скачивания и загрузки файлов. Модуль использует различные криптографические методы для обеспечения безопасности данных.

## Подробней

Этот модуль позволяет автоматизировать взаимодействие с сервисом Mega, включая аутентификацию, управление файлами и передачу данных. Он использует криптографические методы, такие как AES и RSA, для защиты данных при передаче и хранении.

## Классы

### `Mega`

**Описание**: Класс для взаимодействия с сервисом Mega.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `Mega`.
- `from_credentials`: Создает экземпляр класса `Mega` с использованием email и пароля.
- `from_ephemeral`: Создает экземпляр класса `Mega` для анонимного входа.
- `api_req`: Выполняет API-запрос к сервису Mega.
- `login_user`: Аутентифицирует пользователя с использованием email и пароля.
- `login_ephemeral`: Выполняет анонимный вход в систему.
- `_login_common`: Общая логика для входа в систему.
- `get_files`: Получает список файлов пользователя.
- `download_from_url`: Загружает файл из публичного URL.
- `download_file`: Загружает файл по его ID и ключу.
- `get_public_url`: Возвращает публичный URL файла.
- `uploadfile`: Загружает файл в облачное хранилище.

#### `__init__`

```python
    def __init__(self):
        """
        Инициализирует экземпляр класса Mega.

        Args:
            self (Mega): Экземпляр класса Mega.

        Returns:
            None

        Raises:
            None
        """
        ...
```

**Описание**: Инициализирует экземпляр класса `Mega`, устанавливая начальное значение для номера последовательности и идентификатора сессии.

#### `from_credentials`

```python
    @classmethod
    def from_credentials(cls, email: str, password: str) -> 'Mega':
        """
        Создает экземпляр класса Mega с использованием email и пароля.

        Args:
            cls (Mega): Класс Mega.
            email (str): Email пользователя.
            password (str): Пароль пользователя.

        Returns:
            Mega: Экземпляр класса Mega.

        Raises:
            None
        """
        ...
```

**Описание**: Создает экземпляр класса `Mega` и выполняет вход в систему с использованием предоставленных email и пароля.

#### `from_ephemeral`

```python
    @classmethod
    def from_ephemeral(cls) -> 'Mega':
        """
        Создает экземпляр класса Mega для анонимного входа.

        Args:
            cls (Mega): Класс Mega.

        Returns:
            Mega: Экземпляр класса Mega.

        Raises:
            None
        """
        ...
```

**Описание**: Создает экземпляр класса `Mega` и выполняет анонимный вход в систему.

#### `api_req`

```python
    def api_req(self, data: dict) -> dict:
        """
        Выполняет API-запрос к сервису Mega.

        Args:
            data (dict): Данные запроса в формате словаря.

        Returns:
            dict: Ответ от API в формате словаря.

        Raises:
            MegaRequestException: Если API возвращает код ошибки.
        """
        ...
```

**Описание**: Выполняет API-запрос к сервису Mega, добавляя параметры идентификации и сессии, а также обрабатывая возможные ошибки.

#### `login_user`

```python
    def login_user(self, email: str, password: str):
        """
        Аутентифицирует пользователя с использованием email и пароля.

        Args:
            email (str): Email пользователя.
            password (str): Пароль пользователя.

        Returns:
            None

        Raises:
            MegaIncorrectPasswordExcetion: Если введен неверный email или пароль.
        """
        ...
```

**Описание**: Аутентифицирует пользователя, подготавливая ключ пароля и выполняя API-запрос для входа в систему.

#### `login_ephemeral`

```python
    def login_ephemeral(self):
        """
        Выполняет анонимный вход в систему.

        Args:
            None

        Returns:
            None

        Raises:
            MegaRequestException: Если API возвращает код ошибки.
        """
        ...
```

**Описание**: Выполняет анонимный вход в систему, генерируя случайные ключи и выполняя API-запросы для получения пользовательского идентификатора.

#### `_login_common`

```python
    def _login_common(self, res: dict, password: list[int]):
        """
        Общая логика для входа в систему.

        Args:
            res (dict): Ответ от API с данными для входа.
            password (list[int]): Ключ пароля.

        Returns:
            None

        Raises:
            MegaIncorrectPasswordExcetion: Если введен неверный email или пароль.
        """
        ...
```

**Описание**: Общая логика для завершения процесса входа в систему, включающая расшифровку мастер-ключа и установку идентификатора сессии.

#### `get_files`

```python
    def get_files(self) -> dict:
        """
        Получает список файлов пользователя.

        Args:
            None

        Returns:
            dict: Данные о файлах пользователя.

        Raises:
            MegaRequestException: Если API возвращает код ошибки.
        """
        ...
```

**Описание**: Получает список файлов и каталогов пользователя, расшифровывая ключи и атрибуты файлов.

#### `download_from_url`

```python
    def download_from_url(self, url: str) -> str:
        """
        Загружает файл из публичного URL.

        Args:
            url (str): Публичный URL файла.

        Returns:
            str: Имя загруженного файла.

        Raises:
            MegaRequestException: Если API возвращает код ошибки.
        """
        ...
```

**Описание**: Загружает файл из публичного URL, извлекая идентификатор файла и ключ из URL.

#### `download_file`

```python
    def download_file(self, file_id: str, file_key: str, public: bool = False, store_path: Optional[str] = None) -> str:
        """
        Загружает файл по его ID и ключу.

        Args:
            file_id (str): Идентификатор файла.
            file_key (str): Ключ файла.
            public (bool, optional): Флаг, указывающий, является ли файл публичным. По умолчанию False.
            store_path (Optional[str], optional): Путь для сохранения файла. По умолчанию None.

        Returns:
            str: Имя загруженного файла.

        Raises:
            MegaRequestException: Если API возвращает код ошибки.
            ValueError: Если MAC не совпадает.
        """
        ...
```

**Описание**: Загружает файл по его ID и ключу, расшифровывая содержимое файла и проверяя его целостность.

#### `get_public_url`

```python
    def get_public_url(self, file_id: str, file_key: list[int]) -> str:
        """
        Возвращает публичный URL файла.

        Args:
            file_id (str): Идентификатор файла.
            file_key (list[int]): Ключ файла.

        Returns:
            str: Публичный URL файла.

        Raises:
            MegaRequestException: Если API возвращает код ошибки.
        """
        ...
```

**Описание**: Возвращает публичный URL файла, комбинируя идентификатор файла и зашифрованный ключ.

#### `uploadfile`

```python
    def uploadfile(self, filename: str, dst: Optional[str] = None) -> dict:
        """
        Загружает файл в облачное хранилище.

        Args:
            filename (str): Путь к файлу для загрузки.
            dst (Optional[str], optional): Идентификатор целевого каталога. По умолчанию None.

        Returns:
            dict: Данные о загруженном файле.

        Raises:
            MegaRequestException: Если API возвращает код ошибки.
        """
        ...
```

**Описание**: Загружает файл в облачное хранилище, шифруя содержимое файла и отправляя его на сервер.

## Функции

### `aes_cbc_encrypt_a32`

```python
def aes_cbc_encrypt_a32(chunk_mac: list[int], ul_key: list[int]) -> list[int]:
    """
    Шифрует блок данных с использованием AES в режиме CBC.

    Args:
        chunk_mac (list[int]): Блок данных для шифрования.
        ul_key (list[int]): Ключ шифрования.

    Returns:
        list[int]: Зашифрованный блок данных.
    """
```

**Описание**: Шифрует блок данных с использованием AES в режиме CBC.

**Параметры**:

- `chunk_mac` (list[int]): Блок данных для шифрования.
- `ul_key` (list[int]): Ключ шифрования.

**Возвращает**:

- `list[int]`: Зашифрованный блок данных.