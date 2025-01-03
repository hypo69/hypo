# Локаторы для создания события в Facebook

## Обзор

Этот файл `post_event.json` содержит JSON-структуру, определяющую локаторы веб-элементов на странице создания события в Facebook. Эти локаторы используются для автоматизации взаимодействия с веб-интерфейсом, например, для заполнения полей и отправки формы.

## Содержание

1. [event_title](#event_title)
2. [start_date](#start_date)
3. [start_time](#start_time)
4. [event_description](#event_description)
5. [event_send](#event_send)

## Локаторы

### `event_title`

**Описание**: Локатор для поля ввода названия мероприятия.

**Свойства**:
- **attribute**: `null` (атрибут не используется).
- **by**: `XPATH` (метод поиска элемента).
- **selector**: `//label[@aria-label = 'Название мероприятия']//input` (XPath-выражение для поиска поля ввода).
- **if_list**: `first` (выбирается первый найденный элемент).
- **use_mouse**: `false` (использование мыши не требуется).
- **timeout**: `0` (таймаут не установлен).
- **timeout_for_event**: `presence_of_element_located` (событие ждет появления элемента).
- **event**: `click();%EXTERNAL_MESSAGE%` (событие - клик с последующей подстановкой сообщения).
- **mandatory**: `true` (поле обязательно для заполнения).
- **locator_description**: `поле ввода названия сообщения. При переходе по специально сконструированной ссылке откроется сразу. См код сценария` (описание локатора).

### `start_date`

**Описание**: Локатор для поля ввода даты начала мероприятия.

**Свойства**:
- **attribute**: `null` (атрибут не используется).
- **by**: `XPATH` (метод поиска элемента).
- **selector**: `//label[@aria-label = 'Дата начала']//input` (XPath-выражение для поиска поля ввода).
- **if_list**: `first` (выбирается первый найденный элемент).
- **use_mouse**: `false` (использование мыши не требуется).
- **timeout**: `0` (таймаут не установлен).
- **timeout_for_event**: `presence_of_element_located` (событие ждет появления элемента).
- **event**: `click();backspace(10);%EXTERNAL_MESSAGE%` (событие - клик, удаление 10 символов и подстановка сообщения).
- **mandatory**: `true` (поле обязательно для заполнения).
- **locator_description**: `поле ввода даты начала мероприятия` (описание локатора).

### `start_time`

**Описание**: Локатор для поля ввода времени начала мероприятия.

**Свойства**:
- **attribute**: `null` (атрибут не используется).
- **by**: `XPATH` (метод поиска элемента).
- **selector**: `//label[@aria-label = 'Время начала']//input` (XPath-выражение для поиска поля ввода).
- **if_list**: `first` (выбирается первый найденный элемент).
- **use_mouse**: `false` (использование мыши не требуется).
- **timeout**: `0` (таймаут не установлен).
- **timeout_for_event**: `presence_of_element_located` (событие ждет появления элемента).
- **event**: `click();backspace();%EXTERNAL_MESSAGE%` (событие - клик, удаление символа и подстановка сообщения).
- **mandatory**: `true` (поле обязательно для заполнения).
- **locator_description**: `поле ввода даты начала мероприятия` (описание локатора).

### `event_description`

**Описание**: Локатор для поля ввода описания мероприятия.

**Свойства**:
- **attribute**: `null` (атрибут не используется).
- **by**: `XPATH` (метод поиска элемента).
- **selector**: `//label[@aria-label = 'Расскажите подробнее о мероприятии.']//textarea` (XPath-выражение для поиска поля ввода).
- **if_list**: `first` (выбирается первый найденный элемент).
- **use_mouse**: `false` (использование мыши не требуется).
- **timeout**: `0` (таймаут не установлен).
- **timeout_for_event**: `presence_of_element_located` (событие ждет появления элемента).
- **event**: `click();%EXTERNAL_MESSAGE%` (событие - клик с последующей подстановкой сообщения).
- **mandatory**: `true` (поле обязательно для заполнения).
- **locator_description**: `поле ввода даты начала мероприятия` (описание локатора).

### `event_send`

**Описание**: Локатор для кнопки отправки формы создания мероприятия.

**Свойства**:
- **attribute**: `null` (атрибут не используется).
- **by**: `XPATH` (метод поиска элемента).
- **selector**: `//div[@aria-label = 'Создать мероприятие']` (XPath-выражение для поиска кнопки).
- **if_list**: `first` (выбирается первый найденный элемент).
- **use_mouse**: `false` (использование мыши не требуется).
- **timeout**: `0` (таймаут не установлен).
- **timeout_for_event**: `presence_of_element_located` (событие ждет появления элемента).
- **event**: `click()` (событие - клик).
- **mandatory**: `true` (кнопка обязательна для нажатия).
- **locator_description**: `Кнопка отправки` (описание локатора).