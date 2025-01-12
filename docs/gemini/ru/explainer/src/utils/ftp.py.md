## <алгоритм>

**1. Функция `write(source_file_path, dest_dir, dest_file_name)`:**

   *   **Начало:** Функция принимает путь к локальному файлу (`source_file_path`), удаленную директорию (`dest_dir`) и имя файла на FTP (`dest_file_name`).
   *   **Подключение к FTP:**
        *   Пытается установить соединение с FTP-сервером, используя параметры из глобальной переменной `_connection`.
        *   Если соединение не установлено, записывается ошибка в лог и функция возвращает `False`.
   *   **Переход в директорию:**
        *   Переходит в указанную директорию `dest_dir` на FTP-сервере.
   *   **Отправка файла:**
        *   Открывает локальный файл `source_file_path` в двоичном режиме для чтения (`'rb'`).
        *   Отправляет содержимое файла на FTP-сервер с именем `dest_file_name` с помощью `session.storbinary`.
        *   Если отправка успешна, функция возвращает `True`.
        *   В случае ошибки при отправке файла, записывается ошибка в лог и функция возвращает `False`.
   *   **Закрытие соединения:**
        *   В блоке `finally` всегда пытается закрыть соединение с FTP-сервером. Если закрытие не удалось, то ошибка записывается в лог.
   *   **Конец:** Функция возвращает `True` при успешной отправке файла, в противном случае `False`.

**Пример использования `write`:**

1.  `source_file_path = 'my_image.jpg'`, `dest_dir = '/images'`, `dest_file_name = 'new_image.jpg'`.
2.  Устанавливается FTP соединение.
3.  Файл `my_image.jpg` отправляется в директорию `/images` на FTP сервере с именем `new_image.jpg`.
4.  Если всё успешно, возвращается `True`.

**2. Функция `read(source_file_path, dest_dir, dest_file_name)`:**

   *   **Начало:** Функция принимает локальный путь для сохранения файла (`source_file_path`), удаленную директорию (`dest_dir`) и имя файла на FTP (`dest_file_name`).
   *   **Подключение к FTP:**
        *   Пытается установить соединение с FTP-сервером, используя параметры из глобальной переменной `_connection`.
        *   Если соединение не установлено, записывается ошибка в лог и функция возвращает `None`.
   *  **Переход в директорию:**
        *   Переходит в указанную директорию `dest_dir` на FTP-сервере.
   *   **Получение файла:**
        *   Создаёт (или перезаписывает) локальный файл `source_file_path` в двоичном режиме для записи (`'wb'`).
        *   Записывает содержимое файла, полученного с FTP-сервера, в локальный файл с помощью `session.retrbinary`
        *   Открывает локальный файл `source_file_path` в двоичном режиме для чтения (`'rb'`).
        *   Возвращает содержимое файла.
        *   Если получение файла не удалось, записывается ошибка в лог и функция возвращает `None`.
   *   **Закрытие соединения:**
        *   В блоке `finally` всегда пытается закрыть соединение с FTP-сервером. Если закрытие не удалось, то ошибка записывается в лог.
   *   **Конец:** Функция возвращает содержимое полученного файла или `None` в случае ошибки.

**Пример использования `read`:**

1.  `source_file_path = 'downloaded_file.txt'`, `dest_dir = '/docs'`, `dest_file_name = 'remote_file.txt'`.
2.  Устанавливается FTP соединение.
3.  Содержимое файла `remote_file.txt` с FTP сервера сохраняется в `downloaded_file.txt`.
4.  Возвращается содержимое `downloaded_file.txt`.

