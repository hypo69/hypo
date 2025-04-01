# Модуль для сокращения партнерских ссылок AliExpress
## Обзор

Модуль содержит эксперимент по сокращению партнерских ссылок для AliExpress. Включает импорт необходимых модулей и вызов функции сокращения партнерской ссылки.

## Подробней

Данный код является частью экспериментов, связанных с AliExpress. Он предназначен для демонстрации и тестирования функциональности сокращения партнерских ссылок с использованием класса `AffiliateLinksShortener`. Файл импортирует необходимые модули и выполняет вызов метода `short_affiliate_link` для сокращения предоставленной ссылки.

## Функции

### `short_affiliate_link`

```python
link = a.short_affiliate_link(url)
```

**Назначение**: Сокращение партнерской ссылки AliExpress.

**Как работает функция**:

1.  Создается экземпляр класса `AffiliateLinksShortener`.
2.  Определяется URL для сокращения.
3.  Вызывается метод `short_affiliate_link` с переданным URL.
4.  Результат сокращения ссылки сохраняется в переменной `link`.

```
Создание экземпляра класса AffiliateLinksShortener
↓
Определение URL для сокращения
↓
Вызов метода short_affiliate_link(url)
↓
Сохранение результата в переменной link
```

**Примеры**:

```python
from src.suppliers.aliexpress import AffiliateLinksShortener

a = AffiliateLinksShortener()
url = 'https://aliexpress.com'
link = a.short_affiliate_link(url)