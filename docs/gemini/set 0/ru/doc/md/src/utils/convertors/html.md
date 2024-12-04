# Модуль `hypotez/src/utils/convertors/html.py`

## Обзор

Модуль `src.utils.convertors.html` предоставляет инструменты для конвертации HTML кода в различные форматы, включая escape-последовательности, словари и объекты `SimpleNamespace`.  Также модуль содержит функцию для конвертации HTML в PDF с использованием библиотеки `WeasyPrint`.

## Функции

### `html2escape`

**Описание**: Преобразует HTML-теги в escape-последовательности.

**Параметры**:

- `input_str` (str): Входная строка HTML-кода.

**Возвращает**:

- str: Строка с HTML-тегами, преобразованными в escape-последовательности.

**Пример**:

```python
html = "<p>Hello, world!</p>"
result = html2escape(html)
print(result)  # Вывод: &lt;p&gt;Hello, world!&lt;/p&gt;
```

### `escape2html`

**Описание**: Преобразует escape-последовательности обратно в HTML-теги.

**Параметры**:

- `input_str` (str): Входная строка с escape-последовательностями.

**Возвращает**:

- str: Строка с escape-последовательностями, преобразованными обратно в HTML-теги.

**Пример**:

```python
escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
result = escape2html(escaped)
print(result)  # Вывод: <p>Hello, world!</p>
```

### `html2dict`

**Описание**: Преобразует HTML-код в словарь, где ключи — теги, а значения — содержимое тегов.

**Параметры**:

- `html_str` (str): Входная строка HTML-кода.

**Возвращает**:

- dict: Словарь, где ключи — теги, а значения — их содержимое.

**Пример**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2dict(html)
print(result)  # Вывод: {'p': 'Hello', 'a': 'World'}
```

### `html2ns`

**Описание**: Преобразует HTML-код в объект `SimpleNamespace`, где атрибуты — теги, а значения — их содержимое.

**Параметры**:

- `html_str` (str): Входная строка HTML-кода.

**Возвращает**:

- SimpleNamespace: Объект `SimpleNamespace` с тегами в качестве атрибутов и их содержимым в качестве значений.

**Пример**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2ns(html)
print(result.p)  # Вывод: Hello
print(result.a)  # Вывод: World
```

### `html2pdf`

**Описание**: Преобразует HTML-код в PDF-файл с использованием `WeasyPrint`.

**Параметры**:

- `html_str` (str): Входная строка HTML-кода.
- `pdf_file` (str | Path): Путь к выходному PDF-файлу.

**Возвращает**:

- bool | None: `True`, если конвертация прошла успешно; `None`, в противном случае.

**Примечания**: Эта функция использует `WeasyPrint` для конвертации. Если `WeasyPrint` не установлен, будет выведено сообщение об ошибке.


## Обработка исключений

В функции `html2pdf` и других местах, где может произойти ошибка, используется блок `try...except` для обработки исключений, с использованием `ex` вместо `e`. Это стандартная практика для улучшения читаемости кода.


##  Модульные зависимости

Этот модуль использует следующие модули:
- `re`
- `typing`
- `pathlib`
- `venv` (вероятно, для логирования)
- `src.utils.string`
- `src.logger`
- `types`
- `html.parser`
- `xhtml2pdf` (для конвертации в PDF)
- `weasyprint` (для конвертации в PDF)