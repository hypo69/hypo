# ToolBox_requests

## Обзор

Модуль `ToolBox_requests.py` содержит основной класс `ToolBox`, который используется для обработки запросов от пользователей Telegram-бота. Класс включает в себя функциональность для работы с текстом, изображениями, тарифами и свободным режимом. Модуль интегрирован с другими модулями проекта, такими как `BaseSettings.AuxiliaryClasses` и `ToolBox_n_networks`.

## Подробней

Этот модуль является центральным звеном в обработке запросов пользователей. Он содержит методы для различных типов запросов, таких как генерация текста, создание изображений, управление тарифами и работа в свободном режиме. Модуль использует другие классы и функции из проекта для выполнения этих задач, такие как `PromptsCompressor` для сжатия подсказок и `neural_networks` для работы с нейронными сетями.

## Классы

### `ToolBox`

**Описание**: Класс `ToolBox` является основным классом, который обрабатывает запросы пользователей Telegram-бота. Он включает в себя методы для работы с текстом, изображениями, тарифами и свободным режимом.

**Методы**:
- `__init__`: Инициализация класса `ToolBox`.
- `Text_types`: Обрабатывает выбор типа текста.
- `Basic_tariff`: Обрабатывает запрос на подключение базового тарифа.
- `Pro_tariff`: Обрабатывает запрос на подключение профессионального тарифа.
- `TextCommands`: Обрабатывает текстовые команды.
- `SomeTextsCommand`: Обрабатывает команды для нескольких текстов.
- `ImageCommand`: Обрабатывает команды для генерации изображений.
- `Image_Regen_And_Upscale`: Обрабатывает команды для регенерации и улучшения изображений.
- `FreeCommand`: Обрабатывает команды для свободного режима.
- `__gpt_4o_mini`: (Private) Обрабатывает запросы к GPT 4o mini.
- `__FLUX_schnell`: (Private) Обрабатывает запросы к FLUX schnell.

#### `__init__`

```python
def __init__(self):
    """
    Инициализация класса ToolBox.

    Args:
        self (ToolBox): Экземпляр класса ToolBox.

    Returns:
        None

    Raises:
        None

    Example:
        >>> toolbox = ToolBox()
    """
```

**Описание**: Инициализирует класс `ToolBox`, устанавливает начальные значения для кнопок, загружает подсказки из файла, инициализирует Telegram-бота и определяет лямбда-функции для различных действий.

#### `Text_types`

```python
def Text_types(self, message):
    """
    Обрабатывает выбор типа текста.

    Args:
        message (telebot.types.Message): Объект сообщения Telegram.

    Returns:
        telebot.types.Message: Отредактированное сообщение с вариантами типов текста.

    Raises:
        None

    Example:
        >>> toolbox = ToolBox()
        >>> message = telebot.types.Message(chat=telebot.types.Chat(id=123), message_id=456, date=1678886400)
        >>> toolbox.Text_types(message)
    """
```

**Описание**: Отображает пользователю варианты типов текста для выбора.

#### `Basic_tariff`

```python
def Basic_tariff(self, message):
    """
    Обрабатывает запрос на подключение базового тарифа.

    Args:
        message (telebot.types.Message): Объект сообщения Telegram.

    Returns:
        None

    Raises:
        None

    Example:
        >>> toolbox = ToolBox()
        >>> message = telebot.types.Message(chat=telebot.types.Chat(id=123), message_id=456, date=1678886400)
        >>> toolbox.Basic_tariff(message)
    """
```

**Описание**: Отправляет пользователю счет для оплаты базового тарифа.

#### `Pro_tariff`

```python
def Pro_tariff(self, message):
    """
    Обрабатывает запрос на подключение профессионального тарифа.

    Args:
        message (telebot.types.Message): Объект сообщения Telegram.

    Returns:
        None

    Raises:
        None

    Example:
        >>> toolbox = ToolBox()
        >>> message = telebot.types.Message(chat=telebot.types.Chat(id=123), message_id=456, date=1678886400)
        >>> toolbox.Pro_tariff(message)
    """
```

**Описание**: Отправляет пользователю счет для оплаты профессионального тарифа.

#### `TextCommands`

```python
def TextCommands(self, message, ind: int):
    """
    Обрабатывает текстовые команды.

    Args:
        message (telebot.types.Message): Объект сообщения Telegram.
        ind (int): Индекс команды.

    Returns:
        tuple[int, int, int]: Кортеж, содержащий количество входящих токенов, исходящих токенов и 1.

    Raises:
        None

    Example:
        >>> toolbox = ToolBox()
        >>> message = telebot.types.Message(chat=telebot.types.Chat(id=123), text="Some text", message_id=456, date=1678886400)
        >>> toolbox.TextCommands(message, 0)
    """
```

**Описание**: Обрабатывает текстовые команды, отправляет запрос на ввод дополнительных параметров, формирует подсказку и отправляет её в модель GPT 4o mini.

#### `SomeTextsCommand`

```python
def SomeTextsCommand(self, message, ind: int, tokens: dict[str, int]):
    """
    Обрабатывает команды для нескольких текстов.

    Args:
        message (telebot.types.Message): Объект сообщения Telegram.
        ind (int): Индекс команды.
        tokens (dict[str, int]): Словарь с информацией о токенах.

    Returns:
        tuple[int, int, int]: Кортеж, содержащий количество входящих токенов, исходящих токенов и количество обработанных текстов.

    Raises:
        None

    Example:
        >>> toolbox = ToolBox()
        >>> message = telebot.types.Message(chat=telebot.types.Chat(id=123), text="2", message_id=456, date=1678886400)
        >>> tokens = {'incoming_tokens': 1000, 'outgoing_tokens': 1000, 'free_requests': 10}
        >>> toolbox.SomeTextsCommand(message, 0, tokens)
    """
```

