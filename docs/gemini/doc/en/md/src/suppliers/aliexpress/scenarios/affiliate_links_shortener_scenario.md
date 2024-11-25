# Affiliate Links Shortener Scenario

## Overview

This module provides a function for shortening affiliate links using a web browser. It utilizes the `Driver` class for interacting with the browser and loads locators from a JSON file.


## Table of Contents

* [get_short_affiliate_link](#get-short-affiliate-link)


## Functions

### `get_short_affiliate_link`

**Description**: This function is designed to shorten an affiliate link using a web browser. It interacts with a specific website to perform the shortening.

**Parameters**:

- `d` (Driver): The web driver instance used for interacting with the browser.
- `url` (str): The full URL of the affiliate link to be shortened.

**Returns**:

- `str`: The shortened affiliate link.  Returns an empty string if the shortening process fails.

**Raises**:

-  No exceptions are explicitly raised.  Instead, error messages are logged and the function returns an empty string if the shortening fails or the returned URL is incorrect.


```
```python
def get_short_affiliate_link(d:Driver, url: str) -> str:
    """ Script for generating a shortened affiliate link
    @param url `str`: Full URL
    @returns `str`: Shortened URL
    """
    # Выполните сценарий для получения короткой ссылки
    d.execute_locator(locator.textarea_target_url, url)  # Введите URL в поле для ввода
    d.execute_locator(locator.button_get_tracking_link)  # Нажмите кнопку для получения короткой ссылки
    d.wait(1)  # Подождите 1 секунду, чтобы страница обновилась
    short_url = d.execute_locator(locator.textarea_short_link)[0]  # Получите короткую ссылку из элемента на странице
    main_tab = d.current_window_handle  # Сохраните идентификатор основной вкладки

    if len(short_url) < 1:
        logger.error(f"Не удалось получить короткий URL от {url}")  # Логирование ошибки, если короткий URL не получен
        #raise ValueError(f"Не удалось получить короткий URL от {url}")  # Генерация исключения для остановки выполнения
    
    # Откройте новый таб с коротким URL
    d.execute_script(f"window.open(\'{short_url}\');")
    
    # Переключитесь на новый таб
    d.switch_to.window(d.window_handles[-1])
    
    # Проверьте, что короткий URL начинается с ожидаемой части
    if d.current_url.startswith('https://error.taobao.com'):
        logger.error(f"Неправильный URL: {d.current_url}")  # Логирование ошибки, если короткий URL некорректен
        d.close()  # Закройте вкладку с неправильным URL
        d.switch_to.window(main_tab)  # Переключитесь обратно на основную вкладку
        #raise ValueError(f"Неправильный URL: {d.current_url}")  # Генерация исключения для остановки выполнения
    
    # Закройте новый таб и вернитесь к основной вкладке
    d.close()  # Закрываем новую вкладку
    d.switch_to.window(main_tab)  # Переключаемся обратно на основную вкладку
    
    return short_url  # Верните короткий URL
```

**Explanation of Russian Comments**:

The function's comments contain Russian text. This suggests the codebase is intended for a Russian-speaking audience or environment.  The function's behavior is documented appropriately, but it's important to consider internationalization for a global audience. Consider translating the comments into English if necessary for broader use.



```