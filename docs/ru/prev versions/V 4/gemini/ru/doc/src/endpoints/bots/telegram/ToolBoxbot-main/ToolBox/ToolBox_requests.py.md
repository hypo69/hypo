# hypotez/src/endpoints/bots/telegram/ToolBoxbot-main/ToolBox/ToolBox_requests.py

## Обзор

Данный модуль содержит класс `ToolBox`, который является основным классом для обработки запросов в Telegram-боте. Класс включает в себя методы для работы с текстом, изображениями, тарифами и другими функциями бота.

## Подробней

`ToolBox_requests.py` является ключевым компонентом Telegram-бота, отвечающим за обработку различных типов запросов от пользователей. Он включает в себя функциональность для генерации текста и изображений, а также для управления тарифами и бесплатным режимом. Этот файл содержит класс `ToolBox`, который наследует от классов `keyboards` и `neural_networks`, предоставляя пользователю возможность взаимодействовать с ботом через удобные интерфейсы и использовать нейронные сети для генерации контента. Расположение файла в структуре проекта `hypotez` указывает на его роль как одной из основных точек входа для обработки запросов пользователей через Telegram.

## Классы

### `ToolBox`

**Описание**: Основной класс для обработки запросов в Telegram-боте.

**Методы**:
- `__init__`: Инициализация класса, загрузка текстов подсказок, инициализация Telegram-бота и определение функций для обработки различных запросов.
- `Text_types`: Отправляет пользователю сообщение с выбором типа текста.
- `Basic_tariff`: Отправляет пользователю информацию о базовом тарифе и предлагает его подключить.
- `Pro_tariff`: Отправляет пользователю информацию о профессиональном тарифе и предлагает его подключить.
- `TextCommands`: Обрабатывает команды для генерации текста на основе введенных пользователем данных.
- `SomeTextsCommand`: Обрабатывает команды для генерации нескольких текстов одновременно.
- `ImageCommand`: Обрабатывает команды для генерации изображений на основе введенного запроса и размера.
- `Image_Regen_And_Upscale`: Обрабатывает команды для регенерации и улучшения изображений.
- `FreeCommand`: Обрабатывает команды для работы в свободном режиме.
- `__gpt_4o_mini`: (Приватный метод) Обрабатывает запросы к модели GPT-4o mini.
- `__FLUX_schnell`: (Приватный метод) Обрабатывает запросы к модели FLUX schnell для генерации изображений.

**Параметры**:
- Нет явных параметров для класса, но используются параметры в методах класса.

**Примеры**
```python
# Пример инициализации класса ToolBox
toolbox = ToolBox()
```

## Функции

### `Text_types`

```python
def Text_types(self, message):
    """ This if example function
    Args:
        message: message

    Returns:
        dict | None: edit_message_text
    """
```

**Описание**: Отправляет пользователю сообщение с выбором типа текста.

**Параметры**:
- `message`: Объект сообщения от Telegram.

**Возвращает**:
- `None`: Редактирует сообщение с вариантами выбора типа текста.

**Примеры**:
```python
# Пример вызова функции Text_types
toolbox.Text_types(message)
```

### `Basic_tariff`

```python
def Basic_tariff(self, message):
    """ This if example function
    Args:
        message: message

    Returns:
        dict | None: send_invoice
    """
```

**Описание**: Отправляет пользователю информацию о базовом тарифе и предлагает его подключить.

**Параметры**:
- `message`: Объект сообщения от Telegram.

**Возвращает**:
- `None`: Отправляет счет на оплату базового тарифа.

**Примеры**:
```python
# Пример вызова функции Basic_tariff
toolbox.Basic_tariff(message)
```

### `Pro_tariff`

```python
def Pro_tariff(self, message):
    """ This if example function
    Args:
        message: message

    Returns:
        dict | None: send_invoice
    """
```

**Описание**: Отправляет пользователю информацию о профессиональном тарифе и предлагает его подключить.

**Параметры**:
- `message`: Объект сообщения от Telegram.

**Возвращает**:
- `None`: Отправляет счет на оплату профессионального тарифа.

