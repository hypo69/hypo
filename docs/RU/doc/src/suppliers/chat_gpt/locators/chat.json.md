# Локаторы чата ChatGPT

## Обзор

Этот документ описывает JSON-файл, содержащий локаторы для элементов чата ChatGPT. Локаторы используются для идентификации элементов на веб-странице, таких как сообщения от ассистента и пользователя.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
- [Раздел "assistant"](#раздел-assistant)
- [Раздел "user"](#раздел-user)

## Структура JSON

Файл имеет следующую структуру JSON, где каждый раздел описывает локаторы для разных ролей в чате:

```json
{
  "assistant": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//div[@data-message-author-role='assistant']",
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located",
    "event": null,
    "if_list": "first",
    "use_mouse": false,
    "mandatory": true,
    "locator_description": "Я получаю весь контейнер и в коде вытескиваю .text"
  },
  "user": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//div[@data-message-author-role='user']",
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located",
    "event": null,
    "if_list": "first",
    "use_mouse": false,
    "mandatory": true,
    "locator_description": "Я получаю весь контейнер и в коде вытескиваю .text"
  }
}
```

## Раздел "assistant"

### Описание

Этот раздел содержит локаторы для сообщений, отправленных ассистентом.

**Параметры:**
*   `attribute` (null): Атрибут элемента, который нужно извлечь (в данном случае не используется).
*   `by` (str): Метод поиска элемента (`XPATH`).
*   `selector` (str): XPath-селектор для поиска элемента сообщения ассистента `//div[@data-message-author-role='assistant']`.
*   `timeout` (int): Время ожидания элемента в секундах (0 - не ожидать).
*   `timeout_for_event` (str): Событие ожидания элемента (`presence_of_element_located`).
*   `event` (null): Событие, которое нужно выполнить (не используется).
*   `if_list` (str): Условие выбора элемента из списка (`first` - первый элемент).
*   `use_mouse` (bool): Признак использования мыши (false).
*   `mandatory` (bool): Признак обязательности локатора (true).
*   `locator_description` (str): Описание локатора - "Я получаю весь контейнер и в коде вытескиваю .text".

## Раздел "user"

### Описание

Этот раздел содержит локаторы для сообщений, отправленных пользователем.

**Параметры:**
*   `attribute` (null): Атрибут элемента, который нужно извлечь (в данном случае не используется).
*   `by` (str): Метод поиска элемента (`XPATH`).
*   `selector` (str): XPath-селектор для поиска элемента сообщения пользователя `//div[@data-message-author-role='user']`.
*   `timeout` (int): Время ожидания элемента в секундах (0 - не ожидать).
*   `timeout_for_event` (str): Событие ожидания элемента (`presence_of_element_located`).
*   `event` (null): Событие, которое нужно выполнить (не используется).
*   `if_list` (str): Условие выбора элемента из списка (`first` - первый элемент).
*   `use_mouse` (bool): Признак использования мыши (false).
*   `mandatory` (bool): Признак обязательности локатора (true).
*   `locator_description` (str): Описание локатора - "Я получаю весь контейнер и в коде вытескиваю .text".