# Модуль hypotez/src/webdriver/firefox/firefox.py

## Обзор

Этот модуль определяет подкласс `webdriver.Firefox` с именем `Firefox`. Он предоставляет расширенные возможности, такие как запуск Firefox в режиме киоска и настройку профиля Firefox для WebDriver.  Модуль использует конфигурационный файл `firefox.json` для управления настройками.

## Классы

### `Firefox`

**Описание**: Подкласс `webdriver.Firefox`, предоставляющий дополнительные функции для работы с браузером Firefox.

**Атрибуты**:

- `driver_name` (str): Имя используемого WebDriver, по умолчанию 'firefox'.


**Методы**:

### `__init__`

**Описание**: Инициализирует Firefox WebDriver с заданными параметрами запуска, профилем, версиями GeckoDriver и Firefox, а также пользовательским User-Agent.

**Параметры**:

- `profile_name` (Optional[str], optional): Имя профиля Firefox для использования.
- `geckodriver_version` (Optional[str], optional): Версия GeckoDriver для использования.
- `firefox_version` (Optional[str], optional): Версия Firefox для использования.
- `user_agent` (Optional[dict], optional): Словарь с настройками User-Agent.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `WebDriverException`:  Возникает, если не удаётся запустить WebDriver (например, из-за отсутствия или несовместимости GeckoDriver).
- `Exception`: Возникает при других ошибках инициализации.


### `_payload`

**Описание**: Загружает исполнители для локаторов и сценариев JavaScript.

**Параметры**:

- Нет

**Возвращает**:

- `None`

**Вызывает исключения**:

- Нет


## Функции

### Нет функций в этом модуле.



## Использование

Пример использования класса `Firefox`:

```python
if __name__ == "__main__":
    profile_name = "custom_profile"
    geckodriver_version = "v0.29.0"
    firefox_version = "78.0"

    browser = Firefox(profile_name=profile_name, geckodriver_version=geckodriver_version, firefox_version=firefox_version)
    browser.get("https://www.example.com")
    browser.quit()
```

Обратите внимание, что пример демонстрирует использование класса `Firefox`, но сам модуль содержит более сложную логику, в частности, для загрузки настроек из `firefox.json` и обработки профилей.

```


```