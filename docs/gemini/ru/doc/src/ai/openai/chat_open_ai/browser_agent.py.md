# Модуль для работы с ИИ-агентом, использующим браузер
=========================================================

Модуль `browser_agent` предоставляет класс `AIBrowserAgent`, который позволяет быстро настроить и запустить ИИ-агента, способного искать информацию в Google и анализировать веб-страницы.

Пример использования
----------------------

```python
>>> from src.ai.openai.chat_openai.browser_agent import AIBrowserAgent
>>> agent = AIBrowserAgent(api_key='YOUR_API_KEY', model_name='gpt-4o-mini')
>>> asyncio.run(agent.ask_async('Какая сейчас погода в Москве?'))
```

## Оглавление

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
    - [AIBrowserAgent](#aibrowseragent)
- [Функции](#функции)
    - [main](#main)

## Обзор

Модуль `browser_agent` предоставляет класс `AIBrowserAgent`, который позволяет создавать агентов, использующих браузер для выполнения задач, таких как поиск информации и анализ веб-страниц. Он использует библиотеку `browser_use` и модель `ChatOpenAI` для обработки естественного языка и взаимодействия с поисковыми системами.

## Подробнее

Этот модуль предназначен для упрощения процесса создания ИИ-агентов, способных взаимодействовать с веб-страницами. Он предоставляет удобный интерфейс для выполнения задач, таких как поиск аналогов продуктов или ответы на вопросы с использованием поиска в интернете. Модуль использует библиотеку `browser_use` для управления браузером и `ChatOpenAI` для обработки естественного языка.

## Классы

### `AIBrowserAgent`

**Описание**: Класс для создания агента, использующего браузер для выполнения задач.

**Принцип работы**:
Класс `AIBrowserAgent` инициализируется с ключом API OpenAI, названием языковой модели и поисковой системой. Он предоставляет методы для запуска агента для выполнения задач, поиска аналогов продуктов и ответов на вопросы с использованием поиска в интернете. Класс использует библиотеку `browser_use` для управления браузером и `ChatOpenAI` для обработки естественного языка.

**Аттрибуты**:
- `api_key` (str): Ключ API OpenAI.
- `model_name` (str): Название языковой модели OpenAI для использования (по умолчанию "gpt-4o-mini").
- `search_engine` (str): Поисковая система для использования (по умолчанию "google").
- `llm`: Инстанс языковой модели OpenAI.
- `custom_driver`: Инстанс веб-драйвера (опционально).

**Методы**:
- `__init__`: Инициализирует класс `AIBrowserAgent`.
- `run_task`: Запускает агента для выполнения заданной задачи.
- `find_product_alternatives`: Ищет аналоги для продукта по заданному URL или SKU.
- `ask`: Синхронная обертка для асинхронного метода `ask_async`. Не рекомендуется к использованию.
- `ask_async`: Отвечает на заданный вопрос, используя поиск в интернете, если это необходимо.

### `AIBrowserAgent.__init__`

```python
    def __init__(self,
                 api_key: str,
                 model_name: str = "gpt-4o-mini",
                 search_engine: str = "google",
                 custom_driver: Optional[object] = None):
        """
        Инициализирует класс BrowserAgent.

        Args:
            api_key: Ключ API OpenAI (необязательный). Если не указан, будет использован ключ из переменных окружения.
            model_name: Название языковой модели OpenAI для использования (по умолчанию "gpt-4o-mini").
            search_engine: Поисковая система для использования (по умолчанию "google").
            custom_driver: Optionally injected WebDriver instance, defaults to None (browser_use default).
        """
        self.api_key = api_key
        self.model_name = model_name
        self.search_engine = search_engine
        self.llm = ChatOpenAI(model=self.model_name, api_key=self.api_key)  # Initialize LLM here
        self.custom_driver = custom_driver  # Save injected driver to local variable
```
**Назначение**: Инициализация экземпляра класса `AIBrowserAgent`.

**Параметры**:
- `api_key` (str): Ключ API OpenAI. Если не указан, будет использован ключ из переменных окружения.
- `model_name` (str): Название языковой модели OpenAI для использования. По умолчанию "gpt-4o-mini".
- `search_engine` (str): Поисковая система для использования. По умолчанию "google".
- `custom_driver` (Optional[object], optional): Опционально внедренный экземпляр WebDriver. По умолчанию `None`.

**Как работает функция**:

1.  Присваивает переданные значения параметрам экземпляра класса.
2.  Инициализирует языковую модель OpenAI (`llm`) с использованием `model_name` и `api_key`.
3.  Сохраняет внедренный драйвер в локальной переменной `custom_driver`.

```
Инициализация класса AIBrowserAgent
│
├── api_key = api_key
│
├── model_name = model_name
│
├── search_engine = search_engine
│
├── Инициализация LLM (llm = ChatOpenAI(...))
│
└── custom_driver = custom_driver
```

**Примеры**:

```python
# Пример инициализации агента с ключом API и названием модели
agent = AIBrowserAgent(api_key='YOUR_API_KEY', model_name='gpt-4o-mini')

# Пример инициализации агента с пользовательским драйвером
# from selenium import webdriver
# custom_driver = webdriver.Firefox()
# agent = AIBrowserAgent(api_key='YOUR_API_KEY', model_name='gpt-4o-mini', custom_driver=custom_driver)
```

### `AIBrowserAgent.run_task`

```python
    async def run_task(self, task_prompt: str) -> Optional[str]:
        """
        Запускает агента для выполнения заданной задачи.

        Args:
            task_prompt: Текст задачи для агента.

        Returns:
            Результат выполнения задачи в виде строки, или None в случае ошибки.
        """
        try:
            logger.info(f"Агент начал выполнение задачи: {task_prompt}")

            # 1. Default:  browser_use managed Playwright driver (no driver needed)
            driver = None  # By default let browser_use create its own driver.

            # 2. CUSTOM:  Adapt Selenium-based driver
            # if self.custom_driver:  # if injected instance of webdriver.FireFox
            #      playwright_driver = PlaywrightFirefoxAdapter(self.custom_driver)  # Adapt.
            #      driver = playwright_driver

            # 3. Playwright driver already adapted (or pure Playwright)
            if self.custom_driver:
                driver = self.custom_driver

            agent = Agent(task=task_prompt, llm=self.llm, driver=driver)  # Pass to agent
            result = await agent.run()
            logger.info("Агент завершил выполнение задачи.")

            if hasattr(driver, 'close') and callable(getattr(driver, 'close')) :
                driver.close()  # Try closing driver, if implemented

            return result

        except Exception as ex:
            logger.error(f"Произошла ошибка во время выполнения задачи: ", ex, exc_info=True)
            return None
```

**Назначение**: Запускает агента для выполнения заданной задачи.

**Параметры**:
- `task_prompt` (str): Текст задачи для агента.

**Возвращает**:
- `Optional[str]`: Результат выполнения задачи в виде строки, или `None` в случае ошибки.

**Как работает функция**:

1.  Логирует начало выполнения задачи.
2.  Определяет, какой драйвер использовать:
    *   По умолчанию, `browser_use` создает свой собственный драйвер Playwright.
    *   Если внедрен `custom_driver`, использует его.
3.  Создает экземпляр класса `Agent` из библиотеки `browser_use`, передавая текст задачи, языковую модель и драйвер.
4.  Запускает агента для выполнения задачи с помощью метода `run()`.
5.  Логирует завершение выполнения задачи.
6.  Пытается закрыть драйвер, если это возможно.
7.  Возвращает результат выполнения задачи или `None` в случае ошибки.

```
run_task
│
├── Логирование начала выполнения задачи
│
├── Определение драйвера
│   ├── По умолчанию: driver = None
│   └── Если внедрен custom_driver: driver = custom_driver
│
├── Создание экземпляра Agent (agent = Agent(...))
│
├── Запуск агента (result = await agent.run())
│
├── Логирование завершения выполнения задачи
│
├── Попытка закрытия драйвера (driver.close())
│
└── Возврат результата
```

**Примеры**:

```python
# Пример запуска агента для выполнения задачи
task_prompt = "Найди информацию о последних новостях в мире."
result = asyncio.run(agent.run_task(task_prompt))
if result:
    print("Результат выполнения задачи:")
    print(result)
else:
    print("Не удалось выполнить задачу.")
```

### `AIBrowserAgent.find_product_alternatives`

```python
    async def find_product_alternatives(self, product_url: Optional[str] = None,
                                        sku: Optional[str] = None) -> Optional[str]:
        """
        Ищет в сети аналоги для продукта по заданному URL или SKU.

        Args:
            product_url: URL продукта, для которого нужно найти аналоги (опционально).
            sku: SKU продукта, для которого нужно найти аналоги (опционально).

        Returns:
            Строку с описанием найденных аналогов, или None в случае ошибки.
        """

        if product_url:
            search_query = f"аналоги {product_url}"
        elif sku:
            search_query = f"аналоги товара с артикулом {sku}"
        else:
            logger.warning("Не указан ни product_url, ни sku.  Невозможно выполнить поиск аналогов.")
            return None

        encoded_search_query = urllib.parse.quote_plus(search_query)  # URL encode search query

        if self.search_engine == "google":
            search_url = f"https://www.google.com/search?q={encoded_search_query}"
        else:  # DuckDuckGo
            search_url = f"https://duckduckgo.com/?q={encoded_search_query}"

        task_prompt = f"""Используя поисковую систему {self.search_engine}, перейди по адресу {search_url}.  
        Найди и предоставь список из 3-5 аналогов продукта.  
        Для каждого аналога укажи название и краткое описание."""

        return await self.run_task(task_prompt)
```

**Назначение**: Ищет в сети аналоги для продукта по заданному URL или SKU.

**Параметры**:
- `product_url` (Optional[str], optional): URL продукта, для которого нужно найти аналоги. По умолчанию `None`.
- `sku` (Optional[str], optional): SKU продукта, для которого нужно найти аналоги. По умолчанию `None`.

**Возвращает**:
- `Optional[str]`: Строку с описанием найденных аналогов, или `None` в случае ошибки.

**Как работает функция**:

1.  Формирует поисковый запрос на основе URL или SKU продукта.
2.  Если не указан ни URL, ни SKU, логирует предупреждение и возвращает `None`.
3.  Кодирует поисковый запрос для использования в URL.
4.  Формирует URL поисковой системы (Google или DuckDuckGo) с закодированным запросом.
5.  Формирует текст задачи для агента, указывая использовать поисковую систему и найти аналоги продукта.
6.  Запускает агента для выполнения задачи с помощью метода `run_task()`.
7.  Возвращает результат выполнения задачи или `None` в случае ошибки.

```
find_product_alternatives
│
├── Формирование поискового запроса
│   ├── Если product_url: search_query = f"аналоги {product_url}"
│   └── Если sku: search_query = f"аналоги товара с артикулом {sku}"
│
├── Если не указан ни URL, ни SKU: логирование и возврат None
│
├── Кодирование поискового запроса (encoded_search_query = urllib.parse.quote_plus(search_query))
│
├── Формирование URL поисковой системы
│   ├── Если self.search_engine == "google": search_url = f"https://www.google.com/search?q={encoded_search_query}"
│   └── Иначе: search_url = f"https://duckduckgo.com/?q={encoded_search_query}"
│
├── Формирование текста задачи (task_prompt)
│
└── Запуск агента (return await self.run_task(task_prompt))
```

**Примеры**:

```python
# Пример поиска аналогов продукта по URL
product_url = "https://www.apple.com/iphone-14/"
alternatives = asyncio.run(agent.find_product_alternatives(product_url=product_url))
if alternatives:
    print("Найденные аналоги:")
    print(alternatives)
else:
    print("Не удалось найти аналоги.")

# Пример поиска аналогов продукта по SKU
sku = "1493001"
alternatives = asyncio.run(agent.find_product_alternatives(sku=sku))
if alternatives:
    print("Найденные аналоги:")
    print(alternatives)
else:
    print("Не удалось найти аналоги.")
```

### `AIBrowserAgent.ask`

```python
    def ask(self, q: str) -> Optional[str]:
        """
        Синхронная обертка для асинхронного метода ask_async.  Не рекомендуется к использованию.
        """
        task_prompt = f"""Ответь на следующий вопрос, используя поиск в интернете, если это необходимо: {q}"""
        return self.run_task(task_prompt)
```

**Назначение**: Синхронная обертка для асинхронного метода `ask_async`. Не рекомендуется к использованию.

**Параметры**:
- `q` (str): Вопрос, на который нужно ответить.

**Возвращает**:
- `Optional[str]`: Ответ на вопрос в виде строки, или `None` в случае ошибки.

**Как работает функция**:

1.  Формирует текст задачи для агента, указывая ответить на вопрос с использованием поиска в интернете.
2.  Запускает агента для выполнения задачи с помощью метода `run_task()`.
3.  Возвращает результат выполнения задачи или `None` в случае ошибки.

```
ask
│
├── Формирование текста задачи (task_prompt)
│
└── Запуск агента (return self.run_task(task_prompt))
```

**Примеры**:

```python
# Пример ответа на вопрос
question = "Какая сейчас погода в Москве?"
answer = agent.ask(question)  # Не рекомендуется к использованию
if answer:
    print("Ответ на вопрос:")
    print(answer)
else:
    print("Не удалось получить ответ на вопрос.")
```

### `AIBrowserAgent.ask_async`

```python
    async def ask_async(self, q: str) -> Optional[str]:
        """
        Отвечает на заданный вопрос, используя поиск в интернете, если это необходимо.

        Args:
            question: Вопрос, на который нужно ответить.

        Returns:
            Ответ на вопрос в виде строки, или None в случае ошибки.
        """
        task_prompt = f"""Ответь на следующий вопрос, используя поиск в интернете, если это необходимо: {q}"""
        return await self.run_task(task_prompt)
```

**Назначение**: Отвечает на заданный вопрос, используя поиск в интернете, если это необходимо.

**Параметры**:
- `q` (str): Вопрос, на который нужно ответить.

**Возвращает**:
- `Optional[str]`: Ответ на вопрос в виде строки, или `None` в случае ошибки.

**Как работает функция**:

1.  Формирует текст задачи для агента, указывая ответить на вопрос с использованием поиска в интернете.
2.  Запускает агента для выполнения задачи с помощью метода `run_task()`.
3.  Возвращает результат выполнения задачи или `None` в случае ошибки.

```
ask_async
│
├── Формирование текста задачи (task_prompt)
│
└── Запуск агента (return await self.run_task(task_prompt))
```

**Примеры**:

```python
# Пример ответа на вопрос
question = "Какая сейчас погода в Москве?"
answer = asyncio.run(agent.ask_async(question))  # Используем асинхронный метод напрямую
if answer:
    print("Ответ на вопрос:")
    print(answer)
else:
    print("Не удалось получить ответ на вопрос.")
```

## Функции

### `main`

```python
async def main():
    """
    Пример использования класса BrowserAgent.
    """
    # api_key: str = gs.credentials.openai.hypotez.api_key  # Replace with your actual method of obtaining the API key
    api_key: str = None  # Replace with your actual method of obtaining the API key
    model_name: str = 'gpt-4o-mini'  # gpt-4o-mini существует, если указан api_key

    #########################################################################
    # OPTIONAL:  Inject custom Chrome, Firefox, Edge driver
    # selenium_driver = Firefox()  # (Or with args you use in Firefox class)
    # playwright_driver = PlaywrightFirefoxAdapter(selenium_driver)
    # agent = BrowserAgent(api_key=api_key, model_name=model_name, custom_driver = playwright_driver)
    #########################################################################
    agent = AIBrowserAgent(api_key=api_key, model_name=model_name) #  Default browser_use driver

    # Пример поиска аналогов продукта
    sku: str = '1493001'
    product_url: str = None  # "https://www.apple.com/iphone-14/"  # Замените на URL интересующего вас продукта
    alternatives = await agent.find_product_alternatives(product_url=product_url, sku=sku)
    if alternatives:
        print("Найденные аналоги:")
        print(alternatives)
    else:
        print("Не удалось найти аналоги.")

    # Пример ответа на вопрос
    question = "Какая сейчас погода в Москве?"
    answer = await agent.ask_async(question)  # Используем асинхронный метод напрямую
    if answer:
        print("Ответ на вопрос:")
        print(answer)
    else:
        print("Не удалось получить ответ на вопрос.")
```

**Назначение**: Пример использования класса `AIBrowserAgent`.

**Как работает функция**:

1.  Определяет ключ API OpenAI и название языковой модели.
2.  Создает экземпляр класса `AIBrowserAgent`.
3.  Ищет аналоги продукта по SKU.
4.  Отвечает на вопрос с использованием поиска в интернете.

```
main
│
├── Определение ключа API и названия модели
│
├── Создание экземпляра AIBrowserAgent (agent = AIBrowserAgent(...))
│
├── Поиск аналогов продукта (alternatives = await agent.find_product_alternatives(...))
│
└── Ответ на вопрос (answer = await agent.ask_async(question))
```

**Примеры**:

Запуск функции `main` приведет к выполнению поиска аналогов продукта и ответа на вопрос о погоде в Москве с использованием ИИ-агента.
```python
if __name__ == "__main__":
    asyncio.run(main())