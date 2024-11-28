# Модуль `hypotez/src/utils/convertors/html.py`

## Обзор

Модуль `hypotez/src/utils/convertors/html.py` предоставляет набор функций для конвертации HTML-кода в различные форматы, включая escape-последовательности, словари и объекты `SimpleNamespace`.  Также реализована функция конвертации HTML в PDF с использованием библиотеки WeasyPrint.


## Функции

### `html2escape`

**Описание**: Преобразует HTML-теги в escape-последовательности.

**Параметры**:

- `input_str` (str): Входная строка с HTML-кодом.

**Возвращает**:

- str: Строка с HTML-тегами, преобразованными в escape-последовательности.

**Примеры**:

```python
html = "<p>Hello, world!</p>"
result = html2escape(html)
print(result)  # Вывод: &lt;p&gt;Hello, world!&lt;/p&gt;
```


### `escape2html`

**Описание**: Преобразует escape-последовательности в HTML-теги.

**Параметры**:

- `input_str` (str): Входная строка с escape-последовательностями.

**Возвращает**:

- str: Строка с escape-последовательностями, преобразованными в HTML-теги.

**Примеры**:

```python
escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
result = escape2html(escaped)
print(result)  # Вывод: <p>Hello, world!</p>
```


### `html2dict`

**Описание**: Преобразует HTML-строку в словарь, где ключами являются теги, а значениями — их содержимое.

**Параметры**:

- `html_str` (str): Входная HTML-строка.

**Возвращает**:

- dict: Словарь, содержащий теги и их содержимое.

**Примеры**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2dict(html)
print(result)  # Вывод: {'p': 'Hello', 'a': 'World'}
```


### `html2ns`

**Описание**: Преобразует HTML-строку в объект `SimpleNamespace`, где атрибутами являются теги, а значениями — их содержимое.

**Параметры**:

- `html_str` (str): Входная HTML-строка.

**Возвращает**:

- `SimpleNamespace`: Объект `SimpleNamespace` с тегами в качестве атрибутов и их содержимым.

**Примеры**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2ns(html)
print(result.p)  # Вывод: Hello
print(result.a)  # Вывод: World
```


### `html2pdf`

**Описание**: Преобразует HTML-строку в PDF-файл с использованием библиотеки WeasyPrint.

**Параметры**:

- `html_str` (str): Входная HTML-строка.
- `pdf_file` (str | Path): Путь к выходному PDF-файлу.

**Возвращает**:

- bool | None: `True` в случае успешного преобразования, `None` при ошибке.

**Обработка исключений**:

- `Exception`: Выводит сообщение об ошибке.


**Примечания**:

Функция `html2pdf` использует библиотеку `weasyprint`. Убедитесь, что она установлена.

```python
html_content = "<p>This is some HTML content.</p>"
pdf_filename = "output.pdf"

success = html2pdf(html_content, pdf_filename)

if success:
  print(f"PDF file '{pdf_filename}' created successfully.")
```

```
```
```
```
```