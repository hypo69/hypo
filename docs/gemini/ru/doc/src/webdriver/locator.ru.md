# Локаторы веб-элементов

## Обзор

Этот файл описывает формат и работу локаторов для взаимодействия с веб-элементами в рамках проекта. Локаторы служат для определения и управления действиями над веб-элементами, такими как клики, извлечение атрибутов, и т.д.  Они передаются в класс `ExecuteLocator` для выполнения указанных задач.

## Примеры локаторов

### `close_banner`

**Описание**: Локатор для закрытия всплывающего баннера (pop-up).

**Параметры**:

* `attribute` (Optional[Any], optional): Не используется в этом случае. По умолчанию `None`.
* `by` (str): Тип локатора (`XPATH`).
* `selector` (str): Выражение для поиска элемента (`//button[@id = 'closeXButton']`).
* `if_list` (str, optional): Если найдено несколько элементов, используется первый (`first`). По умолчанию `first`.
* `use_mouse` (bool, optional): Не использовать мышь (`false`). По умолчанию `false`.
* `mandatory` (bool, optional): Необязательное действие (`false`). По умолчанию `false`.
* `timeout` (int, optional): Таймаут для поиска элемента (`0`). По умолчанию `0`.
* `timeout_for_event` (str, optional): Условие ожидания (`presence_of_element_located`). По умолчанию `presence_of_element_located`.
* `event` (str, optional): Событие для выполнения (`click()`). По умолчанию `click()`.
* `locator_description` (str, optional): Описание локатора. По умолчанию `None`.

**Возвращает**:

* `None`: Локатор не возвращает значения.

**Вызывает исключения**:

* `ElementNotFoundEx`: Если элемент не найден и `mandatory=true`.


### `id_manufacturer`

**Описание**: Локатор для получения значения `id_manufacturer`.

**Параметры**:

* `attribute` (int): Значение атрибута (`11290`).
* `by` (str): Тип локатора (`VALUE`).
* `selector` (Optional[str], optional): Не используется в данном случае. По умолчанию `None`.
* `if_list` (str, optional): Если найдено несколько элементов, используется первый (`first`). По умолчанию `first`.
* `use_mouse` (bool, optional): Не использовать мышь (`false`). По умолчанию `false`.
* `mandatory` (bool, optional): Обязательное действие (`true`). По умолчанию `true`.
* `timeout` (int, optional): Таймаут для поиска элемента (`0`). По умолчанию `0`.
* `timeout_for_event` (str, optional): Условие ожидания (`presence_of_element_located`). По умолчанию `presence_of_element_located`.
* `event` (Optional[str], optional): Нет события (`null`). По умолчанию `None`.
* `locator_description` (str, optional): Описание локатора. По умолчанию `None`.


**Возвращает**:

* int: Значение атрибута `attribute`.


**Вызывает исключения**:

* `ElementNotFoundEx`: Если элемент не найден и `mandatory=true`.


### `additional_images_urls`

**Описание**: Локатор для извлечения URL дополнительных изображений.

(Аналогично описываются остальные локаторы `additional_images_urls`, `default_image_url`, `id_supplier`,  следуя указанному шаблону, подробно описывая каждый параметр и ожидаемое возвращаемое значение, а так же возможные исключения)

### `default_image_url`

**Описание**: Локатор для получения скриншота изображения по умолчанию.

### `id_supplier`

**Описание**: Локатор для извлечения текста SKU.


## Взаимодействие с `executor`

`executor` использует локаторы для выполнения действий на веб-странице. Процесс включает в себя:

1. Парсинг локатора.
2. Поиск элемента по типу локатора и селектору.
3. Выполнение события (если указано).
4. Извлечение атрибута (если указано).
5. Обработку ошибок (если действие не обязательно, `mandatory=false`, или выдача исключения `ElementNotFoundEx` при `mandatory=true` и отсутствии элемента).


**Важно:**  Каждый локатор должен иметь корректный тип (`by`) и соответствующий селектор (`selector`) для эффективного поиска и взаимодействия с веб-элементами. Необходимо обращать внимание на обработку возможных исключений.