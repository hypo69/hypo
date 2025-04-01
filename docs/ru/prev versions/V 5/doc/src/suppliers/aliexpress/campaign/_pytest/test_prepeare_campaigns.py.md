# Модуль тестирования подготовки кампаний

## Обзор

Модуль `test_prepeare_campaigns.py` содержит набор тестов, предназначенных для проверки функциональности подготовки кампаний AliExpress. Он использует библиотеку `pytest` для организации и выполнения тестов, а также `unittest.mock` для создания мок-объектов, имитирующих взаимодействие с внешними зависимостями и API.

## Подробней

Этот модуль тестирует функции, отвечающие за обновление категорий, обработку кампаний по категориям и обработку кампаний в целом. Он также включает тесты для основной функции `main`, которая координирует процесс подготовки кампаний. Модуль использует моки для изоляции тестируемых функций и проверки их поведения в различных сценариях, включая успешное выполнение и возникновение ошибок.

## Классы

В данном модуле классы отсутствуют. Вместо этого используются фикстуры `pytest` для подготовки тестового окружения и предоставления мок-объектов.

## Функции

### `mock_j_loads`

```python
@pytest.fixture
def mock_j_loads():
    with patch("src.utils.jjson.j_loads") as mock:
        yield mock
```

**Описание**: Фикстура `mock_j_loads` создает мок-объект для функции `j_loads` из модуля `src.utils.jjson`.

**Как работает функция**:
- Использует `patch` для замены `j_loads` мок-объектом.
- Предоставляет мок-объект для использования в тестах.
- После завершения теста `patch` восстанавливает оригинальную функцию `j_loads`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `mock`: Мок-объект функции `j_loads`.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
def test_function(mock_j_loads):
    mock_j_loads.return_value = {"key": "value"}
    result = some_function()
    assert result == "value"
```

### `mock_j_dumps`

```python
@pytest.fixture
def mock_j_dumps():
    with patch("src.utils.jjson.j_dumps") as mock:
        yield mock
```

**Описание**: Фикстура `mock_j_dumps` создает мок-объект для функции `j_dumps` из модуля `src.utils.jjson`.

**Как работает функция**:
- Использует `patch` для замены `j_dumps` мок-объектом.
- Предоставляет мок-объект для использования в тестах.
- После завершения теста `patch` восстанавливает оригинальную функцию `j_dumps`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `mock`: Мок-объект функции `j_dumps`.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
def test_function(mock_j_dumps):
    some_data = {"key": "value"}
    some_function(some_data)
    mock_j_dumps.assert_called_once_with(some_data, "filename.json")
```

### `mock_logger`

```python
@pytest.fixture
def mock_logger():
    with patch("src.logger.logger") as mock:
        yield mock
```

**Описание**: Фикстура `mock_logger` создает мок-объект для логгера из модуля `src.logger`.

**Как работает функция**:
- Использует `patch` для замены логгера мок-объектом.
- Предоставляет мок-объект для использования в тестах.
- После завершения теста `patch` восстанавливает оригинальный логгер.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `mock`: Мок-объект логгера.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
def test_function(mock_logger):
    some_function()
    mock_logger.info.assert_called_once_with("Some message")
```

### `mock_get_directory_names`

```python
@pytest.fixture
def mock_get_directory_names():
    with patch("src.utils.get_directory_names") as mock:
        yield mock
```

**Описание**: Фикстура `mock_get_directory_names` создает мок-объект для функции `get_directory_names` из модуля `src.utils`.

**Как работает функция**:
- Использует `patch` для замены `get_directory_names` мок-объектом.
- Предоставляет мок-объект для использования в тестах.
- После завершения теста `patch` восстанавливает оригинальную функцию `get_directory_names`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `mock`: Мок-объект функции `get_directory_names`.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
def test_function(mock_get_directory_names):
    mock_get_directory_names.return_value = ["dir1", "dir2"]
    result = some_function()
    assert result == ["dir1", "dir2"]
```

### `mock_ali_promo_campaign`

```python
@pytest.fixture
def mock_ali_promo_campaign():
    with patch("src.suppliers.aliexpress.campaign.AliPromoCampaign") as mock:
        yield mock
```

