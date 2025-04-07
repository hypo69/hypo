# Модуль `scenario`

## Обзор

Модуль `scenario.py` предназначен для реализации сценариев сбора данных о товарах с различных веб-сайтов, их обработки с использованием AI и последующего формирования отчетов. Он содержит класс `Scenario`, который управляет всем процессом, начиная от парсинга URL-адресов и заканчивая генерацией отчетов на разных языках. Модуль интегрирован с другими компонентами проекта, такими как граберы веб-страниц, AI-модели и генераторы отчетов, что позволяет автоматизировать процесс анализа и представления данных о товарах.

## Подробнее

Этот модуль является ключевым компонентом системы, ответственным за автоматизированный сбор, обработку и анализ данных о товарах. Он использует различные инструменты и методы для извлечения информации с веб-сайтов, ее преобразования и представления в удобном для анализа виде. Основная цель модуля - упростить и ускорить процесс получения актуальной информации о товарах для принятия обоснованных решений.

## Функции

### `fetch_target_urls_onetab`

```python
def fetch_target_urls_onetab(one_tab_url: str) -> tuple[str, str, list[str]] | bool:
    """
    Функция паресит целевые URL из полученного OneTab.
    """
    ...
```

**Назначение**: Извлекает целевые URL, цену и имя из OneTab URL.

**Параметры**:
- `one_tab_url` (str): URL OneTab, содержащий целевые URL.

**Возвращает**:
- `tuple[str, str, list[str]] | bool`: Кортеж, содержащий цену (str), имя (str) и список URL (list[str]). Возвращает `False`, если происходит ошибка при выполнении запроса.

**Вызывает исключения**:
- `requests.exceptions.RequestException`: Возникает при проблемах с выполнением HTTP-запроса.

**Как работает функция**:

1. Функция отправляет GET-запрос по указанному `one_tab_url`.
2. Извлекает все ссылки с классом `tabLink` из HTML-содержимого, используя `BeautifulSoup`.
3. Извлекает цену и имя из элемента с классом `tabGroupLabel`, разделяя строку по первому пробелу.
4. Возвращает цену, имя и список URL.

```
A: Отправка GET-запроса к OneTab URL
|
B: Извлечение URL, цены и имени из HTML-содержимого
|
C: Возврат цены, имени и списка URL
```

**Примеры**:

```python
# Пример использования функции fetch_target_urls_onetab
one_tab_url = "https://example.com/onetab"
price, mexiron_name, urls = fetch_target_urls_onetab(one_tab_url)
if urls:
    print(f"Цена: {price}, Имя: {mexiron_name}, URL-ы: {urls}")
else:
    print("Не удалось извлечь данные из OneTab URL.")
```

## Классы

### `Scenario`

```python
class Scenario(QuotationBuilder):
    """Исполнитель сценария для Казаринова"""
    ...
```

**Описание**: Класс `Scenario` предназначен для выполнения сценариев сбора информации о товарах, их обработки с использованием AI и генерации отчетов.

**Наследует**:
- `QuotationBuilder`: Класс, предоставляющий функциональность для построения ценовых предложений.

**Принцип работы**:
1. Инициализируется с именем сценария (`mexiron_name`) и драйвером веб-браузера (`driver`).
2. Использует методы класса `QuotationBuilder` для управления процессом сбора данных, AI-обработки и генерации отчетов.
3. Предоставляет метод `run_scenario_async` для запуска сценария в асинхронном режиме.

**Методы**:

- `__init__(self, mexiron_name: Optional[str] = gs.now, driver: Optional[Firefox | Playwrid | str] = None, **kwards)`:
    - Инициализирует экземпляр класса `Scenario`.
    - Устанавливает имя сценария, драйвер веб-браузера и другие параметры.

- `run_scenario_async(self, urls: List[str], price: Optional[str] = '', mexiron_name: Optional[str] = gs.now, bot: Optional[telebot.TeleBot] = None, chat_id: Optional[int] = 0, attempts: int = 3) -> bool`:
    - Запускает сценарий сбора данных, AI-обработки и генерации отчетов.
    - Принимает список URL-адресов товаров, цену, имя сценария, бота Telegram (опционально), ID чата (опционально) и количество попыток.
    - Возвращает `True` после успешного завершения сценария.

### `Scenario.__init__`

```python
def __init__(self, mexiron_name:Optional[str] = gs.now, driver:Optional[Firefox | Playwrid | str] = None, **kwards):
    """Сценарий сбора информации."""
    ...
```

**Назначение**: Инициализирует объект `Scenario` с заданными параметрами.

