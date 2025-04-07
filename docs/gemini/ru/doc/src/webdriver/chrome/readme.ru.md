# Документация модуля `src.webdriver.chrome`

## Обзор

Этот модуль предоставляет кастомную реализацию Chrome WebDriver с использованием Selenium. Он предназначен для интеграции настроек конфигурации из файла `chrome.json`, таких как user-agent и настройки профиля браузера, для обеспечения гибкого и автоматизированного взаимодействия с браузером.

## Подробнее

Модуль упрощает настройку и использование Chrome WebDriver, централизуя параметры конфигурации и предоставляя улучшенное логирование. Он поддерживает несколько профилей браузера, что позволяет настраивать различные параметры для тестирования.

## Классы

### `Chrome`

**Описание**: Класс `Chrome` предоставляет кастомную реализацию Chrome WebDriver с использованием Selenium.

**Принцип работы**:
Класс автоматически загружает настройки из файла `chrome.json` и использует их для конфигурации WebDriver. Он также позволяет указывать пользовательский user-agent и передавать дополнительные опции при инициализации WebDriver. WebDriver для `Chrome` использует паттерн Singleton, гарантируя создание только одного экземпляра WebDriver.

**Методы**:

- **`__init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None)`**: Инициализирует Chrome WebDriver с заданными параметрами.
- **`close(self)`**: Закрывает текущее окно браузера.
- **`quit(self)`**: Закрывает все окна браузера и завершает сессию WebDriver.
- **`get(self, url: str)`**: Открывает указанный URL в браузере.
- **`execute_script(self, script: str, *args)`**: Выполняет JavaScript-код в контексте текущей страницы.
- **`execute_locator(self, l: dict)`**: Находит и выполняет действие с веб-элементом, используя данные из локатора.
- **`get_page_source(self) -> str`**: Возвращает исходный код текущей страницы.
- **`save_screenshot(self, filename: str)`**: Сохраняет скриншот текущей страницы.

**Параметры**:

- `user_agent` (Optional[str]): Пользовательский user-agent для браузера. По умолчанию `None`.
- `options` (Optional[List[str]]): Список дополнительных опций для Chrome. По умолчанию `None`.

**Примеры**:

```python
from src.webdriver.chrome import Chrome

# Инициализация Chrome WebDriver с настройками user-agent и пользовательскими опциями
browser = Chrome(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)", options=["--headless", "--disable-gpu"])

# Открытие веб-сайта
browser.get("https://www.example.com")

# Закрытие браузера
browser.quit()