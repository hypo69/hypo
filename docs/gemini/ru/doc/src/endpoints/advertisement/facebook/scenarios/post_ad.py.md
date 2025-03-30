# Модуль `post_ad`

## Обзор

Модуль `post_ad` предназначен для автоматической публикации рекламных сообщений в группах Facebook. Он использует Selenium WebDriver для взаимодействия с веб-интерфейсом Facebook. Модуль выполняет шаги по отправке заголовка сообщения, загрузке медиафайлов (изображений) и публикации сообщения.

## Подробней

Основная цель модуля - автоматизировать процесс размещения рекламы в Facebook, уменьшая необходимость ручного ввода данных и взаимодействия с интерфейсом. Он обрабатывает сценарии публикации сообщений, включая загрузку изображений и отправку текста.

## Функции

### `post_ad`

```python
def post_ad(d: Driver, message:SimpleNamespace) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        event (SimpleNamespace): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """
```

**Описание**: Функция `post_ad` выполняет публикацию рекламного сообщения в Facebook. Она принимает объект `Driver` для управления браузером и объект `SimpleNamespace`, содержащий данные сообщения.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `message` (SimpleNamespace): Объект, содержащий данные сообщения, такие как описание и путь к изображению.

**Возвращает**:
- `bool`: Возвращает `True`, если сообщение успешно опубликовано, иначе `None`.

**Примеры**:
```python
from selenium import webdriver
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Пример использования функции post_ad
driver = Driver(webdriver.Chrome())  # Инициализация драйвера Chrome
message = SimpleNamespace(description='Текст рекламного сообщения', image_path='path/to/image.jpg')
result = post_ad(driver, message)
print(f'Результат публикации: {result}')