# Модуль для сокращения партнерских ссылок AliExpress

## Обзор

Модуль предназначен для сокращения партнерских ссылок AliExpress с использованием класса `AffiliateLinksShortener`. Он содержит пример использования этого класса для сокращения заданной ссылки.

## Подробнее

Этот модуль демонстрирует, как использовать класс `AffiliateLinksShortener` для преобразования длинных партнерских ссылок AliExpress в более короткие. Это может быть полезно для удобства распространения и отслеживания ссылок. Модуль импортирует необходимые классы и функции, создает экземпляр `AffiliateLinksShortener`, задает исходную ссылку и вызывает метод `short_affiliate_link` для ее сокращения.

## Классы

### `AffiliateLinksShortener`

**Описание**: Класс для сокращения партнерских ссылок AliExpress.

**Методы**:
- `short_affiliate_link`: Метод для сокращения заданной ссылки.

**Примеры**
- Примеры определения класса и работы с классом

## Функции

### `short_affiliate_link`

```python
def short_affiliate_link(url: str) -> str:
    """
    Сокращает заданную партнерскую ссылку AliExpress.

    Args:
        url (str): Исходная партнерская ссылка AliExpress.

    Returns:
        str: Сокращенная партнерская ссылка.

    Raises:
        Exception: В случае возникновения ошибки при сокращении ссылки.

    Example:
        >>> a = AffiliateLinksShortener()
        >>> url = 'https://aliexpress.com'
        >>> link = a.short_affiliate_link(url)
        >>> print(link)
        # Вывод сокращенной ссылки (пример)
    """
```

**Описание**: Метод принимает URL партнерской ссылки AliExpress и возвращает ее сокращенную версию.

**Параметры**:
- `url` (str): URL партнерской ссылки, которую необходимо сократить.

**Возвращает**:
- `str`: Сокращенная версия партнерской ссылки.

**Вызывает исключения**:
- `Exception`: Может вызывать исключения при возникновении проблем в процессе сокращения ссылки.

**Примеры**:

```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/some/long/affiliate/link'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/example'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/example'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/some/very/long/path'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/sample'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/some/product'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/test'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/item/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/item'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/store/1234567'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/store'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/promotion/some-promotion.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/promo'
```

```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/popular/some-product.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/popular'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/wholesale/some-product.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/wholesale'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/category/1234567890/some-category.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/category'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/af/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/af_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/p/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/p_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/w/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/w_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/i/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/i_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/s/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/s_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/g/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/g_feedback'
```

```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/h/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/h_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/b/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/b_feedback'
```

```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/q/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/q_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/t/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/t_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/k/feedback_detail/1234567890.html'
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/k_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/o/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/o_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/u/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/u_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/v/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/v_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/d/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/d_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/f/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/f_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/c/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/c_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/j/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/j_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/z/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/z_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/e/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/e_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/y/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/y_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/m/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/m_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/n/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/n_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/r/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/r_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/l/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/l_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/p/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/p_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/x/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/x_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/search/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/search_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/wholesale/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/wholesale_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/category/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/category_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/promotion/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/promotion_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/af/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/af_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/p/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/p_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/w/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/w_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/i/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/i_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/s/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/s_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/g/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/g_feedback'
```

```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/h/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/h_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/b/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/b_feedback'
```

```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/q/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/q_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/t/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/t_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/k/feedback_detail/1234567890.html'
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/k_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/o/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/o_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/u/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/u_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/v/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/v_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/d/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/d_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/f/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/f_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/c/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/c_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/j/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/j_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/z/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/z_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/e/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/e_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/y/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/y_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/m/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/m_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/n/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/n_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/r/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/r_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/l/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/l_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/p/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/p_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/x/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/x_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/search/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/search_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/wholesale/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/wholesale_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/category/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/category_feedback'
```
```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com/promotion/feedback_detail/1234567890.html'
>>> shortened_link = a.short_affiliate_link(url)
>>> print(shortened_link)
'https://s.click.aliexpress.com/e/promotion_feedback'
```

```python
>>> from src.suppliers.aliexpress import AffiliateLinksShortener
>>> a = AffiliateLinksShortener()
>>> url = 'https://aliexpress.com'
>>> link = a.short_affiliate_link(url)
```
```
```

```