# Модуль hypotez/src/endpoints/advertisement/facebook/scenarios/__init__.py

## Обзор

Этот модуль предоставляет функции для управления сценариями рекламы на Facebook. Он импортирует функции из различных подмодулей, позволяя организовать и использовать эти функции для работы с различными аспектами рекламных кампаний.

## Модули

### `login`

Этот модуль содержит функции для входа в аккаунт Facebook.

### `post_message`

Этот модуль содержит функции для публикации сообщений.  Он включает в себя функции для публикации заголовков, загрузки медиафайлов, обновления подписей к изображениям и публикации самих сообщений.

### `switch_account`

Этот модуль предоставляет функции для переключения между аккаунтами Facebook.

### `post_event`

Этот модуль содержит функции для публикации событий. Он включает функции для указания названия события, описания, даты и времени события, а также для публикации самого события.

### `post_ad`

Этот модуль содержит функцию для публикации объявлений.


## Переменные

### `MODE`

**Описание**: Переменная, определяющая режим работы (например, 'dev' для разработки, 'prod' для производства).

**Значение**: 'dev' по умолчанию.

## Функции

### `login`

**Описание**: Функция входа в аккаунт Facebook.


### `post_message`


**Описание**: Функция публикации сообщения.

**Возвращает**:  Возвращает результат выполнения функции публикации (dict) или None при ошибке.


### `switch_account`

**Описание**: Функция переключения аккаунтов Facebook.

**Возвращает**: Возвращает True при успешном переключении, False при ошибке.


### `post_event`


**Описание**: Функция для публикации событий.


### `post_ad`

**Описание**: Функция публикации объявления.