**Примеры**:
```python
# Пример вызова функции Pro_tariff
toolbox.Pro_tariff(message)
```

### `TextCommands`

```python
def TextCommands(self, message, ind: int):
    """ This if example function
    Args:
        message: message
        ind (int): int

    Returns:
        dict | None: incoming_tokens, outgoing_tokens, 1
    """
```

**Описание**: Обрабатывает команды для генерации текста на основе введенных пользователем данных.

**Параметры**:
- `message`: Объект сообщения от Telegram.
- `ind` (int): Индекс команды.

**Возвращает**:
- `tuple[int, int, int]`: Количество входящих и исходящих токенов и 1.

**Примеры**:
```python
# Пример вызова функции TextCommands
toolbox.TextCommands(message, 0)
```

### `SomeTextsCommand`

```python
def SomeTextsCommand(self, message, ind: int, tokens: dict[str, int]):
    """ This if example function
    Args:
        message: message
        ind (int): int
        tokens (dict[str, int]): dict[str, int]

    Returns:
        dict | None: incoming_tokens, outgoing_tokens, n
    """
```

**Описание**: Обрабатывает команды для генерации нескольких текстов одновременно.

**Параметры**:
- `message`: Объект сообщения от Telegram.
- `ind` (int): Индекс команды.
- `tokens` (dict[str, int]): Словарь с токенами.

**Возвращает**:
- `tuple[int, int, int]`: Количество входящих и исходящих токенов и количество сгенерированных текстов.

**Примеры**:
```python
# Пример вызова функции SomeTextsCommand
toolbox.SomeTextsCommand(message, 0, {'incoming_tokens': 1000, 'outgoing_tokens': 1000, 'free_requests': 10})
```

### `ImageCommand`

```python
def ImageCommand(self, message, prompt: str, size: list[int]):
    """ This if example function
    Args:
        message: message
        prompt (str): str
        size (list[int]): list[int]

    Returns:
        dict | None: seed
    """
```

**Описание**: Обрабатывает команды для генерации изображений на основе введенного запроса и размера.

**Параметры**:
- `message`: Объект сообщения от Telegram.
- `prompt` (str): Запрос для генерации изображения.
- `size` (list[int]): Список с размерами изображения.

**Возвращает**:
- `int`: Сгенерированный seed.

**Примеры**:
```python
# Пример вызова функции ImageCommand
toolbox.ImageCommand(message, "cat", [512, 512])
```

### `Image_Regen_And_Upscale`

```python
def Image_Regen_And_Upscale(self, message, prompt: str, size: list[int], seed, num_inference_steps=4):
    """ This if example function
    Args:
        message: message
        prompt (str): str
        size (list[int]): list[int]
        seed: seed
        num_inference_steps: num_inference_steps

    Returns:
        dict | None: self.__FLUX_schnell
    """
```

**Описание**: Обрабатывает команды для регенерации и улучшения изображений.

**Параметры**:
- `message`: Объект сообщения от Telegram.
- `prompt` (str): Запрос для генерации изображения.
- `size` (list[int]): Список с размерами изображения.
- `seed`: Seed для регенерации изображения.
- `num_inference_steps`: Количество шагов для улучшения изображения.

**Возвращает**:
- `None`:

**Примеры**:
```python
# Пример вызова функции Image_Regen_And_Upscale
toolbox.Image_Regen_And_Upscale(message, "cat", [512, 512], 12345)
```

### `FreeCommand`

```python
def FreeCommand(self, message, prompts: list[str]):
    """ This if example function
    Args:
        message: message
        prompts (list[str]): list[str]

    Returns:
        dict | None: incoming_tokens, outgoing_tokens, prompts
    """
```

**Описание**: Обрабатывает команды для работы в свободном режиме.

**Параметры**:
- `message`: Объект сообщения от Telegram.
- `prompts` (list[str]): Список запросов.

**Возвращает**:
- `tuple[int, int, list[str]]`: Количество входящих и исходящих токенов и список запросов.

**Примеры**:
```python
# Пример вызова функции FreeCommand
toolbox.FreeCommand(message, [])