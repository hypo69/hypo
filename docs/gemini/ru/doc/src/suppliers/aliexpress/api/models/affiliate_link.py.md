# Модуль affiliate_link

## Обзор

Модуль `affiliate_link` содержит класс `AffiliateLink`, предназначенный для представления партнерской ссылки AliExpress. Он включает поля для хранения самой ссылки и источника ее получения.

## Подробней

Этот модуль предоставляет простую структуру данных для хранения информации о партнерских ссылках, полученных от AliExpress. Класс `AffiliateLink` используется для удобной передачи и обработки этих данных внутри системы. Он позволяет хранить как саму партнерскую ссылку (`promotion_link`), так и информацию об источнике, из которого она была получена (`source_value`).

## Классы

### `AffiliateLink`

**Описание**: Класс для представления партнерской ссылки AliExpress.

**Методы**:
- Отсутствуют

**Параметры**:
- `promotion_link` (str): Партнерская ссылка.
- `source_value` (str): Источник партнерской ссылки.

**Примеры**
```python
# Пример определения класса и работы с классом
affiliate_link = AffiliateLink()
affiliate_link.promotion_link = "https://example.com/aliexpress_affiliate_link"
affiliate_link.source_value = "admitad"

print(affiliate_link.promotion_link)
print(affiliate_link.source_value)
```