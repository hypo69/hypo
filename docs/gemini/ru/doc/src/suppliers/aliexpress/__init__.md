# Модуль `hypotez/src/suppliers/aliexpress/__init__.py`

## Обзор

Этот модуль предоставляет доступ к API AliExpress, позволяя управлять кампаниями и получать информацию о продуктах и категориях. Он содержит классы для работы с API, управления кампаниями и генерации HTML-отчетов.

## Модули

### `aliexpress`

Этот модуль содержит класс `Aliexpress`, предоставляющий основной интерфейс для работы с AliExpress API.

### `aliapi`

Этот модуль содержит класс `AliApi`, предоставляющий методы для взаимодействия с API AliExpress.

### `alirequests`

Этот модуль содержит класс `AliRequests`, предоставляющий методы для отправки HTTP-запросов к API AliExpress.

### `campaign`

Этот модуль содержит класс `AliCampaignEditor`, предоставляющий методы для управления рекламными кампаниями.

### `campaign.html_generators`

Этот модуль содержит классы для генерации HTML-отчетов:
    * `ProductHTMLGenerator`: Генерирует HTML-отчеты о продуктах.
    * `CategoryHTMLGenerator`: Генерирует HTML-отчеты о категориях.
    * `CampaignHTMLGenerator`: Генерирует HTML-отчеты о рекламных кампаниях.


## Переменные

### `MODE`

```python
MODE = 'dev'
```

**Описание**: Переменная, определяющая режим работы (например, `dev` или `prod`).


## Импорты

```python
from .aliexpress import Aliexpress
from .aliapi import AliApi
from .alirequests import AliRequests
from .campaign import AliCampaignEditor
from .campaign.html_generators import ProductHTMLGenerator, CategoryHTMLGenerator, CampaignHTMLGenerator
```

**Описание**: Импорты необходимых классов и модулей из других файлов текущего пакета.