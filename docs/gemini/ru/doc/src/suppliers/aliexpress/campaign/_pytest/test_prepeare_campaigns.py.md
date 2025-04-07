# Модуль для тестирования подготовки кампаний AliExpress

## Обзор

Модуль содержит набор тестов для функций, связанных с подготовкой кампаний AliExpress, таких как обновление категорий, обработка кампаний по категориям, обработка кампаний целиком и запуск процесса подготовки кампаний.

## Подробнее

Этот модуль использует библиотеку `pytest` для организации и запуска тестов. В тестах активно применяются `mock`-объекты для изоляции тестируемых функций от внешних зависимостей и контроля их поведения. Модуль предназначен для проверки корректности работы функций подготовки кампаний AliExpress, включая обработку данных, взаимодействие с внешними сервисами и логирование ошибок.

## Fixtures

### `mock_j_loads`

```python
@pytest.fixture
def mock_j_loads():
    with patch("src.utils.jjson.j_loads") as mock:
        yield mock
```

**Описание**:
- `Fixture` для имитации функции `j_loads` из модуля `src.utils.jjson`.

### `mock_j_dumps`

```python
@pytest.fixture
def mock_j_dumps():
    with patch("src.utils.jjson.j_dumps") as mock:
        yield mock
```

**Описание**:
- `Fixture` для имитации функции `j_dumps` из модуля `src.utils.jjson`.

### `mock_logger`

```python
@pytest.fixture
def mock_logger():
    with patch("src.logger.logger") as mock:
        yield mock
```

**Описание**:
- `Fixture` для имитации объекта `logger` из модуля `src.logger`.

### `mock_get_directory_names`

```python
@pytest.fixture
def mock_get_directory_names():
    with patch("src.utils.get_directory_names") as mock:
        yield mock
```

**Описание**:
- `Fixture` для имитации функции `get_directory_names` из модуля `src.utils`.

### `mock_ali_promo_campaign`

```python
@pytest.fixture
def mock_ali_promo_campaign():
    with patch("src.suppliers.aliexpress.campaign.AliPromoCampaign") as mock:
        yield mock
```

**Описание**:
- `Fixture` для имитации класса `AliPromoCampaign` из модуля `src.suppliers.aliexpress.campaign`.

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

**Назначение**: Тест проверяет успешное обновление категории.

**Параметры**:
- `mock_j_loads`: `mock`-объект функции `j_loads`.
- `mock_j_dumps`: `mock`-объект функции `j_dumps`.
- `mock_logger`: `mock`-объект логгера.

**Как работает функция**:
1. **Инициализация моков**:
   - Создаются мок-путь к JSON-файлу категории (`mock_json_path`) и мок-объект категории (`mock_category`) с именем "test_category".
2. **Настройка поведения моков**:
   - Функция `mock_j_loads` настраивается так, чтобы возвращать пустой словарь `{"category": {}}`.
3. **Вызов тестируемой функции**:
   - Вызывается функция `update_category` с мок-путем и мок-категорией.
4. **Ассерты**:
   - Проверяется, что функция `update_category` возвращает `True`, указывая на успешное обновление.
   - Проверяется, что функция `mock_j_dumps` была вызвана ровно один раз с ожидаемыми аргументами: словарем с обновленной категорией и мок-путем к файлу.
   - Убеждаемся, что логгер не вызывал ошибки.
     ```
     Обновление категории
     │
     ├── Загрузка JSON (mock_j_loads)
     │   └── {"category": {}}
     │
     ├── Обновление категории
     │   └── {"category": {"name": "test_category"}}
     │
     └── Сохранение JSON (mock_j_dumps)
         └── {"category": {"name": "test_category"}} в mock_json_path
     ```
**Примеры**:

