# Модуль для сокращения партнерских ссылок AliExpress
## Обзор

Модуль `affiliate_links_shortener.py` предназначен для сокращения длинных партнерских ссылок AliExpress. Он использует класс `AffiliateLinksShortener` для генерации коротких ссылок, которые удобнее для распространения и отслеживания.

## Подробней

Этот модуль является частью экспериментов по работе с партнерскими ссылками AliExpress в проекте `hypotez`. Он позволяет генерировать короткие партнерские ссылки на товары AliExpress.

## Классы

### `AffiliateLinksShortener`

**Описание**: Класс предназначен для сокращения партнерских ссылок AliExpress.

**Принцип работы**:
Класс `AffiliateLinksShortener` содержит методы для генерации коротких партнерских ссылок на товары AliExpress. Он использует API AliExpress для сокращения ссылок и отслеживания переходов.

## Функции

В предоставленном коде нет описания функций, поэтому сгенерировать описание невозможно.

## Пример

```python
import header
from src.suppliers.aliexpress import AffiliateLinksShortener

a = AffiliateLinksShortener()
url = 'https://aliexpress.com'
link = a.short_affiliate_link(url)
...
```