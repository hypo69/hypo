# Модуль: src.suppliers.aliexpress.api.models.affiliate_link

## Обзор

Модуль `affiliate_link` определяет структуру данных для хранения информации о партнерской ссылке, связанной с AliExpress. Он содержит класс `AffiliateLink`, который используется для представления партнерской ссылки и ее источника.

## Подробнее

Этот модуль предоставляет способ организации и хранения данных, связанных с партнерскими ссылками AliExpress. Класс `AffiliateLink` служит контейнером для атрибутов, описывающих партнерскую ссылку, таких как сама ссылка и источник, из которого она была получена.

## Классы

### `AffiliateLink`

**Описание**: Класс `AffiliateLink` представляет структуру данных для партнерской ссылки AliExpress.

**Методы**: 
- Отсутствуют

**Параметры**: 
- `promotion_link` (str): Сама партнерская ссылка.
- `source_value` (str): Источник, из которого была получена партнерская ссылка.

**Примеры**
```python
affiliate_link = AffiliateLink()
affiliate_link.promotion_link = 'https://example.com/aliexpress_affiliate_link'
affiliate_link.source_value = 'admitad'
print(affiliate_link.promotion_link)
print(affiliate_link.source_value)
```
```
https://example.com/aliexpress_affiliate_link
admitad
```
## Функции

Отсутствуют