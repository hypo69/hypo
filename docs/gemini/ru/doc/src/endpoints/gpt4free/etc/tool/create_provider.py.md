# Модуль для создания нового провайдера g4f

## Обзор

Этот модуль предназначен для автоматического создания нового провайдера для библиотеки `g4f` на основе предоставленной команды cURL. Он принимает имя провайдера, запрашивает команду cURL у пользователя, генерирует код провайдера с использованием модели `gpt-4o` и сохраняет его в соответствующий файл.

## Подробнее

Модуль состоит из нескольких функций и логических блоков, которые обеспечивают создание нового провайдера на основе команды cURL. Основная цель - упростить процесс добавления новых провайдеров в библиотеку `g4f` путем автоматической генерации большей части необходимого кода.

## Функции

### `read_code`

```python
def read_code(text):
    """Извлекает код Python из текстовой строки, содержащей блоки кода, размеченные обратными кавычками.

    Args:
        text (str): Текст для поиска блоков кода Python.

    Returns:
        str | None: Извлеченный код Python или None, если код не найден.
    """
    ...
```

**Как работает функция**:

1.  Функция принимает строку `text` в качестве аргумента.
2.  Использует регулярное выражение для поиска блоков кода Python, заключенных в тройные обратные кавычки (```). Регулярное выражение ищет блоки кода, которые начинаются с ```python или ```py.
3.  Если блок кода найден, функция возвращает извлеченный код.
4.  Если блок кода не найден, функция возвращает `None`.

```ascii
    Текст запроса (text)
    │
    └──> Поиск кода Python с помощью регулярного выражения
         │
         └──> Код найден?
              │
              ├──> Да: Извлечь код
              │    │
              │    └──> Вернуть извлеченный код
              │
              └──> Нет: Вернуть None
```

**Примеры**:

```python
text_with_code = "Some text ```python\nprint('Hello')\n```"
code = read_code(text_with_code)
print(code)  # Вывод: print('Hello')

text_without_code = "Some text without code"
code = read_code(text_without_code)
print(code)  # Вывод: None
```

### `input_command`

```python
def input_command():
    """Считывает многострочный ввод от пользователя до тех пор, пока не будет встречен символ EOF (End-of-File).

    Args:
        None

    Returns:
        str: Объединенная строка, содержащая все введенные строки.
    """
    ...
```

**Как работает функция**:

1.  Выводит сообщение пользователю с просьбой ввести или вставить команду cURL.
2.  Инициализирует пустой список `contents` для хранения введенных строк.
3.  Входит в бесконечный цикл, пока не будет встречен символ EOF (End-of-File).
4.  Внутри цикла пытается прочитать строку ввода с помощью функции `input()`.
5.  Если возникает исключение `EOFError`, цикл прерывается.
6.  Каждая введенная строка добавляется в список `contents`.
7.  После завершения ввода функция объединяет все строки из списка `contents` в одну строку, разделенную символами новой строки (`\n`).
8.  Возвращает объединенную строку.

```ascii
    Начало
    │
    └──> Вывод сообщения пользователю
    │
    └──> Инициализация списка contents
    │
    └──> Цикл чтения ввода
         │
         ├──> Попытка чтения строки
         │    │
         │    └──> EOFError?
         │         │
         │         ├──> Да: Выход из цикла
         │         │
         │         └──> Нет: Добавить строку в contents
         │
    └──> Объединение строк из contents
    │
    └──> Возврат объединенной строки
```

**Примеры**:

Пример использования в интерактивном режиме:

```python
# Пользователь вводит следующие строки:
# строка 1
# строка 2
# строка 3
# (Ctrl-D)

command = input_command()
print(command)  # Вывод: строка 1\nстрока 2\nстрока 3
```

## Основной код

### Запрос имени провайдера

```python
name = input("Name: ")
```

Запрашивает у пользователя имя нового провайдера.

### Определение пути к файлу провайдера

```python
provider_path = f"g4f/Provider/{name}.py"
```

Формирует путь к файлу, в котором будет сохранен код нового провайдера.

### Шаблон кода провайдера

```python
example = """
from __future__ import annotations

from aiohttp import ClientSession

from ..typing import AsyncResult, Messages
from .base_provider import AsyncGeneratorProvider, ProviderModelMixin
from .helper import format_prompt


class {name}(AsyncGeneratorProvider, ProviderModelMixin):
    label = ""
    url = "https://example.com"
    api_endpoint = "https://example.com/api/completion"
    working = True
    needs_auth = False
    supports_stream = True
    supports_system_message = True
    supports_message_history = True
    
    default_model = ''
    models = ['', '']
    
    model_aliases = {
        "alias1": "model1",
    }

   @classmethod
    def get_model(cls, model: str) -> str:
        if model in cls.models:
            return model
        elif model in cls.model_aliases:
            return cls.model_aliases[model]
        else:
            return cls.default_model

    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        **kwargs
    ) -> AsyncResult:
        model = cls.get_model(model)
        
        headers = {{
            "authority": "example.com",
            "accept": "application/json",
            "origin": cls.url,
            "referer": f"{{cls.url}}/chat",
        }}
        async with ClientSession(headers=headers) as session:
            prompt = format_prompt(messages)
            data = {{
                "prompt": prompt,
                "model": model,
            }}
            async with session.post(f"{{cls.url}}/api/chat", json=data, proxy=proxy) as response:
                response.raise_for_status()
                async for chunk in response.content:
                    if chunk:
                        yield chunk.decode()
"""
```

Определяет шаблон кода провайдера, который будет использоваться в качестве примера для `gpt-4o`.

### Проверка существования файла провайдера

```python
if not path.isfile(provider_path):
    command = input_command()

    prompt = f"""
Create a provider from a cURL command. The command is:
```bash
{command}
```
A example for a provider:
```python
{example}
```
The name for the provider class:
{name}
Replace "hello" with `format_prompt(messages)`.
And replace "gpt-3.5-turbo" with `model`.
"""

    print("Create code...")
    response = []
    for chunk in g4f.ChatCompletion.create(
        model=g4f.models.gpt_4o,
        messages=[{"role": "user", "content": prompt}],
        timeout=300,
        stream=True,
    ):
        print(chunk, end="", flush=True)
        response.append(chunk)
    print()
    response = "".join(response)

    if code := read_code(response):
        with open(provider_path, "w") as file:
            file.write(code)
        print("Saved at:", provider_path)
        with open("g4f/Provider/__init__.py", "a") as file:
            file.write(f"\nfrom .{name} import {name}")
else:
    with open(provider_path, "r") as file:
        code = file.read()
```

1.  Проверяет, существует ли файл провайдера по указанному пути.
2.  Если файл не существует:
    *   Запрашивает у пользователя команду cURL с помощью функции `input_command()`.
    *   Формирует запрос для модели `gpt-4o`, включающий команду cURL, пример кода провайдера и имя класса провайдера.
    *   Отправляет запрос к модели `gpt-4o` для генерации кода провайдера.
    *   Читает сгенерированный код из ответа модели.
    *   Извлекает код Python из ответа с помощью функции `read_code()`.
    *   Сохраняет извлеченный код в файл провайдера.
    *   Добавляет строку импорта для нового провайдера в файл `__init__.py` в каталоге `g4f/Provider/`.
3.  Если файл существует, читает код из файла.