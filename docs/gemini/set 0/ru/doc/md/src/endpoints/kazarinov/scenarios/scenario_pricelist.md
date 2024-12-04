# Модуль hypotez/src/endpoints/kazarinov/scenarios/scenario_pricelist.py

## Обзор

Модуль `scenario_pricelist.py` предоставляет функциональность для извлечения, разбора и обработки данных о продуктах от различных поставщиков. Модуль обрабатывает подготовку данных, обработку с помощью ИИ и интеграцию с Facebook для публикации данных о продуктах.

## Классы

### `Mexiron`

**Описание**: Класс `Mexiron` обрабатывает извлечение, разбор и сохранение данных о продуктах от различных поставщиков. Поддерживаемые поставщики: morlevi.co.il, ivory.co.il, ksp.co.il, grandadvance.co.il.

**Атрибуты**:

- `driver`: экземпляр класса `Driver` (Selenium WebDriver).
- `export_path`: путь к директории для экспорта данных.
- `mexiron_name`: имя текущего процесса.
- `price`: цена продукта.
- `timestamp`: отметка времени.
- `products_list`: список продуктов.
- `model`: экземпляр класса `GoogleGenerativeAI`.
- `model_command`: команда для модели ИИ.
- `config`: объект `SimpleNamespace` с настройками.

**Методы**:

#### `__init__(self, driver: Driver, mexiron_name: Optional[str] = None)`

**Описание**: Инициализирует класс `Mexiron` с необходимыми компонентами.

**Параметры**:

- `driver (Driver)`: Экземпляр класса `Driver` (Selenium WebDriver).
- `mexiron_name (Optional[str], optional)`: Название процесса `Mexiron`. По умолчанию использует текущее время.

#### `run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None) -> bool`

**Описание**: Выполняет сценарий: анализирует продукты, обрабатывает их с помощью ИИ и сохраняет данные.

**Параметры**:

- `system_instruction (Optional[str], optional)`: Системные инструкции для модели ИИ.
- `price (Optional[str], optional)`: Цена продукта для обработки.
- `mexiron_name (Optional[str], optional)`: Название процесса `Mexiron`.
- `urls (Optional[str | List[str]], optional)`: URL-адреса страниц продуктов.

**Возвращает**:

- `bool`: `True`, если сценарий выполняется успешно, `False` иначе.

**Обрабатываемые исключения**:

- Любые исключения (`Exception`) при работе с URL или анализом данных.

#### `get_graber_by_supplier_url(self, url: str) -> Optional[object]`

**Описание**: Возвращает соответствующий грабер для заданного URL поставщика.

**Параметры**:

- `url (str)`: URL страницы поставщика.

**Возвращает**:

- `Optional[object]`: Экземпляр класса грабера, если найдено соответствие, иначе `None`.

#### `convert_product_fields(self, f: ProductFields) -> dict`

**Описание**: Преобразует поля продукта в словарь.

**Параметры**:

- `f (ProductFields)`: Объект, содержащий обработанные данные о продукте.

**Возвращает**:

- `dict`: Отформатированный словарь данных о продукте.

#### `save_product_data(self, product_data: dict) -> bool`

**Описание**: Сохраняет данные об отдельном продукте в файл.

**Параметры**:

- `product_data (dict)`: Отформатированные данные продукта.

**Возвращает**:

- `bool`: `True`, если сохранение прошло успешно, `False` иначе.

#### `process_ai(self, products_list: str, attempts: int = 3) -> tuple | bool`

**Описание**: Обрабатывает список продуктов с помощью модели ИИ.

**Параметры**:

- `products_list (str)`: Список словарей данных о продуктах в виде строки.
- `attempts (int, optional)`: Количество попыток повторной обработки при ошибке. По умолчанию 3.

**Возвращает**:

- `tuple`: Обработанный ответ в форматах `ru` и `he`.
- `bool`: `False`, если не удалось получить допустимый ответ после попыток.


#### `post_facebook(self, mexiron: SimpleNamespace) -> bool`

**Описание**: Выполняет сценарий публикации в Facebook.

**Параметры**:

- `mexiron (SimpleNamespace)`: Данные продукта для публикации.


#### `create_report(self)`

**Описание**: Создает отчет в форматах `html` и `pdf`.


## Функции

(Список функций и методов, которые не являются методами класса `Mexiron`, можно добавить сюда)


## Модульные переменные

(Список констант и переменных модуля, которые не являются атрибутами класса `Mexiron`)


## Использование

(Добавьте примеры использования модуля)