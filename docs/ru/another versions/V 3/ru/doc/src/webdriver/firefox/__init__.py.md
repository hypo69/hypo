# Модуль `src.webdriver.firefox`

## Обзор

Модуль `src.webdriver.firefox` предоставляет функциональность для управления браузером Firefox в контексте автоматизированного тестирования или сбора данных. В настоящее время, модуль импортирует класс `Firefox` из подмодуля `firefox`, что позволяет использовать его для создания и настройки экземпляров браузера Firefox.

## Подробней

Этот модуль служит как точка входа для работы с Firefox. Он упрощает импорт и использование класса `Firefox`, предоставляя удобный интерфейс для взаимодействия с браузером. В проекте `hypotez`, этот модуль может использоваться для автоматизации действий в браузере Firefox, таких как навигация по веб-страницам, заполнение форм, клики по элементам и сбор данных.

## Классы

### `Firefox`

**Описание**: Описание класса для управления браузером Firefox.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Firefox`.
- `start`: Запускает браузер Firefox.
- `stop`: Останавливает браузер Firefox.
- `get`: Открывает указанный URL в браузере.
- `find_element`: Находит элемент на странице по заданным критериям.
- `click`: Кликает на найденный элемент.
- `send_keys`: Вводит текст в текстовое поле.
- `execute_script`: Выполняет JavaScript-код в контексте браузера.

**Параметры**:
- `driver_path` (str, optional): Путь к исполняемому файлу драйвера Firefox (geckodriver). По умолчанию `None`.
- `profile_path` (str, optional): Путь к профилю Firefox. По умолчанию `None`.
- `options` (Options, optional): Объект `Options` для настройки параметров запуска Firefox. По умолчанию `None`.
- `capabilities` (dict, optional):  Словарь с требуемыми capabilities для драйвера Firefox. По умолчанию `None`.
- `proxy` (str, optional): Строка с адресом прокси-сервера. По умолчанию `None`.
- `headless` (bool, optional):  Запускать Firefox в headless-режиме. По умолчанию `False`.

**Примеры**

```python
from src.webdriver.firefox import Firefox
from selenium.webdriver.firefox.options import Options

# Пример создания экземпляра Firefox с настройками
options = Options()
options.headless = True  # Запуск в headless-режиме

firefox_browser = Firefox(options=options)
firefox_browser.start()
firefox_browser.get("https://www.example.com")
print(firefox_browser.driver.title)
firefox_browser.stop()
```

## Функции

В данном модуле явно не определены функции, но он импортирует класс `Firefox`, который можно использовать для создания экземпляров и управления браузером Firefox.
```
from .firefox import Firefox
```
```markdown
## Оглавление

1. [Обзор](#обзор)
2. [Подробней](#подробней)
3. [Классы](#классы)
    - [Firefox](#firefox)
4. [Функции](#функции)