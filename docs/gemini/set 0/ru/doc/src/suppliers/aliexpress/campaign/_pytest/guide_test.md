# Руководство для Тестера Модуля Рекламных Кампаний AliExpress

## Обзор

Данный документ предназначен для тестеров, проверяющих модуль подготовки рекламных кампаний на платформе AliExpress.  Модуль включает файлы для управления кампаниями, подготовки категорий и интеграционных тестов.

## Файлы Модуля

### `edit_campaign.py`

**Описание**: Файл содержит класс `AliCampaignEditor`, наследующий от `AliPromoCampaign`, для управления рекламной кампанией.

**Классы**:

#### `AliCampaignEditor`

**Описание**: Класс для инициализации и управления рекламной кампанией.


**Методы** (Подробные описания методов потребуют доступа к коду самого файла `edit_campaign.py`)


### `prepare_campaigns.py`

**Описание**: Файл содержит функции для подготовки материалов рекламной кампании, включая обновление категорий и обработку кампаний по категориям.

**Функции**:

#### `update_category(category_data: dict, file_path: str) -> bool`

**Описание**: Обновляет данные категории в JSON файле.

**Параметры**:
- `category_data` (dict): Словарь с данными категории для обновления.
- `file_path` (str): Путь к JSON файлу с данными кампании.

**Возвращает**:
- `bool`: `True`, если обновление прошло успешно, иначе `False`.

#### `process_campaign_category(category_data: dict, campaign_id: int) -> dict | None`

**Описание**: Обрабатывает конкретную категорию в рамках кампании.

**Параметры**:
- `category_data` (dict): Данные категории.
- `campaign_id` (int): Идентификатор кампании.

**Возвращает**:
- `dict | None`: Результат обработки категории или `None`, если произошла ошибка.

#### `process_campaign(campaign_data: dict) -> list | None`

**Описание**: Обрабатывает всю кампанию по всем категориям.

**Параметры**:
- `campaign_data` (dict): Данные кампании.

**Возвращает**:
- `list | None`: Список результатов обработки каждой категории или `None`, если произошла ошибка.


#### `main(campaign_data: dict) -> None`

**Описание**: Асинхронная основная функция для обработки кампании.

**Параметры**:
- `campaign_data` (dict): Данные кампании.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Общие исключения, возникающие во время обработки.


### `test_campaign_integration.py`

**Описание**: Файл содержит тесты для проверки интеграции всех компонентов модуля.

**Тесты**:

#### `test_update_category_success`

**Описание**: Проверка успешного обновления категории.


#### `test_update_category_failure`

**Описание**: Проверка обработки ошибки при обновлении категории.


#### `test_process_campaign_category_success`

**Описание**: Проверка успешной обработки категории.


#### `test_process_campaign_category_failure`

**Описание**: Проверка обработки ошибки при обработке категории.


#### `test_process_campaign`

**Описание**: Проверка обработки всех категорий в кампании.


#### `test_main`

**Описание**: Проверка основного сценария выполнения кампании.


## Инструкции по Тестированию

### Установка Зависимостей

```bash
pip install -r requirements.txt
```

### Запуск Тестов

```bash
pytest test_campaign_integration.py
```

## Проверка Функциональности

(Подробные описания проверки функциональности, с ожидаемыми результатами, требуют доступа к коду `edit_campaign.py` и `prepare_campaigns.py`)


## Заключение

Убедитесь, что все тесты пройдены успешно. В случае проблем, обратитесь к разработчикам.