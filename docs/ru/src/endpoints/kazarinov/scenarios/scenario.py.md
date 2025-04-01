# Модуль `scenario.py`

## Обзор

Модуль `scenario.py` предназначен для реализации сценариев парсинга, обработки данных с использованием AI и генерации отчетов для проекта `hypotez`. Основной класс `Scenario` наследует функциональность из `QuotationBuilder` и выполняет оркестрацию всего процесса.

## Подробней

Этот модуль отвечает за сбор информации о товарах с различных веб-сайтов, их обработку с помощью AI (например, Google Gemini) для перевода и анализа, а также за создание отчетов на основе полученных данных. Он включает в себя функции для парсинга URL из OneTab, класс `Scenario` для управления процессом и функцию `run_sample_scenario` для демонстрации работы.

## Классы

### `Scenario(QuotationBuilder)`

**Описание**: Класс `Scenario` является исполнителем сценария для сбора и обработки информации о товарах. Он наследует функциональность построения коммерческих предложений из класса `QuotationBuilder`.

**Наследует**:

- `QuotationBuilder`: Предоставляет базовые методы для создания структуры коммерческих предложений.

**Атрибуты**:

- `driver` (Driver): Экземпляр веб-драйвера для управления браузером и выполнения парсинга веб-страниц.
- `mexiron_name` (Optional[str]): Имя для идентификации сценария, по умолчанию `gs.now`.

**Методы**:

- `__init__(self, mexiron_name: Optional[str] = gs.now, driver: Optional[Firefox | Playwrid | str] = None, **kwards)`: Инициализирует экземпляр класса `Scenario`, настраивает драйвер и вызывает конструктор родительского класса `QuotationBuilder`.
- `run_scenario_async(self, urls: List[str], price: Optional[str] = '', mexiron_name: Optional[str] = gs.now, bot: Optional[telebot.TeleBot] = None, chat_id: Optional[int] = 0, attempts: int = 3) -> bool`: Асинхронно выполняет сценарий: парсит продукты, обрабатывает их с помощью AI и сохраняет данные.

## Функции

### `fetch_target_urls_onetab(one_tab_url: str) -> tuple[str, str, list[str]] | bool`

**Назначение**: Извлекает целевые URL, цену и имя из OneTab URL.

**Параметры**:

- `one_tab_url` (str): URL OneTab, содержащий целевые URL.

**Возвращает**:

- `tuple[str, str, list[str]] | bool`: Кортеж, содержащий цену, имя mexiron и список URL, или `False` в случае ошибки.

**Вызывает исключения**:

- `requests.exceptions.RequestException`: Возникает при ошибках выполнения HTTP-запроса.

**Как работает функция**:

1.  Выполняет GET-запрос к указанному `one_tab_url`.
2.  Использует `BeautifulSoup` для парсинга содержимого HTML.
3.  Извлекает все ссылки с классом `tabLink`.
4.  Извлекает данные из элемента с классом `tabGroupLabel`, разделяя их на цену и имя.
5.  В случае ошибки логирует исключение и возвращает `False`.

```
A: GET-запрос к one_tab_url
|
B: Парсинг HTML с BeautifulSoup
|
C: Извлечение ссылок и данных
|
D: Обработка данных (цена, имя)
|
E: Возврат результатов
```

**Примеры**:

```python
one_tab_url = "https://example.com/onetab"
price, mexiron_name, urls = fetch_target_urls_onetab(one_tab_url)
if urls:
    print(f"Цена: {price}, Имя: {mexiron_name}, URL: {urls}")
else:
    print("Не удалось извлечь URL из OneTab.")
```

### `Scenario.__init__(self, mexiron_name: Optional[str] = gs.now, driver: Optional[Firefox | Playwrid | str] = None, **kwards)`

**Назначение**: Инициализирует экземпляр класса `Scenario`, настраивая драйвер и вызывая конструктор родительского класса `QuotationBuilder`.

**Параметры**:

- `mexiron_name` (Optional[str]): Имя для идентификации сценария, по умолчанию `gs.now`.
- `driver` (Optional[Firefox | Playwrid | str]): Экземпляр веб-драйвера или строка, указывающая на необходимость создания экземпляра `Firefox`, `Playwrid`. По умолчанию `None`.
- `**kwards`: Дополнительные параметры, передаваемые драйверу.

**Как работает функция**:

