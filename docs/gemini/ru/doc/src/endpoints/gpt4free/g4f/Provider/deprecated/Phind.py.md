# Модуль `Phind`

## Обзор

Модуль `Phind` предоставляет асинхронный генератор для взаимодействия с сервисом `Phind.com`. Он предназначен для получения ответов на запросы, используя различные модели, включая `GPT-4` и `Phind-34B`. Модуль поддерживает потоковую передачу данных, сохранение истории сообщений и работу через прокси.

## Подробнее

Модуль использует асинхронные запросы для взаимодействия с API `Phind.com`. Он извлекает данные из веб-страницы, формирует запрос на основе истории сообщений и текущего запроса, а затем генерирует ответ, передаваемый по частям. Важной особенностью является функция генерации `challenge`, которая используется для защиты от автоматических запросов.
Расположение модуля в проекте `hypotez` указывает на его использование в качестве одного из провайдеров для получения ответов от AI-моделей.

## Классы

### `Phind`

**Описание**: Класс `Phind` является асинхронным генератором провайдера.

**Наследует**:
- `AsyncGeneratorProvider`: Наследует функциональность асинхронного генератора провайдера.

**Атрибуты**:
- `url` (str): URL сервиса `Phind.com`.
- `working` (bool): Указывает, находится ли провайдер в рабочем состоянии.
- `lockdown` (bool): Указывает, находится ли провайдер в режиме "lockdown".
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер сохранение истории сообщений.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от `Phind.com`.

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
    """
    Создает асинхронный генератор для получения ответов от Phind.com.

    Args:
        model (str): Название модели для использования (например, "gpt-4" или "Phind-34B").
        messages (Messages): Список сообщений, представляющих историю общения.
        proxy (str, optional): Адрес прокси-сервера для использования. По умолчанию `None`.
        timeout (int, optional): Максимальное время ожидания ответа в секундах. По умолчанию 120.
        creative_mode (bool, optional): Флаг, указывающий на включение креативного режима. По умолчанию `False`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий части ответа.

    Raises:
        RuntimeError: Если возникает ошибка на стороне сервера Phind.com.

    """
```

**Назначение**: Функция `create_async_generator` создает и возвращает асинхронный генератор, который взаимодействует с API `Phind.com` для получения ответов на основе предоставленных сообщений и параметров.

**Параметры**:
- `cls`: Ссылка на класс `Phind`.
- `model` (str): Название модели для использования (например, `"gpt-4"` или `"Phind-34B"`).
- `messages` (Messages): Список сообщений, представляющих историю общения. Каждое сообщение содержит роль (`user` или `assistant`) и контент.
- `proxy` (str, optional): Адрес прокси-сервера для использования. По умолчанию `None`.
- `timeout` (int, optional): Максимальное время ожидания ответа в секундах. По умолчанию `120`.
- `creative_mode` (bool, optional): Флаг, указывающий на включение креативного режима. По умолчанию `False`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий части ответа.

**Вызывает исключения**:
- `RuntimeError`: Если возникает ошибка на стороне сервера `Phind.com`.

**Как работает функция**:

1. **Подготовка заголовков**: Функция задает заголовки HTTP-запроса, включая `Accept`, `Origin`, `Referer`, `Sec-Fetch-Dest`, `Sec-Fetch-Mode` и `Sec-Fetch-Site`.

2. **Создание сессии**: Создается асинхронная сессия с использованием `StreamSession` для выполнения HTTP-запросов. При необходимости устанавливается прокси и таймаут.

3. **Получение challenge_seeds**: Функция выполняет GET-запрос к `https://www.phind.com/search?home=true` для получения `challenge_seeds` из HTML-кода страницы. Эти значения используются для генерации challenge.

