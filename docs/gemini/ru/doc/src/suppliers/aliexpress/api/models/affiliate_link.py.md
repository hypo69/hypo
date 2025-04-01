# Модуль affiliate_link

## Обзор

Модуль `affiliate_link` содержит класс `AffiliateLink`, который предназначен для хранения информации о партнерской ссылке.
Класс включает в себя атрибуты для хранения самой партнерской ссылки и источника, из которого она была получена.

## Подробней

Данный модуль используется для представления данных о партнерских ссылках, полученных от AliExpress.
Он обеспечивает удобный способ хранения и доступа к этим данным.

## Классы

### `AffiliateLink`

**Описание**: Класс `AffiliateLink` используется для представления партнерской ссылки и источника её получения.

**Принцип работы**:
Класс `AffiliateLink` представляет собой структуру данных, содержащую два атрибута: `promotion_link` и `source_value`.
`promotion_link` хранит саму партнерскую ссылку, а `source_value` - источник, из которого была получена данная ссылка.

**Атрибуты**:
- `promotion_link` (str): Партнерская ссылка.
- `source_value` (str): Источник партнерской ссылки.

**Примеры**:

```python
affiliate_link = AffiliateLink()
affiliate_link.promotion_link = "https://example.com/aliexpress_promotion"
affiliate_link.source_value = "aliexpress"

print(affiliate_link.promotion_link)  # Вывод: https://example.com/aliexpress_promotion
print(affiliate_link.source_value)  # Вывод: aliexpress
```