**Параметры**:
- `mexiron_name` (Optional[str]): Имя Mexiron. По умолчанию `gs.now`.
- `driver` (Optional[Firefox | Playwrid | str]): Драйвер для управления браузером. По умолчанию `None`.
- `**kwards`: Дополнительные параметры, передаваемые драйверу.

**Как работает функция**:

1. Устанавливает `window_mode` в значение `'normal'`.
2. Инициализирует драйвер, если он не был передан в качестве аргумента. Использует `Driver` с `Firefox` в качестве драйвера по умолчанию.
3. Вызывает конструктор родительского класса `QuotationBuilder`.

### `Scenario.run_scenario_async`

```python
async def run_scenario_async(
    self,
    urls: List[str],  
    price: Optional[str] = '',
    mexiron_name: Optional[str] = gs.now, 
    bot: Optional[telebot.TeleBot] = None,
    chat_id: Optional[int] = 0,
    attempts: int = 3,
) -> bool:
    """
    Executes the scenario: parses products, processes them via AI, and stores data.
    """
    ...
```

**Назначение**: Выполняет основной сценарий: парсит продукты, обрабатывает их с помощью AI и сохраняет данные.

**Параметры**:
- `urls` (List[str]): Список URL для парсинга.
- `price` (Optional[str]): Цена. По умолчанию `'`.
- `mexiron_name` (Optional[str]): Имя Mexiron. По умолчанию `gs.now`.
- `bot` (Optional[telebot.TeleBot]): Бот Telegram для отправки уведомлений. По умолчанию `None`.
- `chat_id` (Optional[int]): ID чата Telegram для отправки уведомлений. По умолчанию `0`.
- `attempts` (int): Количество попыток. По умолчанию `3`.

**Возвращает**:
- `bool`: `True` в случае успешного завершения сценария.

**Как работает функция**:

1. Инициализирует пустой список `products_list` для хранения данных о товарах.
2. Перебирает URL из списка `urls` и для каждого URL:
   - Получает грабер (`Graber`) с помощью `get_graber_by_supplier_url`.
   - Если грабер не найден, логирует ошибку и отправляет сообщение в Telegram (если бот предоставлен).
   - Использует грабер для извлечения полей товара (`grab_page_async`).
   - Преобразует поля товара с помощью `convert_product_fields`.
   - Сохраняет данные о товаре с помощью `save_product_data` и добавляет их в `products_list`.
3. Перебирает языки из списка `langs_list` (`"he"`, `"ru"`). Для каждого языка:
   - Запускает AI-обработку товаров с помощью `process_ai_async`.
   - Если AI-обработка завершается неудачно, логирует ошибку и отправляет сообщение в Telegram (если бот предоставлен).
   - Извлекает данные для текущего языка из результата AI-обработки.
   - Добавляет цену и валюту в данные.
   - Сохраняет данные в JSON-файл.
   - Создает отчет с помощью `ReportGenerator` и отправляет его в Telegram (если бот предоставлен).
4. Возвращает `True` после завершения всех шагов.

```
A: Инициализация списка товаров
|
B: Перебор URL
|
C: Получение грабера
|
D: Извлечение полей товара
|
E: Преобразование полей товара
|
F: Сохранение данных о товаре
|
G: Перебор языков
|
H: AI-обработка товаров
|
I: Добавление цены и валюты
|
J: Сохранение данных в JSON
|
K: Создание отчета
|
L: Возврат True
```

**Примеры**:

```python
# Пример использования run_scenario_async
import asyncio
from telebot import TeleBot

# Предварительная настройка:
# 1. Установите telebot: pip install pyTelegramBotAPI
# 2. Укажите токен вашего бота в TeleBot("YOUR_TELEGRAM_BOT_TOKEN")
# bot = TeleBot("YOUR_TELEGRAM_BOT_TOKEN")  # Укажите токен вашего бота
# chat_id = 123456789  # Замените на ваш chat_id

# urls = ['https://www.example.com/product1', 'https://www.example.com/product2']

# s = Scenario()
# asyncio.run(s.run_scenario_async(urls=urls, price='100', mexiron_name='Test', bot=bot, chat_id=chat_id))
```

## Другие функции

### `run_sample_scenario`

```python
def run_sample_scenario():
    """"""
    ...
```

**Назначение**: Запускает пример сценария с предопределенным списком URL.

**Как работает функция**:

1. Определяет список URL `urls_list`.
2. Создает экземпляр класса `Scenario` с `window_mode` установленным в `'headless'`.
3. Запускает сценарий `run_scenario_async` с предопределенными URL и именем `'test price quotation'`.

**Примеры**:

```python
# Пример использования run_sample_scenario
run_sample_scenario()
```

```
A: Определение списка URL
|
B: Создание экземпляра Scenario
|
C: Запуск сценария
```

```python
if __name__ == '__main__':
    run_sample_scenario()