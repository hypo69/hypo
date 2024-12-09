# Модуль `hypotez/src/suppliers/aliexpress/campaign/ali_promo_campaign.py`

## Обзор

Модуль `ali_promo_campaign.py` предназначен для управления рекламными кампаниями на AliExpress. Он предоставляет возможности загрузки, обработки и генерации данных о кампаниях, категориях и товарах с использованием искусственного интеллекта.  Модуль поддерживает разные языки и валюты, обеспечивая гибкость в настройке кампаний.  Он также предоставляет функциональность для создания и заполнения JSON файлов, обработки данных о категориях и товарах, а также генерации контента с помощью ИИ.

## Классы

### `AliPromoCampaign`

**Описание**: Класс `AliPromoCampaign` отвечает за управление рекламной кампанией на AliExpress. Он предоставляет методы для инициализации, обработки кампаний, категорий и товаров, а также для использования ИИ для генерации данных.

**Атрибуты**:

- `language`: Язык кампании.
- `currency`: Валюта кампании.
- `base_path`: Базовая директория для хранения данных кампании.
- `campaign_name`: Название кампании.
- `campaign`: Объект `SimpleNamespace`, представляющий данные кампании.
- `campaign_ai`: Объект `SimpleNamespace`, представляющий данные для AI.
- `gemini`: Объект `GoogleGenerativeAI`, используемый для генерации данных с помощью Gemini.
- `openai`: Объект `OpenAIModel`, используемый для генерации данных с помощью OpenAI (в коде присутствует, но может быть неактивным).

**Методы**:

- `__init__(campaign_name: str, language: Optional[str] = None, currency: Optional[str] = None, model:str = 'openai')`: Инициализирует объект `AliPromoCampaign`.  Загружает данные из JSON файла, если он существует. Иначе, запускает процесс создания новой кампании.
- `_models_payload()`: Инициализирует модели ИИ (Gemini и OpenAI).
- `process_campaign()`: Обрабатывает все категории кампании, включая обработку товаров в каждой категории и генерацию данных с помощью ИИ.
- `process_campaign_category(category_name: str) -> list[SimpleNamespace] | None`: Обрабатывает указанную категорию для всех языков и валют.
- `process_new_campaign(campaign_name: str, language: Optional[str] = None, currency: Optional[str] = None)`: Создает новую рекламную кампанию.  Создание файла JSON для кампании, обработка категорий и товаров.
- `process_ai_category(category_name: Optional[str] = None)`: Обрабатывает данные категории с помощью ИИ.  Получает данные из файлов, генерирует запрос для ИИ, обновляет данные в `campaign_ai`.
- `process_category_products(category_name: str) -> Optional[List[SimpleNamespace]]`: Обрабатывает продукты в указанной категории, используя генератор партнерских ссылок.  Ищет продуктные id в HTML файлах и sources.txt, инициирует запрос к генератору партнерских ссылок.
- `dump_category_products_files(category_name: str, products: List[SimpleNamespace])`: Сохраняет данные о товарах в JSON файлы.
- `set_categories_from_directories()`: Устанавливает категории кампании из названий директорий.
- `generate_output(campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace)`: Сохраняет данные о товарах в различные форматы (JSON, HTML).
- `generate_html(campaign_name:str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace)`: Создает HTML файлы для каждой категории и для корневого индекса кампании.
- `generate_html_for_campaign(campaign_name: str)`: Генерирует HTML-страницы для всех категорий рекламной кампании.


## Функции

(Здесь перечислены другие функции, если таковые имеются)


## Заметки

- Код использует `SimpleNamespace` для представления данных.
- Используется асинхронное программирование (`asyncio`).
- Имеется обработка ошибок (блоками `try...except`).
- Присутствует обширная документация внутри кода.
- Модуль предполагает организацию данных в структуре директорий (например, для категорий и файлов).
- В коде присутствуют вызовы внешних библиотек (`gs`, `header`, `GoogleGenerativeAI`, `OpenAIModel`, `AliAffiliatedProducts` и др.), которые не представлены в данном документе.  Необходимо документация для этих внешних библиотек для полного понимания функциональности `ali_promo_campaign.py`.
- Функции `save_promotion_links`, `save_product_titles`, `generate_html` являются асинхронными (предполагается использование `async def`).