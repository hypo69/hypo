# Документация для `affiliate_links_shortener.json`

## Обзор

Данный файл `affiliate_links_shortener.json` содержит JSON-объект с локаторами для элементов веб-страницы, используемой для сокращения партнерских ссылок AliExpress. Локаторы определяют, как программно взаимодействовать с элементами на странице, такими как поля ввода, кнопки и текстовые области. Каждый локатор включает информацию о способе поиска элемента (например, XPATH), его селекторе, поведении и других свойствах.

## Содержание

- [Обзор](#обзор)
- [Локаторы](#локаторы)
    - [`textarea_target_url`](#textarea_target_url)
    - [`button_get_tracking_link`](#button_get_tracking_link)
    - [`textarea_short_link`](#textarea_short_link)

## Локаторы

### `textarea_target_url`

**Описание**: Локатор для текстового поля, в которое вводится полная ссылка для сокращения.

**Свойства**:
- `attribute`: `false` (не используется атрибут элемента).
- `by`: `XPATH` (метод поиска элемента).
- `selector`: `//textarea[@id = 'targetUrl']` (XPATH-выражение для поиска элемента).
- `if_list`: `first` (выбрать первый элемент, если найдено несколько).
- `use_mouse`: `false` (не использовать мышь для взаимодействия).
- `timeout`: `0` (таймаут не установлен).
- `timeout_for_event`: `presence_of_element_located` (ожидать присутствие элемента перед событием).
- `event`: `clear();%EXTERNAL_MESSAGE%` (событие для элемента: очистка и отправка внешнего сообщения).
- `mandatory`: `true` (локатор является обязательным).
- `locator_description`: `Full link input box` (описание локатора).

### `button_get_tracking_link`

**Описание**: Локатор для кнопки, которая запускает процесс сокращения ссылки.

**Свойства**:
- `attribute`: `false` (не используется атрибут элемента).
- `by`: `XPATH` (метод поиска элемента).
- `selector`: `//button[contains(@class, 'link-form-submit')]` (XPATH-выражение для поиска кнопки).
- `if_list`: `first` (выбрать первый элемент, если найдено несколько).
- `use_mouse`: `false` (не использовать мышь для взаимодействия).
- `timeout`: `0` (таймаут не установлен).
- `timeout_for_event`: `presence_of_element_located` (ожидать присутствие элемента перед событием).
- `event`: `click()` (событие для элемента: клик).
- `mandatory`: `true` (локатор является обязательным).
- `locator_description`: `Send form button` (описание локатора).

### `textarea_short_link`

**Описание**: Локатор для текстового поля, в котором отображается сокращенная ссылка.

**Свойства**:
- `attribute`: `value` (использовать атрибут 'value' для извлечения текста).
- `by`: `XPATH` (метод поиска элемента).
- `selector`: `//form[contains(@class, 'link-form-text')]//textarea` (XPATH-выражение для поиска текстовой области).
- `if_list`: `first` (выбрать первый элемент, если найдено несколько).
- `use_mouse`: `false` (не использовать мышь для взаимодействия).
- `timeout`: `0` (таймаут не установлен).
- `timeout_for_event`: `presence_of_element_located` (ожидать присутствие элемента перед событием).
- `event`: `false` (событие не определено).
- `mandatory`: `true` (локатор является обязательным).
- `locator_description`: `Send form button` (описание локатора).