# Модуль prepare_ai_campaign

## Обзор

Модуль `prepare_ai_campaign.py` предназначен для подготовки и обработки рекламных кампаний AliExpress с использованием AI. Он включает в себя функции для обработки категорий кампаний, отдельных кампаний и всех кампаний в целом. Основной функциональностью модуля является использование класса `AliCampaignEditor` для обработки AI кампаний.

## Подробней

Этот модуль является частью системы управления рекламными кампаниями AliExpress. Он автоматизирует процесс подготовки кампаний с использованием AI, что позволяет упростить и ускорить создание и настройку рекламных кампаний. Модуль использует другие модули проекта, такие как `src.suppliers.aliexpress.campaign`, `src.utils` и `src.logger`, для выполнения своих задач.

## Классы

### `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` используется для редактирования и обработки рекламных кампаний AliExpress.

**Методы**:
- `process_ai_campaign`: Метод для обработки AI кампаний.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `campaign_file` (str): Файл кампании.

**Примеры**
```python
campaign_name = 'lighting'
campaign_file = 'EN_US.JSON'
campaign_editor = AliCampaignEditor(campaign_name = campaign_name, campaign_file = campaign_file )
campaign_editor.process_ai_campaign(campaign_name)
```

## Функции

### `process_campaign_category`

```python
def process_campaign_category(...):
    """ """
```

**Описание**: Функция для обработки категорий кампаний.

### `process_campaign`

```python
def process_campaign(...):
    """ """
```

**Описание**: Функция для обработки отдельной кампании.

### `process_all_campaigns`

```python
def process_all_campaigns(...):
    """ """
```

**Описание**: Функция для обработки всех кампаний.

### `get_filenames`

```python
def get_filenames(...):
    """ """
```

**Описание**: Функция для получения имен файлов.

### `get_directory_names`

```python
def get_directory_names(...):
    """ """
```

**Описание**: Функция для получения имен директорий.