# Модуль для скачивания файлов с использованием wget

## Обзор

Этот модуль содержит функцию `wget_dl`, которая позволяет скачивать файлы по URL-адресу с использованием команды `wget`. Он предназначен для простой загрузки файлов из сети с обработкой ошибок.

## Функции

### `wget_dl`

```python
def wget_dl(url: str) -> str | tuple[str, str]:
    """
    Скачивает файл по заданному URL-адресу с использованием команды wget.

    Args:
        url (str): URL-адрес файла для скачивания.

    Returns:
        str | tuple[str, str]: Имя скачанного файла в случае успеха, или кортеж ("error", имя файла) в случае ошибки.

    Raises:
        Exception: Если возникает ошибка при выполнении команды wget.

    Example:
        >>> wget_dl('http://example.com/file.txt')
        Downloading Started
        Downloading Complete file.txt
        'file.txt'

        >>> wget_dl('http://example.com/nonexistent_file.txt')
        Downloading Started
        DOWNLAOD ERROR : ...
        ('error', 'nonexistent_file.txt')
    """
```

**Как работает функция**:

1.  **Инициализация**: Функция начинает работу с URL-адреса, который необходимо скачать.
2.  **Подготовка к скачиванию**:
    *   Печатает сообщение "Downloading Started" в консоль.
    *   Извлекает имя файла из URL-адреса, используя `os.path.basename(url)`. Это имя будет использоваться для сохранения файла локально.
3.  **Выполнение скачивания**:
    *   Использует `subprocess.check_output` для выполнения команды `wget`.
    *   Команда `wget` скачивает файл по указанному URL-адресу и сохраняет его с именем, полученным на шаге 2.
    *   `stderr=subprocess.STDOUT` перенаправляет стандартный поток ошибок в стандартный поток вывода, что позволяет перехватывать ошибки `wget`.
    *   `shell=True` позволяет выполнять команду через shell.
4.  **Обработка результата**:
    *   Если скачивание успешно, печатает сообщение "Downloading Complete" и имя файла.
    *   Возвращает имя скачанного файла.
5.  **Обработка ошибок**:
    *   Если во время скачивания происходит исключение, печатает сообщение "DOWNLAOD ERROR :" и текст ошибки.
    *   Возвращает кортеж `("error", filename)`, где `filename` - имя файла, который пытались скачать.

**ASCII flowchart**:

```
A[Начало]
|
B[Печать "Downloading Started"]
|
C[filename = os.path.basename(url)]
|
D[Выполнение wget команды через subprocess.check_output]
|
E[Успех?] -- Да --> F[Печать "Downloading Complete"] --> G[Возврат filename]
|
Нет
|
H[Обработка исключения]
|
I[Печать "DOWNLAOD ERROR :"]
|
J[Возврат ("error", filename)]
|
K[Конец]
```

**Примеры**:

```python
# Пример успешного скачивания
filename = wget_dl('http://example.com/file.txt')
print(filename)  # Вывод: file.txt

# Пример неуспешного скачивания
result = wget_dl('http://example.com/nonexistent_file.txt')
print(result)  # Вывод: ('error', 'nonexistent_file.txt')