**Описание**: Фикстура `mock_ali_promo_campaign` создает мок-объект для класса `AliPromoCampaign` из модуля `src.suppliers.aliexpress.campaign`.

**Как работает функция**:
- Использует `patch` для замены класса `AliPromoCampaign` мок-объектом.
- Предоставляет мок-объект для использования в тестах.
- После завершения теста `patch` восстанавливает оригинальный класс `AliPromoCampaign`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `mock`: Мок-объект класса `AliPromoCampaign`.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
def test_function(mock_ali_promo_campaign):
    instance = mock_ali_promo_campaign.return_value
    instance.process_data.return_value = "success"
    result = some_function()
    assert result == "success"
```

### `test_update_category_success`

```python
def test_update_category_success(mock_j_loads, mock_j_dumps, mock_logger):
    mock_json_path = Path("mock/path/to/category.json")
    mock_category = SimpleNamespace(name="test_category")

    mock_j_loads.return_value = {"category": {}}
    
    result = update_category(mock_json_path, mock_category)
    
    assert result is True
    mock_j_dumps.assert_called_once_with({"category": {"name": "test_category"}}, mock_json_path)
    mock_logger.error.assert_not_called()
```

**Описание**: Тест проверяет успешное обновление категории с использованием функции `update_category`.

**Как работает функция**:
- Создает мок-путь к JSON-файлу и мок-объект категории.
- Устанавливает возвращаемое значение для `mock_j_loads`, чтобы имитировать успешную загрузку данных.
- Вызывает функцию `update_category` с мок-объектами.
- Проверяет, что функция вернула `True`, `mock_j_dumps` был вызван с ожидаемыми аргументами, и `mock_logger.error` не был вызван.

**Параметры**:
- `mock_j_loads`: Мок-объект функции `j_loads`.
- `mock_j_dumps`: Мок-объект функции `j_dumps`.
- `mock_logger`: Мок-объект логгера.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:
- Пример вызова функции не требуется, так как это тестовая функция.

### `test_update_category_failure`

```python
def test_update_category_failure(mock_j_loads, mock_j_dumps, mock_logger):
    mock_json_path = Path("mock/path/to/category.json")
    mock_category = SimpleNamespace(name="test_category")

    mock_j_loads.side_effect = Exception("Error")
    
    result = update_category(mock_json_path, mock_category)
    
    assert result is False
    mock_j_dumps.assert_not_called()
    mock_logger.error.assert_called_once()
```

**Описание**: Тест проверяет ситуацию, когда обновление категории завершается с ошибкой из-за исключения при загрузке JSON.

**Как работает функция**:
- Создает мок-путь к JSON-файлу и мок-объект категории.
- Устанавливает `side_effect` для `mock_j_loads`, чтобы имитировать исключение при загрузке данных.
- Вызывает функцию `update_category` с мок-объектами.
- Проверяет, что функция вернула `False`, `mock_j_dumps` не был вызван, и `mock_logger.error` был вызван один раз.

**Параметры**:
- `mock_j_loads`: Мок-объект функции `j_loads`.
- `mock_j_dumps`: Мок-объект функции `j_dumps`.
- `mock_logger`: Мок-объект логгера.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:
- Пример вызова функции не требуется, так как это тестовая функция.

### `test_process_campaign_category_success`

```python
@pytest.mark.asyncio
async def test_process_campaign_category_success(mock_ali_promo_campaign, mock_logger):
    mock_campaign_name = "test_campaign"
    mock_category_name = "test_category"
    mock_language = "EN"
    mock_currency = "USD"

    mock_ali_promo = mock_ali_promo_campaign.return_value
    mock_ali_promo.process_affiliate_products = MagicMock()

    result = await process_campaign_category(mock_campaign_name, mock_category_name, mock_language, mock_currency)

    assert result is not None
    mock_logger.error.assert_not_called()
