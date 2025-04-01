# Модуль для тестирования подготовки кампаний AliExpress

## Обзор

Модуль содержит набор тестов для функций, связанных с подготовкой кампаний AliExpress, включая обновление категорий, обработку кампаний и запуск основного процесса подготовки.

## Подробнее

Этот файл содержит тесты, проверяющие корректность работы функций `update_category`, `process_campaign_category`, `process_campaign` и `main` из модуля `src.suppliers.aliexpress.campaign.prepare_campaigns`.  В тестах используются моки (mocks) для изоляции тестируемых функций от внешних зависимостей и для контроля их поведения.

## Fixtures (фикстуры)

### `mock_j_loads`

```python
@pytest.fixture
def mock_j_loads():
    with patch("src.utils.jjson.j_loads") as mock:
        yield mock
```

**Назначение**: Создает мок для функции `j_loads` из модуля `src.utils.jjson`.

**Как работает фикстура**:

1.  Использует `patch` из модуля `unittest.mock` для замены функции `j_loads` моком.
2.  Передает мок в тест через `yield`.

### `mock_j_dumps`

```python
@pytest.fixture
def mock_j_dumps():
    with patch("src.utils.jjson.j_dumps") as mock:
        yield mock
```

**Назначение**: Создает мок для функции `j_dumps` из модуля `src.utils.jjson`.

**Как работает фикстура**:

1.  Использует `patch` из модуля `unittest.mock` для замены функции `j_dumps` моком.
2.  Передает мок в тест через `yield`.

### `mock_logger`

```python
@pytest.fixture
def mock_logger():
    with patch("src.logger.logger") as mock:
        yield mock
```

**Назначение**: Создает мок для объекта `logger` из модуля `src.logger`.

**Как работает фикстура**:

1.  Использует `patch` из модуля `unittest.mock` для замены объекта `logger` моком.
2.  Передает мок в тест через `yield`.

### `mock_get_directory_names`

```python
@pytest.fixture
def mock_get_directory_names():
    with patch("src.utils.get_directory_names") as mock:
        yield mock
```

**Назначение**: Создает мок для функции `get_directory_names` из модуля `src.utils`.

**Как работает фикстура**:

1.  Использует `patch` из модуля `unittest.mock` для замены функции `get_directory_names` моком.
2.  Передает мок в тест через `yield`.

### `mock_ali_promo_campaign`

```python
@pytest.fixture
def mock_ali_promo_campaign():
    with patch("src.suppliers.aliexpress.campaign.AliPromoCampaign") as mock:
        yield mock
```

**Назначение**: Создает мок для класса `AliPromoCampaign` из модуля `src.suppliers.aliexpress.campaign`.

**Как работает фикстура**:

1.  Использует `patch` из модуля `unittest.mock` для замены класса `AliPromoCampaign` моком.
2.  Передает мок в тест через `yield`.

## Функции

### `test_update_category_success`

```python
def test_update_category_success(mock_j_loads, mock_j_dumps, mock_logger):
    """
    Тестирует успешное обновление категории.

    Args:
        mock_j_loads: Мок функции j_loads.
        mock_j_dumps: Мок функции j_dumps.
        mock_logger: Мок объекта logger.
    """
    ...
```

**Назначение**: Тестирует успешный сценарий функции `update_category`.

**Параметры**:

*   `mock_j_loads`: Мок функции `j_loads`.
*   `mock_j_dumps`: Мок функции `j_dumps`.
*   `mock_logger`: Мок объекта `logger`.

**Как работает функция**:

1.  Определяет путь к мок-файлу JSON и создает объект `SimpleNamespace` для представления категории.
2.  Настраивает `mock_j_loads` для возврата словаря с категорией.
3.  Вызывает функцию `update_category` с мок-путем и мок-категорией.
4.  Проверяет, что функция вернула `True`.
5.  Проверяет, что `mock_j_dumps` был вызван с ожидаемыми аргументами.
6.  Проверяет, что `mock_logger.error` не был вызван.

**Примеры**:

```python
# Пример вызова теста с использованием фикстур
def test_update_category_success(mock_j_loads, mock_j_dumps, mock_logger):
    # ... (код теста)
    pass
```

### `test_update_category_failure`

```python
def test_update_category_failure(mock_j_loads, mock_j_dumps, mock_logger):
    """
    Тестирует ситуацию, когда обновление категории завершается с ошибкой.

    Args:
        mock_j_loads: Мок функции j_loads.
        mock_j_dumps: Мок функции j_dumps.
        mock_logger: Мок объекта logger.
    """
    ...
```

**Назначение**: Тестирует сценарий, когда функция `update_category` завершается с ошибкой.

**Параметры**:

*   `mock_j_loads`: Мок функции `j_loads`.
*   `mock_j_dumps`: Мок функции `j_dumps`.
*   `mock_logger`: Мок объекта `logger`.

**Как работает функция**:

1.  Определяет путь к мок-файлу JSON и создает объект `SimpleNamespace` для представления категории.
2.  Настраивает `mock_j_loads` для вызова исключения.
3.  Вызывает функцию `update_category` с мок-путем и мок-категорией.
4.  Проверяет, что функция вернула `False`.
5.  Проверяет, что `mock_j_dumps` не был вызван.
6.  Проверяет, что `mock_logger.error` был вызван один раз.