1.  Устанавливает режим окна в `normal`.
2.  Инициализирует драйвер, если он не был передан, используя `Driver` с `Firefox` и переданными `kwards`.
3.  Вызывает конструктор родительского класса `QuotationBuilder`, передавая имя `mexiron_name` и драйвер.

```
A: Установка режима окна
|
B: Инициализация драйвера (если необходимо)
|
C: Вызов конструктора QuotationBuilder
```

**Примеры**:

```python
s = Scenario(mexiron_name="test_scenario", window_mode="headless")
```

### `Scenario.run_scenario_async(self, urls: List[str], price: Optional[str] = '', mexiron_name: Optional[str] = gs.now, bot: Optional[telebot.TeleBot] = None, chat_id: Optional[int] = 0, attempts: int = 3) -> bool`

**Назначение**: Асинхронно выполняет сценарий: парсит продукты, обрабатывает их с помощью AI и сохраняет данные.

**Параметры**:

- `urls` (List[str]): Список URL для парсинга продуктов.
- `price` (Optional[str]): Цена продукта, по умолчанию ''.
- `mexiron_name` (Optional[str]): Имя для идентификации сценария, по умолчанию `gs.now`.
- `bot` (Optional[telebot.TeleBot]): Экземпляр бота `Telebot` для отправки уведомлений, по умолчанию `None`.
- `chat_id` (Optional[int]): ID чата для отправки уведомлений, по умолчанию 0.
- `attempts` (int): Количество попыток выполнения сценария, по умолчанию 3.

**Возвращает**:

- `bool`: `True` в случае успешного выполнения сценария.

**Как работает функция**:

1.  Инициализирует пустой список `products_list` для хранения данных о продуктах.
2.  Для каждого URL в списке `urls`:
    *   Получает граббер (`Graber`) для данного URL.
    *   Парсит страницу с помощью граббера, извлекая необходимые поля продукта.
    *   Преобразует извлеченные поля продукта.
    *   Сохраняет данные продукта.
    *   Добавляет данные продукта в `products_list`.
3.  Для каждого языка в списке `langs_list`:
    *   Обрабатывает `products_list` с помощью AI для перевода и анализа.
    *   Создает отчет на основе обработанных данных.
    *   Сохраняет отчет в формате JSON и DOCX.

```
A: Инициализация products_list
|
B: Для каждого URL:
|   C: Получение граббера
|   |
|   D: Парсинг страницы
|   |
|   E: Преобразование полей продукта
|   |
|   F: Сохранение данных продукта
|   |
|   G: Добавление в products_list
|
H: Для каждого языка:
|   I: AI обработка products_list
|   |
|   J: Создание отчета
|   |
|   K: Сохранение отчета (JSON, DOCX)
|
L: Возврат True
```

**Примеры**:

```python
urls = ["https://example.com/product1", "https://example.com/product2"]
s = Scenario(window_mode="headless")
asyncio.run(s.run_scenario_async(urls=urls, mexiron_name="test_scenario"))
```

#### `Scenario.run_scenario_async` -> `ProductFields = await graber.grab_page_async(*self.required_fields)`

**Назначение**: Асинхронно извлекает поля продукта с использованием граббера.

**Параметры**:

- `*self.required_fields`: Необходимые поля продукта для извлечения.

**Возвращает**:

- `ProductFields`: Объект, содержащий извлеченные поля продукта.

**Как работает функция**:

1.  Вызывает метод `grab_page_async` граббера, передавая необходимые поля продукта.
2.  Возвращает объект `ProductFields`, содержащий извлеченные данные.

#### `Scenario.run_scenario_async` -> `data: dict = await self.process_ai_async(products_list, lang)`

**Назначение**: Асинхронно обрабатывает список продуктов с использованием AI для перевода и анализа.

**Параметры**:

- `products_list` (list): Список данных о продуктах.
- `lang` (str): Язык для перевода и анализа.

**Возвращает**:

- `dict`: Словарь, содержащий обработанные AI данные.

**Как работает функция**:

1.  Вызывает метод `process_ai_async`, передавая список продуктов и язык.
2.  Возвращает словарь с обработанными AI данными.

### `run_sample_scenario()`

**Назначение**: Запускает пример сценария для демонстрации работы модуля.

**Как работает функция**:

1.  Определяет список URL `urls_list`.
2.  Создает экземпляр класса `Scenario` с режимом `headless`.
3.  Запускает асинхронный сценарий `run_scenario_async` с заданными параметрами.

**Примеры**:

```python
run_sample_scenario()
```
```