```python
mock_json_path = Path("mock/path/to/category.json")
mock_category = SimpleNamespace(name="test_category")
mock_j_loads.return_value = {"category": {}}
result = update_category(mock_json_path, mock_category)
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

**Назначение**: Тест проверяет ситуацию, когда обновление категории завершается с ошибкой.

**Параметры**:
- `mock_j_loads`: `mock`-объект функции `j_loads`.
- `mock_j_dumps`: `mock`-объект функции `j_dumps`.
- `mock_logger`: `mock`-объект логгера.

**Как работает функция**:
1. **Инициализация моков**:
   - Создаются мок-путь к JSON-файлу категории (`mock_json_path`) и мок-объект категории (`mock_category`) с именем "test_category".
2. **Настройка поведения моков**:
   - Функция `mock_j_loads` настраивается так, чтобы выбрасывать исключение `Exception("Error")`.
3. **Вызов тестируемой функции**:
   - Вызывается функция `update_category` с мок-путем и мок-категорией.
4. **Ассерты**:
   - Проверяется, что функция `update_category` возвращает `False`, указывая на неудачное обновление.
   - Проверяется, что функция `mock_j_dumps` не была вызвана.
   - Проверяется, что функция `mock_logger.error` была вызвана ровно один раз.
     ```
     Обновление категории
     │
     ├── Загрузка JSON (mock_j_loads)
     │   └── Выбрасывает исключение: Exception("Error")
     │
     └── Ошибка обновления
         └── Логгирование ошибки (mock_logger.error)
     ```

**Примеры**:

```python
mock_json_path = Path("mock/path/to/category.json")
mock_category = SimpleNamespace(name="test_category")
mock_j_loads.side_effect = Exception("Error")
result = update_category(mock_json_path, mock_category)
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

**Назначение**: Тест проверяет успешную обработку категории кампании.

**Параметры**:
- `mock_ali_promo_campaign`: `mock`-объект класса `AliPromoCampaign`.
- `mock_logger`: `mock`-объект логгера.

**Как работает функция**:
1. **Инициализация моков**:
   - Определяются мок-имя кампании (`mock_campaign_name`), мок-имя категории (`mock_category_name`), мок-язык (`mock_language`) и мок-валюта (`mock_currency`).
2. **Настройка поведения моков**:
   - Создается мок-объект `mock_ali_promo` на основе `mock_ali_promo_campaign`, и его метод `process_affiliate_products` заменяется на `MagicMock`.
3. **Вызов тестируемой функции**:
   - Вызывается асинхронная функция `process_campaign_category` с мок-параметрами.
4. **Ассерты**:
   - Проверяется, что функция `process_campaign_category` возвращает не `None`.
   - Проверяется, что логгер не вызывал ошибки.
     ```
     Обработка категории кампании
     │
     ├── Создание экземпляра AliPromoCampaign (mock_ali_promo_campaign)
     │   └── mock_ali_promo
     │
     ├── Обработка партнерских продуктов (mock_ali_promo.process_affiliate_products)
     │   └── MagicMock
     │
     └── Результат обработки
         └── Не None
     ```

**Примеры**:

```python
mock_campaign_name = "test_campaign"
mock_category_name = "test_category"
mock_language = "EN"
mock_currency = "USD"
mock_ali_promo = mock_ali_promo_campaign.return_value
mock_ali_promo.process_affiliate_products = MagicMock()
result = await process_campaign_category(mock_campaign_name, mock_category_name, mock_language, mock_currency)
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

**Назначение**: Тест проверяет ситуацию, когда обработка категории кампании завершается с ошибкой.

**Параметры**:
- `mock_ali_promo_campaign`: `mock`-объект класса `AliPromoCampaign`.
- `mock_logger`: `mock`-объект логгера.

**Как работает функция**:
1. **Инициализация моков**:
   - Определяются мок-имя кампании (`mock_campaign_name`), мок-имя категории (`mock_category_name`), мок-язык (`mock_language`) и мок-валюта (`mock_currency`).
2. **Настройка поведения моков**:
   - Создается мок-объект `mock_ali_promo` на основе `mock_ali_promo_campaign`, и его метод `process_affiliate_products` настраивается так, чтобы выбрасывать исключение `Exception("Error")`.
3. **Вызов тестируемой функции**:
   - Вызывается асинхронная функция `process_campaign_category` с мок-параметрами.
4. **Ассерты**:
   - Проверяется, что функция `process_campaign_category` возвращает `None`.
   - Проверяется, что функция `mock_logger.error` была вызвана ровно один раз.
     ```
     Обработка категории кампании
     │
     ├── Создание экземпляра AliPromoCampaign (mock_ali_promo_campaign)
     │   └── mock_ali_promo
     │
     ├── Обработка партнерских продуктов (mock_ali_promo.process_affiliate_products)
     │   └── Выбрасывает исключение: Exception("Error")
     │
     └── Ошибка обработки
         └── Логгирование ошибки (mock_logger.error)
     ```

**Примеры**:

```python
mock_campaign_name = "test_campaign"
mock_category_name = "test_category"
mock_language = "EN"
mock_currency = "USD"
mock_ali_promo = mock_ali_promo_campaign.return_value
mock_ali_promo.process_affiliate_products.side_effect = Exception("Error")
result = await process_campaign_category(mock_campaign_name, mock_category_name, mock_language, mock_currency)
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

