# Модуль `post_ad`

## Обзор

Модуль `post_ad` предназначен для публикации рекламных сообщений в группах Facebook. Он использует Selenium WebDriver для автоматизации процесса отправки заголовка, загрузки медиафайлов (изображений) и публикации сообщения.

## Подробней

Этот модуль является частью системы автоматизации для размещения рекламы в Facebook. Он включает в себя функции для отправки заголовка сообщения, загрузки медиаконтента и финальной публикации объявления. Расположение файла в структуре проекта указывает на его роль в качестве одного из сценариев для работы с Facebook.

## Функции

### `post_ad`

```python
def post_ad(d: Driver, message:SimpleNamespace) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        message (SimpleNamespace): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> message = SimpleNamespace(title="Campaign Title", description="Event Description", image_path="path/to/image.jpg")
        >>> post_ad(driver, message)
        True
    """
    ...
```

**Назначение**: Публикует рекламное сообщение в Facebook, включая заголовок, медиафайлы (если есть) и выполняет публикацию.

**Параметры**:

-   `d` (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
-   `message` (SimpleNamespace): Объект, содержащий информацию о рекламном сообщении, такую как заголовок, описание и путь к изображению.

**Возвращает**:

-   `bool`: `True`, если заголовок и описание успешно отправлены, в противном случае - `None`.

**Как работает функция**:

1.  Инициализирует глобальную переменную `fails` для отслеживания количества неудачных попыток.
2.  Вызывает функцию `post_message_title` для отправки заголовка сообщения. Если отправка не удалась, увеличивает счетчик `fails` и, если количество неудачных попыток меньше 15, завершает функцию.
3.  Если у объекта `message` есть атрибут `image_path`, вызывает функцию `upload_post_media` для загрузки медиафайла.
4.  Вызывает функцию `message_publish` для публикации сообщения.
5.  Обнуляет счетчик `fails` и возвращает `True`, если все этапы выполнены успешно.

**Внутренние функции**: Отсутствуют.

**Примеры**:

```python
from src.webdriver.driver import Driver, Chrome
from types import SimpleNamespace
from pathlib import Path

# Создание инстанса драйвера (пример с Chrome)
driver = Driver(Chrome)
message = SimpleNamespace(description="Новое рекламное сообщение", image_path=Path("path/to/image.jpg"))
result = post_ad(driver, message)
print(f"Результат публикации: {result}")
```

**ASII flowchart**:

```
Начало
    │
    ├───> Отправка заголовка сообщения (post_message_title)
    │       └───> Неудачно: Увеличение fails, проверка < 15, выход
    │       └───> Успешно: Продолжение
    │
    ├───> Проверка наличия image_path
    │       └───> Нет: Переход к публикации
    │       └───> Да: Загрузка медиафайла (upload_post_media)
    │
    ├───> Публикация сообщения (message_publish)
    │
    └───> Сброс fails, возврат True