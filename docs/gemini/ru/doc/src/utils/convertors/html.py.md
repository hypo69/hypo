# Модуль `html`

## Обзор

Модуль `html` предоставляет набор утилит для преобразования HTML в различные форматы, включая экранированные последовательности, словари и объекты `SimpleNamespace`, а также для конвертации HTML в PDF.

## Оглавление

- [Функции](#Функции)
    - [`html2escape`](#html2escape)
    - [`escape2html`](#escape2html)
    - [`html2dict`](#html2dict)
    - [`html2ns`](#html2ns)
    - [`html2pdf`](#html2pdf)

## Функции

### `html2escape`

**Описание**: Преобразует HTML в экранированные последовательности.

**Параметры**:
- `input_str` (str): HTML код.

**Возвращает**:
- `str`: HTML, преобразованный в экранированные последовательности.

**Пример**:
```python
>>> html = "<p>Hello, world!</p>"
>>> result = html2escape(html)
>>> print(result)
&lt;p&gt;Hello, world!&lt;/p&gt;
```

### `escape2html`

**Описание**: Преобразует экранированные последовательности обратно в HTML.

**Параметры**:
- `input_str` (str): Строка с экранированными последовательностями.

**Возвращает**:
- `str`: Экранированные последовательности, преобразованные обратно в HTML.

**Пример**:
```python
>>> escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
>>> result = escape2html(escaped)
>>> print(result)
<p>Hello, world!</p>
```

### `html2dict`

**Описание**: Преобразует HTML в словарь, где теги являются ключами, а содержимое - значениями.

**Параметры**:
- `html_str` (str): HTML строка для преобразования.

**Возвращает**:
- `dict`: Словарь, где HTML теги являются ключами, а их содержимое - значениями.

**Пример**:
```python
>>> html = "<p>Hello</p><a href='link'>World</a>"
>>> result = html2dict(html)
>>> print(result)
{'p': 'Hello', 'a': 'World'}
```

### `html2ns`

**Описание**: Преобразует HTML в объект `SimpleNamespace`, где теги являются атрибутами, а содержимое - значениями.

**Параметры**:
- `html_str` (str): HTML строка для преобразования.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace`, где HTML теги являются атрибутами, а их содержимое - значениями.

**Пример**:
```python
>>> html = "<p>Hello</p><a href='link'>World</a>"
>>> result = html2ns(html)
>>> print(result.p)
Hello
>>> print(result.a)
World
```
### `html2pdf`

**Описание**: Конвертирует HTML-контент в PDF файл, используя `WeasyPrint`.

**Параметры**:
- `html_str` (str): HTML контент в виде строки.
- `pdf_file` (str | Path): Путь к выходному PDF файлу.

**Возвращает**:
- `bool | None`: Возвращает `True`, если генерация PDF успешна; `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Вызывает исключение в случае ошибки при генерации PDF.