# Модуль locator

## Обзор

Этот модуль содержит описание локаторов для взаимодействия с веб-элементами. Локаторы описывают, как найти элементы на странице и выполнить действия (клик, скриншот, извлечение атрибутов). Они передаются в класс `ExecuteLocator` для выполнения.

## Локаторы

### `close_banner`

**Описание**: Закрывает баннер (pop-up окно), если он появился на странице.

**Параметры**:

- `attribute` (Optional[Any]): Не используется.
- `by` (str): Тип локатора (`XPATH`).
- `selector` (str): Выражение для поиска элемента (`//button[@id = 'closeXButton']`).
- `if_list` (str): Если найдено несколько элементов, использовать первый (`first`).
- `use_mouse` (bool): Не использовать мышь (`False`).
- `mandatory` (bool): Необязательное действие (`False`).
- `timeout` (int): Таймаут для поиска элемента (`0`).
- `timeout_for_event` (str): Условие ожидания (`presence_of_element_located`).
- `event` (str): Событие для выполнения (`click()`).
- `locator_description` (str): Описание локатора.

**Возвращает**:

- (None): Не возвращает значений.

**Вызывает исключения**:

- `ElementClickInterruptedException`: Если произошла ошибка при клике.


### `id_manufacturer`

**Описание**: Возвращает значение, установленное в `attribute`.

**Параметры**:

- `attribute` (Any): Значение атрибута (`11290`).
- `by` (str): Тип локатора (`VALUE`).
- `selector` (Optional[str]): Не используется.
- `if_list` (str): Если найдено несколько элементов, использовать первый (`first`).
- `use_mouse` (bool): Не использовать мышь (`False`).
- `mandatory` (bool): Обязательное действие (`True`).
- `timeout` (int): Таймаут для поиска элемента (`0`).
- `timeout_for_event` (str): Условие ожидания (`presence_of_element_located`).
- `event` (Optional[str]): Нет события (`None`).
- `locator_description` (str): Описание локатора.

**Возвращает**:

- (Any): Значение, установленное в `attribute`.

**Вызывает исключения**:

- `ElementDoesNotExistError`: Если элемент не найден и `mandatory` = `True`.


### `additional_images_urls`

**Описание**: Извлекает URL дополнительных изображений.

**Параметры**:

- `attribute` (str): Атрибут для извлечения (`src`).
- `by` (str): Тип локатора (`XPATH`).
- `selector` (str): Выражение для поиска элементов (`//ol[contains(@class, 'flex-control-thumbs')]//img`).
- `if_list` (str): Если найдено несколько элементов, использовать первый (`first`).
- `use_mouse` (bool): Не использовать мышь (`False`).
- `mandatory` (bool): Необязательное действие (`False`).
- `timeout` (int): Таймаут для поиска элемента (`0`).
- `timeout_for_event` (str): Условие ожидания (`presence_of_element_located`).
- `event` (Optional[str]): Нет события (`None`).


**Возвращает**:

- (List[str] | None): Список URL изображений или `None`, если элементы не найдены.

**Вызывает исключения**:

- (None): Нет специфичных исключений.


### `default_image_url`

**Описание**: Делает скриншот изображения по умолчанию.

**Параметры**:

- `attribute` (Optional[Any]): Не используется.
- `by` (str): Тип локатора (`XPATH`).
- `selector` (str): Выражение для поиска элемента (`//a[@id = 'mainpic']//img`).
- `if_list` (str): Если найдено несколько элементов, использовать первый (`first`).
- `use_mouse` (bool): Не использовать мышь (`False`).
- `timeout` (int): Таймаут для поиска элемента (`0`).
- `timeout_for_event` (str): Условие ожидания (`presence_of_element_located`).
- `event` (str): Событие для выполнения (`screenshot()`).
- `mandatory` (bool): Обязательное действие (`True`).
- `locator_description` (str): Описание локатора.

**Возвращает**:

- (bytes): Скриншот изображения в формате `PNG`.

**Вызывает исключения**:

- `ElementDoesNotExistError`: Если элемент не найден и `mandatory` = `True`.


### `id_supplier`

**Описание**: Извлекает текст внутри элемента, содержащего SKU.

**Параметры**:

- `attribute` (str): Атрибут для извлечения (`innerText`).
- `by` (str): Тип локатора (`XPATH`).
- `selector` (str): Выражение для поиска элемента (`//span[@class = 'ltr sku-copy']`).
- `if_list` (str): Если найдено несколько элементов, использовать первый (`first`).
- `use_mouse` (bool): Не использовать мышь (`False`).
- `mandatory` (bool): Обязательное действие (`True`).
- `timeout` (int): Таймаут для поиска элемента (`0`).
- `timeout_for_event` (str): Условие ожидания (`presence_of_element_located`).
- `event` (Optional[str]): Нет события (`None`).
- `locator_description` (str): Описание локатора.

**Возвращает**:

- (str): Текст внутри элемента.

**Вызывает исключения**:

- `ElementDoesNotExistError`: Если элемент не найден и `mandatory` = `True`.


## Взаимодействие с `executor`

Executor использует локаторы для выполнения действий на странице.  Процесс включает поиск элемента по указанным параметрам, выполнение события, если указано, и возврат атрибута или результата действия.  Если действие необязательно (`mandatory: false`), и элемент не найден, выполнение продолжается. В противном случае возникает исключение.