**Описание**: Обрабатывает команды для нескольких текстов, запрашивает у пользователя текст и параметры, формирует подсказку и отправляет её в модель GPT 4o mini для каждого текста.

#### `ImageCommand`

```python
def ImageCommand(self, message, prompt: str, size: list[int]):
    """
    Обрабатывает команды для генерации изображений.

    Args:
        message (telebot.types.Message): Объект сообщения Telegram.
        prompt (str): Текст запроса для генерации изображения.
        size (list[int]): Размеры изображения.

    Returns:
        int: Случайное число, используемое в качестве seed для генерации изображения.

    Raises:
        None

    Example:
        >>> toolbox = ToolBox()
        >>> message = telebot.types.Message(chat=telebot.types.Chat(id=123), text="Generate image", message_id=456, date=1678886400)
        >>> toolbox.ImageCommand(message, "cat", [512, 512])
    """
```

**Описание**: Обрабатывает команды для генерации изображений, генерирует случайное число для seed, вызывает метод `__FLUX_schnell` для генерации изображения и отображает кнопки для дальнейших действий с изображением.

#### `Image_Regen_And_Upscale`

```python
def Image_Regen_And_Upscale(self, message, prompt: str, size: list[int], seed, num_inference_steps=4):
    """
    Обрабатывает команды для регенерации и улучшения изображений.

    Args:
        message (telebot.types.Message): Объект сообщения Telegram.
        prompt (str): Текст запроса для генерации изображения.
        size (list[int]): Размеры изображения.
        seed (int): Seed для генерации изображения.
        num_inference_steps (int, optional): Количество шагов для улучшения изображения. По умолчанию 4.

    Returns:
        None

    Raises:
        None

    Example:
        >>> toolbox = ToolBox()
        >>> message = telebot.types.Message(chat=telebot.types.Chat(id=123), text="Regenerate image", message_id=456, date=1678886400)
        >>> toolbox.Image_Regen_And_Upscale(message, "cat", [512, 512], 12345)
    """
```

**Описание**: Обрабатывает команды для регенерации и улучшения изображений, вызывает метод `__FLUX_schnell` для выполнения этих действий.

#### `FreeCommand`

```python
def FreeCommand(self, message, prompts: list[str]):
    """
    Обрабатывает команды для свободного режима.

    Args:
        message (telebot.types.Message): Объект сообщения Telegram.
        prompts (list[str]): Список подсказок.

    Returns:
        tuple[int, int, list[str]]: Кортеж, содержащий количество входящих токенов, исходящих токенов и обновленный список подсказок.

    Raises:
        None

    Example:
        >>> toolbox = ToolBox()
        >>> message = telebot.types.Message(chat=telebot.types.Chat(id=123), text="Some text", message_id=456, date=1678886400)
        >>> toolbox.FreeCommand(message, [])
    """
```

**Описание**: Обрабатывает команды для свободного режима, добавляет текст пользователя в список подсказок, вызывает метод `__gpt_4o_mini` для получения ответа от модели и возвращает обновленный список подсказок.

#### `__gpt_4o_mini`

```python
def __gpt_4o_mini(self, prompt: list[dict], message) -> tuple[dict[str, str], int, int]:
    """
    Обрабатывает запросы к GPT 4o mini.

    Args:
        prompt (list[dict]): Список подсказок в формате словаря.
        message (telebot.types.Message): Объект сообщения Telegram.

    Returns:
        tuple[dict[str, str], int, int]: Кортеж, содержащий ответ от модели, количество входящих токенов и количество исходящих токенов.

    Raises:
        None

    Example:
        >>> toolbox = ToolBox()
        >>> message = telebot.types.Message(chat=telebot.types.Chat(id=123), text="Some text", message_id=456, date=1678886400)
        >>> toolbox.__gpt_4o_mini([{'role': 'user', 'content': 'Hello'}], message)
    """
```

**Описание**: (Private) Отправляет запрос в модель GPT 4o mini, получает ответ, извлекает количество входящих и исходящих токенов и возвращает их.

#### `__FLUX_schnell`

```python
def __FLUX_schnell(self, prompt: str, size: list[int], message, seed: int, num_inference_steps: int)-> None:
    """
    Обрабатывает запросы к FLUX schnell.

    Args:
        prompt (str): Текст запроса для генерации изображения.
        size (list[int]): Размеры изображения.
        message (telebot.types.Message): Объект сообщения Telegram.
        seed (int): Seed для генерации изображения.
        num_inference_steps (int): Количество шагов для генерации изображения.

    Returns:
        None

    Raises:
        None

    Example:
        >>> toolbox = ToolBox()
        >>> message = telebot.types.Message(chat=telebot.types.Chat(id=123), text="Generate image", message_id=456, date=1678886400)
        >>> toolbox.__FLUX_schnell("cat", [512, 512], message, 12345, 4)
    """
```

**Описание**: (Private) Отправляет запрос в модель FLUX schnell, получает изображение и отправляет его пользователю.