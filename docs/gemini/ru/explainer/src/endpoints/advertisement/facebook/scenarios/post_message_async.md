```MD
# <input code>

```python
## \file hypotez/src/endpoints/advertisement/facebook/scenarios/post_message_async.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.advertisement.facebook.scenarios 
	:platform: Windows, Unix
	:synopsis: Публикация сообщения из `aliexpress` промо

"""
MODE = 'dev'

import time
import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, List
from selenium.webdriver.remote.webelement import WebElement
from src import gs
from src.webdriver import Driver
from src.utils import j_loads_ns, pprint
from src.logger import logger

# Load locators from JSON file.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)


def post_title(d: Driver, category: SimpleNamespace) -> bool:
    """ Sends the title and description of a campaign to the post message box.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        category (SimpleNamespace): The category containing the title and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> post_title(driver, category)
        True
    """
    # Scroll backward in the page
    if not d.scroll(1, 1200, 'backward'):
        logger.error("Scroll failed during post title", exc_info=False)
        return
    # Open the 'add post' box
    if not d.execute_locator(locator.open_add_post_box):
        logger.error("Failed to open 'add post' box", exc_info=False)
        return
    # Construct the message with title and description
    message = f"{category.title}; {category.description};"
    # Add the message to the post box
    if not d.execute_locator(locator.add_message, message):
        logger.error(f"Failed to add message to post box: {message=}", exc_info=False)
        return
    return True


async def upload_media(d: Driver, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    # ... (rest of the function)
```

# <algorithm>

**Алгоритм работы функции `promote_post`:**

1. **post_title(d, category):**
    - Прокручивает страницу назад.
    - Открывает форму добавления поста.
    - Формирует сообщение из title и description.
    - Добавляет сообщение в форму поста.
    - Возвращает True в случае успеха, иначе None.

2. **upload_media(d, products, no_video):**
    - Открывает форму добавления медиа.
    - Обрабатывает список продуктов, проверяя наличие `local_saved_video` или `local_saved_image`.
    - Загружает каждое медиа в форму.
    - Возвращает `True` в случае успеха, иначе None.
    - Обновляет подписи к изображениям асинхронно с помощью функции `update_images_captions`.


3. **update_images_captions(d, products, textarea_list):**
    - Загружает файл `translations.json` для локальных переводов.
    - Для каждого продукта:
        - Определяет направление текста (LTR/RTL) на основе языка из `local_units.LOCALE`.
        - Формирует строку с информацией о продукте, используя `product.title`, `product.original_price`, `product.sale_price`, `product.discount`, `product.evaluate_rate`, `product.promotion_link`, `product.tags` и `local_units.LOCALE`.
        - Асинхронно отправляет сформированную строку в соответствующие текстовые поля `textarea_list`.


4. **promote_post(d, category, products, no_video):**
    - Вызывает `post_title` для заголовка и описания.
    - Вызывает `upload_media` для загрузки медиа.
    - Выполняет действия для завершения редактирования и публикации поста.
    - Возвращает `True` в случае успеха, иначе None.


**Пример данных:**

```
category = SimpleNamespace(title="Новый сезон", description="Стильные модели")
products = [
    SimpleNamespace(local_saved_image="image1.jpg", product_title="Платье", original_price=100, sale_price=80, language='ru'),
    SimpleNamespace(local_saved_image="image2.png", product_title="Блузка", original_price=50, language='ru'),
]
```


# <mermaid>

```mermaid
graph LR
    A[promote_post] --> B{post_title};
    A --> C{upload_media};
    C --> D[update_images_captions];
    B --> E[finish_editing];
    E --> F[publish];
    F --> G[success];
    B --> H{error};
    C --> H;
    E --> H;
    F --> H;
    subgraph Driver Interactions
        B --> I[execute_locator(open_add_post_box)];
        B --> J[execute_locator(add_message)];
        C --> K[execute_locator(open_add_foto_video_form)];
        C --> L[execute_locator(foto_video_input)];
        C --> M[execute_locator(edit_uloaded_media_button)];
        C --> N[execute_locator(uploaded_media_frame)];
        C --> O[execute_locator(edit_image_properties_textarea)];
        D --> P[handle_product];
        E --> Q[execute_locator(finish_editing_button)];
        F --> R[execute_locator(publish)];
    end
```

**Описание диаграммы:**

Диаграмма описывает последовательность вызовов функций и взаимодействий с драйвером.  
- `promote_post` - запускает `post_title` и `upload_media`, которые в свою очередь выполняют ряд действий с WebDriver для взаимодействия с веб-страницей.
- `update_images_captions` - выполняется асинхронно для обработки изображений.
- Обработка ошибок (`error`) происходит на каждом этапе.
- Зависимость от `src.webdriver` (Driver) для взаимодействия с браузером.
- Зависимость от `src.logger` для логирования ошибок.
- Зависимость от `src.utils` для обработки JSON.
- Зависимость от `gs.path.src` для загрузки локаторов.

# <explanation>

**Импорты:**

- `time`, `asyncio`, `pathlib`, `SimpleNamespace`, `Dict`, `List`: Стандартные библиотеки Python для работы со временем, асинхронностью, путями, именованными пространствами, и типами данных.
- `selenium.webdriver.remote.webelement`: Для работы с веб-элементами Selenium.
- `src.gs`:  Вероятно, содержит конфигурацию и пути к ресурсам проекта (например, к файлам локаторов).
- `src.webdriver`:  Содержит класс `Driver` для взаимодействия с веб-драйвером (например, ChromeDriver или GeckoDriver).
- `src.utils`: Содержит функции для работы с JSON, например `j_loads_ns` для загрузки JSON в объекты `SimpleNamespace`.
- `src.logger`: Модуль для логирования событий.

**Классы:**

- `Driver`:  Управление взаимодействием с веб-драйвером (Selenium).  Не видим его реализации, но предполагается, что он предоставляет методы для взаимодействия с веб-страницей (напр., `scroll`, `execute_locator`, `wait`).

**Функции:**

- `post_title(d, category)`: Отправляет заголовок и описание в поле поста. Принимает экземпляр класса `Driver` и объект `category` для данных поста.
- `upload_media(d, products, no_video)`: Загружает медиафайлы (изображения, видео) и обновляет подписи. Принимает экземпляр `Driver`, список `products` (с путями к файлам) и флаг `no_video`.
- `update_images_captions(d, products, textarea_list)`: Обновляет подписи к изображениям асинхронно. Принимает список объектов `products` с информацией о продуктах, и список веб-элементов для редактирования текста.
- `promote_post(d, category, products, no_video)`: Основная функция для публикации поста, которая вызывает `post_title`, `upload_media` и завершающие действия.

**Переменные:**

- `locator`: Объект `SimpleNamespace`, содержащий загруженные из `post_message.json` локаторы элементов на веб-странице (например, для кнопок, полей ввода).
- `MODE`: Строковая константа, вероятно, для определения режима работы (например, `dev`, `prod`).
- `products`: Список объектов `SimpleNamespace`, содержащих информацию о продуктах (пути к изображениям, названия, цены и т.д.).
- `no_video`: Флаг, чтобы обрабатывать только изображения.


**Возможные ошибки и улучшения:**

- **Обработка ошибок:** В функциях `post_title`, `upload_media`, `update_images_captions` необходимо улучшить обработку ошибок (использовать `try...except` блоки) для более надежного поведения. Например, если функция `d.execute_locator` возвращает `None`, это нужно учитывать.
- **Проверка параметров:** Необходимо добавить проверки на корректность входных данных (например, `products` должен быть списком, объекты `SimpleNamespace` должны содержать необходимые поля).
- **Время ожидания:** `d.wait()` — предполагается, что этот метод отвечает за ожидание загрузки или реакции интерфейса. Стоит добавить обоснование и логику этих ожиданий (сколько ждать).
- **Локализация:** Использование `j_loads_ns(Path(gs.path.src / 'advertisement' / 'facebook' / 'scenarios' / 'translations.json'))` предполагает большую сложность и зависимость. Возможно, стоит упростить или пересмотреть структуру данных для локализаций.


**Цепочка взаимосвязей:**

Код находится в рамках рекламной кампании (advertisement).  Зависит от `src.gs` (конфигурации), `src.webdriver` (для работы с браузером), `src.utils` (для работы с JSON), и `src.logger` (для логирования).  Локаторы из `post_message.json`  описывают элементы на Facebook странице, что указывает на интеграцию с Facebook API или веб-интерфейсом.  Возможно, существуют другие сценарии (файлы) в этом модуле для различных действий.