4. **Подготовка данных запроса**: Функция подготавливает данные для POST-запроса, включая текущий вопрос, историю вопросов и ответов, параметры запроса (дата, язык, режим и т.д.) и контекст.
   - Извлекает контент из сообщений с ролью `"user"` и `"assistant"`.
   - Устанавливает параметры, такие как `date`, `language`, `detailed`, `anonUserId`, `answerModel` и `creativeMode`.
   - Если модель начинается с `"gpt-4"`, то используется `"GPT-4"`, иначе `"Phind-34B"`.

5. **Генерация challenge**: Функция генерирует `challenge` с использованием функции `generate_challenge` и полученных `challenge_seeds`.

6. **Выполнение POST-запроса**: Функция выполняет POST-запрос к `https://https.api.phind.com/infer/` с подготовленными данными и заголовками.

7. **Обработка ответа**: Функция итерируется по строкам ответа, полученным от сервера.

   - Если строка начинается с `b"data: "`, то извлекается полезная нагрузка.
   - Если полезная нагрузка начинается с `b'<PHIND_DONE/>'`, то генерация завершается.
   - Если полезная нагрузка начинается с `b'<PHIND_BACKEND_ERROR>'`, то вызывается исключение `RuntimeError`.
   - Игнорируются строки, начинающиеся с `b'<PHIND_WEBRESULTS>'`, `b'<PHIND_FOLLOWUP>'`, `b"<PHIND_METADATA>"` или `b"<PHIND_INDICATOR>"`.
   - Если строка начинается с `<PHIND_SPAN_BEGIN>` или `<PHIND_SPAN_END>`, то игнорируется
   - В противном случае полезная нагрузка декодируется и выдается как часть ответа.

```
A: Подготовка заголовков и создание асинхронной сессии
|
B: GET-запрос к https://www.phind.com/search?home=true и извлечение challenge_seeds
|
C: Подготовка данных запроса (question, question_history, answer_history, options, context)
|
D: Генерация challenge с использованием challenge_seed
|
E: POST-запрос к https://https.api.phind.com/infer/ с данными и заголовками
|
F: Итерация по строкам ответа и выдача частей ответа или обработка ошибок
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict

async def main():
    model = "gpt-4"
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Напиши функцию на Python, которая вычисляет факториал числа."},
    ]
    proxy = None
    timeout = 120
    creative_mode = False

    generator = await Phind.create_async_generator(model, messages, proxy, timeout, creative_mode)
    async for chunk in generator:
        print(chunk, end="")

asyncio.run(main())
```

```python
# Пример использования create_async_generator с прокси
import asyncio
from typing import List, Dict

async def main():
    model = "Phind-34B"
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Объясни, что такое машинное обучение."},
    ]
    proxy = "http://your_proxy:8080"
    timeout = 120
    creative_mode = True

    generator = await Phind.create_async_generator(model, messages, proxy, timeout, creative_mode)
    async for chunk in generator:
        print(chunk, end="")

asyncio.run(main())
```

### `deterministic_stringify`

```python
def deterministic_stringify(obj):
    """
    Преобразует объект в детерминированную строку JSON.

    Args:
        obj (dict): Объект для преобразования.

    Returns:
        str: Детерминированная строка JSON.

    """
```

**Назначение**: Функция `deterministic_stringify` преобразует объект (словарь) в детерминированную строку JSON, где порядок ключей всегда одинаков. Это необходимо для обеспечения воспроизводимости при генерации `challenge`.

**Параметры**:
- `obj` (dict): Объект (словарь) для преобразования.

**Возвращает**:
- `str`: Детерминированная строка JSON.

**Как работает функция**:

1. **Внутренняя функция `handle_value`**:
   - Определяет тип значения и обрабатывает его соответствующим образом.
   - Для списков и словарей рекурсивно вызывает `deterministic_stringify`.
   - Преобразует булевы значения в `"true"` или `"false"`.
   - Преобразует числа в строки с фиксированной точностью (8 знаков после запятой) и удаляет лишние нули.
   - Преобразует строки, заключая их в двойные кавычки.
   - Возвращает `"null"` для других типов данных.

2. **Сортировка элементов**:
   - Сортирует элементы словаря по ключам.

