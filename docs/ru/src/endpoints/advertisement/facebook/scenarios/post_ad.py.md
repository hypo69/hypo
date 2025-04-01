# Модуль `post_ad.py`

## Обзор

Модуль `post_ad.py` предназначен для публикации рекламных сообщений в группах Facebook. Он содержит функции для отправки заголовка сообщения, загрузки медиафайлов и публикации всего сообщения.

## Подробней

Этот модуль является частью системы автоматизации размещения рекламы в Facebook. Он использует Selenium WebDriver для взаимодействия с веб-интерфейсом Facebook и выполняет следующие шаги:

1.  Отправляет заголовок сообщения.
2.  Загружает медиафайлы (изображения).
3.  Публикует сообщение.

Расположение файла в проекте: `hypotez/src/endpoints/advertisement/facebook/scenarios/post_ad.py`

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

**Назначение**: Отправляет рекламное сообщение, состоящее из заголовка и медиафайлов, в Facebook.

**Параметры**:

*   `d` (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
*   `message` (SimpleNamespace): Объект, содержащий заголовок сообщения, путь к изображению и описание.

**Возвращает**:

*   `bool`: `True`, если заголовок и описание были успешно отправлены, иначе `None`.

**Как работает функция**:

1.  Устанавливает глобальную переменную `fails` равной 0.
2.  Вызывает функцию `post_message_title` для отправки заголовка сообщения. Если отправка не удалась, увеличивает счетчик `fails` и возвращается, если количество неудачных попыток меньше 15.
3.  Если в объекте `message` есть атрибут `image_path`, вызывает функцию `upload_post_media` для загрузки медиафайла.
4.  Вызывает функцию `message_publish` для публикации сообщения.
5.  Сбрасывает счетчик `fails` в 0.
6.  Возвращает `True`.

**Внутренние функции**:

Функция `post_ad` использует следующие внутренние функции для выполнения своих задач:

*   `post_message_title(d, message.description)`: Отправляет заголовок сообщения.

    ```python
    def post_message_title(d: Driver, message: str) -> bool:
        """Отправляет заголовок сообщения.

        Args:
            d (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
            message (str): Текст сообщения для отправки.

        Returns:
            bool: True, если заголовок был успешно отправлен, иначе False.

        Как работает функция:
            1. Находит элемент ввода заголовка с использованием локатора locator.post_text.
            2. Отправляет текст сообщения в элемент ввода.
            3. Возвращает True, если отправка прошла успешно, иначе False.
        """
    ```

*   `upload_post_media(d, media = message.image_path, without_captions = True)`: Загружает медиафайл (изображение).

    ```python
    def upload_post_media(d: Driver, media: str, without_captions: bool = True) -> bool:
        """Загружает медиафайл (изображение) в сообщение.

        Args:
            d (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
            media (str): Путь к медиафайлу.
            without_captions (bool): Если True, не добавляет подпись к изображению. По умолчанию True.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.

        Как работает функция:
            1. Находит элемент загрузки медиафайла с использованием локатора locator.photo_video.
            2. Отправляет путь к медиафайлу в элемент загрузки.
            3. Ожидает завершения загрузки.
            4. Возвращает True, если загрузка прошла успешно, иначе False.
        """
    ```

*   `message_publish(d)`: Публикует сообщение.

    ```python
    def message_publish(d: Driver) -> bool:
        """Публикует сообщение.

        Args:
            d (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.

        Returns:
            bool: True, если публикация прошла успешно, иначе False.

        Как работает функция:
            1. Находит кнопку публикации с использованием локатора locator.submit.
            2. Кликает на кнопку публикации.
            3. Ожидает завершения публикации.
            4. Возвращает True, если публикация прошла успешно, иначе False.
        """
    ```

**ASCII Flowchart**:

```
    Начало
     |
     V
Отправка заголовка (post_message_title)
     |
     V
Есть ли изображение? (hasattr(message, 'image_path'))
     |
     +-- Да --> Загрузка медиафайла (upload_post_media)
     |
     V
Публикация сообщения (message_publish)
     |
     V
    Конец
```

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Пример использования функции post_ad
driver = Driver(...)  # инициализация драйвера
message = SimpleNamespace(description="Новая акция! Скидки до 50%!", image_path="/path/to/image.jpg")
result = post_ad(driver, message)
if result:
    print("Сообщение успешно опубликовано!")
else:
    print("Ошибка при публикации сообщения.")