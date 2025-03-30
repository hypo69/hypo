# Модуль `post_ad`

## Обзор

Модуль `post_ad` предназначен для автоматической публикации рекламных сообщений в группах Facebook. Он использует Selenium WebDriver для взаимодействия с веб-интерфейсом Facebook и выполняет шаги по заполнению заголовка сообщения, загрузке медиафайлов и публикации объявления.

## Подробней

Этот модуль является частью системы автоматизации маркетинга `hypotez`. Он позволяет автоматизировать процесс публикации рекламы, что экономит время и ресурсы. Модуль загружает локаторы элементов интерфейса из JSON-файла, что обеспечивает гибкость и упрощает поддержку. В случае сбоев предусмотрен механизм повторных попыток, а также логирование для отслеживания ошибок.

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

**Описание**: Функция `post_ad` автоматизирует процесс публикации рекламного сообщения в Facebook, используя предоставленный драйвер Selenium и объект `SimpleNamespace`, содержащий информацию о сообщении.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `message` (SimpleNamespace): Объект, содержащий данные для публикации, такие как описание и путь к изображению.

**Возвращает**:
- `bool`: `True`, если публикация прошла успешно, в противном случае `None`.

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Инициализация драйвера (пример)
driver = Driver(webdriver.Chrome())

# Создание объекта сообщения (пример)
message = SimpleNamespace(description="Текст рекламного сообщения", image_path="path/to/image.jpg")

# Вызов функции публикации
result = post_ad(driver, message)
print(f"Результат публикации: {result}")

# Закрытие драйвера (пример)
driver.close()