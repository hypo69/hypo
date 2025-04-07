# Модуль для работы с партнерскими ссылками AliExpress
## Обзор

Модуль `affiliate_link.py` содержит класс `AffiliateLink`, предназначенный для представления партнерской ссылки AliExpress. Класс хранит информацию о рекламной ссылке и источнике, из которого она была получена.

## Подробней

Этот модуль предоставляет структуру данных для хранения информации о партнерских ссылках, полученных от AliExpress. Он используется для унификации представления данных о ссылках и облегчения их дальнейшей обработки и анализа.

## Классы

### `AffiliateLink`

**Описание**: Класс `AffiliateLink` представляет собой модель данных для хранения информации о партнерской ссылке AliExpress.

**Принцип работы**:
Класс `AffiliateLink` содержит два атрибута: `promotion_link` и `source_value`. Атрибут `promotion_link` хранит саму партнерскую ссылку, а `source_value` указывает на источник, из которого эта ссылка была получена.

**Атрибуты**:

- `promotion_link` (str): Партнерская ссылка.
- `source_value` (str): Источник ссылки.

**Методы**:
*   У класса `AffiliateLink` нет собственных методов, он служит контейнером для хранения данных.

**Примеры**:

```python
# Пример создания экземпляра класса AffiliateLink
affiliate_link = AffiliateLink()
affiliate_link.promotion_link = "https://example.com/aliexpress_affiliate_link"
affiliate_link.source_value = "admitad"

print(affiliate_link.promotion_link) # Вывод: https://example.com/aliexpress_affiliate_link
print(affiliate_link.source_value) # Вывод: admitad
```
```