# Документация для `post_message.json`

## Оглавление

1.  [Обзор](#обзор)
2.  [Локаторы](#локаторы)
    *   [open\_add\_post\_box](#open_add_post_box)
    *   [add\_message](#add_message)
    *   [open\_add\_foto\_video\_form](#open_add_foto_video_form)
    *  [foto\_video\_input](#foto_video_input)
    *  [edit\_uloaded\_media\_button](#edit_uloaded_media_button)
    *  [uploaded\_media\_frame](#uploaded_media_frame)
    *  [edit\_image\_properties\_textarea](#edit_image_properties_textarea)
    *  [finish\_editing\_button](#finish_editing_button)
    *  [publish](#publish)
    *  [send](#send)
    *  [not\_now](#not_now)
    *  [close\_pop\_up](#close_pop_up)
    *  [edit\_posts](#edit_posts)

## Обзор

Файл `post_message.json` содержит JSON-объект с набором локаторов для управления публикациями в Facebook. Каждый локатор описывает элемент на странице, который может быть использован для автоматизации действий, таких как открытие формы ввода сообщения, добавление медиафайлов и публикация контента.

## Локаторы

### `open_add_post_box`

**Описание**: Локатор для открытия окна ввода сообщения. Находит элемент, который содержит текст "Что у вас нового" или "Напишите что-нибудь...".

**Параметры**:
- `attribute` (null): Атрибут элемента не указан.
- `by` (str): Способ поиска элемента - `XPATH`.
- `selector` (str):  `XPATH` выражение для поиска элемента `//span[contains(text(), 'Что у вас нового') or contains(text(), 'Напишите что-нибудь...')]`.
- `if_list` (str): Выбор первого элемента из списка, если найдено несколько.
- `use_mouse` (bool): Использование мыши не требуется.
- `timeout` (int): Время ожидания элемента - 0.
- `timeout_for_event` (str): Тип события для ожидания - `presence_of_element_located`.
- `event` (str): Событие для выполнения - `click()`.
- `mandatory` (bool): Локатор обязателен для использования.
- `locator_description` (str): Описание локатора - "открытие окна для ввода сообщения, пауза, отправка сообщения".

### `add_message`

**Описание**: Локатор для добавления текста сообщения. Находит последний элемент `div` с `role='textbox'`.

**Параметры**:
- `attribute` (str): Атрибут элемента не указан.
- `by` (str): Способ поиска элемента - `XPATH`.
- `selector` (str): `XPATH` выражение для поиска элемента `(//div[@role='textbox'])[last()]`.
- `if_list` (str): Выбор первого элемента из списка, если найдено несколько.
- `use_mouse` (str): Использование мыши не требуется.
- `timeout` (int): Время ожидания элемента - 0.
- `timeout_for_event` (str): Тип события для ожидания - `presence_of_element_located`.
- `event` (str): Событие для выполнения - `pause(1);%EXTERNAL_MESSAGE%`, вставка текста с паузой в 1 секунду.
- `mandatory` (str): Локатор обязателен для использования.
- `locator_description` (str): Описание локатора - "через `execute_locator()` будет передан текст".
- `deprecated` (str): Помечен как устаревший, рекомендуется использовать `open_add_post_box`.

### `open_add_foto_video_form`

**Описание**: Локатор для открытия формы добавления фото или видео. Находит `div` с `aria-label='Фото/видео'`.

**Параметры**:
- `attribute` (null): Атрибут элемента не указан.
- `by` (str): Способ поиска элемента - `XPATH`.
- `selector` (str): `XPATH` выражение для поиска элемента `//div[@aria-label='Фото/видео']`.
- `#selector` (str): Альтернативный, не используемый `XPATH` `//span[contains(text(),'или перетащите файлы')]`
- `if_list` (str): Выбор первого элемента из списка, если найдено несколько.
- `use_mouse` (bool): Использование мыши обязательно.
- `timeout` (int): Время ожидания элемента - 0.
- `timeout_for_event` (str): Тип события для ожидания - `presence_of_element_located`.
- `event` (str): Событие для выполнения - `click()`.
- `mandatory` (bool): Локатор обязателен для использования.
- `locator_description` (str): Описание локатора - "Нажать для меню загрузки видео".

### `foto_video_input`

**Описание**: Локатор для загрузки медиафайлов. Находит элемент `input` с `type='file'` внутри `div` с `role='dialog'`.

**Параметры**:
- `attribute` (null): Атрибут элемента не указан.
- `by` (str): Способ поиска элемента - `XPATH`.
- `selector` (str): `XPATH` выражение для поиска элемента `//div[@role='dialog']//input[@type = 'file']`.
- `#selector` (str): Альтернативный, не используемый `XPATH` `//div[@role='presentation']/following-sibling::div//input[@type='file']`
- `##selector` (str): Альтернативный, не используемый `XPATH` `//div[@role='presentation']/following-sibling::div`
- `###selector` (str): Альтернативный, не используемый `XPATH` `(//input[@type='file'])[1]`
- `timeout` (int): Время ожидания элемента - 0.
- `timeout_for_event` (str): Тип события для ожидания - `presence_of_element_located`.
- `event` (str): Событие для выполнения - `upload_media()`, загрузка медиафайла.
- `mandatory` (bool): Локатор обязателен для использования.
- `locator_description` (str): Описание локатора - "Загрузка медиа, Путь к файлу передается через код сценария ".

### `edit_uloaded_media_button`

**Описание**: Локатор для открытия полей описаний загруженных медиафайлов. Ищет `div` с `role='button'` и `aria-label` содержащим "Редактировать всё".

**Параметры**:
- `attribute` (null): Атрибут элемента не указан.
- `by` (str): Способ поиска элемента - `XPATH`.
- `selector` (str): `XPATH` выражение для поиска элемента `//div[@role='button' and contains(@aria-label,'Редактировать всё')]`.
- `timeout` (int): Время ожидания элемента - 0.
- `timeout_for_event` (str): Тип события для ожидания - `presence_of_element_located`.
- `event` (str): Событие для выполнения - `click()`.
- `mandatory` (bool): Локатор обязателен для использования.
- `locator_description` (str): Описание локатора - "Открывает поля описаний для загруженных медиафайлов".

### `uploaded_media_frame`

**Описание**: Локатор для попапа с загруженными медиа для редакции. Находит `div` с `aria-label='Фото/видео'`.

**Параметры**:
- `attribute` (null): Атрибут элемента не указан.
- `by` (str): Способ поиска элемента - `XPATH`.
- `selector` (str): `XPATH` выражение для поиска элемента `//div[@aria-label='Фото/видео']`.
- `timeout` (int): Время ожидания элемента - 0.
- `timeout_for_event` (str): Тип события для ожидания - `presence_of_element_located`.
- `event` (str): Событие не указано - `null`.
- `mandatory` (bool): Локатор обязателен для использования.
- `locator_description` (str): Описание локатора - "Попап с открытыми медиа для редакции".

### `edit_image_properties_textarea`

**Описание**: Локатор для текстовых полей описания к медиафайлу. Находит элемент `textarea`.

**Параметры**:
- `attribute` (null): Атрибут элемента не указан.
- `by` (str): Способ поиска элемента - `XPATH`.
- `selector` (str): `XPATH` выражение для поиска элемента `//textarea`.
- `timeout` (int): Время ожидания элемента - 0.
- `timeout_for_event` (str): Тип события для ожидания - `presence_of_element_located`.
- `event` (str): Событие не указано - `null`.
- `mandatory` (bool): Локатор обязателен для использования.
- `locator_description` (str): Описание локатора - "Текстовые поля для описания к медиафайлу".

### `finish_editing_button`

**Описание**: Локатор для закрытия окна загрузки фото и описаний. Ищет `span`, содержащий текст "Готово".

**Параметры**:
- `attribute` (null): Атрибут элемента не указан.
- `by` (str): Способ поиска элемента - `XPATH`.
- `selector` (str): `XPATH` выражение для поиска элемента `//span[contains(text(),'Готово')]`.
- `timeout` (int): Время ожидания элемента - 0.
- `timeout_for_event` (str): Тип события для ожидания - `presence_of_element_located`.
- `event` (str): Событие для выполнения - `click()`.
- `mandatory` (bool): Локатор обязателен для использования.
- `locator_description` (str): Описание локатора - "Закрытие окна загрузки фото и описаний".

### `publish`

**Описание**: Локатор для кнопки публикации. Ищет `div` с `aria-label` "Опубликовать", "Отправить" или "Далее".

**Параметры**:
- `attribute` (null): Атрибут элемента не указан.
- `by` (str): Способ поиска элемента - `XPATH`.
- `selector` (str): `XPATH` выражение для поиска элемента `//div[@aria-label='Опубликовать' or @aria-label='Отправить' or @aria-label='Далее']`.
- `timeout` (int): Время ожидания элемента - 0.
- `timeout_for_event` (str): Тип события для ожидания - `presence_of_element_located`.
- `event` (str): Событие для выполнения - `click()`.
- `mandatory` (bool): Локатор обязателен для использования.
- `locator_description` (str): Описание локатора - "Закрытие окна загрузки фото и описаний".

### `send`

**Описание**: Локатор для кнопки "Отправить". Ищет последний `span`, содержащий текст "Отправить".

**Параметры**:
- `attribute` (null): Атрибут элемента не указан.
- `by` (str): Способ поиска элемента - `XPATH`.
- `selector` (str): `XPATH` выражение для поиска элемента `(//span[contains(text(),'Отправить')])[last()]`.
- `timeout` (int): Время ожидания элемента - 0.
- `timeout_for_event` (str): Тип события для ожидания - `presence_of_element_located`.
- `event` (str): Событие для выполнения - `click()`.
- `mandatory` (bool): Локатор обязателен для использования.
- `locator_description` (str): Описание локатора - "Если было одно изображение - будет эта кнопка".

### `not_now`

**Описание**: Локатор для кнопки "Не сейчас". Ищет `span`, содержащий текст "Не сейчас".

**Параметры**:
- `attribute` (null): Атрибут элемента не указан.
- `by` (str): Способ поиска элемента - `XPATH`.
- `selector` (str): `XPATH` выражение для поиска элемента `//span[contains(text(),'Не сейчас')]`.
- `timeout` (int): Время ожидания элемента - 0.
- `timeout_for_event` (str): Тип события для ожидания - `presence_of_element_located`.
- `event` (str): Событие для выполнения - `click()`.
- `mandatory` (bool): Локатор обязателен для использования.
- `locator_description` (str): Описание локатора не указано.

### `close_pop_up`

**Описание**: Локатор для закрытия всплывающего окна. Ищет `div` с `aria-label` "Закрыть".

**Параметры**:
- `attribute` (null): Атрибут элемента не указан.
- `by` (str): Способ поиска элемента - `XPATH`.
- `selector` (str): `XPATH` выражение для поиска элемента `//div[@aria-label = 'Закрыть']`.
- `timeout` (int): Время ожидания элемента - 0.
- `timeout_for_event` (str): Тип события для ожидания - `presence_of_element_located`.
- `event` (str): Событие для выполнения - `click()`.
- `mandatory` (bool): Локатор обязателен для использования.
- `locator_description` (str): Описание локатора не указано.

### `edit_posts`

**Описание**: Локатор для кнопки "Управление публикациями". Ищет `span` с `text` "Управление публикациями".

**Параметры**:
- `attribute` (null): Атрибут элемента не указан.
- `by` (str): Способ поиска элемента - `XPATH`.
- `selector` (str): `XPATH` выражение для поиска элемента `//span[@text = 'Управление публикациями']`.
- `timeout` (int): Время ожидания элемента - 0.
- `timeout_for_event` (str): Тип события для ожидания - `presence_of_element_located`.
- `event` (str): Событие для выполнения - `click()`.
- `mandatory` (bool): Локатор обязателен для использования.
- `locator_description` (str): Описание локатора не указано.