**3. Функция `delete(source_file_path, dest_dir, dest_file_name)`:**

   *   **Начало:** Функция принимает путь к локальному файлу (`source_file_path`, не используется), удаленную директорию (`dest_dir`) и имя файла на FTP (`dest_file_name`).
   *   **Подключение к FTP:**
        *   Пытается установить соединение с FTP-сервером, используя параметры из глобальной переменной `_connection`.
        *   Если соединение не установлено, записывается ошибка в лог и функция возвращает `False`.
   *   **Переход в директорию:**
        *   Переходит в указанную директорию `dest_dir` на FTP-сервере.
   *   **Удаление файла:**
        *   Удаляет файл с именем `dest_file_name` на FTP-сервере с помощью `session.delete`.
        *   Если удаление успешно, функция возвращает `True`.
        *   В случае ошибки, записывается ошибка в лог и функция возвращает `False`.
   *   **Закрытие соединения:**
        *   В блоке `finally` всегда пытается закрыть соединение с FTP-сервером. Если закрытие не удалось, то ошибка записывается в лог.
   *   **Конец:** Функция возвращает `True` при успешном удалении файла, в противном случае `False`.

**Пример использования `delete`:**

1.  `source_file_path = 'local_dummy.txt'`, `dest_dir = '/archive'`, `dest_file_name = 'old_file.txt'`.
2.  Устанавливается FTP соединение.
3.  Файл `old_file.txt` удаляется из директории `/archive` на FTP сервере.
4.  Если всё успешно, возвращается `True`.

## <mermaid>

```mermaid
flowchart TD
    Start_Write[Start: write()] --> Connect_Write{Connect to FTP Server}
    Connect_Write -- Success --> ChangeDir_Write[Change Directory on FTP]
    Connect_Write -- Fail --> LogError_Write[Log Error: Connection Failed]
    LogError_Write --> ReturnFalse_Write[Return False]
    ChangeDir_Write --> OpenFile_Write[Open Local File (Read Binary)]
    OpenFile_Write --> SendFile_Write[Send File to FTP Server]
    SendFile_Write -- Success --> ReturnTrue_Write[Return True]
    SendFile_Write -- Fail --> LogError2_Write[Log Error: Send Failed]
    LogError2_Write --> ReturnFalse2_Write[Return False]
    ReturnTrue_Write --> FinallyBlock_Write
    ReturnFalse2_Write --> FinallyBlock_Write
    FinallyBlock_Write --> CloseConnection_Write[Close FTP Session]
    CloseConnection_Write --> End_Write[End: write()]
    

    Start_Read[Start: read()] --> Connect_Read{Connect to FTP Server}
    Connect_Read -- Success --> ChangeDir_Read[Change Directory on FTP]
    Connect_Read -- Fail --> LogError_Read[Log Error: Connection Failed]
    LogError_Read --> ReturnNone_Read[Return None]
    ChangeDir_Read --> CreateFile_Read[Create/Open Local File (Write Binary)]
    CreateFile_Read --> GetFile_Read[Get File from FTP Server]
    GetFile_Read --> OpenFile2_Read[Open Local File (Read Binary)]
    OpenFile2_Read --> ReturnContent_Read[Return File Content]
    GetFile_Read -- Fail --> LogError2_Read[Log Error: Retrieve Failed]
    LogError2_Read --> ReturnNone2_Read[Return None]
    ReturnContent_Read --> FinallyBlock_Read
     ReturnNone2_Read --> FinallyBlock_Read
    FinallyBlock_Read --> CloseConnection_Read[Close FTP Session]
   CloseConnection_Read --> End_Read[End: read()]

    Start_Delete[Start: delete()] --> Connect_Delete{Connect to FTP Server}
    Connect_Delete -- Success --> ChangeDir_Delete[Change Directory on FTP]
    Connect_Delete -- Fail --> LogError_Delete[Log Error: Connection Failed]
    LogError_Delete --> ReturnFalse_Delete[Return False]
    ChangeDir_Delete --> DeleteFile_Delete[Delete File on FTP Server]
    DeleteFile_Delete -- Success --> ReturnTrue_Delete[Return True]
    DeleteFile_Delete -- Fail --> LogError2_Delete[Log Error: Delete Failed]
    LogError2_Delete --> ReturnFalse2_Delete[Return False]
    ReturnTrue_Delete --> FinallyBlock_Delete
    ReturnFalse2_Delete --> FinallyBlock_Delete
    FinallyBlock_Delete --> CloseConnection_Delete[Close FTP Session]
    CloseConnection_Delete --> End_Delete[End: delete()]
    
    style Start_Write fill:#f9f,stroke:#333,stroke-width:2px
    style Start_Read fill:#f9f,stroke:#333,stroke-width:2px
    style Start_Delete fill:#f9f,stroke:#333,stroke-width:2px
    style End_Write fill:#ccf,stroke:#333,stroke-width:2px
    style End_Read fill:#ccf,stroke:#333,stroke-width:2px
    style End_Delete fill:#ccf,stroke:#333,stroke-width:2px
```

