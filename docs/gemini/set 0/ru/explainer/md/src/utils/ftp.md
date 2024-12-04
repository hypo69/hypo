```MD
# <input code>

```python
## \file hypotez/src/utils/ftp.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils 
	:platform: Windows, Unix
	:synopsis: interface for interacting with FTP servers
This module provides an interface for interacting with FTP servers. It includes functions to send, receive, and delete files from an FTP server.

** Purpose **:
Allows for sending media files (images, videos), spreadsheets, and other files to and from an FTP server. 

** Modules **:
- helpers (local): Local helper utilities for FTP operations.
- typing: Type hints for function parameters and return values.
- ftplib: Provides FTP protocol client capabilities.
- pathlib: For handling file system paths.

Functions:
    - `write`: Sends a file to an FTP server.
    - `read`: Retrieves a file from an FTP server.
    - `delete`: Deletes a file from an FTP server.
"""
MODE = 'dev'
from src.logger import logger
from typing import Union
import ftplib
from pathlib import Path

# Connection configuration (assumed to be defined elsewhere)
_connection = {
    'server': 'ftp.example.com',
    'port': 21,
    'user': 'username',
    'password': 'password'
}

def write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
    Sends a file to an FTP server.

    Args:
        source_file_path (str): The path of the file to be sent.
        dest_dir (str): The destination directory on the FTP server.
        dest_file_name (str): The name of the file on the FTP server.

    Returns:
        bool: True if the file is successfully sent, False otherwise.

    Example:
        >>> success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    # ... (same as in the code)
```

# <algorithm>

**Алгоритм работы модуля ftp.py:**

1. **Инициализация:** Модуль импортирует необходимые библиотеки (`ftplib`, `typing`, `pathlib`, `logger`). Определяет конфигурацию подключения к FTP серверу (`_connection`).

2. **Функция write():**
    * **Подключение:** Устанавливает соединение с FTP сервером с помощью `ftplib.FTP` используя данные из `_connection`. Обрабатывает исключение (`try...except`) при подключении.
    * **Изменение директории:** Переходит в указанный каталог на FTP сервере (`session.cwd(dest_dir)`). Обрабатывает исключение при переходе.
    * **Отправка файла:** Открывает локальный файл для чтения в бинарном режиме (`'rb'`). Использует `session.storbinary` для передачи файла на сервер. Возвращает `True` в случае успеха, `False` в случае ошибки.
    * **Закрытие сессии:** Закрывает сессию (`session.quit`) и обрабатывает возможные исключения.

3. **Функция read():**
    * **Подключение:**  Устанавливает соединение с FTP сервером аналогично `write()`.
    * **Изменение директории:** Переходит в указанный каталог на FTP сервере (`session.cwd(dest_dir)`). Обрабатывает исключение при переходе.
    * **Получение файла:** Открывает локальный файл для записи в бинарном режиме (`'wb'`). Использует `session.retrbinary` для получения файла с сервера. Сохраняет содержимое в локальный файл.
    * **Чтение файла:** Читает содержимое из локального файла и возвращает его. Возвращает `None` в случае ошибки.
    * **Закрытие сессии:** Закрывает сессию (`session.quit`) и обрабатывает возможные исключения.

4. **Функция delete():**
    * **Подключение:** Устанавливает соединение с FTP сервером аналогично `write()` и `read()`.
    * **Изменение директории:** Переходит в указанный каталог на FTP сервере (`session.cwd(dest_dir)`). Обрабатывает исключение при переходе.
    * **Удаление файла:** Удаляет файл с FTP сервера с помощью `session.delete(dest_file_name)`.
    * **Возврат:** Возвращает `True` при успешном удалении, `False` при ошибке.
    * **Закрытие сессии:** Закрывает сессию (`session.quit`) и обрабатывает возможные исключения.


# <mermaid>

```mermaid
graph TD
    A[ftp.py] --> B(write);
    B --> C{Подключение к FTP};
    C --Успешно-- --> D[session.cwd(dest_dir)];
    D --> E{Открыть локальный файл};
    E --> F[session.storbinary];
    F --Успешно-- --> G[Закрытие сессии];
    G --> H[Возврат True];
    C --Ошибка-- --> I[Лог ошибки];
    I --> J[Возврат False];
    
    A --> K(read);
    K --> C;
    F --Ошибка-- --> I;
    K --> L[session.retrbinary];
    L --> M{Открыть локальный файл};
    M --> N[Чтение файла];
    N --> O[Возврат содержимого файла];
    K --> J;
    G --> O;


    A --> P(delete);
    P --> C;
    P --> Q[session.delete];
    Q --Успешно-- --> G;
    Q --Ошибка-- --> I;
    
    subgraph "Внешние зависимости"
        C --> ftplib;
        E --> pathlib;
        F --> io;
        I --> src.logger;
    end

```


# <explanation>

**Импорты:**

- `from src.logger import logger`: Импортирует функцию логгирования из модуля `logger` в папке `src`.  Это указывает на зависимость от модуля `logger` в проекте `hypotez`.
- `from typing import Union`:  Импортирует тип данных `Union` из модуля `typing` для указания возможности возвращать различные типы данных (строку, байты, `None`).
- `import ftplib`: Импортирует модуль `ftplib`, необходимый для работы с протоколом FTP.
- `from pathlib import Path`: Импортирует класс `Path` из модуля `pathlib` для работы с путями к файлам.

**Классы:**

- Нет определенных классов в данном модуле.

**Функции:**

- `write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool`: Отправляет файл на FTP-сервер.
    - `source_file_path`: Путь к локальному файлу.
    - `dest_dir`: Каталог на FTP-сервере.
    - `dest_file_name`: Имя файла на FTP-сервере.
    - Возвращает `True`, если отправка успешна, `False` в противном случае.
- `read(source_file_path: str, dest_dir: str, dest_file_name: str) -> Union[str, bytes, None]`: Загружает файл с FTP-сервера.
    - Аргументы такие же, как в `write`.
    - Возвращает содержимое файла, если загрузка успешна, иначе `None`.
- `delete(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool`: Удаляет файл с FTP-сервера.
    - Аргументы такие же, как в `write`.
    - Возвращает `True`, если удаление прошло успешно, `False` в противном случае.


**Переменные:**

- `_connection`: Словарь с настройками подключения к FTP-серверу.  Важно, что этот словарь не хранится в модуле `ftp.py`, а импортируется в него извне (в данном случае, предполагается, что он определен в другом месте, например, в файле настроек).

**Возможные ошибки и улучшения:**

- **Отсутствует валидация ввода:**  Функции принимают пути и имена файлов без проверки их корректности.  Необходимо проверить, что `source_file_path` существует, а `dest_dir` и `dest_file_name` имеют допустимые значения.
- **Нет обработки ошибок:** Нехватка проверки на существующие каталоги, или отказ доступа.
- **Оптимизация:** Отдельный блок `finally` для закрытия сессии выглядит избыточным. Можно объединить обработку ошибок с закрытием сессии.
- **Статические методы:** Возможно, `_connection` лучше сделать статическими атрибутами класса, если он будет использоваться в других частях проекта.

**Цепочка взаимосвязей:**

Модуль `ftp.py` зависит от модуля `src.logger` для логгирования ошибок.  Также он зависит от конфигурации подключения, хранящейся вне данного модуля.  Этот модуль, вероятно, используется другими частями проекта для взаимодействия с FTP-сервером.