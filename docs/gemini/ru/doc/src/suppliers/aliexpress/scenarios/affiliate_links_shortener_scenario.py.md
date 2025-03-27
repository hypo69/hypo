# Модуль affiliate_links_shortener_scenario

## Обзор

Модуль `affiliate_links_shortener_scenario.py` предназначен для сокращения партнерских ссылок AliExpress с использованием веб-драйвера. Он содержит функцию `get_short_affiliate_link`, которая автоматизирует процесс получения короткой партнерской ссылки из полной ссылки, введенной пользователем.

## Подорбней

Этот модуль предоставляет функциональность для автоматического сокращения ссылок AliExpress через веб-интерфейс. Он использует драйвер веб-браузера для взаимодействия с сайтом, ввода полной ссылки и получения сокращенной версии. Полученная короткая ссылка проверяется на корректность. В случае ошибки, информация об этом логируется.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `get_short_affiliate_link`

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
    if d.current_url.startswith(\'https://error.taobao.com\'):
        logger.error(f"Неправильный URL: {d.current_url}")  # Логирование ошибки, если короткий URL некорректен
        d.close()  # Закройте вкладку с неправильным URL
        d.switch_to.window(main_tab)  # Переключитесь обратно на основную вкладку
        #raise ValueError(f"Неправильный URL: {d.current_url}")  # Генерация исключения для остановки выполнения
    
    # Закройте новый таб и вернитесь к основной вкладке
    d.close()  # Закрываем новую вкладку
    d.switch_to.window(main_tab)  # Переключаемся обратно на основную вкладку
    
    return short_url  # Верните короткий URL
```

**Описание**: Скрипт для генерации сокращенной партнерской ссылки.

**Параметры**:
- `d` (`Driver`): Экземпляр веб-драйвера.
- `url` (`str`): Полный URL для сокращения.

**Возвращает**:
- `str`: Сокращенный URL.

**Вызывает исключения**:
- Отсутствуют явные исключения, но в коде закомментированы строки, которые могут вызывать `ValueError` в случае неудачи получения или некорректности короткой ссылки. Вместо этого используется логирование ошибок.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.suppliers.aliexpress.scenarios.affiliate_links_shortener_scenario import get_short_affiliate_link

# Пример использования функции get_short_affiliate_link
driver = Driver()  # Инициализация драйвера (требуется предварительная настройка)
full_url = "https://aliexpress.ru/item/1234567890.html"  # Замените на реальный URL
short_url = get_short_affiliate_link(driver, full_url)
if short_url:
    print(f"Сокращенная ссылка: {short_url}")
else:
    print("Не удалось получить сокращенную ссылку.")
driver.quit()  # Закрытие драйвера