**Примеры**:

```python
# Пример вызова теста с использованием фикстур
def test_update_category_failure(mock_j_loads, mock_j_dumps, mock_logger):
    # ... (код теста)
    pass
```

### `test_process_campaign_category_success`

```python
@pytest.mark.asyncio
async def test_process_campaign_category_success(mock_ali_promo_campaign, mock_logger):
    """
    Тестирует успешную обработку категории кампании.

    Args:
        mock_ali_promo_campaign: Мок класса AliPromoCampaign.
        mock_logger: Мок объекта logger.
    """
    ...
```

**Назначение**: Тестирует успешный сценарий функции `process_campaign_category`.

**Параметры**:

*   `mock_ali_promo_campaign`: Мок класса `AliPromoCampaign`.
*   `mock_logger`: Мок объекта `logger`.

**Как работает функция**:

1.  Определяет мок-имена кампании и категории, язык и валюту.
2.  Настраивает `mock_ali_promo_campaign` для возврата мок-объекта.
3.  Настраивает мок-объект для успешной обработки аффилированных продуктов.
4.  Вызывает функцию `process_campaign_category` с мок-параметрами.
5.  Проверяет, что функция вернула не `None`.
6.  Проверяет, что `mock_logger.error` не был вызван.

**Примеры**:

```python
# Пример вызова теста с использованием фикстур
@pytest.mark.asyncio
async def test_process_campaign_category_success(mock_ali_promo_campaign, mock_logger):
    # ... (код теста)
    pass
```

### `test_process_campaign_category_failure`

```python
@pytest.mark.asyncio
async def test_process_campaign_category_failure(mock_ali_promo_campaign, mock_logger):
    """
    Тестирует ситуацию, когда обработка категории кампании завершается с ошибкой.

    Args:
        mock_ali_promo_campaign: Мок класса AliPromoCampaign.
        mock_logger: Мок объекта logger.
    """
    ...
```

**Назначение**: Тестирует сценарий, когда функция `process_campaign_category` завершается с ошибкой.

**Параметры**:

*   `mock_ali_promo_campaign`: Мок класса `AliPromoCampaign`.
*   `mock_logger`: Мок объекта `logger`.

**Как работает функция**:

1.  Определяет мок-имена кампании и категории, язык и валюту.
2.  Настраивает `mock_ali_promo_campaign` для возврата мок-объекта.
3.  Настраивает мок-объект для вызова исключения при обработке аффилированных продуктов.
4.  Вызывает функцию `process_campaign_category` с мок-параметрами.
5.  Проверяет, что функция вернула `None`.
6.  Проверяет, что `mock_logger.error` был вызван один раз.

**Примеры**:

```python
# Пример вызова теста с использованием фикстур
@pytest.mark.asyncio
async def test_process_campaign_category_failure(mock_ali_promo_campaign, mock_logger):
    # ... (код теста)
    pass
```

### `test_process_campaign`

```python
def test_process_campaign(mock_get_directory_names, mock_logger):
    """
    Тестирует обработку кампании.

    Args:
        mock_get_directory_names: Мок функции get_directory_names.
        mock_logger: Мок объекта logger.
    """
    ...
```

**Назначение**: Тестирует функцию `process_campaign`.

**Параметры**:

*   `mock_get_directory_names`: Мок функции `get_directory_names`.
*   `mock_logger`: Мок объекта `logger`.

**Как работает функция**:

1.  Определяет мок-имя кампании, список категорий, язык, валюту и флаг `force`.
2.  Настраивает `mock_get_directory_names` для возврата списка мок-категорий.
3.  Вызывает функцию `process_campaign` с мок-параметрами.
4.  Проверяет, что длина списка результатов равна 2.
5.  Проверяет, что имя категории присутствует в списке мок-категорий и что результат не `None` для каждой категории.
6.  Проверяет, что `mock_logger.warning` не был вызван.

**Примеры**:

```python
# Пример вызова теста с использованием фикстур
def test_process_campaign(mock_get_directory_names, mock_logger):
    # ... (код теста)
    pass
```

### `test_main`

```python
@pytest.mark.asyncio
async def test_main(mock_get_directory_names):
    """
    Тестирует основную функцию.

    Args:
        mock_get_directory_names: Мок функции get_directory_names.
    """
    ...
```

**Назначение**: Тестирует функцию `main`.

**Параметры**:

*   `mock_get_directory_names`: Мок функции `get_directory_names`.

**Как работает функция**:

1.  Определяет мок-имя кампании, список категорий, язык, валюту и флаг `force`.
2.  Настраивает `mock_get_directory_names` для возврата списка мок-категорий.
3.  Вызывает функцию `main` с мок-параметрами.
4.  Проверяет, что `mock_get_directory_names` был вызван один раз.

**Примеры**:

```python
# Пример вызова теста с использованием фикстур
@pytest.mark.asyncio
async def test_main(mock_get_directory_names):
    # ... (код теста)
    pass