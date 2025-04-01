# Документация для `base_provider.py`

## Обзор

Модуль `base_provider.py` определяет базовые классы и типы, используемые для взаимодействия с различными провайдерами в проекте `hypotez`. Он предоставляет основу для создания и управления провайдерами, обработки запросов и ответов, а также для поддержки потоковой передачи данных.

## Содержание

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
    - [`BaseProvider`](#BaseProvider)
    - [`AsyncProvider`](#AsyncProvider)
    - [`ProviderUtils`](#ProviderUtils)
- [Импортированные модули](#Импортированные-модули)

## Подробнее

Этот модуль служит основой для реализации различных провайдеров, обеспечивая единообразный интерфейс для взаимодействия с ними. Он определяет абстрактные классы, которые должны быть реализованы конкретными провайдерами, а также вспомогательные функции и классы для упрощения разработки.

## Импортированные модули

В данном файле импортируются следующие модули:

- `..providers.base_provider`: Импортирует базовые классы провайдеров, определенные в родительском каталоге.
- `..providers.types`: Импортирует типы данных, используемые для работы с провайдерами, такие как `Streaming`.
- `..providers.response`: Импортирует классы для представления ответов от провайдеров, такие как `BaseConversation`, `Sources`, `FinishReason`.
- `.helper`: Импортирует вспомогательные функции из локального модуля `helper`, такие как `get_cookies` и `format_prompt`.

## Классы

### `BaseProvider`

**Описание**: Базовый класс для всех провайдеров.

**Принцип работы**: Этот класс является абстрактным и предоставляет общую структуру для провайдеров. Он определяет основные методы, которые должны быть реализованы в дочерних классах, такие как `create_completion`, `create_conversation` и другие.

**Методы**:

- `__init__(self, **kwargs: Any)`:
   ```python
   def __init__(self, **kwargs: Any):
        """Инициализирует экземпляр класса BaseProvider.

        Args:
            **kwargs (Any): Произвольные аргументы ключевых слов.
        """
   ```

- `create_completion(self, prompt: str, stream: bool = False, **kwargs: Any) -> str | Generator[str, None, None] | None`:
   ```python
   def create_completion(self, prompt: str, stream: bool = False, **kwargs: Any) -> str | Generator[str, None, None] | None:
        """Создает завершение на основе предоставленного запроса.

        Args:
            prompt (str): Запрос для создания завершения.
            stream (bool, optional): Если `True`, возвращает генератор для потоковой передачи данных. По умолчанию `False`.
            **kwargs (Any): Дополнительные аргументы для создания завершения.

        Returns:
            str | Generator[str, None, None] | None: Завершенный текст или генератор потока текста, или None в случае ошибки.
        """
   ```

- `create_conversation(self, messages: list[dict[str, str]], stream: bool = False, **kwargs: Any) -> BaseConversation | None`:
   ```python
   def create_conversation(self, messages: list[dict[str, str]], stream: bool = False, **kwargs: Any) -> BaseConversation | None:
        """Создает разговор на основе предоставленных сообщений.

        Args:
            messages (list[dict[str, str]]): Список сообщений для создания разговора.
            stream (bool, optional): Если `True`, возвращает генератор для потоковой передачи данных. По умолчанию `False`.
            **kwargs (Any): Дополнительные аргументы для создания разговора.

        Returns:
            BaseConversation | None: Объект разговора или None в случае ошибки.
        """
   ```

- `supports_streaming(self) -> bool`:
   ```python
   def supports_streaming(self) -> bool:
        """Проверяет, поддерживает ли провайдер потоковую передачу данных.

        Returns:
            bool: `True`, если провайдер поддерживает потоковую передачу данных, `False` в противном случае.
        """
   ```

- `get_sources(self, response: str, prompt: str, **kwargs: Any) -> Sources | None`:
   ```python
   def get_sources(self, response: str, prompt: str, **kwargs: Any) -> Sources | None:
        """Извлекает источники для предоставленного ответа.

        Args:
            response (str): Ответ для извлечения источников.
            prompt (str): Исходный запрос.
            **kwargs (Any): Дополнительные аргументы для извлечения источников.

        Returns:
            Sources | None: Объект источников или None, если источники не найдены.
        """
   ```

- `report(self, data: dict[str, str]) -> None`:
   ```python
   def report(self, data: dict[str, str]) -> None:
        """Отправляет отчет о данных.

        Args:
            data (dict[str, str]): Данные для отправки в отчете.
        """
   ```

- `convert_to_base_class(self, response: str, **kwargs: Any) -> BaseConversation`:
   ```python
   def convert_to_base_class(self, response: str, **kwargs: Any) -> BaseConversation:
        """Преобразует ответ в базовый класс разговора.

        Args:
            response (str): Ответ для преобразования.
            **kwargs (Any): Дополнительные аргументы для преобразования.

        Returns:
            BaseConversation: Объект BaseConversation.
        """
   ```

- `process_message(self, message: str) -> str`:
   ```python
   def process_message(self, message: str) -> str:
        """Обрабатывает сообщение.

        Args:
            message (str): Сообщение для обработки.

        Returns:
            str: Обработанное сообщение.
        """
   ```

- `get_cost(self, model: str, prompt_tokens: int, completion_tokens: int) -> float | None`:
   ```python
   def get_cost(self, model: str, prompt_tokens: int, completion_tokens: int) -> float | None:
        """Рассчитывает стоимость использования модели.

        Args:
            model (str): Название модели.
            prompt_tokens (int): Количество токенов в запросе.
            completion_tokens (int): Количество токенов в завершении.

        Returns:
            float | None: Стоимость использования модели или None, если стоимость не может быть рассчитана.
        """
   ```

- `check_response(self, response: str | None, prompt: str | None = None) -> None`:
   ```python
   def check_response(self, response: str | None, prompt: str | None = None) -> None:
        """Проверяет ответ на наличие ошибок.

        Args:
            response (str | None): Ответ для проверки.
            prompt (str | None, optional): Исходный запрос. По умолчанию None.
        """
   ```

- `adapt_model_name(self, model: str) -> str`:
   ```python
   def adapt_model_name(self, model: str) -> str:
        """Адаптирует название модели к формату, требуемому провайдером.

        Args:
            model (str): Название модели для адаптации.

        Returns:
            str: Адаптированное название модели.
        """
   ```

- `to_system(self) -> dict[str, str]`:
   ```python
   def to_system(self) -> dict[str, str]:
        """Преобразует настройки провайдера в формат системного сообщения.

        Returns:
            dict[str, str]: Словарь с настройками провайдера.
        """
   ```

- `to_user(self, messages: list[dict[str, str]]) -> list[dict[str, str]]`:
   ```python
   def to_user(self, messages: list[dict[str, str]]) -> list[dict[str, str]]:
        """Преобразует список сообщений в формат, требуемый провайдером.

        Args:
            messages (list[dict[str, str]]): Список сообщений для преобразования.

        Returns:
            list[dict[str, str]]: Преобразованный список сообщений.
        """
   ```

- `get_token_price(self, model: str, is_input: bool) -> float`:
   ```python
   def get_token_price(self, model: str, is_input: bool) -> float:
        """Получает цену токена для указанной модели.

        Args:
            model (str): Название модели.
            is_input (bool): Определяет, является ли токен входным или выходным.

        Returns:
            float: Цена токена.
        """
   ```

- `max_model_tokens(self, model: str) -> int | None`:
   ```python
   def max_model_tokens(self, model: str) -> int | None:
        """Возвращает максимальное количество токенов, поддерживаемых моделью.

        Args:
            model (str): Название модели.

        Returns:
            int | None: Максимальное количество токенов или None, если информация недоступна.
        """
   ```
### `AsyncProvider`

**Описание**: Асинхронный базовый класс для всех провайдеров.

**Принцип работы**: Этот класс является асинхронной версией `BaseProvider` и предоставляет асинхронные методы для взаимодействия с провайдерами.

**Методы**:

- `__init__(self, **kwargs: Any)`:
   ```python
   def __init__(self, **kwargs: Any):
        """Инициализирует экземпляр класса AsyncProvider.

        Args:
            **kwargs (Any): Произвольные аргументы ключевых слов.
        """
   ```

- `create_completion(self, prompt: str, stream: bool = False, **kwargs: Any) -> str | Generator[str, None, None] | None`:
   ```python
   def create_completion(self, prompt: str, stream: bool = False, **kwargs: Any) -> str | Generator[str, None, None] | None:
        """Создает завершение на основе предоставленного запроса.

        Args:
            prompt (str): Запрос для создания завершения.
            stream (bool, optional): Если `True`, возвращает генератор для потоковой передачи данных. По умолчанию `False`.
            **kwargs (Any): Дополнительные аргументы для создания завершения.

        Returns:
            str | Generator[str, None, None] | None: Завершенный текст или генератор потока текста, или None в случае ошибки.
        """
   ```

- `create_conversation(self, messages: list[dict[str, str]], stream: bool = False, **kwargs: Any) -> BaseConversation | None`:
   ```python
   def create_conversation(self, messages: list[dict[str, str]], stream: bool = False, **kwargs: Any) -> BaseConversation | None:
        """Создает разговор на основе предоставленных сообщений.

        Args:
            messages (list[dict[str, str]]): Список сообщений для создания разговора.
            stream (bool, optional): Если `True`, возвращает генератор для потоковой передачи данных. По умолчанию `False`.
            **kwargs (Any): Дополнительные аргументы для создания разговора.

        Returns:
            BaseConversation | None: Объект разговора или None в случае ошибки.
        """
   ```

### `ProviderUtils`

**Описание**:  Это класс-контейнер, предоставляющий статические методы для работы с провайдерами.

**Принцип работы**:  Он включает в себя методы для выполнения общих задач, таких как получение cookie, форматирование запросов и другие вспомогательные операции.

**Методы**:

- `get_cookies(url: str) -> dict[str, str]`:
   ```python
   def get_cookies(url: str) -> dict[str, str]:
        """Получает куки для указанного URL.

        Args:
            url (str): URL для получения куки.

        Returns:
            dict[str, str]: Словарь с куки.
        """
   ```

- `format_prompt(prompt: str, model: str) -> str`:
   ```python
   def format_prompt(prompt: str, model: str) -> str:
        """Форматирует запрос для указанной модели.

        Args:
            prompt (str): Запрос для форматирования.
            model (str): Название модели.

        Returns:
            str: Отформатированный запрос.
        """
   ```