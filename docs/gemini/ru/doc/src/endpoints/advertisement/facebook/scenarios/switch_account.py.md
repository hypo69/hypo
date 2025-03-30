# Модуль `switch_account`

## Обзор

Модуль `switch_account` предназначен для автоматического переключения между аккаунтами в Facebook с использованием Selenium WebDriver. Он определяет функцию `switch_account`, которая проверяет наличие кнопки "Переключить" и нажимает её для смены аккаунта.

## Подробней

Этот модуль является частью системы автоматизации задач в Facebook. Он использует JSON-файл с локаторами элементов интерфейса (`post_message.json`) для поиска кнопки переключения аккаунта. Функция `switch_account` принимает объект `Driver` (обёртку над Selenium WebDriver) и выполняет нажатие на кнопку, если она обнаружена.

## Функции

### `switch_account`

```python
def switch_account(driver: Driver):
    """ Если есть кнопка `Переключить` - нажимаю её  """
```

**Описание**:
Функция `switch_account` предназначена для переключения между аккаунтами в Facebook путем нажатия на кнопку "Переключить", если она доступна.

**Параметры**:
- `driver` (Driver): Экземпляр класса `Driver`, представляющий собой обёртку над Selenium WebDriver.

**Возвращает**:
- `None`: Функция ничего не возвращает явно.

**Вызывает исключения**:
- Отсутствуют явные исключения, но могут возникнуть исключения, связанные с работой Selenium WebDriver (например, если элемент не найден).

**Примеры**:

```python
from src.webdriver.driver import Driver
from selenium import webdriver
from src import gs
from pathlib import Path
from src.utils.jjson import j_loads_ns

# Создание экземпляра драйвера (пример)
options = webdriver.ChromeOptions()
service = webdriver.ChromeService(executable_path=gs.path.chromedriver)
driver = Driver(webdriver.Chrome(options=options, service=service))
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)
# Вызов функции switch_account
switch_account(driver)

# Закрытие драйвера (пример)
driver.quit()