**Назначение**: Тест проверяет обработку кампании.

**Параметры**:
- `mock_get_directory_names`: `mock`-объект функции `get_directory_names`.
- `mock_logger`: `mock`-объект логгера.

**Как работает функция**:
1. **Инициализация моков**:
   - Определяются мок-имя кампании (`mock_campaign_name`), мок-список категорий (`mock_categories`), мок-язык (`mock_language`), мок-валюта (`mock_currency`) и мок-флаг `force` (`mock_force`).
2. **Настройка поведения моков**:
   - Функция `mock_get_directory_names` настраивается так, чтобы возвращать мок-список категорий.
3. **Вызов тестируемой функции**:
   - Вызывается функция `process_campaign` с мок-параметрами.
4. **Ассерты**:
   - Проверяется, что длина списка результатов равна 2.
   - Проверяется, что каждая категория из списка результатов содержится в мок-списке категорий и что результат обработки не равен `None`.
   - Проверяется, что логгер не вызывал предупреждения.
     ```
     Обработка кампании
     │
     ├── Получение списка категорий (mock_get_directory_names)
     │   └── ["category1", "category2"]
     │
     ├── Обработка каждой категории
     │   ├── category1: результат не None
     │   └── category2: результат не None
     │
     └── Проверка отсутствия предупреждений (mock_logger.warning)
     ```

**Примеры**:

```python
mock_campaign_name = "test_campaign"
mock_categories = ["category1", "category2"]
mock_language = "EN"
mock_currency = "USD"
mock_force = False
mock_get_directory_names.return_value = mock_categories
results = process_campaign(mock_campaign_name, mock_categories, mock_language, mock_currency, mock_force)
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

**Назначение**: Тест проверяет функцию `main`.

**Параметры**:
- `mock_get_directory_names`: `mock`-объект функции `get_directory_names`.

**Как работает функция**:
1. **Инициализация моков**:
   - Определяются мок-имя кампании (`mock_campaign_name`), мок-список категорий (`mock_categories`), мок-язык (`mock_language`), мок-валюта (`mock_currency`) и мок-флаг `force` (`mock_force`).
2. **Настройка поведения моков**:
   - Функция `mock_get_directory_names` настраивается так, чтобы возвращать мок-список категорий.
3. **Вызов тестируемой функции**:
   - Вызывается асинхронная функция `main` с мок-параметрами.
4. **Ассерты**:
   - Проверяется, что функция `mock_get_directory_names` была вызвана ровно один раз.
     ```
     Запуск main
     │
     ├── Получение списка категорий (mock_get_directory_names)
     │   └── ["category1", "category2"]
     │
     └── Вызов main
         └── mock_get_directory_names был вызван один раз
     ```

**Примеры**:

```python
mock_campaign_name = "test_campaign"
mock_categories = ["category1", "category2"]
mock_language = "EN"
mock_currency = "USD"
mock_force = False
mock_get_directory_names.return_value = mock_categories
await main(mock_campaign_name, mock_categories, mock_language, mock_currency, mock_force)
```