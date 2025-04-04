# Модуль `Phind`

## Обзор

Модуль `Phind` предоставляет асинхронтный генератор для взаимодействия с сервисом `Phind`. Он предназначен для выполнения поисковых запросов и получения ответов с использованием моделей, таких как GPT-4 и Phind-34B. Модуль поддерживает потоковую передачу данных, историю сообщений и может работать через прокси.

## Подробнее

Модуль использует асинхронные запросы для взаимодействия с API `Phind`. Он извлекает данные из веб-страницы для генерации запросов и обрабатывает потоковые ответы. Модуль предназначен для интеграции в системы, требующие асинхронного взаимодействия с `Phind` для получения информации.

## Классы

### `Phind`

**Описание**: Класс `Phind` является асинхронным провайдером генератора.

**Наследует**: `AsyncGeneratorProvider`

**Атрибуты**:

-   `url` (str): URL сервиса `Phind` (`https://www.phind.com`).
-   `working` (bool): Указывает, работает ли провайдер (в данном случае `False`).
-   `lockdown` (bool): Указывает, находится ли провайдер в режиме блокировки (в данном случае `True`).
-   `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (`True`).
-   `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (`True`).

**Методы**:

-   `create_async_generator`: Создает асинхронный генератор для выполнения запросов к `Phind`.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    timeout: int = 120,
    creative_mode: bool = False,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для взаимодействия с API Phind.

    Args:
        model (str): Используемая модель (например, "gpt-4" или "Phind-34B").
        messages (Messages): Список сообщений для контекста запроса.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        timeout (int, optional): Время ожидания запроса в секундах. По умолчанию `120`.
        creative_mode (bool, optional): Включает креативный режим. По умолчанию `False`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор для получения ответов от Phind.

    Raises:
        RuntimeError: Если возникает ошибка на стороне сервера Phind.
    """
```

**Назначение**: Функция `create_async_generator` создает асинхронный генератор для взаимодействия с API `Phind`. Она выполняет запрос к сервису `Phind` с заданными параметрами и возвращает асинхронный генератор, который выдает части ответа по мере их поступления.

**Параметры**:

-   `cls`: Ссылка на класс `Phind`.
-   `model` (str): Имя используемой модели (`gpt-4` или `Phind-34B`).
-   `messages` (Messages): Список сообщений, представляющих историю разговора.
-   `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
-   `timeout` (int, optional): Время ожидания ответа от сервера в секундах. По умолчанию `120`.
-   `creative_mode` (bool, optional): Флаг, указывающий, следует ли использовать креативный режим. По умолчанию `False`.
-   `**kwargs`: Дополнительные параметры, которые могут быть переданы.

**Возвращает**:

-   `AsyncResult`: Асинхронный генератор, выдающий части ответа от `Phind`.

**Вызывает исключения**:

-   `RuntimeError`: Если сервер `Phind` возвращает сообщение об ошибке.

**Как работает функция**:

1.  **Подготовка заголовков**: Создаются заголовки HTTP-запроса, необходимые для взаимодействия с API `Phind`.
2.  **Создание сессии**: Инициализируется асинхронная сессия с использованием `StreamSession` для управления запросами.
3.  **Получение challenge_seeds**: Выполняется GET-запрос к `Phind`, извлекается `challenge_seeds` из HTML ответа.
4.  **Подготовка данных запроса**: Формируются данные для POST-запроса, включая историю сообщений, параметры модели и прочее.
5.  **Генерация challenge**: Генерируется challenge на основе данных запроса и `challenge_seeds`.
6.  **Выполнение POST-запроса**: Отправляется POST-запрос к API `Phind` с данными и заголовками.
7.  **Обработка потокового ответа**: Асинхронно обрабатываются строки ответа, удаляются префиксы и теги, и извлекается полезная информация.
8.  **Генерация результатов**: Возвращается асинхронный генератор, который выдает декодированные части ответа.

```
Начало
↓
Создание HTTP заголовков
↓
Создание асинхронной сессии
↓
Получение challenge_seeds из HTML ответа
↓
Формирование данных POST запроса (история, модель, параметры)
↓
Генерация challenge
↓
POST запрос к API Phind
↓
Асинхронная обработка потокового ответа
│
├── Строка начинается с "data: "?
│   └── Да: Извлечение данных
│   │    ├── Данные - "<PHIND_DONE/>"?
│   │    │   └── Да: Завершение генерации
│   │    ├── Данные - "<PHIND_BACKEND_ERROR>"
│   │    │   └── Да: Выброс RuntimeError
│   │    ├── Данные - "<PHIND_WEBRESULTS>" или "<PHIND_FOLLOWUP>"?
│   │    │   └── Да: Пропуск
│   │    ├── Данные - "<PHIND_METADATA>" или "<PHIND_INDICATOR>"?
│   │    │   └── Да: Пропуск
│   │    ├── Данные - "<PHIND_SPAN_BEGIN>" или "<PHIND_SPAN_END>"?
│   │    │   └── Да: Пропуск
│   │    ├── Данные не пустые?
│   │    │   └── Да: Декодирование и передача
│   │    ├── Новая строка?
│   │    │   └── Да: передача "\n"
│   │    └── Нет:  new_line = True
│   └── Нет: Пропуск строки
↓
Конец
```

**Примеры**:

```python
# Пример использования create_async_generator
messages = [
    {"role": "user", "content": "Напиши программу на Python, которая выводит 'Hello, world!'"}
]
async def main():
    generator = await Phind.create_async_generator(model="Phind-34B", messages=messages)
    async for chunk in generator:
        print(chunk, end="")

# Запуск примера
# import asyncio
# asyncio.run(main())
```

### `deterministic_stringify`

```python
def deterministic_stringify(obj):
    """Преобразует объект в строку JSON с детерминированным порядком ключей.

    Args:
        obj (dict): Объект для преобразования в строку.

    Returns:
        str: Строка JSON с детерминированным порядком ключей.
    """
```

**Назначение**: Функция `deterministic_stringify` преобразует объект (словарь) в строку JSON с детерминированным порядком ключей. Это необходимо для обеспечения консистентности при генерации challenge.

**Параметры**:

-   `obj` (dict): Объект (словарь) для преобразования в строку.

**Возвращает**:

-   `str`: Строка JSON с детерминированным порядком ключей.

**Как работает функция**:

1.  **Обработка значений**: Рекурсивно обрабатывает значения в словаре, сортируя списки и форматируя числа.
2.  **Сортировка ключей**: Сортирует ключи словаря.
3.  **Формирование строки**: Создает строку JSON, объединяя ключи и значения.

```
Начало
↓
Обработка значений: рекурсивная обработка значений, сортировка списков, форматирование чисел
↓
Сортировка ключей словаря
↓
Формирование JSON строки
↓
Конец
```

**Примеры**:

```python
# Пример использования deterministic_stringify
obj = {"b": 2, "a": 1}
result = deterministic_stringify(obj)
print(result)  # Вывод: a:1.00000000,b:2.00000000
```

### `prng_general`

```python
def prng_general(seed, multiplier, addend, modulus):
    """Генерирует псевдослучайное число с использованием общих параметров.

    Args:
        seed (int): Начальное значение.
        multiplier (int): Множитель.
        addend (int): Добавляемое значение.
        modulus (int): Модуль.

    Returns:
        float: Псевдослучайное число в диапазоне [0, 1).
    """
```

**Назначение**: Функция `prng_general` генерирует псевдослучайное число с использованием общих параметров.

**Параметры**:

-   `seed` (int): Начальное значение.
-   `multiplier` (int): Множитель.
-   `addend` (int): Добавляемое значение.
-   `modulus` (int): Модуль.

**Возвращает**:

-   `float`: Псевдослучайное число в диапазоне [0, 1).

**Как работает функция**:

1.  **Вычисление значения**: Вычисляет новое значение на основе seed, multiplier, addend и modulus.
2.  **Нормализация**: Нормализует результат в диапазон [0, 1).

```
Начало
↓
Вычисление нового значения: a = seed * multiplier + addend
↓
Нормализация: a % modulus / modulus
↓
Конец
```

**Примеры**:

```python
# Пример использования prng_general
seed = 1
multiplier = 1664525
addend = 1013904223
modulus = 2**32
result = prng_general(seed, multiplier, addend, modulus)
print(result)
```

### `generate_challenge_seed`

```python
def generate_challenge_seed(l):
    """Генерирует seed для challenge на основе входных данных.

    Args:
        l (dict): Входные данные для генерации seed.

    Returns:
        int: Seed для challenge.
    """
```

**Назначение**: Функция `generate_challenge_seed` генерирует seed для challenge на основе входных данных.

**Параметры**:

-   `l` (dict): Входные данные для генерации seed.

**Возвращает**:

-   `int`: Seed для challenge.

**Как работает функция**:

1.  **Преобразование в строку**: Преобразует входные данные в строку с использованием `deterministic_stringify`.
2.  **Кодирование URL**: Кодирует строку для использования в URL.
3.  **Вычисление хеша**: Вычисляет хеш строки с использованием `simple_hash`.

```
Начало
↓
Преобразование в строку: deterministic_stringify(l)
↓
Кодирование URL
↓
Вычисление хеша: simple_hash(строка)
↓
Конец
```

**Примеры**:

```python
# Пример использования generate_challenge_seed
data = {"a": 1, "b": 2}
result = generate_challenge_seed(data)
print(result)
```

### `simple_hash`

```python
def simple_hash(s):
    """Вычисляет простой хеш строки.

    Args:
        s (str): Строка для вычисления хеша.

    Returns:
        int: Хеш строки.
    """
```

**Назначение**: Функция `simple_hash` вычисляет простой хеш строки.

**Параметры**:

-   `s` (str): Строка для вычисления хеша.

**Возвращает**:

-   `int`: Хеш строки.

**Как работает функция**:

1.  **Инициализация хеша**: Устанавливает начальное значение хеша равным 0.
2.  **Итерация по символам**: Итерируется по символам в строке.
3.  **Вычисление хеша**: Вычисляет хеш на основе кода символа.

```
Начало
↓
Инициализация хеша: d = 0
↓
Итерация по символам строки
↓
Вычисление хеша: d = ((d << 5) - d + ord(char[0])) & 0xFFFFFFFF
↓
Конец
```

**Примеры**:

```python
# Пример использования simple_hash
string = "example"
result = simple_hash(string)
print(result)
```

### `generate_challenge`

```python
def generate_challenge(obj, **kwargs):
    """Генерирует challenge на основе входных данных и параметров.

    Args:
        obj (dict): Входные данные для генерации challenge.
        **kwargs: Параметры для prng_general.

    Returns:
        float: Сгенерированный challenge.
    """
```

**Назначение**: Функция `generate_challenge` генерирует challenge на основе входных данных и параметров.

**Параметры**:

-   `obj` (dict): Входные данные для генерации challenge.
-   `**kwargs`: Параметры для `prng_general`.

**Возвращает**:

-   `float`: Сгенерированный challenge.

**Как работает функция**:

1.  **Генерация seed**: Генерирует seed с использованием `generate_challenge_seed`.
2.  **Генерация псевдослучайного числа**: Генерирует псевдослучайное число с использованием `prng_general`.

```
Начало
↓
Генерация seed: generate_challenge_seed(obj)
↓
Генерация псевдослучайного числа: prng_general(seed, **kwargs)
↓
Конец
```

**Примеры**:

```python
# Пример использования generate_challenge
data = {"a": 1, "b": 2}
kwargs = {"multiplier": 1664525, "addend": 1013904223, "modulus": 2**32}
result = generate_challenge(data, **kwargs)
print(result)