3. **Формирование строки**:
   - Преобразует каждый элемент в строку вида `"ключ:значение"`.
   - Объединяет строки элементов через запятую.

```
A: Сортировка элементов словаря по ключам
|
B: Преобразование каждого элемента в строку "ключ:значение" с использованием handle_value
|
C: Объединение строк элементов через запятую
```

**Примеры**:

```python
# Пример использования deterministic_stringify
obj = {"b": 2, "a": 1, "c": {"f": 6, "e": 5}}
result = deterministic_stringify(obj)
print(result)  # Вывод: a:1.00000000,b:2.00000000,c:{e:5.00000000,f:6.00000000}
```

```python
# Пример использования deterministic_stringify с булевыми значениями
obj = {"x": True, "y": False}
result = deterministic_stringify(obj)
print(result)  # Вывод: x:true,y:false
```

### `prng_general`

```python
def prng_general(seed, multiplier, addend, modulus):
    """
    Генерирует псевдослучайное число с использованием общего алгоритма PRNG.

    Args:
        seed (int): Начальное значение.
        multiplier (int): Множитель.
        addend (int): Приращение.
        modulus (int): Модуль.

    Returns:
        float: Псевдослучайное число в диапазоне [0, 1).

    """
```

**Назначение**: Функция `prng_general` генерирует псевдослучайное число с использованием общего алгоритма PRNG (Pseudo-Random Number Generator).

**Параметры**:
- `seed` (int): Начальное значение.
- `multiplier` (int): Множитель.
- `addend` (int): Приращение.
- `modulus` (int): Модуль.

**Возвращает**:
- `float`: Псевдослучайное число в диапазоне `[0, 1)`.

**Как работает функция**:

1. **Вычисление `a`**:
   - Вычисляет значение `a` как `seed * multiplier + addend`.

2. **Обработка отрицательных значений**:
   - Если `a` меньше `0`, то вычисляется `((a % modulus) - modulus) / modulus`.

3. **Вычисление псевдослучайного числа**:
   - Если `a` не меньше `0`, то вычисляется `(a % modulus) / modulus`.

```
A: Вычисление a = seed * multiplier + addend
|
B: Проверка, является ли a отрицательным
|
C: Если a < 0: вычисление ((a % modulus) - modulus) / modulus
|
D: Если a >= 0: вычисление (a % modulus) / modulus
```

**Примеры**:

```python
# Пример использования prng_general
seed = 12345
multiplier = 1103515245
addend = 12345
modulus = 2**31
result = prng_general(seed, multiplier, addend, modulus)
print(result)  # Вывод: 0.16341147422790527
```

```python
# Пример использования prng_general с другими параметрами
seed = 67890
multiplier = 1664525
addend = 1013904223
modulus = 2**32
result = prng_general(seed, multiplier, addend, modulus)
print(result)  # Вывод: 0.48224735260009766
```

### `generate_challenge_seed`

```python
def generate_challenge_seed(l):
    """
    Генерирует seed для challenge на основе списка.

    Args:
        l (list): Список для генерации seed.

    Returns:
        int: Seed для challenge.

    """
```

**Назначение**: Функция `generate_challenge_seed` генерирует seed для challenge на основе списка, преобразуя список в строку и вычисляя хеш.

**Параметры**:
- `l` (list): Список для генерации seed.

**Возвращает**:
- `int`: Seed для challenge.

**Как работает функция**:

1. **Преобразование в строку**:
   - Преобразует список `l` в детерминированную строку с использованием функции `deterministic_stringify`.

2. **Кодирование URL**:
   - Кодирует строку для использования в URL с помощью `parse.quote`.

3. **Вычисление хеша**:
   - Вычисляет хеш закодированной строки с помощью функции `simple_hash`.

```
A: Преобразование списка в детерминированную строку с использованием deterministic_stringify
|
B: Кодирование строки для URL с помощью parse.quote
|
C: Вычисление хеша закодированной строки с помощью simple_hash
```

