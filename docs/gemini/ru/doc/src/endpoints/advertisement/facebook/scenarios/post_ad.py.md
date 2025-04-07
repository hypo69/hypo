# Модуль `post_ad.py`

## Обзор

Модуль `post_ad.py` предназначен для публикации рекламных сообщений в группах Facebook. Он содержит функцию `post_ad`, которая автоматизирует процесс отправки заголовка сообщения, загрузки медиафайлов (если они есть) и публикации сообщения.

## Подробней

Этот модуль является частью системы автоматизации размещения рекламы в Facebook. Он использует Selenium WebDriver для взаимодействия с веб-интерфейсом Facebook. Модуль загружает локаторы элементов интерфейса из JSON-файла, что позволяет легко адаптировать его к изменениям в структуре веб-страницы Facebook.
Модуль использует другие модули:
- `post_message_title` отвечает за ввод заголовка и описания поста
- `upload_post_media` - загружает медиафайлы к посту
- `message_publish` - непосредственно публикует сообщение

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

**Назначение**:
Функция `post_ad` автоматизирует процесс публикации рекламного сообщения в группе Facebook. Она принимает объект драйвера WebDriver и объект SimpleNamespace, содержащий информацию о сообщении, такую как заголовок, описание и путь к изображению.

**Параметры**:

-   `d` (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
-   `message` (SimpleNamespace): Объект, содержащий данные сообщения (описание и путь к изображению, если есть).

**Возвращает**:

-   `bool`: `True`, если сообщение было успешно отправлено, иначе `None`.

**Как работает функция**:

1.  **Отправка заголовка сообщения**: Функция вызывает `post_message_title` для отправки заголовка и описания сообщения. В случае неудачи увеличивает счетчик `fails` и возвращается, если количество неудач не превышает 15.
2.  **Загрузка медиафайла**: Если у сообщения есть изображение (`message.image_path`), функция вызывает `upload_post_media` для загрузки изображения в сообщение.
3.  **Публикация сообщения**: Функция вызывает `message_publish` для публикации сообщения.
4.  **Сброс счетчика неудач**: Если все этапы прошли успешно, счетчик `fails` сбрасывается.

**ASCII flowchart**:

```
Начало
    ↓
post_message_title (Отправка заголовка и описания сообщения)
    ↓
    Успех? -- Нет --> fails += 1 --> fails < 15? -- Да --> Конец
    |   
    Да
    ↓
hasattr(message, 'image_path') and message.image_path (Проверка наличия изображения)
    ↓
    Есть изображение? -- Да --> upload_post_media (Загрузка изображения)
    |
    Нет
    ↓
message_publish (Публикация сообщения)
    ↓
fails = 0 (Сброс счетчика неудач)
    ↓
Конец
```

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Пример использования функции post_ad
driver = Driver(webdriver.Chrome())
message = SimpleNamespace(description="Новое рекламное предложение!", image_path="path/to/image.jpg")

if post_ad(driver, message):
    print("Сообщение успешно опубликовано")
else:
    print("Ошибка при публикации сообщения")