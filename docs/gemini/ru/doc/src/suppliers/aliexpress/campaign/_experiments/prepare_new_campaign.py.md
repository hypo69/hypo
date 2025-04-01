# Модуль подготовки новой рекламной кампании на AliExpress

## Обзор

Модуль `prepare_new_campaign.py` предназначен для автоматизации процесса подготовки и запуска новой рекламной кампании на платформе AliExpress. Он использует класс `AliCampaignEditor` для управления и настройки параметров кампании.

## Подробней

Модуль выполняет эксперименты над сценарием создания новой рекламной кампании. Он импортирует необходимые библиотеки, такие как `header`, `Path`, `gs`, `AliCampaignEditor`, `get_filenames`, `get_directory_names`, `pprint` и `logger`. Основная функциональность заключается в создании экземпляра класса `AliCampaignEditor` и вызове метода `process_new_campaign` для запуска процесса подготовки кампании.

## Функции

В данном коде присутствуют импорты, переменные и вызовы функций.

### `campaign_name`

```python
campaign_name = 'rc'
```

**Назначение**: Определяет название рекламной кампании.

**Как работает функция**:

1.  Присваивает строковое значение `'rc'` переменной `campaign_name`.

**Примеры**:

```python
campaign_name = 'rc'
print(campaign_name)  # Вывод: rc
```

### `aliexpress_editor`

```python
aliexpress_editor =  AliCampaignEditor(campaign_name)
```

**Назначение**: Создает экземпляр класса `AliCampaignEditor` для работы с рекламной кампанией AliExpress.

**Параметры**:

*   `campaign_name` (str): Название рекламной кампании.

**Как работает функция**:

1.  Создает экземпляр класса `AliCampaignEditor`, передавая название кампании в качестве аргумента.
2.  Этот экземпляр будет использоваться для дальнейшей настройки и управления кампанией.

```
Начало
    ↓
Создание экземпляра AliCampaignEditor с campaign_name
    ↓
Конец
```

**Примеры**:

```python
from src.suppliers.aliexpress.campaign import AliCampaignEditor

campaign_name = 'rc'
aliexpress_editor = AliCampaignEditor(campaign_name)
print(aliexpress_editor)  #  <src.suppliers.aliexpress.campaign.editor.AliCampaignEditor object at 0x...>
```

### `aliexpress_editor.process_new_campaign(campaign_name)`

```python
aliexpress_editor.process_new_campaign(campaign_name)
```

**Назначение**: Запускает процесс подготовки новой рекламной кампании.

**Параметры**:

*   `campaign_name` (str): Название рекламной кампании.

**Как работает функция**:

1.  Вызывает метод `process_new_campaign` экземпляра `aliexpress_editor`, передавая название кампании в качестве аргумента.
2.  Этот метод выполняет все необходимые шаги для подготовки и запуска кампании, такие как настройка параметров, выбор товаров и т.д.

```
Начало
    ↓
Вызов process_new_campaign с campaign_name
    ↓
Конец
```

**Примеры**:

```python
from src.suppliers.aliexpress.campaign import AliCampaignEditor

campaign_name = 'rc'
aliexpress_editor = AliCampaignEditor(campaign_name)
aliexpress_editor.process_new_campaign(campaign_name) # Запускает процесс подготовки кампании