**Описание `mermaid` диаграммы:**

1.  **`flowchart TD`**: Объявляет тип диаграммы как блок-схему.
2.  **Блоки:**
    *   **`Start_*`**: Начало каждой функции `write`, `read` и `delete`.
    *   **`Connect_*`**: Блоки проверки подключения к FTP-серверу.
    *    **`ChangeDir_*`**: Блоки изменения рабочей директории на FTP-сервере.
    *   **`OpenFile_Write`**: Блок открытия файла для записи в функции `write`.
    *   **`CreateFile_Read`**: Блок создания файла для чтения в функции `read`.
    *    **`OpenFile2_Read`**: Блок открытия файла после получения с FTP-сервера в функции `read`.
    *   **`SendFile_Write`**: Блок отправки файла на FTP-сервер в функции `write`.
    *   **`GetFile_Read`**: Блок получения файла с FTP-сервера в функции `read`.
    *    **`DeleteFile_Delete`**: Блок удаления файла на FTP-сервере в функции `delete`.
    *   **`LogError_*`**: Блоки логирования ошибок при подключении.
    *   **`LogError2_*`**: Блоки логирования ошибок при отправке/получении/удалении файла.
    *   **`ReturnTrue_*`**: Блоки возврата `True` в случае успеха.
    *    **`ReturnFalse_*`**: Блоки возврата `False` в случае ошибки.
    *    **`ReturnNone_*`**: Блоки возврата `None` в случае ошибки в функции `read`.
    *   **`FinallyBlock_*`**: Блоки `finally` для закрытия FTP-соединения.
    *   **`CloseConnection_*`**: Блоки закрытия FTP соединения.
    *   **`End_*`**: Конец каждой функции `write`, `read` и `delete`.
3.  **Связи (`-->`)**: Обозначают последовательность выполнения операций и поток данных между блоками.
4.  **Условия (`-- Success -->`, `-- Fail -->`)**: Отображают ветвление выполнения программы в зависимости от результата.

**Зависимости:**

*   `ftplib`: Этот модуль используется для установления соединения с FTP-сервером, навигации по директориям и выполнения операций по передаче, чтению и удалению файлов.
*  `pathlib`: Используется для работы с путями к файлам, но в данном коде не используется для создания или обработки файловых путей, хотя импортирован.
*  `src.logger.logger`: Модуль для логирования ошибок и другой информации, позволяющий отслеживать проблемы, возникающие в процессе работы.
*  `typing`: Используется для аннотации типов в функциях, улучшает читаемость кода и упрощает отладку.

## <объяснение>

**Импорты:**

*   `from src.logger.logger import logger`: Импортирует объект `logger` из модуля `src.logger.logger`. Этот объект используется для логирования событий, таких как ошибки подключения, передачи или удаления файлов. Логгирование важно для отладки и мониторинга работы скрипта.
*   `from typing import Union`: Импортирует тип `Union` из модуля `typing`. `Union` используется для указания, что функция может возвращать значения разных типов (например, строку, байты или `None`).
*   `import ftplib`: Импортирует модуль `ftplib`, который предоставляет классы и функции для работы с FTP-серверами. Этот модуль используется для установления FTP-соединения, навигации по каталогам и передачи файлов.
*   `from pathlib import Path`: Импортирует класс `Path` из модуля `pathlib`. Используется для представления файловых путей, хотя в данном коде не используется для непосредственной работы с файлами.

**Классы:**

В данном коде не используются пользовательские классы.  `ftplib.FTP` используется как класс для работы с FTP соединениями.

**Функции:**

