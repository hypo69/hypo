# Модуль browser_agent

## Обзор

Модуль `browser_agent` предназначен для быстрого развертывания и запуска AI-агента, способного искать информацию в Google и анализировать веб-страницы.

## Подробнее

Этот модуль содержит класс `AIBrowserAgent`, который упрощает создание агентов, использующих браузер для выполнения различных задач, таких как поиск информации или анализ веб-страниц. В основе работы лежит интеграция с OpenAI для обработки естественного языка и `browser_use` для управления браузером.

## Классы

### `AIBrowserAgent`

**Описание**: Класс для создания агента, использующего браузер для выполнения задач.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AIBrowserAgent`.
- `run_task`: Запускает агента для выполнения заданной задачи.
- `find_product_alternatives`: Ищет аналоги для продукта по заданному URL или SKU.
- `ask`: Синхронная обертка для асинхронного метода `ask_async`. Не рекомендуется к использованию.
- `ask_async`: Отвечает на заданный вопрос, используя поиск в интернете, если это необходимо.

#### `__init__`

```python
def __init__(self, api_key: str, model_name: str = "gpt-4o-mini", search_engine: str = "google", custom_driver: Optional[object] = None):
    """
    Args:
        api_key (str): Ключ API OpenAI (необязательный). Если не указан, будет использован ключ из переменных окружения.
        model_name (str): Название языковой модели OpenAI для использования (по умолчанию "gpt-4o-mini").
        search_engine (str): Поисковая система для использования (по умолчанию "google").
        custom_driver (Optional[object], optional): Optionally injected WebDriver instance, defaults to None (browser_use default).
    """
```

**Описание**: Инициализирует класс `AIBrowserAgent`.

**Параметры**:
- `api_key` (str): Ключ API OpenAI (необязательный). Если не указан, будет использован ключ из переменных окружения.
- `model_name` (str, optional): Название языковой модели OpenAI для использования (по умолчанию `"gpt-4o-mini"`).
- `search_engine` (str, optional): Поисковая система для использования (по умолчанию `"google"`).
- `custom_driver` (Optional[object], optional): Optionally injected WebDriver instance, defaults to None (browser_use default).

**Примеры**:
```python
agent = AIBrowserAgent(api_key='YOUR_API_KEY', model_name='gpt-4o-mini', search_engine='google')
```

#### `run_task`

```python
async def run_task(self, task_prompt: str) -> Optional[str]:
    """
    Args:
        task_prompt (str): Текст задачи для агента.

    Returns:
        Optional[str]: Результат выполнения задачи в виде строки, или None в случае ошибки.
    """
```

**Описание**: Запускает агента для выполнения заданной задачи.

**Параметры**:
- `task_prompt` (str): Текст задачи для агента.

**Возвращает**:
- `Optional[str]`: Результат выполнения задачи в виде строки, или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка во время выполнения задачи.

**Примеры**:
```python
task = "Найти последнюю новость о компании OpenAI."
result = await agent.run_task(task)
if result:
    print(f"Результат: {result}")
else:
    print("Не удалось выполнить задачу.")
```

#### `find_product_alternatives`

```python
async def find_product_alternatives(self, product_url: Optional[str] = None, sku: Optional[str] = None) -> Optional[str]:
    """
    Args:
        product_url (Optional[str], optional): URL продукта, для которого нужно найти аналоги (опционально).
        sku (Optional[str], optional): SKU продукта, для которого нужно найти аналоги (опционально).

    Returns:
        Optional[str]: Строку с описанием найденных аналогов, или None в случае ошибки.
    """
```

**Описание**: Ищет в сети аналоги для продукта по заданному URL или SKU.

**Параметры**:
- `product_url` (Optional[str], optional): URL продукта, для которого нужно найти аналоги (опционально).
- `sku` (Optional[str], optional): SKU продукта, для которого нужно найти аналоги (опционально).

**Возвращает**:
- `Optional[str]`: Строку с описанием найденных аналогов, или `None` в случае ошибки.

**Примеры**:
```python
product_url = "https://www.apple.com/iphone-14/"
alternatives = await agent.find_product_alternatives(product_url=product_url)
if alternatives:
    print(f"Найденные аналоги: {alternatives}")
else:
    print("Не удалось найти аналоги.")
```

#### `ask`

```python
def ask(self, q: str) -> Optional[str]:
    """
    Args:
        q (str): _description_

    Returns:
        Optional[str]: _description_
    """
```

**Описание**: Синхронная обертка для асинхронного метода `ask_async`. Не рекомендуется к использованию.

**Параметры**:
- `q` (str): Вопрос, на который нужно ответить.

**Возвращает**:
- `Optional[str]`: Ответ на вопрос в виде строки, или `None` в случае ошибки.

**Примеры**:
```python
question = "Какая сейчас погода в Москве?"
answer = agent.ask(question)
if answer:
    print(f"Ответ: {answer}")
else:
    print("Не удалось получить ответ.")
```

#### `ask_async`

```python
async def ask_async(self, q: str) -> Optional[str]:
    """
    Args:
        q (str): Вопрос, на который нужно ответить.

    Returns:
        Optional[str]: Ответ на вопрос в виде строки, или None в случае ошибки.
    """
```

**Описание**: Отвечает на заданный вопрос, используя поиск в интернете, если это необходимо.

**Параметры**:
- `q` (str): Вопрос, на который нужно ответить.

**Возвращает**:
- `Optional[str]`: Ответ на вопрос в виде строки, или `None` в случае ошибки.

**Примеры**:
```python
question = "Какая сейчас погода в Москве?"
answer = await agent.ask_async(question)
if answer:
    print(f"Ответ: {answer}")
else:
    print("Не удалось получить ответ.")
```

## Функции

### `main`

```python
async def main():
    """
    """
```

**Описание**: Пример использования класса `AIBrowserAgent`.

**Примеры**:
```python
asyncio.run(main())