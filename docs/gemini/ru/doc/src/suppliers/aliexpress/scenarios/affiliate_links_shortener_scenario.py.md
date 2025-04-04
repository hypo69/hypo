# Модуль: Сокращение партнерских ссылок AliExpress через веб-браузер

## Обзор

Модуль предназначен для автоматического сокращения партнерских ссылок AliExpress с использованием веб-браузера. Он предоставляет функцию `get_short_affiliate_link`, которая принимает полную URL-ссылку и возвращает ее сокращенную версию, полученную через специальный интерфейс на сайте AliExpress.

## Подробней

Этот модуль автоматизирует процесс сокращения партнерских ссылок AliExpress. Он использует веб-драйвер для взаимодействия с веб-сайтом AliExpress, ввода полной ссылки и получения сокращенной версии. Модуль обрабатывает возможные ошибки, такие как некорректные сокращенные ссылки, и возвращает либо сокращенную ссылку, либо сообщает об ошибке.

## Функции

### `get_short_affiliate_link`

```python
def get_short_affiliate_link(d: Driver, url: str) -> str:
    """ Script for generating a shortened affiliate link
    @param url `str`: Full URL
    @returns `str`: Shortened URL
    """
    ...
```

**Назначение**: Получение сокращенной партнерской ссылки на основе предоставленной полной ссылки.

**Параметры**:

- `d` (Driver): Инстанс веб-драйвера, используемый для взаимодействия с веб-сайтом AliExpress.
- `url` (str): Полная URL-ссылка, которую необходимо сократить.

**Возвращает**:

- `str`: Сокращенная URL-ссылка.

**Как работает функция**:

1.  **Ввод URL**: Вводит предоставленную полную URL-ссылку в текстовое поле на странице AliExpress.
2.  **Получение короткой ссылки**: Нажимает кнопку для генерации сокращенной ссылки.
3.  **Ожидание**: Ожидает обновления страницы (1 секунду).
4.  **Извлечение короткой ссылки**: Извлекает сокращенную ссылку из соответствующего элемента на странице.
5.  **Проверка на ошибки**: Проверяет, что сокращенная ссылка не ведет на страницу ошибки `error.taobao.com`. Если ссылка ведет на страницу ошибки, то об этом сообщается в лог, и функция возвращает `None`.
6.  **Возврат результата**: Возвращает сокращенную URL-ссылку.

```
      Ввод URL в текстовое поле             Нажатие кнопки для генерации короткой ссылки
      A                                  B
      |                                  |
      ------------------------------------>| Ожидание обновления страницы
                                           C
                                           |
                                           |Извлечение короткой ссылки
                                           D
                                           |
                                           |Проверка на ошибки
                                           E
                                           |
                                           F
```

**Примеры**:

```python
from src.webdriver.driver import Driver, Chrome
from src.suppliers.aliexpress.scenarios.affiliate_links_shortener_scenario import get_short_affiliate_link

# Пример использования с Chrome
driver = Driver(Chrome)
full_url = "https://aliexpress.ru/item/10050000000000.html"  # Замените на реальную ссылку
short_url = get_short_affiliate_link(driver, full_url)
if short_url:
    print(f"Сокращенная ссылка: {short_url}")
else:
    print("Не удалось получить сокращенную ссылку.")
driver.quit()