```

**Описание**: Тест проверяет успешную обработку категории кампании с использованием функции `process_campaign_category`.

**Как работает функция**:
- Создает мок-имена кампании и категории, язык и валюту.
- Получает мок-объект `AliPromoCampaign` и устанавливает `MagicMock` для метода `process_affiliate_products`.
- Вызывает функцию `process_campaign_category` с мок-объектами.
- Проверяет, что функция вернула не `None`, и `mock_logger.error` не был вызван.

**Параметры**:
- `mock_ali_promo_campaign`: Мок-объект класса `AliPromoCampaign`.
- `mock_logger`: Мок-объект логгера.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:
- Пример вызова функции не требуется, так как это тестовая функция.

### `test_process_campaign_category_failure`

```python
@pytest.mark.asyncio
async def test_process_campaign_category_failure(mock_ali_promo_campaign, mock_logger):
    mock_campaign_name = "test_campaign"
    mock_category_name = "test_category"
    mock_language = "EN"
    mock_currency = "USD"

    mock_ali_promo = mock_ali_promo_campaign.return_value
    mock_ali_promo.process_affiliate_products.side_effect = Exception("Error")

    result = await process_campaign_category(mock_campaign_name, mock_category_name, mock_language, mock_currency)

    assert result is None
    mock_logger.error.assert_called_once()
```

**Описание**: Тест проверяет ситуацию, когда обработка категории кампании завершается с ошибкой из-за исключения в методе `process_affiliate_products`.

**Как работает функция**:
- Создает мок-имена кампании и категории, язык и валюту.
- Получает мок-объект `AliPromoCampaign` и устанавливает `side_effect` для метода `process_affiliate_products`, чтобы имитировать исключение.
- Вызывает функцию `process_campaign_category` с мок-объектами.
- Проверяет, что функция вернула `None`, и `mock_logger.error` был вызван один раз.

**Параметры**:
- `mock_ali_promo_campaign`: Мок-объект класса `AliPromoCampaign`.
- `mock_logger`: Мок-объект логгера.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:
- Пример вызова функции не требуется, так как это тестовая функция.

### `test_process_campaign`

```python
def test_process_campaign(mock_get_directory_names, mock_logger):
    mock_campaign_name = "test_campaign"
    mock_categories = ["category1", "category2"]
    mock_language = "EN"
    mock_currency = "USD"
    mock_force = False

    mock_get_directory_names.return_value = mock_categories

    results = process_campaign(mock_campaign_name, mock_categories, mock_language, mock_currency, mock_force)

    assert len(results) == 2
    for category_name, result in results:
        assert category_name in mock_categories
        assert result is not None
    mock_logger.warning.assert_not_called()
```

**Описание**: Тест проверяет обработку кампании с использованием функции `process_campaign`.

**Как работает функция**:
- Создает мок-имя кампании, список категорий, язык, валюту и флаг `force`.
- Устанавливает возвращаемое значение для `mock_get_directory_names`, чтобы имитировать получение списка категорий.
- Вызывает функцию `process_campaign` с мок-объектами.
- Проверяет, что функция вернула список результатов длиной 2, каждая категория присутствует в списке мок-категорий, результат не `None`, и `mock_logger.warning` не был вызван.

**Параметры**:
- `mock_get_directory_names`: Мок-объект функции `get_directory_names`.
- `mock_logger`: Мок-объект логгера.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:
- Пример вызова функции не требуется, так как это тестовая функция.

### `test_main`

```python
@pytest.mark.asyncio
async def test_main(mock_get_directory_names):
    mock_campaign_name = "test_campaign"
    mock_categories = ["category1", "category2"]
    mock_language = "EN"
    mock_currency = "USD"
    mock_force = False

    mock_get_directory_names.return_value = mock_categories

    await main(mock_campaign_name, mock_categories, mock_language, mock_currency, mock_force)

    mock_get_directory_names.assert_called_once()
```

**Описание**: Тест проверяет основную функцию `main`, которая координирует процесс подготовки кампаний.

**Как работает функция**:
- Создает мок-имя кампании, список категорий, язык, валюту и флаг `force`.
- Устанавливает возвращаемое значение для `mock_get_directory_names`, чтобы имитировать получение списка категорий.
- Вызывает асинхронную функцию `main` с мок-объектами.
- Проверяет, что функция `mock_get_directory_names` была вызвана один раз.

**Параметры**:
- `mock_get_directory_names`: Мок-объект функции `get_directory_names`.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:
- Пример вызова функции не требуется, так как это тестовая функция.