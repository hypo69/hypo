# Модуль для тестирования подготовки кампаний AliExpress

## Обзор

Модуль содержит набор тестов для функций подготовки кампаний AliExpress, включая обновление категорий, обработку кампаний и запуск процесса подготовки. Используются фикстуры `pytest` для мокирования зависимостей, таких как загрузка и сохранение JSON, логирование и получение списка директорий.

## Подробней

Этот модуль тестирует основные функции подготовки кампаний AliExpress, обеспечивая их корректную работу. Тесты охватывают успешные и неудачные сценарии, а также проверяют взаимодействие функций с внешними зависимостями.

## Фикстуры

### `mock_j_loads`

```python
@pytest.fixture
def mock_j_loads():
    with patch("src.utils.jjson.j_loads") as mock:
        yield mock
```

**Описание**:
Мокирует функцию `j_loads` из модуля `src.utils.jjson` для загрузки JSON-данных.

### `mock_j_dumps`

```python
@pytest.fixture
def mock_j_dumps():
    with patch("src.utils.jjson.j_dumps") as mock:
        yield mock
```

**Описание**:
Мокирует функцию `j_dumps` из модуля `src.utils.jjson` для сохранения JSON-данных.

### `mock_logger`

```python
@pytest.fixture
def mock_logger():
    with patch("src.logger.logger") as mock:
        yield mock
```

**Описание**:
Мокирует модуль логирования `src.logger.logger`.

### `mock_get_directory_names`

```python
@pytest.fixture
def mock_get_directory_names():
    with patch("src.utils.get_directory_names") as mock:
        yield mock
```

**Описание**:
Мокирует функцию `get_directory_names` из модуля `src.utils` для получения списка директорий.

### `mock_ali_promo_campaign`

```python
@pytest.fixture
def mock_ali_promo_campaign():
    with patch("src.suppliers.aliexpress.campaign.AliPromoCampaign") as mock:
        yield mock
```

**Описание**:
Мокирует класс `AliPromoCampaign` из модуля `src.suppliers.aliexpress.campaign`.

## Функции

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

**Назначение**:
Тестирует успешное обновление категории.

**Параметры**:
- `mock_j_loads`: Мокированная функция `j_loads`.
- `mock_j_dumps`: Мокированная функция `j_dumps`.
- `mock_logger`: Мокированный модуль логирования.

**Возвращает**:
`None`

**Как работает функция**:
1.  **Определение переменных**: Определяет мокированный путь к JSON-файлу и создает мокированный объект категории.
2.  **Мокирование возвращаемого значения `j_loads`**: Устанавливает возвращаемое значение для `mock_j_loads` в виде словаря с пустой категорией.
3.  **Вызов функции `update_category`**: Вызывает функцию `update_category` с мокированными параметрами.
4.  **Проверки**: Проверяет, что функция вернула `True`, `mock_j_dumps` была вызвана один раз с ожидаемыми аргументами, и `mock_logger.error` не вызывался.

**Примеры**:

```python
# Пример вызова функции в тесте
test_update_category_success(mock_j_loads, mock_j_dumps, mock_logger)
```

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

**Назначение**:
Тестирует неудачное обновление категории.

**Параметры**:
- `mock_j_loads`: Мокированная функция `j_loads`.
- `mock_j_dumps`: Мокированная функция `j_dumps`.
- `mock_logger`: Мокированный модуль логирования.

**Возвращает**:
`None`

**Как работает функция**:
1.  **Определение переменных**: Определяет мокированный путь к JSON-файлу и создает мокированный объект категории.
2.  **Мокирование исключения `j_loads`**: Устанавливает, что `mock_j_loads` вызывает исключение.
3.  **Вызов функции `update_category`**: Вызывает функцию `update_category` с мокированными параметрами.
4.  **Проверки**: Проверяет, что функция вернула `False`, `mock_j_dumps` не вызывалась, и `mock_logger.error` был вызван один раз.

**Примеры**:

```python
# Пример вызова функции в тесте
test_update_category_failure(mock_j_loads, mock_j_dumps, mock_logger)
```

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

**Назначение**:
Тестирует успешную обработку категории кампании.

**Параметры**:
- `mock_ali_promo_campaign`: Мокированный класс `AliPromoCampaign`.
- `mock_logger`: Мокированный модуль логирования.

**Возвращает**:
`None`

**Как работает функция**:
1.  **Определение переменных**: Определяет мокированные параметры кампании и категории.
2.  **Мокирование метода `process_affiliate_products`**: Мокирует метод `process_affiliate_products` класса `AliPromoCampaign`.
3.  **Вызов функции `process_campaign_category`**: Вызывает функцию `process_campaign_category` с мокированными параметрами.
4.  **Проверки**: Проверяет, что функция вернула не `None`, и `mock_logger.error` не вызывался.

**Примеры**:

```python
# Пример вызова функции в тесте
await test_process_campaign_category_success(mock_ali_promo_campaign, mock_logger)
```

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

**Назначение**:
Тестирует неудачную обработку категории кампании.

**Параметры**:
- `mock_ali_promo_campaign`: Мокированный класс `AliPromoCampaign`.
- `mock_logger`: Мокированный модуль логирования.

**Возвращает**:
`None`

**Как работает функция**:
1.  **Определение переменных**: Определяет мокированные параметры кампании и категории.
2.  **Мокирование исключения метода `process_affiliate_products`**: Устанавливает, что метод `process_affiliate_products` класса `AliPromoCampaign` вызывает исключение.
3.  **Вызов функции `process_campaign_category`**: Вызывает функцию `process_campaign_category` с мокированными параметрами.
4.  **Проверки**: Проверяет, что функция вернула `None`, и `mock_logger.error` был вызван один раз.

**Примеры**:

```python
# Пример вызова функции в тесте
await test_process_campaign_category_failure(mock_ali_promo_campaign, mock_logger)
```

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

**Назначение**:
Тестирует обработку кампании.

**Параметры**:
- `mock_get_directory_names`: Мокированная функция `get_directory_names`.
- `mock_logger`: Мокированный модуль логирования.

**Возвращает**:
`None`

**Как работает функция**:
1.  **Определение переменных**: Определяет мокированные параметры кампании и список категорий.
2.  **Мокирование возвращаемого значения `get_directory_names`**: Устанавливает возвращаемое значение для `mock_get_directory_names` в виде списка категорий.
3.  **Вызов функции `process_campaign`**: Вызывает функцию `process_campaign` с мокированными параметрами.
4.  **Проверки**: Проверяет, что длина возвращаемого списка равна 2, каждый результат соответствует ожидаемой категории, и `mock_logger.warning` не вызывался.

**Примеры**:

```python
# Пример вызова функции в тесте
test_process_campaign(mock_get_directory_names, mock_logger)
```

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

**Назначение**:
Тестирует основную функцию `main`.

**Параметры**:
- `mock_get_directory_names`: Мокированная функция `get_directory_names`.

**Возвращает**:
`None`

**Как работает функция**:
1.  **Определение переменных**: Определяет мокированные параметры кампании и список категорий.
2.  **Мокирование возвращаемого значения `get_directory_names`**: Устанавливает возвращаемое значение для `mock_get_directory_names` в виде списка категорий.
3.  **Вызов функции `main`**: Вызывает функцию `main` с мокированными параметрами.
4.  **Проверки**: Проверяет, что `mock_get_directory_names` была вызвана один раз.

**Примеры**:

```python
# Пример вызова функции в тесте
await test_main(mock_get_directory_names)
```