# Модуль hypotez/src/scenario/_examples/_example_executor.py

## Обзор

Данный модуль предоставляет примеры использования функций из модуля `src.scenario.executor`. Примеры демонстрируют, как запускать сценарии, обрабатывать файлы сценариев и взаимодействовать с API PrestaShop. Включает примеры работы со списками файлов сценариев, одиночными файлами и сценариями, а также вставку данных в PrestaShop.


## Классы

### `MockSupplier`

**Описание**:  Заглушка для класса поставщика (`Supplier`), используемая в примерах.  Имитирует взаимодействие с файлами сценариев и другими необходимыми компонентами.

**Атрибуты**:

- `supplier_abs_path` (Path): Путь к папке с сценариями.
- `scenario_files` (list[Path]): Список путей к файлам сценариев.
- `current_scenario` (object): Текущий сценарий.
- `supplier_settings` (dict): Настройки поставщика.
- `related_modules` (MockRelatedModules): Объект для взаимодействия с зависимыми модулями (MockRelatedModules).
- `driver` (MockDriver): Заглушка для драйвера (MockDriver).


### `MockRelatedModules`

**Описание**: Заглушка для класса, взаимодействующего с другими модулями, необходимыми для работы сценариев.

**Методы**:

- `get_list_products_in_category(s)`: Возвращает список URL-адресов страниц продуктов в указанной категории.
- `grab_product_page(s)`: Имитирует загрузку данных со страницы продукта и возвращает объект `ProductFields`.
- `grab_page(s)`: Асинхронный метод для получения данных со страницы продукта.


### `MockDriver`

**Описание**: Заглушка для класса драйвера, необходимой для имитации взаимодействия с веб-драйвером (например, Selenium).

**Методы**:

- `get_url(url)`: Метод для проверки URL, возвращает True в случае успешной проверки.


## Функции

### `example_run_scenario_files()`

**Описание**: Пример запуска списка файлов сценариев.

**Параметры**:
- `supplier` (MockSupplier): Экземпляр класса `MockSupplier`.
- `scenario_files` (list[Path]): Список путей к файлам сценариев.

**Возвращает**:
- `bool`: True, если все сценарии выполнены успешно, иначе False.


### `example_run_scenario_file()`

**Описание**: Пример запуска одного файла сценария.

**Параметры**:
- `supplier` (MockSupplier): Экземпляр класса `MockSupplier`.
- `scenario_file` (Path): Путь к файлу сценария.

**Возвращает**:
- `bool`: True, если сценарий выполнен успешно, иначе False.


### `example_run_scenario()`

**Описание**: Пример запуска одного сценария.

**Параметры**:
- `supplier` (MockSupplier): Экземпляр класса `MockSupplier`.
- `scenario` (dict): Словарь, представляющий сценарий.

**Возвращает**:
- `bool`: True, если сценарий выполнен успешно, иначе False.


### `example_insert_grabbed_data()`

**Описание**: Пример вставки данных, полученных со страницы продукта, в PrestaShop.

**Параметры**:
- `product_fields` (ProductFields): Данные продукта.


### `example_add_coupon()`

**Описание**: Пример добавления купона через API PrestaShop.

**Параметры**:
- `credentials` (dict): Кредиты для доступа к API.
- `reference` (str): Идентификатор продукта.
- `coupon_code` (str): Код купона.
- `start_date` (str): Дата начала действия купона.
- `end_date` (str): Дата окончания действия купона.


### `example_execute_PrestaShop_insert_async()`

**Описание**: Пример асинхронной вставки данных в PrestaShop.

**Параметры**:
- `product_fields` (ProductFields): Данные продукта.


### `example_execute_PrestaShop_insert()`

**Описание**: Пример синхронной вставки данных в PrestaShop.

**Параметры**:
- `product_fields` (ProductFields): Данные продукта.

**Возвращает**:
- `bool`: True, если вставка прошла успешно, иначе False.


## Зависимые модули

- `asyncio`
- `pathlib`
- `src.scenario.executor`
- `src.utils.jjson`
- `src.product.product_fields`
- `src.endpoints.PrestaShop`


## Примечания

-  `MockSupplier`, `MockRelatedModules`, и `MockDriver` - это заглушки. В реальной реализации необходимо использовать соответствующие классы.
- Примеры предполагают наличие модуля `ProductFields` и других необходимых для работы компонентов.
- Подробнее об API PrestaShop и нужных для работы данных нужно уточнить в документации к API PrestaShop.
- `YOUR_API_KEY` - нужно заменить на ваш ключ API.