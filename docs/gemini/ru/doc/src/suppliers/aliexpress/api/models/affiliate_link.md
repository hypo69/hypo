# Модуль `hypotez/src/suppliers/aliexpress/api/models/affiliate_link.py`

## Обзор

Модуль `affiliate_link.py` определяет класс `AffiliateLink` для работы с аффилиатными ссылками AliExpress.  Класс содержит атрибуты для хранения ссылки на промоакцию и исходного значения.

## Оглавление

- [## Классы](#классы)
    - [`AffiliateLink`](#affiliateLink)


## Классы

### `AffiliateLink`

**Описание**: Класс `AffiliateLink` представляет аффилиатную ссылку.

**Атрибуты**:

- `promotion_link` (str): Ссылка на промоакцию.
- `source_value` (str): Исходное значение (вероятно, источник ссылки).


```python
class AffiliateLink:
    promotion_link: str
    source_value: str
```