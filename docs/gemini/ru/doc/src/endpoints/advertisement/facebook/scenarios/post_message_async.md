# Модуль `hypotez/src/endpoints/advertisement/facebook/scenarios/post_message_async.py`

## Обзор

Этот модуль предоставляет асинхронные функции для публикации сообщений в Facebook с использованием Selenium WebDriver.  Модуль ориентирован на публикацию рекламных сообщений, включая заголовок, описание и медиафайлы. Он обрабатывает такие задачи, как отправка текста, загрузка изображений/видео и добавление подписей к медиа.


## Функции

### `post_title`

**Описание**: Отправляет заголовок и описание кампании в поле сообщения поста.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Объект `SimpleNamespace`, содержащий заголовок и описание, которые нужно отправить.

**Возвращает**:
- `bool`: `True`, если заголовок и описание были отправлены успешно, иначе `None`.

**Обрабатывает исключения**:
- `Exception`:  Возникает в случае проблем со скроллингом или взаимодействием с элементами страницы.  Подробные сообщения об ошибках записываются в лог.


### `upload_media`

**Описание**: Загружает медиафайлы (изображения или видео) в раздел изображений и обновляет подписи.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список объектов `SimpleNamespace`, каждый из которых содержит путь к медиафайлу.
- `no_video` (bool, optional):  Флаг, указывающий, нужно ли пропускать загрузку видео. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если медиафайлы были загружены успешно, иначе `None`.

**Обрабатывает исключения**:
- `Exception`: Возникает в случае ошибок при загрузке медиафайлов или обновлении подписей. Подробные сообщения об ошибках записываются в лог.


### `update_images_captions`

**Описание**: Асинхронно добавляет описания к загруженным медиафайлам.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список объектов `SimpleNamespace`, содержащих данные для обновления подписей.
- `textarea_list` (List[WebElement]): Список текстовых областей, в которые будут добавлены подписи.

**Обрабатывает исключения**:
- `Exception`: Возникает в случае ошибок при обновлении подписей к медиафайлам. Подробные сообщения об ошибках записываются в лог.


### `promote_post`

**Описание**: Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

**Параметры**:
- `d` (Driver): Экземпляр драйвера.
- `category` (SimpleNamespace): Объект `SimpleNamespace`, содержащий данные для заголовка и описания поста.
- `products` (List[SimpleNamespace]): Список объектов `SimpleNamespace`, содержащих данные для медиафайлов.
- `no_video` (bool, optional):  Флаг, указывающий, нужно ли пропускать загрузку видео. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если пост был успешно опубликован, иначе `None`.

**Примеры использования**:
```python
# Пример использования функции post_title
# ... (создание драйвера)
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
result = post_title(driver, category)
if result:
    print("Заголовок и описание успешно отправлены")

# Пример использования функции promote_post
# ... (создание драйвера, списка продуктов)
await promote_post(driver, category, products)

```

## Замечания

- Используется асинхронное программирование (`async def`) для повышения производительности.
- Функции используют логгирование для отслеживания ошибок.
-  Модуль полагается на внешние библиотеки (`selenium`, `asyncio`, `jjson`, `gs`, `src.utils`).
- Входные данные должны быть подготовлены в соответствующем формате (объекты `SimpleNamespace`).
- Локализационные данные берутся из `translations.json`.