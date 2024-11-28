# Модуль `hypotez/src/endpoints/kazarinov/scenarios/scenario_pricelist.py`

## Обзор

Модуль предоставляет функциональность для извлечения, парсинга и обработки данных о продуктах от различных поставщиков. Он обрабатывает подготовку данных, обработку с помощью ИИ и интеграцию с Facebook для публикации продуктов.

## Классы

### `Mexiron`

**Описание**: Класс `Mexiron` обрабатывает извлечение, парсинг и сохранение данных продуктов от поставщиков. Поддерживаемые поставщики: morlevi.co.il, ivory.co.il, ksp.co.il, grandadvance.co.il.

**Атрибуты**:

- `driver`: Экземпляр класса `Driver` для управления Selenium WebDriver.
- `export_path`: Путь к папке для экспорта данных.
- `mexiron_name`: Имя процесса Mexiron.
- `price`: Цена продукта.
- `timestamp`: Метка времени.
- `products_list`: Список продуктов.
- `model`: Экземпляр класса `GoogleGenerativeAI`.
- `model_command`: Команда для модели.
- `config`: Объект SimpleNamespace с настройками.

**Методы**:

#### `__init__(self, driver: Driver, mexiron_name: Optional[str] = None)`

**Описание**: Инициализирует класс `Mexiron` с необходимыми компонентами.

**Параметры**:
- `driver` (Driver): Экземпляр класса `Driver`.
- `mexiron_name` (Optional[str], optional): Название процесса. По умолчанию - метка времени.

#### `run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None) -> bool`

**Описание**: Выполняет сценарий: парсит продукты, обрабатывает их с помощью ИИ и сохраняет данные.

**Параметры**:
- `system_instruction` (Optional[str], optional): Системные инструкции для модели ИИ.
- `price` (Optional[str], optional): Цена для обработки.
- `mexiron_name` (Optional[str], optional): Название Mexiron.
- `urls` (Optional[str | List[str]], optional): URL-адреса страниц продуктов.

**Возвращает**:
- `bool`: `True`, если сценарий выполнен успешно, `False` иначе.

**Замечания**:
- Требуется реализовать обработку ошибок и логирование.
- Модель может ошибаться.

#### `get_graber_by_supplier_url(self, url: str) -> Optional[object]`

**Описание**: Возвращает подходящий грабер для данного URL-адреса поставщика.

**Параметры**:
- `url` (str): URL-адрес страницы поставщика.

**Возвращает**:
- `Optional[object]`: Экземпляр класса грабера, если найден соответствие, иначе `None`.


#### `convert_product_fields(self, f: ProductFields) -> dict`

**Описание**: Преобразует поля продукта в словарь.

**Параметры**:
- `f` (ProductFields): Объект, содержащий обработанные данные продукта.

**Возвращает**:
- `dict`: Отформатированный словарь данных продукта.


#### `save_product_data(self, product_data: dict) -> bool`

**Описание**: Сохраняет индивидуальные данные продукта в файл.

**Параметры**:
- `product_data` (dict): Отформатированные данные продукта.

**Возвращает**:
- `bool`: `True`, если данные сохранены успешно, `False` иначе.


#### `process_ai(self, products_list: str, attempts: int = 3) -> tuple | bool`

**Описание**: Обрабатывает список продуктов с помощью модели ИИ.

**Параметры**:
- `products_list` (str): Список словарей данных продуктов в виде строки.
- `attempts` (int, optional): Количество попыток повтора в случае сбоя. По умолчанию 3.

**Возвращает**:
- `tuple`: Обработанный ответ в форматах `ru` и `he`.
- `bool`: `False`, если не удалось получить корректный ответ после повторов.

**Замечания**:
- Модель может возвращать неверные результаты.
- В случае ошибки, функция будет повторно вызвана.

#### `post_facebook(self, mexiron:SimpleNamespace) -> bool`

**Описание**: Выполняет сценарий рекламного модуля Facebook.

**Параметры**:
- `mexiron` (SimpleNamespace): Данные мехирона.

**Возвращает**:
- `bool`: `True`, если публикация успешна, `False` иначе.


#### `create_report(self)`

**Описание**: Создаёт отчёт в формате `html` и `pdf`.


## Функции

(Список функций с подробными описаниями по формату, описанному в инструкции)