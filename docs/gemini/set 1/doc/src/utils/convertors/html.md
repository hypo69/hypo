# Модуль `hypotez/src/utils/convertors/html.py`

## Обзор

Этот модуль предоставляет функции для преобразования HTML-кода в различные форматы, включая escape-последовательности, словари и объекты `SimpleNamespace`. Также реализована функция преобразования HTML в PDF с использованием библиотеки `WeasyPrint`.

## Функции

### `html2escape`

**Описание**: Преобразует HTML-теги в escape-последовательности.

**Параметры**:

- `input_str` (str): Входная HTML-строка.

**Возвращает**:

- str: Преобразованная строка с HTML-тегами в escape-последовательности.

**Примеры**:

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

- str: Преобразованная строка с escape-последовательностями в HTML-теги.

**Примеры**:

```python
escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
result = escape2html(escaped)
print(result)  # Выведет: <p>Hello, world!</p>
```


### `html2dict`

**Описание**: Преобразует HTML-строку в словарь, где теги являются ключами, а их содержимое — значениями.

**Параметры**:

- `html_str` (str): Входная HTML-строка.

**Возвращает**:

- dict: Словарь, содержащий теги и их содержимое.

**Примеры**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2dict(html)
print(result)  # Выведет: {'p': 'Hello', 'a': 'World'}
```


### `html2ns`

**Описание**: Преобразует HTML-строку в объект `SimpleNamespace`, где теги являются атрибутами, а их содержимое — значениями.

**Параметры**:

- `html_str` (str): Входная HTML-строка.

**Возвращает**:

- `SimpleNamespace`: Объект `SimpleNamespace`, содержащий теги и их содержимое в виде атрибутов.

**Примеры**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2ns(html)
print(result.p)  # Выведет: Hello
print(result.a)  # Выведет: World
```


### `html2pdf`

**Описание**: Преобразует HTML-строку в PDF-файл с использованием `WeasyPrint`.

**Параметры**:

- `html_str` (str): Входная HTML-строка.
- `pdf_file` (str | Path): Путь к выходному PDF-файлу.

**Возвращает**:

- bool | None: `True`, если преобразование прошло успешно; `None`, если произошла ошибка.

**Примечания**: Функция `html2pdf` обрабатывает HTML и генерирует PDF-файл, используя библиотеку `WeasyPrint`.  В случае возникновения исключения (например, проблемы с форматированием), функция сообщает об ошибке и возвращает `None`.


```