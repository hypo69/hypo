# src.utils.convertors.html

## Обзор

Модуль `src.utils.convertors.html` предоставляет утилиты для преобразования HTML, включая функции для кодирования и декодирования HTML-сущностей, преобразования HTML в словари и объекты SimpleNamespace, а также для генерации PDF из HTML.

## Оглавление

- [Функции](#Функции)
    - [`html2escape`](#html2escape)
    - [`escape2html`](#escape2html)
    - [`html2dict`](#html2dict)
    - [`html2ns`](#html2ns)
    - [`html2pdf`](#html2pdf)

## Функции

### `html2escape`

**Описание**: Преобразует HTML в escape-последовательности.

**Параметры**:
- `input_str` (str): HTML код.

**Возвращает**:
- `str`: HTML, преобразованный в escape-последовательности.

**Пример:**
```python
>>> html = "<p>Hello, world!</p>"
>>> result = html2escape(html)
>>> print(result)
&lt;p&gt;Hello, world!&lt;/p&gt;
```

### `escape2html`

**Описание**: Преобразует escape-последовательности обратно в HTML.

**Параметры**:
- `input_str` (str): Строка с escape-последовательностями.

**Возвращает**:
- `str`: Escape-последовательности, преобразованные в HTML.

**Пример:**
```python
>>> escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
>>> result = escape2html(escaped)
>>> print(result)
<p>Hello, world!</p>
```

### `html2dict`

**Описание**: Преобразует HTML в словарь, где ключами являются теги, а значениями - их содержимое.

**Параметры**:
- `html_str` (str): HTML строка для преобразования.

**Возвращает**:
- `dict`: Словарь, где ключи - HTML теги, а значения - их содержимое.

**Пример:**
```python
>>> html = "<p>Hello</p><a href='link'>World</a>"
>>> result = html2dict(html)
>>> print(result)
{'p': 'Hello', 'a': 'World'}
```

### `html2ns`

**Описание**: Преобразует HTML в объект SimpleNamespace, где теги являются атрибутами, а содержимое - значениями.

**Параметры**:
- `html_str` (str): HTML строка для преобразования.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace с тегами HTML как атрибутами и их содержанием как значениями.

**Пример:**
```python
>>> html = "<p>Hello</p><a href='link'>World</a>"
>>> result = html2ns(html)
>>> print(result.p)
Hello
>>> print(result.a)
World
```

### `html2pdf`

**Описание**: Конвертирует HTML-контент в PDF-файл с использованием WeasyPrint.

**Параметры**:
- `html_str` (str): HTML-контент в виде строки.
- `pdf_file` (str | Path): Путь к выходному PDF-файлу.

**Возвращает**:
- `bool | None`: Возвращает `True`, если генерация PDF успешна; `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Описание ситуации, в которой возникает исключение.