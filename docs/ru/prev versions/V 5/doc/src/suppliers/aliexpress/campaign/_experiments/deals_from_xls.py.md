# Модуль deals_from_xls.py

## Обзор

Модуль предназначен для парсинга XLS-таблиц, сгенерированных в личном кабинете portals.aliexpress.com. Он использует класс `DealsFromXLS` из модуля `src.suppliers.aliexpress` для обработки данных и извлечения информации о сделках.

## Подробней

Этот модуль предоставляет способ автоматизированного извлечения данных о сделках из XLS-файлов, что может быть полезно для анализа и обработки данных о кампаниях на AliExpress.

## Функции

В данном коде напрямую не определены функции. Вместо этого, используется класс `DealsFromXLS` для парсинга данных.

### `DealsFromXLS`

```python
class DealsFromXLS:
    ...
```

**Описание**: Класс предназначен для парсинга данных о сделках из XLS-файлов, полученных из личного кабинета AliExpress.

**Как работает класс**:
1.  Инициализируется с параметрами `language` и `currency`.
2.  Использует метод `get_next_deal` для последовательного извлечения информации о сделках.

**Методы**:

*   `get_next_deal`: Метод для получения следующей сделки из XLS-файла.

**Параметры**:

*   `language` (str): Язык, на котором представлена информация о сделках.
*   `currency` (str): Валюта, в которой указаны цены сделок.

**Примеры**:

```python
from src.suppliers.aliexpress import DealsFromXLS
from src.utils.printer import pprint

deals_parser = DealsFromXLS(language='EN', currency='USD')

for deal in deals_parser.get_next_deal():
    pprint(deal)
```

### Пример использования:

```python
deals_parser = DealsFromXLS(language='EN', currency= 'USD')

for deal in deals_parser.get_next_deal():
    pprint(deal)
    ...
```

**Описание**:
1.  Создается экземпляр класса `DealsFromXLS` с указанием языка `EN` и валюты `USD`.
2.  В цикле `for` вызывается метод `get_next_deal` для получения информации о каждой сделке.
3.  Функция `pprint` используется для вывода информации о сделке.

```