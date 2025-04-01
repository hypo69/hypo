# Модуль `affiliate_links_shortener_scenario.py`

## Обзор

Модуль `affiliate_links_shortener_scenario.py` предназначен для сокращения партнерских ссылок AliExpress с использованием веб-браузера. Он предоставляет функцию для автоматического получения короткой партнерской ссылки на основе предоставленного URL.

## Подробней

Этот модуль автоматизирует процесс сокращения ссылок AliExpress через веб-интерфейс. Он использует Selenium WebDriver для взаимодействия с веб-страницей, ввода URL, нажатия на кнопки и извлечения короткой ссылки. Модуль также включает проверки для обработки ошибок и логирования.

## Функции

### `get_short_affiliate_link`

```python
def get_short_affiliate_link(d: Driver, url: str) -> str:
    """
    Получает сокращенную партнерскую ссылку на основе предоставленного URL.

    Args:
        d (Driver): Инстанс драйвера веб-браузера.
        url (str): Полный URL для сокращения.

    Returns:
        str: Сокращенный URL.

    Raises:
        ValueError: Если не удалось получить короткий URL или если короткий URL некорректен.

    Пример:
        >>> from src.webdriver.driver import Driver
        >>> # Предположим, что driver - это инстанс веб-драйвера
        >>> driver = Driver() 
        >>> url = "https://aliexpress.com/some_product_url"
        >>> short_url = get_short_affiliate_link(driver, url)
        >>> print(short_url)
        "https://s.click.aliexpress.com/e/_DeW4RT"
    """
```

**Как работает функция**:

1.  **Ввод URL**: Вводит предоставленный URL в текстовое поле на странице.
2.  **Нажатие кнопки**: Нажимает кнопку для генерации короткой партнерской ссылки.
3.  **Ожидание**: Ожидает обновления страницы.
4.  **Извлечение короткой ссылки**: Извлекает короткую ссылку из текстового поля.
5.  **Обработка ошибок**: Если короткая ссылка не получена, регистрирует ошибку.
6.  **Проверка URL**: Открывает короткую ссылку в новой вкладке, чтобы проверить, что она не ведет на страницу ошибок.
7.  **Закрытие вкладки**: Закрывает новую вкладку и переключается обратно на основную вкладку.
8.  **Возврат значения**: Возвращает полученную короткую ссылку.

**Внутри функции происходят следующие действия и преобразования**:

Ввод URL -> Нажатие кнопки -> Ожидание обновления страницы -> Извлечение короткой ссылки -> Проверка URL -> Закрытие вкладки -> Возврат значения

*   **Ввод URL**: `d.execute_locator(locator.textarea_target_url, url)` - Вводит URL в поле для ввода.
*   **Нажатие кнопки**: `d.execute_locator(locator.button_get_tracking_link)` - Нажимает кнопку для получения короткой ссылки.
*   **Ожидание обновления страницы**: `d.wait(1)` - Ожидает 1 секунду, чтобы страница обновилась.
*   **Извлечение короткой ссылки**: `short_url = d.execute_locator(locator.textarea_short_link)[0]` - Получает короткую ссылку из элемента на странице.
*   **Проверка URL**:
    *   `d.execute_script(f"window.open('{short_url}');")` - Открывает новую вкладку с коротким URL.
    *   `d.switch_to.window(d.window_handles[-1])` - Переключается на новый таб.
    *   `if d.current_url.startswith('https://error.taobao.com'):` - Проверяет, что короткий URL начинается с ожидаемой части.
    *   `d.close()` - Закрывает вкладку с неправильным URL.
    *   `d.switch_to.window(main_tab)` - Переключается обратно на основную вкладку.
*   **Закрытие вкладки**:
    *   `d.close()` - Закрывает новую вкладку.
    *   `d.switch_to.window(main_tab)` - Переключается обратно на основную вкладку.
*   **Возврат значения**: `return short_url` - Возвращает короткий URL.

**Примеры**:

```python
from src.webdriver.driver import Driver
from pathlib import Path
from src import gs
from src.utils.jjson import j_loads_ns
# Загрузка локаторов из JSON-файла
locator = j_loads_ns(Path(gs.path.src, 'suppliers', 'aliexpress', 'locators', 'affiliate_links_shortener.json'))
# Пример использования функции с валидным URL
driver = Driver()
valid_url = "https://aliexpress.ru/item/1005003591958714.html?sku_id=12000026599957073"
short_link = get_short_affiliate_link(driver, valid_url)
print(f"Короткая ссылка для {valid_url}: {short_link}")

# Пример использования функции с другим валидным URL
another_url = "https://aliexpress.com/item/32829230898.html"
short_link = get_short_affiliate_link(driver, another_url)
print(f"Короткая ссылка для {another_url}: {short_link}")

# Пример обработки невалидного URL (который все равно может быть обработан)
invalid_url = "https://example.com"  # Этот URL может быть обработан, но результат может быть неверным
short_link = get_short_affiliate_link(driver, invalid_url)
print(f"Короткая ссылка для {invalid_url}: {short_link}")
```