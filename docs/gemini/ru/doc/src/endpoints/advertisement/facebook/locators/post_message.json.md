# Локаторы для работы с постами в Facebook

## Обзор

Этот файл содержит JSON-конфигурацию с локаторами элементов для работы с постами в Facebook. Каждый локатор описан с использованием XPath и содержит информацию о типе элемента, действии и других параметрах, необходимых для автоматизации взаимодействия с веб-интерфейсом.

## Оглавление

- [Локаторы](#locators)
    - [`open_add_post_box`](#open_add_post_box)
    - [`add_message`](#add_message)
    - [`open_add_foto_video_form`](#open_add_foto_video_form)
    - [`foto_video_input`](#foto_video_input)
    - [`edit_uloaded_media_button`](#edit_uloaded_media_button)
    - [`uploaded_media_frame`](#uploaded_media_frame)
    - [`edit_image_properties_textarea`](#edit_image_properties_textarea)
    - [`finish_editing_button`](#finish_editing_button)
    - [`publish`](#publish)
    - [`send`](#send)
    - [`not_now`](#not_now)
    - [`close_pop_up`](#close_pop_up)
    - [`edit_posts`](#edit_posts)

## Локаторы

### `open_add_post_box`

**Описание**: Локатор для открытия окна ввода сообщения.

**Параметры**:
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//span[contains(text(), \'Что у вас нового\') or contains(text(), \'Напишите что-нибудь...\')]"`
- `if_list`: `"first"`
- `use_mouse`: `false`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"click()"`
- `mandatory`: `true`
- `locator_description`: `"открытие окна для ввода сообщения, пауза, отправка сообщения"`

### `add_message`

**Описание**: Локатор для ввода сообщения в текстовое поле.

**Параметры**:
- `attribute`: `"None"`
- `by`: `"XPATH"`
- `selector`: `"(//div[@role=\'textbox\'])[last()]"`
- `if_list`: `"first"`
- `use_mouse`: `"None"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"pause(1);%EXTERNAL_MESSAGE%"`
- `mandatory`: `"True"`
- `locator_description`: `"через \`execute_locator()\` будет передан текст"`
- `deprecated`: `"используется \`open_add_post_box\`"`

### `open_add_foto_video_form`

**Описание**: Локатор для открытия формы загрузки фото/видео.

**Параметры**:
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//div[@aria-label=\'Фото/видео\']"`
- `if_list`: `"first"`
- `use_mouse`: `true`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"click()"`
- `mandatory`: `true`
- `locator_description`: `"Нажать для меню загрузки видео"`

### `foto_video_input`

**Описание**: Локатор для поля загрузки медиафайлов.

**Параметры**:
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//div[@role=\'dialog\']//input[@type = \'file\']"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"upload_media()"`
- `mandatory`: `true`
- `locator_description`: `"Загрузка медиа, Путь к файлу передается через код сценария "`

### `edit_uloaded_media_button`

**Описание**: Локатор для кнопки редактирования загруженных медиа.

**Параметры**:
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//div[@role=\'button\' and contains(@aria-label,\'Редактировать всё\')]"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"click()"`
- `mandatory`: `true`
- `locator_description`: `"Открывает поля описаний для загруженных медиафайлов"`

### `uploaded_media_frame`

**Описание**: Локатор для фрейма с загруженными медиа для редактирования.

**Параметры**:
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//div[@aria-label=\'Фото/видео\']"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`
- `mandatory`: `true`
- `locator_description`: `"Попап с открытыми медиа для редакции"`

### `edit_image_properties_textarea`

**Описание**: Локатор для текстового поля описания медиафайла.

**Параметры**:
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//textarea"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`
- `mandatory`: `true`
- `locator_description`: `"Текстовые поля для описания к медиафайлу"`

### `finish_editing_button`

**Описание**: Локатор для кнопки завершения редактирования медиа.

**Параметры**:
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//span[contains(text(),\'Готово\')]"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"click()"`
- `mandatory`: `true`
- `locator_description`: `"Закрытие окна загрузки фото и описаний"`

### `publish`

**Описание**: Локатор для кнопки публикации поста.

**Параметры**:
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//div[@aria-label=\'Опубликовать\' or @aria-label=\'Отправить\' or @aria-label=\'Далее\']"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"click()"`
- `mandatory`: `true`
- `locator_description`: `"Закрытие окна загрузки фото и описаний"`

### `send`

**Описание**: Локатор для кнопки отправки поста (если только одно изображение).

**Параметры**:
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"(//span[contains(text(),\'Отправить\')])[last()]"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"click()"`
- `mandatory`: `true`
- `locator_description`: `"Если было одно изображение - будет эта кнопка"`

### `not_now`

**Описание**: Локатор для кнопки "Не сейчас" во всплывающих окнах.

**Параметры**:
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//span[contains(text(),\'Не сейчас\')]"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"click()"`
- `mandatory`: `true`

### `close_pop_up`

**Описание**: Локатор для кнопки закрытия всплывающих окон.

**Параметры**:
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//div[@aria-label = \'Закрыть\']"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"click()"`
- `mandatory`: `true`

### `edit_posts`

**Описание**: Локатор для кнопки перехода к управлению публикациями.

**Параметры**:
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//span[@text = \'Управление публикациями\']"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"click()"`
- `mandatory`: `true`