1.  **`write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool`**:
    *   **Аргументы:**
        *   `source_file_path` (str): Путь к файлу, который нужно отправить.
        *   `dest_dir` (str): Путь к директории на FTP-сервере.
        *   `dest_file_name` (str): Имя файла на FTP-сервере.
    *   **Возвращает:** `bool`: `True` в случае успешной отправки файла, `False` в случае ошибки.
    *   **Назначение:** Отправляет файл на FTP-сервер. Функция сначала пытается установить соединение с FTP-сервером, затем переходит в нужную директорию и отправляет файл. Логирует ошибки в случае неудачи.
    *   **Пример:** `write('local_file.txt', '/remote/folder', 'remote_file.txt')`.

2.  **`read(source_file_path: str, dest_dir: str, dest_file_name: str) -> Union[str, bytes, None]`**:
    *   **Аргументы:**
        *   `source_file_path` (str): Путь, куда нужно сохранить скачанный файл.
        *   `dest_dir` (str): Путь к директории на FTP-сервере.
        *   `dest_file_name` (str): Имя файла на FTP-сервере.
    *   **Возвращает:** `Union[str, bytes, None]`: Содержимое файла (в виде байтов) в случае успеха, `None` в случае ошибки.
    *   **Назначение:** Скачивает файл с FTP-сервера. Функция устанавливает соединение, переходит в нужную директорию, скачивает файл и возвращает его содержимое. Логирует ошибки в случае неудачи.
    *   **Пример:** `file_content = read('downloaded_file.txt', '/remote/folder', 'remote_file.txt')`.

3.  **`delete(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool`**:
    *   **Аргументы:**
        *   `source_file_path` (str): Путь к локальному файлу (не используется).
        *   `dest_dir` (str): Путь к директории на FTP-сервере.
        *   `dest_file_name` (str): Имя файла на FTP-сервере.
    *   **Возвращает:** `bool`: `True` в случае успешного удаления файла, `False` в случае ошибки.
    *   **Назначение:** Удаляет файл с FTP-сервера. Функция устанавливает соединение, переходит в нужную директорию и удаляет файл. Логирует ошибки в случае неудачи.
    *   **Пример:** `delete('local_dummy.txt', '/remote/folder', 'remote_file.txt')`.

**Переменные:**

*   `_connection`: Словарь, содержащий параметры подключения к FTP-серверу (сервер, порт, имя пользователя, пароль).

**Потенциальные ошибки и области для улучшения:**

1.  **Обработка ошибок:**
    *   Код обрабатывает общие исключения (`Exception`), что может затруднить отладку. Лучше обрабатывать конкретные типы исключений (например, `ftplib.error_perm` для ошибок доступа, `ftplib.error_temp` для временных ошибок FTP).
    *   При получении файла в функции `read`  сначала файл сохраняется на диск, а потом считывается, что является неоптимальным вариантом, и при работе с большим файлом это может привести к ошибкам.
2.  **Использование `pathlib`:**
    *   Модуль `pathlib` импортируется, но не используется для обработки путей. Для большей читаемости и кроссплатформенности можно использовать `Path` для формирования путей.
3.  **Конфигурация:**
    *   Параметры FTP-соединения (логин, пароль) хранятся непосредственно в коде, что небезопасно. Их лучше хранить в переменных окружения или отдельном файле конфигурации.
4. **Переиспользование FTP сессии:**
   * Каждая функция создаёт новое FTP соединение, что может быть неэффективным. Можно создать класс, который будет хранить сессию, а функции будут использовать её.

**Взаимосвязи с другими частями проекта:**

*   **`src.logger.logger`**: Этот модуль используется для логирования, что позволяет отслеживать действия скрипта и ошибки. Зависимость от этого модуля позволяет обеспечить единое логирование для всего проекта.
*   Предполагается, что данные о подключении к FTP-серверу (`_connection`) хранятся где-то в глобальной области видимости проекта, и этот файл к ним обращается.

В целом, код реализует основные функции для работы с FTP-сервером. Для повышения надежности и безопасности стоит доработать обработку исключений, хранение конфигурационных данных и пересмотреть логику скачивания файлов.