# Модуль neural_networks

## Обзор

Модуль `neural_networks` предоставляет класс `neural_networks`, который содержит методы для взаимодействия с различными нейронными сетями. Включает методы для генерации изображений на основе текстовых запросов и обработки текстовых сообщений с использованием различных моделей, таких как FLUX.1-schnell, Mistral и GPT-4o-mini.

## Подробней

Этот модуль используется для упрощения взаимодействия с различными API нейронных сетей, абстрагируя детали реализации каждого API. Это позволяет легко переключаться между различными моделями и сервисами, а также обеспечивает централизованное управление параметрами и аутентификацией.

## Классы

### `neural_networks`

**Описание**: Класс, содержащий методы для работы с различными нейронными сетями.

**Методы**:
- `_FLUX_schnell`: Отправляет запрос к модели FLUX.1-schnell для генерации изображения на основе текстового запроса.
- `__mistral_large_2407`: Отправляет запрос к модели Mistral для обработки текстовых сообщений.
- `_free_gpt_4o_mini`: Отправляет запрос к модели GPT-4o-mini для обработки текстовых сообщений.

## Функции

### `_FLUX_schnell`

```python
def _FLUX_schnell(self, prompt: str, size: list[int, int], seed: int, num_inference_steps: int) -> str|None:
    """
    Args:
        prompt (str): Текстовый запрос для генерации изображения.
        size (list[int, int]): Список с шириной и высотой изображения.
        seed (int): Зерно для генерации случайных чисел.
        num_inference_steps (int): Количество шагов для генерации изображения.

    Returns:
        str | None: Объект `Image` с сгенерированным изображением или `None` в случае ошибки.
    """
```

**Описание**: Отправляет запрос к API black-forest-labs/FLUX.1-schnell для генерации изображения на основе текстового запроса.

**Параметры**:
- `prompt` (str): Текстовый запрос для генерации изображения.
- `size` (list[int, int]): Список с шириной и высотой изображения (ширина, высота).
- `seed` (int): Зерно для генерации случайных чисел.
- `num_inference_steps` (int): Количество шагов для генерации изображения.

**Возвращает**:
- `str | None`: Объект `Image` с сгенерированным изображением или `None` в случае ошибки.

**Примеры**:

```python
# Пример вызова функции (предполагается наличие экземпляра класса neural_networks)
# image = neural_networks_instance._FLUX_schnell("A futuristic cityscape", [512, 512], 123, 50)
# if image:
#     image.save("futuristic_cityscape.png")
# else:
#     print("Не удалось сгенерировать изображение.")
```

### `__mistral_large_2407`

```python
def __mistral_large_2407(self, prompt: list[dict[str, str]]) -> tuple[str, int, int]|str:
    """
    Args:
        prompt (list[dict[str, str]]): Список словарей с текстовыми сообщениями.

    Returns:
        tuple[str, int, int] | str: Кортеж, содержащий ответ, количество использованных токенов в запросе и в ответе, или строку с сообщением об ошибке.
    """
```

**Описание**: Отправляет запрос к API Mistral для обработки текстовых сообщений.

**Параметры**:
- `prompt` (list[dict[str, str]]): Список словарей, где каждый словарь содержит ключ "content" с текстом сообщения.

**Возвращает**:
- `tuple[str, int, int] | str`: Кортеж, содержащий ответ, количество использованных токенов в запросе и в ответе, или строку с сообщением об ошибке.

**Примеры**:

```python
# Пример вызова функции (предполагается наличие экземпляра класса neural_networks)
# prompt = [{"role": "user", "content": "Explain the theory of relativity."}]
# response, prompt_tokens, completion_tokens = neural_networks_instance.__mistral_large_2407(prompt)
# print(f"Ответ: {response}")
# print(f"Токены в запросе: {prompt_tokens}, токены в ответе: {completion_tokens}")
```

### `_free_gpt_4o_mini`

```python
def _free_gpt_4o_mini(self, prompt: list[dict[str, str]]) -> tuple[str, int, int]|str:
    """
    Args:
        prompt (list[dict[str, str]]): Список словарей с текстовыми сообщениями.

    Returns:
        tuple[str, int, int] | str: Кортеж, содержащий ответ, количество использованных токенов в запросе и в ответе, или результат вызова `__mistral_large_2407` в случае ошибки.
    """
```

**Описание**: Отправляет запрос к API GPT-4o-mini для обработки текстовых сообщений. Если запрос не удаётся, использует `__mistral_large_2407`.

**Параметры**:
- `prompt` (list[dict[str, str]]): Список словарей, где каждый словарь содержит ключ "content" с текстом сообщения.

**Возвращает**:
- `tuple[str, int, int] | str`: Кортеж, содержащий ответ, количество использованных токенов в запросе и в ответе, или результат вызова `__mistral_large_2407` в случае ошибки.

**Примеры**:

```python
# Пример вызова функции (предполагается наличие экземпляра класса neural_networks)
# prompt = [{"role": "user", "content": "Translate 'Hello, world!' to French."}]
# response, prompt_tokens, completion_tokens = neural_networks_instance._free_gpt_4o_mini(prompt)
# print(f"Ответ: {response}")
# print(f"Токены в запросе: {prompt_tokens}, токены в ответе: {completion_tokens}")