# Модуль deals_from_xls.py

## Обзор

Модуль `deals_from_xls.py` предназначен для парсинга таблиц `xls`, сгенерированных в личном кабинете `portals.aliexpress.com`. Он использует класс `DealsFromXLS` для извлечения информации о сделках из `xls`-файла и последующего представления этих данных.

## Подробней

Этот модуль является частью экспериментов, связанных с кампаниями на AliExpress. Он автоматизирует процесс извлечения данных о сделках из `xls`-файлов, что позволяет упростить анализ и обработку этой информации. Модуль инициализирует парсер `DealsFromXLS` с указанием языка (`EN`) и валюты (`USD`), а затем итерируется по каждой сделке, извлеченной из файла, и выводит ее содержимое с использованием функции `pprint`.

## Функции

### `deals_parser.get_next_deal()`

```python
def get_next_deal() -> Generator[dict, None, None]:
    """
    Args:
        None

    Returns:
        Generator[dict, None, None]: Возвращает генератор словарей, содержащих информацию о сделке.

    Raises:
        Exception: Описание ситуации, в которой возникает исключение.

    Example:
        >>> deals_parser = DealsFromXLS(language='EN', currency='USD')
        >>> deal = next(deals_parser.get_next_deal(), None)
        >>> if deal:
        ...     print(deal)
        ...
    """
```

**Описание**: Извлекает информацию о следующей сделке из `xls`-файла.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `Generator[dict, None, None]`: Генератор словарей, содержащих информацию о сделке.

**Примеры**:

```python
deals_parser = DealsFromXLS(language='EN', currency='USD')
deal = next(deals_parser.get_next_deal(), None)
if deal:
    print(deal)