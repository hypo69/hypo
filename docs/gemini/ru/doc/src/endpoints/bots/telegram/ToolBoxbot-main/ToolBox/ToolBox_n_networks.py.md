# Модуль `ToolBox_n_networks.py`

## Обзор

Модуль `ToolBox_n_networks.py` содержит класс `neural_networks`, который предоставляет методы для взаимодействия с различными нейронными сетями через API. В частности, он включает методы для генерации изображений на основе текстовых запросов и для получения текстовых ответов от языковых моделей.

## Подробней

Этот модуль предоставляет интерфейс для выполнения запросов к различным API нейронных сетей, таким как FLUX.1-schnell для генерации изображений и Mistral Large 2407, free gpt-4o-mini для получения текстовых ответов. Он использует библиотеки `requests` для отправки HTTP-запросов, `json` для обработки JSON-ответов, `os` для доступа к переменным окружения, `io` для работы с потоками ввода-вывода и `PIL` (Pillow) для обработки изображений.

Модуль предназначен для использования в проектах, где требуется интеграция с нейронными сетями для автоматической генерации контента или обработки текстовых данных.

## Классы

### `neural_networks`

**Описание**:
Класс `neural_networks` предоставляет методы для взаимодействия с различными нейронными сетями.

**Методы**:
- `_FLUX_schnell`: Отправляет запрос к API FLUX.1-schnell для генерации изображения на основе текстового запроса.
- `__mistral_large_2407`: Отправляет запрос к API Mistral Large 2407 для получения текстового ответа на основе списка сообщений.
- `_free_gpt_4o_mini`: Отправляет запрос к API free gpt-4o-mini для получения текстового ответа на основе списка сообщений.

## Функции

### `_FLUX_schnell`

```python
def _FLUX_schnell(self, prompt: str, size: list[int, int], seed: int, num_inference_steps: int) -> str|None:
    """
    Args:
        prompt (str): Текстовый запрос для генерации изображения.
        size (list[int, int]): Размеры изображения (ширина, высота).
        seed (int): Зерно для генерации случайных чисел.
        num_inference_steps (int): Количество шагов для генерации изображения.

    Returns:
        str|None: Объект `Image` с сгенерированным изображением или `None` в случае ошибки.

    Raises:
        requests.exceptions.RequestException: Если возникает ошибка при отправке запроса к API.

    Example:
        >>> from PIL import Image
        >>> nn = neural_networks()
        >>> image = nn._FLUX_schnell("a cat", [512, 512], 123, 50)
        >>> if image:
        ...     image.save("cat.png")
    """
```

**Описание**:
Отправляет запрос к API FLUX.1-schnell для генерации изображения на основе текстового запроса.

**Параметры**:
- `prompt` (str): Текстовый запрос для генерации изображения.
- `size` (list[int, int]): Размеры изображения (ширина, высота).
- `seed` (int): Зерно для генерации случайных чисел.
- `num_inference_steps` (int): Количество шагов для генерации изображения.

**Возвращает**:
- `str|None`: Объект `Image` с сгенерированным изображением или `None` в случае ошибки.

**Вызывает исключения**:
- `requests.exceptions.RequestException`: Если возникает ошибка при отправке запроса к API.

### `__mistral_large_2407`

```python
def __mistral_large_2407(self, prompt: list[dict[str, str]]) -> tuple[str, int, int]|str:
    """
    Args:
        prompt (list[dict[str, str]]): Список сообщений для отправки в API.

    Returns:
        tuple[str, int, int]|str: Кортеж, содержащий текстовое сообщение, количество токенов в запросе и количество токенов в ответе, или строка с ошибкой.

    Raises:
        requests.exceptions.RequestException: Если возникает ошибка при отправке запроса к API.

    Example:
        >>> nn = neural_networks()
        >>> prompt = [{"role": "user", "content": "What is the capital of France?"}]
        >>> response, prompt_tokens, completion_tokens = nn.__mistral_large_2407(prompt)
        >>> print(response)
        {'role': 'assistant', 'content': 'The capital of France is Paris.'}
    """
```

**Описание**:
Отправляет запрос к API Mistral Large 2407 для получения текстового ответа на основе списка сообщений.

**Параметры**:
- `prompt` (list[dict[str, str]]): Список сообщений для отправки в API.

**Возвращает**:
- `tuple[str, int, int]|str`: Кортеж, содержащий текстовое сообщение, количество токенов в запросе и количество токенов в ответе, или строка с ошибкой.

**Вызывает исключения**:
- `requests.exceptions.RequestException`: Если возникает ошибка при отправке запроса к API.

### `_free_gpt_4o_mini`

```python
def _free_gpt_4o_mini(self, prompt: list[dict[str, str]]) -> tuple[str, int, int]|str:
    """
    Args:
        prompt (list[dict[str, str]]): Список сообщений для отправки в API.

    Returns:
        tuple[str, int, int]|str: Кортеж, содержащий текстовое сообщение, количество токенов в запросе и количество токенов в ответе, или строка с ошибкой.

    Raises:
        requests.exceptions.RequestException: Если возникает ошибка при отправке запроса к API.

    Example:
        >>> nn = neural_networks()
        >>> prompt = [{"role": "user", "content": "What is the capital of Germany?"}]
        >>> response, prompt_tokens, completion_tokens = nn._free_gpt_4o_mini(prompt)
        >>> print(response)
        {'role': 'assistant', 'content': 'The capital of Germany is Berlin.'}
    """
```

**Описание**:
Отправляет запрос к API free gpt-4o-mini для получения текстового ответа на основе списка сообщений.

**Параметры**:
- `prompt` (list[dict[str, str]]): Список сообщений для отправки в API.

**Возвращает**:
- `tuple[str, int, int]|str`: Кортеж, содержащий текстовое сообщение, количество токенов в запросе и количество токенов в ответе, или строка с ошибкой.

**Вызывает исключения**:
- `requests.exceptions.RequestException`: Если возникает ошибка при отправке запроса к API.