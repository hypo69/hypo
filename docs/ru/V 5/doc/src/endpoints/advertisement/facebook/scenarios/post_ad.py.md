# Модуль `post_ad`

## Обзор

Модуль `post_ad` предназначен для автоматической публикации рекламных сообщений в группах Facebook с использованием Selenium WebDriver. Он включает в себя функции для отправки заголовка сообщения, загрузки медиафайлов (изображений) и публикации сообщения.

## Подробней

Этот модуль является частью системы автоматизации маркетинга `hypotez`. Он позволяет автоматизировать процесс размещения рекламы в Facebook, что экономит время и ресурсы маркетологов. Модуль использует Selenium для управления браузером и выполнения действий на веб-странице Facebook, таких как ввод текста, загрузка изображений и нажатие кнопок.

## Функции

### `post_ad`

```python
def post_ad(d: Driver, message: SimpleNamespace) -> bool:
    """
    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        message (SimpleNamespace): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """
```

**Описание**: Отправляет рекламное сообщение, включающее заголовок и, возможно, изображение, в Facebook.

**Как работает функция**:
1. Функция принимает драйвер Selenium (`d`) и объект `message` (SimpleNamespace), содержащий информацию о рекламном сообщении.
2. Сначала функция вызывает `post_message_title` для отправки заголовка сообщения. Если отправка не удалась, увеличивается счетчик ошибок `fails`.
3. Если `fails` достигает 15, функция прерывает выполнение.
4. Если у объекта `message` есть атрибут `image_path`, функция вызывает `upload_post_media` для загрузки изображения.
5. Затем вызывается `message_publish` для публикации сообщения.
6. В случае успеха счетчик ошибок сбрасывается, и функция возвращает `True`.

**Параметры**:
- `d` (Driver): Экземпляр драйвера Selenium для взаимодействия с веб-страницей.
- `message` (SimpleNamespace): Объект, содержащий данные для рекламного сообщения, такие как заголовок (`title`), описание (`description`) и путь к изображению (`image_path`).

**Возвращает**:
- `bool`: `True`, если сообщение было успешно отправлено и опубликовано, в противном случае `None`.

**Вызывает исключения**:
- `timeout`: Возникает, если истекло время ожидания при взаимодействии с веб-элементами.

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Инициализация драйвера (пример)
driver = Driver(webdriver.Chrome())

# Создание объекта message с данными для рекламного сообщения
message = SimpleNamespace(description="Текст рекламного сообщения", image_path="путь/к/изображению.jpg")

# Вызов функции post_ad
result = post_ad(driver, message)

if result:
    print("Рекламное сообщение успешно опубликовано.")
else:
    print("Не удалось опубликовать рекламное сообщение.")