**Примеры**:

```python
# Пример использования generate_challenge_seed
l = {"question": "hello", "options": {"language": "en-US"}}
result = generate_challenge_seed(l)
print(result)  # Вывод: -1062987937
```

```python
# Пример использования generate_challenge_seed с другим списком
l = {"question": "test", "options": {"language": "ru-RU"}}
result = generate_challenge_seed(l)
print(result)  # Вывод: 1431978065
```

### `simple_hash`

```python
def simple_hash(s):
    """
    Вычисляет простой хеш строки.

    Args:
        s (str): Строка для вычисления хеша.

    Returns:
        int: Хеш строки.

    """
```

**Назначение**: Функция `simple_hash` вычисляет простой хеш строки.

**Параметры**:
- `s` (str): Строка для вычисления хеша.

**Возвращает**:
- `int`: Хеш строки.

**Как работает функция**:

1. **Инициализация хеша**:
   - Инициализирует переменную `d` значением `0`.

2. **Итерация по символам строки**:
   - Итерируется по каждому символу в строке `s`.

3. **Проверка символа**:
   - Проверяет, что длина символа равна `1` и код символа меньше `256`.

4. **Вычисление хеша**:
   - Вычисляет новое значение хеша как `((d << 5) - d + ord(char[0])) & 0xFFFFFFFF`.

5. **Обработка переполнения**:
   - Если хеш больше `0x7FFFFFFF` (2147483647), вычитает `0x100000000` (2**32) из хеша.

```
A: Инициализация хеша d = 0
|
B: Итерация по символам строки
|
C: Проверка, что длина символа равна 1 и код символа меньше 256
|
D: Вычисление хеша: d = ((d << 5) - d + ord(char[0])) & 0xFFFFFFFF
|
E: Обработка переполнения: если d > 0x7FFFFFFF, то d -= 0x100000000
```

**Примеры**:

```python
# Пример использования simple_hash
s = "hello"
result = simple_hash(s)
print(result)  # Вывод: -1790097485
```

```python
# Пример использования simple_hash с другой строкой
s = "test"
result = simple_hash(s)
print(result)  # Вывод: 3556472
```

### `generate_challenge`

```python
def generate_challenge(obj, **kwargs):
    """
    Генерирует challenge на основе объекта и параметров.

    Args:
        obj (dict): Объект для генерации challenge.
        **kwargs: Дополнительные аргументы для prng_general.

    Returns:
        float: Challenge.

    """
```

**Назначение**: Функция `generate_challenge` генерирует challenge на основе объекта и дополнительных параметров, используя функции `generate_challenge_seed` и `prng_general`.

**Параметры**:
- `obj` (dict): Объект для генерации challenge.
- `**kwargs`: Дополнительные аргументы для `prng_general`.

**Возвращает**:
- `float`: Challenge.

**Как работает функция**:

1. **Генерация seed**:
   - Генерирует seed для challenge с помощью функции `generate_challenge_seed` на основе объекта `obj`.

2. **Генерация псевдослучайного числа**:
   - Генерирует псевдослучайное число с помощью функции `prng_general`, используя сгенерированный seed и дополнительные параметры `kwargs`.

```
A: Генерация seed для challenge с помощью generate_challenge_seed
|
B: Генерация псевдослучайного числа с помощью prng_general
```

**Примеры**:

```python
# Пример использования generate_challenge
obj = {"question": "hello", "options": {"language": "en-US"}}
kwargs = {"multiplier": 1103515245, "addend": 12345, "modulus": 2**31}
result = generate_challenge(obj, **kwargs)
print(result)  # Вывод: 0.7879973351955414
```

```python
# Пример использования generate_challenge с другими параметрами
obj = {"question": "test", "options": {"language": "ru-RU"}}
kwargs = {"multiplier": 1664525, "addend": 1013904223, "modulus": 2**32}
result = generate_challenge(obj, **kwargs)
print(result)  # Вывод: 0.21942591667175293