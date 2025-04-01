# Модуль `prepare_new_campaign.py`

## Обзор

Модуль `prepare_new_campaign.py` предназначен для экспериментов с процессом создания новой рекламной кампании на платформе AliExpress. Он использует функциональность класса `AliCampaignEditor` для управления и обработки кампаний.

## Подробней

Этот модуль является частью пакета `src.suppliers.aliexpress.campaign._experiments` и служит для автоматизации и экспериментирования с настройками рекламных кампаний на AliExpress. Он включает в себя импорт необходимых модулей, инициализацию редактора кампаний и запуск процесса создания новой кампании.

## Функции

В данном модуле нет явно определенных функций, однако используется класс `AliCampaignEditor` и его методы для выполнения основных операций.

## Переменные

- `campaign_name (str)`: Имя рекламной кампании, используемое в модуле.
- `aliexpress_editor (AliCampaignEditor)`: Экземпляр класса `AliCampaignEditor`, предназначенный для редактирования и обработки рекламных кампаний AliExpress.

## Классы

### `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` предназначен для редактирования и управления рекламными кампаниями AliExpress.

**Принцип работы**:
Класс инициализируется с именем кампании и предоставляет методы для обработки и настройки кампании. В данном модуле используется метод `process_new_campaign` для запуска процесса создания новой кампании.

**Методы**:
- `__init__(self, campaign_name)`:
    ```python
    def __init__(self, campaign_name):
        """
        Инициализирует экземпляр класса `AliCampaignEditor`.

        Args:
            campaign_name (str): Имя кампании.
        """
        ...
    ```

- `process_new_campaign(self, campaign_name)`:
    ```python
    def process_new_campaign(self, campaign_name):
        """
        Запускает процесс создания новой рекламной кампании.

        Args:
            campaign_name (str): Имя кампании.
        """
        ...
    ```

## Использование

```python
import header

from pathlib import Path

from src import gs

from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.utils import get_filenames, get_directory_names
from src.utils.printer import pprint
from src.logger.logger import logger

campaign_name = 'rc'
aliexpress_editor =  AliCampaignEditor(campaign_name)
aliexpress_editor.process_new_campaign(campaign_name)
```

**Пояснения**:
1. Импортируются необходимые модули и классы.
2. Создается экземпляр класса `AliCampaignEditor` с именем кампании `'rc'`.
3. Вызывается метод `process_new_campaign` для запуска процесса создания новой кампании.

## Как работает модуль:

1. **Импорт необходимых модулей**:
   - Импортируются модули `header`, `Path`, `gs`, `AliCampaignEditor`, `get_filenames`, `get_directory_names`, `pprint`, `logger`.
2. **Инициализация переменных**:
   - `campaign_name` присваивается значение `'rc'`.
   - Создается экземпляр класса `AliCampaignEditor` с именем кампании `campaign_name`.
3. **Запуск процесса создания новой кампании**:
   - Вызывается метод `process_new_campaign` у экземпляра `aliexpress_editor` с именем кампании `campaign_name`.

## Примеры

### Пример 1: Запуск процесса создания новой кампании

```python
campaign_name = 'new_campaign'
aliexpress_editor = AliCampaignEditor(campaign_name)
aliexpress_editor.process_new_campaign(campaign_name)
```

### Пример 2: Использование другого имени для кампании

```python
campaign_name = 'summer_sale'
aliexpress_editor = AliCampaignEditor(campaign_name)
aliexpress_editor.process_new_campaign(campaign_name)
```