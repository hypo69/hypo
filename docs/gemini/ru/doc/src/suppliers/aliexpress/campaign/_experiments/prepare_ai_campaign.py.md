# Модуль `prepare_ai_campaign.py`

## Обзор

Модуль предназначен для подготовки и обработки рекламных кампаний на платформе AliExpress с использованием AI.
Он предоставляет функциональность для создания, редактирования и обработки кампаний, включая работу с категориями и другими параметрами кампании.

## Подробней

Модуль `prepare_ai_campaign.py` является частью экспериментов по автоматизации подготовки рекламных кампаний AliExpress с использованием искусственного интеллекта. Он использует другие модули проекта, такие как `AliCampaignEditor`, `process_campaign_category` и `process_campaign`, для выполнения задач, связанных с обработкой кампаний.

## Функции

### `process_campaign_category`
```python
from src.suppliers.aliexpress.campaign import process_campaign_category
```
Функция для обработки категорий рекламной кампании.

### `process_campaign`
```python
from src.suppliers.aliexpress.campaign import process_campaign
```
Функция для обработки рекламной кампании.

### `process_all_campaigns`
```python
from src.suppliers.aliexpress.campaign import process_all_campaigns
```
Функция для обработки всех рекламных кампаний.

## Переменные

### `campaign_name`
```python
campaign_name = 'lighting'
```
Имя рекламной кампании. В данном случае - 'lighting'.

### `campaign_file`
```python
campaign_file = 'EN_US.JSON'
```
Имя файла конфигурации для рекламной кампании. В данном случае - 'EN_US.JSON'.

### `campaign_editor`
```python
campaign_editor = AliCampaignEditor(campaign_name = campaign_name, campaign_file = campaign_file )
```
Экземпляр класса `AliCampaignEditor`, используемый для редактирования рекламной кампании.

## Классы

### `AliCampaignEditor`

**Описание**: Класс для редактирования рекламных кампаний AliExpress.

**Методы**:
- `process_ai_campaign(campaign_name)`: Метод для обработки AI-кампании.

## Использование

```python
campaign_editor.process_ai_campaign(campaign_name)
```
Вызов метода `process_ai_campaign` для обработки рекламной кампании с заданным именем.