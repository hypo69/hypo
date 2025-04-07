# Модуль `prepare_new_campaign.py`

## Обзор

Модуль `prepare_new_campaign.py` предназначен для экспериментов, связанных с созданием новой рекламной кампании на платформе AliExpress. Он использует функциональность класса `AliCampaignEditor` для обработки и настройки кампании.

## Подробней

Этот модуль является частью подсистемы управления рекламными кампаниями AliExpress в проекте `hypotez`. Он автоматизирует процесс подготовки и запуска новой рекламной кампании, используя инструменты для работы с файлами, директориями и логирования.

## Классы

### `AliCampaignEditor`

**Описание**: Класс предназначен для редактирования и управления рекламными кампаниями на AliExpress.

**Принцип работы**:
Класс предоставляет методы для создания, изменения и запуска рекламных кампаний, взаимодействуя с AliExpress API. Он использует различные утилиты для работы с данными и настройки параметров кампании.

**Методы**:

- `process_new_campaign(campaign_name)`: Обрабатывает создание новой рекламной кампании.

## Функции

В данном коде функции отсутствуют. Вместо них сразу создается экземпляр класса `AliCampaignEditor` и вызывается метод `process_new_campaign`.

## Переменные

- `campaign_name: str = 'rc'`: Имя рекламной кампании, используемое по умолчанию ('rc').
- `aliexpress_editor: AliCampaignEditor`: Экземпляр класса `AliCampaignEditor`, используемый для управления кампанией.

## Примеры

```python
from src.suppliers.aliexpress.campaign import AliCampaignEditor

campaign_name = 'new_campaign'
aliexpress_editor = AliCampaignEditor(campaign_name)
aliexpress_editor.process_new_campaign(campaign_name)
```
В этом примере создается экземпляр класса `AliCampaignEditor` с именем кампании `new_campaign`, после чего вызывается метод `process_new_campaign` для запуска процесса создания новой кампании.