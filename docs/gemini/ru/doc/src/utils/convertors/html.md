# Модуль `hypotez/src/utils/convertors/html.py`

## Обзор

Модуль `hypotez/src/utils/convertors/html.py` содержит функции для конвертации HTML-кода в различные форматы, включая escape-последовательности, словари и объекты `SimpleNamespace`. Также предоставляет функцию для конвертации HTML в PDF используя библиотеку WeasyPrint.

## Функции

### `html2escape`

**Описание**: Преобразует HTML-теги в escape-последовательности.

**Параметры**:
- `input_str` (str): Входная HTML-строка.

**Возвращает**:
- str: Строка с HTML-тегами, преобразованными в escape-последовательности.

**Пример использования**:

```python
html = "<p>Hello, world!</p>"
result = html2escape(html)
print(result)  # Выведет: &lt;p&gt;Hello, world!&lt;/p&gt;
```


### `escape2html`

**Описание**: Преобразует escape-последовательности в HTML-теги.

**Параметры**:
- `input_str` (str): Входная строка с escape-последовательностями.

**Возвращает**:
- str: Строка с escape-последовательностями, преобразованными в HTML-теги.

**Пример использования**:

```python
escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
result = escape2html(escaped)
print(result)  # Выведет: <p>Hello, world!</p>
```


### `html2dict`

**Описание**: Преобразует HTML-строку в словарь, где ключи — теги, а значения — содержимое тегов.

**Параметры**:
- `html_str` (str): Входная HTML-строка.

**Возвращает**:
- dict: Словарь, содержащий теги и их содержимое.

**Пример использования**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2dict(html)
print(result)  # Выведет: {'p': 'Hello', 'a': 'World'}
```


### `html2ns`

**Описание**: Преобразует HTML-строку в объект `SimpleNamespace`, где атрибуты — теги, а значения — содержимое тегов.

**Параметры**:
- `html_str` (str): Входная HTML-строка.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace` с тегами в качестве атрибутов и их содержимым в качестве значений.

**Пример использования**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2ns(html)
print(result.p)  # Выведет: Hello
print(result.a)  # Выведет: World
```


### `html2pdf`

**Описание**: Конвертирует HTML-строку в PDF-файл с помощью WeasyPrint.

**Параметры**:
- `html_str` (str): Входная HTML-строка.
- `pdf_file` (str | Path): Путь к выходному PDF-файлу.

**Возвращает**:
- bool | None: `True`, если конвертация прошла успешно; `None`, если произошла ошибка.

**Обработка исключений**:
- Возможны исключения во время процесса конвертации.  Они обрабатываются, и об ошибке выводится сообщение в консоль.


**Примечание:** В оригинальном коде функция `html2pdf` содержала комментарии, предполагающие использование `xhtml2pdf`. Сейчас эта функция использует `WeasyPrint`.  Обратите внимание на пример использования функции.
```
```
```python
html_content = "<html><body><h1>Hello, world!</h1></body></html>"
pdf_filename = "output.pdf"
success = html2pdf(html_content, pdf_filename)
if success:
  print("PDF успешно создан.")