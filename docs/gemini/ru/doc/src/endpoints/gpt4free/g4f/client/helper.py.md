# Модуль `helper.py`

## Обзор

Модуль `helper.py` содержит набор вспомогательных функций, предназначенных для обработки текста, извлечения информации из строк и безопасного закрытия асинхронных генераторов. Эти функции используются для упрощения разбора текста и обработки данных в проекте `hypotez`.

## Подробней

Модуль предоставляет функции для фильтрации Markdown и JSON блоков кода из текста, поиска стоп-слов и безопасного закрытия асинхронных генераторов. Эти функции полезны для очистки и обработки данных, полученных из различных источников, таких как ответы моделей GPT.

## Функции

### `filter_markdown`

```python
def filter_markdown(text: str, allowd_types=None, default=None) -> str:
    """
    Parses code block from a string.

    Args:
        text (str): A string containing a code block.
        allowd_types: Разрешенные типы блоков кода.
        default: Значение по умолчанию, если блок кода не найден.

    Returns:
        dict: A dictionary parsed from the code block.
    """
```

**Назначение**: Извлекает блок кода из строки, если он соответствует разрешенным типам.

**Параметры**:
- `text` (str): Строка, содержащая блок кода.
- `allowd_types` (list, optional): Список разрешенных типов блоков кода. Если `None`, разрешены все типы.
- `default` (str, optional): Значение, возвращаемое по умолчанию, если блок кода не найден или его тип не разрешен. По умолчанию `None`.

**Возвращает**:
- `str`: Извлеченный блок кода, если он найден и его тип разрешен, иначе возвращает значение `default`.

**Как работает функция**:

1.  **Поиск блока кода**: Функция использует регулярное выражение для поиска блоков кода, заключенных между тройными обратными кавычками (`````).

2.  **Проверка типа**: Если указан параметр `allowd_types`, функция проверяет, соответствует ли тип найденного блока кода одному из разрешенных типов.

3.  **Возврат результата**: Если блок кода найден и его тип разрешен (или `allowd_types` не указан), функция возвращает содержимое блока кода. В противном случае возвращается значение `default`.

4.  **Блок схема**:
```ascii
    Начало
    │
    └──> Поиск блока кода с использованием регулярного выражения
    │
    └──> Проверка, найден ли блок кода (match is not None)
    │   └── Да → Проверка, указан ли allowd_types
    │       ├── Да → Проверка, соответствует ли тип блока кода одному из разрешенных типов
    │       │   ├── Да → Возврат содержимого блока кода
    │       │   └── Нет → Возврат значения default
    │       └── Нет → Возврат содержимого блока кода
    └── Нет → Возврат значения default
    │
    Конец
```

**Примеры**:

```python
text = "```python\nprint('Hello, world!')\n```"
code = filter_markdown(text, allowd_types=['python'])
print(code)  # Вывод: print('Hello, world!')

text = "```json\n{\"key\": \"value\"}\n```"
code = filter_markdown(text, allowd_types=['python'], default='Not found')
print(code)  # Вывод: Not found
```

### `filter_json`

```python
def filter_json(text: str) -> str:
    """
    Parses JSON code block from a string.

    Args:
        text (str): A string containing a JSON code block.

    Returns:
        dict: A dictionary parsed from the JSON code block.
    """
```

**Назначение**: Извлекает JSON блок кода из строки.

**Параметры**:
- `text` (str): Строка, содержащая JSON блок кода.

**Возвращает**:
- `str`: Извлеченный JSON блок кода, если он найден, иначе возвращает исходную строку без изменений.

**Как работает функция**:

1.  **Вызов `filter_markdown`**: Функция вызывает `filter_markdown` с параметрами, настроенными для извлечения JSON блоков кода (разрешенные типы - `""` и `"json"`).
2.  **Удаление лишних символов**: С помощью `text.strip("^\\n ")` обрезаются символы `^`, `\n` и пробелы.
3.  **Возврат результата**: Функция возвращает результат, полученный от `filter_markdown`.

4.  **Блок схема**:
```ascii
    Начало
    │
    └──> Вызов filter_markdown с параметрами для JSON
    │
    └──> Возврат результата
    │
    Конец
```

**Примеры**:

```python
text = "```json\n{\"key\": \"value\"}\n```"
json_code = filter_json(text)
print(json_code)  # Вывод: {"key": "value"}

text = "Some text without JSON"
json_code = filter_json(text)
print(json_code)  # Вывод: Some text without JSON
```

### `find_stop`

```python
def find_stop(stop: Optional[list[str]], content: str, chunk: str = None):
    """
    Находит первое вхождение стоп-слова в контенте.

    Args:
        stop (Optional[list[str]]): Список стоп-слов для поиска.
        content (str): Строка, в которой производится поиск.
        chunk (str, optional): Дополнительная строка (часть контента). По умолчанию None.

    Returns:
        Tuple[int, str, str]: Кортеж, содержащий индекс первого вхождения стоп-слова,
                              обрезанный контент и обрезанный чанк (если применимо).
    """
```

**Назначение**: Находит первое вхождение любого из стоп-слов в заданной строке.

**Параметры**:
- `stop` (Optional[list[str]]): Список стоп-слов для поиска. Если `None`, поиск не производится.
- `content` (str): Строка, в которой производится поиск стоп-слов.
- `chunk` (str, optional): Дополнительная строка (часть контента), которая также обрезается, если стоп-слово найдено. По умолчанию `None`.

**Возвращает**:
- `Tuple[int, str, str]`: Кортеж, содержащий:
    - `first` (int): Индекс первого вхождения стоп-слова (или -1, если стоп-слова не найдены или список стоп-слов пуст).
    - `content` (str): Строка `content`, обрезанная до первого вхождения стоп-слова (или исходная строка, если стоп-слова не найдены).
    - `chunk` (str): Строка `chunk`, обрезанная до первого вхождения стоп-слова (или исходная строка, если стоп-слова не найдены или `chunk` равен `None`).

**Как работает функция**:

1.  **Проверка наличия стоп-слов**: Функция проверяет, что список стоп-слов (`stop`) не равен `None`.
2.  **Поиск стоп-слов**: Функция перебирает стоп-слова из списка `stop` и ищет первое вхождение каждого стоп-слова в строке `content`.
3.  **Обрезание строк**: Если стоп-слово найдено, функция обрезает строки `content` и `chunk` до первого вхождения этого стоп-слова.
4.  **Возврат результата**: Функция возвращает индекс первого вхождения стоп-слова, обрезанную строку `content` и обрезанную строку `chunk`.

5.  **Блок схема**:
```ascii
    Начало
    │
    └──> Проверка, что список стоп-слов не None
    │   └── Да → Инициализация first = -1 и word = None
    │       │
    │       └──> Перебор стоп-слов в списке stop
    │           │
    │           └──> Поиск первого вхождения стоп-слова в content
    │               │
    │               └──> Если стоп-слово найдено (first != -1)
    │                   │   └──> Обрезание content до первого вхождения стоп-слова
    │                   │   └──> Если chunk не None
    │                   │       └──> Поиск первого вхождения стоп-слова в chunk
    │                   │           │   └──> Если стоп-слово найдено в chunk
    │                   │           │       └──> Обрезание chunk до первого вхождения стоп-слова
    │                   │           │   └── Иначе
    │                   │           │       └──> first = 0
    │                   │   └── Выход из цикла перебора стоп-слов
    │   └── Иначе
    │       └──> first = -1
    │
    └──> Возврат кортежа (first, content, chunk)
    │
    Конец
```

**Примеры**:

```python
stop_words = ["stop", "end"]
content = "This is a test stop word."
chunk = "This is a chunk of text."
first, content, chunk = find_stop(stop_words, content, chunk)
print(f"First: {first}, Content: {content}, Chunk: {chunk}")
# Вывод: First: 13, Content: This is a test , Chunk: This is a chunk of text.

stop_words = ["stop", "end"]
content = "This is a test."
chunk = "This is a chunk of text end here."
first, content, chunk = find_stop(stop_words, content, chunk)
print(f"First: {first}, Content: {content}, Chunk: {chunk}")
# Вывод: First: -1, Content: This is a test., Chunk: This is a chunk of text end here.
```

### `filter_none`

```python
def filter_none(**kwargs) -> dict:
    """
    Создает новый словарь, исключая элементы со значением None.

    Args:
        **kwargs: Произвольный набор именованных аргументов.

    Returns:
        dict: Новый словарь, содержащий только элементы с не-None значениями.
    """
```

**Назначение**: Создает новый словарь, исключая элементы со значением `None`.

**Параметры**:
- `**kwargs`: Произвольный набор именованных аргументов, которые будут преобразованы в словарь.

**Возвращает**:
- `dict`: Новый словарь, содержащий только те элементы из `kwargs`, значения которых не равны `None`.

**Как работает функция**:

1.  **Генерация словаря**: Функция использует генератор словаря для создания нового словаря, перебирая элементы входного словаря `kwargs`.
2.  **Фильтрация `None`**: Для каждого элемента проверяется, не равно ли его значение `None`. Если значение не равно `None`, элемент включается в новый словарь.
3.  **Возврат результата**: Функция возвращает новый словарь, содержащий только элементы с не-`None` значениями.

4.  **Блок схема**:
```ascii
    Начало
    │
    └──> Создание словаря с помощью генератора словаря
    │   └──> Перебор элементов kwargs
    │       └──> Проверка, что значение элемента не равно None
    │           ├── Да → Включение элемента в новый словарь
    │           └── Нет → Исключение элемента из нового словаря
    │
    └──> Возврат нового словаря
    │
    Конец
```

**Примеры**:

```python
filtered_dict = filter_none(a=1, b=None, c="test")
print(filtered_dict)  # Вывод: {'a': 1, 'c': 'test'}

filtered_dict = filter_none(a=None, b=None)
print(filtered_dict)  # Вывод: {}
```

### `safe_aclose`

```python
async def safe_aclose(generator: AsyncGenerator) -> None:
    """
    Безопасно закрывает асинхронный генератор.

    Args:
        generator (AsyncGenerator): Асинхронный генератор для закрытия.
    """
```

**Назначение**: Безопасно закрывает асинхронный генератор, обрабатывая возможные исключения при закрытии.

**Параметры**:
- `generator` (AsyncGenerator): Асинхронный генератор, который необходимо закрыть.

**Возвращает**:
- `None`

**Как работает функция**:

1.  **Проверка генератора**: Функция проверяет, что генератор не равен `None` и имеет метод `aclose`.
2.  **Закрытие генератора**: Функция пытается закрыть генератор, вызывая метод `aclose`.
3.  **Обработка исключений**: Если при закрытии генератора возникает исключение, функция перехватывает его и логирует предупреждение.

4.  **Блок схема**:
```ascii
    Начало
    │
    └──> Проверка, что генератор не None и имеет метод aclose
    │   └── Да → Попытка закрытия генератора (await generator.aclose())
    │       └── Если возникло исключение
    │           └──> Логирование предупреждения об ошибке закрытия генератора
    │
    Конец
```

**Примеры**:

```python
async def my_generator():
    try:
        for i in range(3):
            yield i
    finally:
        print("Generator is closing")

async def main():
    gen = my_generator()
    async for i in gen:
        print(i)
        if i == 1:
            await safe_aclose(gen)
            break

# main()
```
В этом примере, если во время итерации `i` становится равным 1, генератор безопасно закрывается с использованием `safe_aclose`.