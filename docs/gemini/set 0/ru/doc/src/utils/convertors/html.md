# Модуль hypotez/src/utils/convertors/html.py

## Обзор

Этот модуль предоставляет инструменты для конвертации HTML в различные форматы, включая escape-последовательности, словари и объекты SimpleNamespace.  Также реализуется конвертация HTML в PDF с использованием библиотеки WeasyPrint.  Модуль содержит функции для работы с HTML-кодом, включая преобразование HTML в escape-последовательности и обратно, а также для парсинга HTML-кода в словари и SimpleNamespace объекты.

## Функции

### `html2escape`

**Описание**: Преобразует HTML-теги в escape-последовательности.

**Параметры**:

- `input_str` (str): Входная строка HTML-кода.

**Возвращает**:

- str: HTML-код, преобразованный в escape-последовательности.

**Примеры**:

```python
html = "<p>Hello, world!</p>"
result = html2escape(html)
print(result)  # Вывод: &lt;p&gt;Hello, world!&lt;/p&gt;
```


### `escape2html`

**Описание**: Преобразует escape-последовательности в HTML-теги.

**Параметры**:

- `input_str` (str): Входная строка со escape-последовательностями.

**Возвращает**:

- str:  Escape-последовательности преобразованные в HTML-код.

**Примеры**:

```python
escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
result = escape2html(escaped)
print(result)  # Вывод: <p>Hello, world!</p>
```


### `html2dict`

**Описание**: Преобразует HTML-код в словарь, где ключи - теги, значения - содержимое тегов.

**Параметры**:

- `html_str` (str): Входная строка HTML-кода.

**Возвращает**:

- dict: Словарь, где ключами являются теги, а значениями - содержимое тегов.

**Примеры**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2dict(html)
print(result) # Вывод: {'p': 'Hello', 'a': 'World'}
```


### `html2ns`

**Описание**: Преобразует HTML-код в объект `SimpleNamespace`, где атрибуты - теги, значения - содержимое тегов.

**Параметры**:

- `html_str` (str): Входная строка HTML-кода.

**Возвращает**:

- SimpleNamespace: Объект `SimpleNamespace` с тегами в качестве атрибутов и их содержимым.

**Примеры**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2ns(html)
print(result.p)  # Вывод: Hello
print(result.a)  # Вывод: World
```


### `html2pdf`

**Описание**: Преобразует HTML-код в PDF-файл с использованием библиотеки WeasyPrint.

**Параметры**:

- `html_str` (str): Входной HTML-код.
- `pdf_file` (str | Path): Путь к файлу вывода PDF.

**Возвращает**:

- bool | None: `True`, если генерация PDF прошла успешно, `None` при ошибке.


**Обрабатываемые исключения**:

- `Exception`: Выводится сообщение об ошибке при возникновении проблем с генерацией PDF.

**Примечания**:

Функция `html2pdf` использует библиотеку `WeasyPrint` для генерации PDF-файлов из HTML.  Она обрабатывает HTML-код и сохраняет его в указанный PDF-файл. Возвращает `True` при успешном завершении, и `None`, если возникла ошибка.

```
```