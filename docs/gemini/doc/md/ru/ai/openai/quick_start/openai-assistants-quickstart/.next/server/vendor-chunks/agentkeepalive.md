```markdown
# Модуль agentkeepalive

## Обзор

Данный модуль предоставляет расширенный класс `Agent` для работы с HTTP-агентами. Он улучшает работу с keep-alive, управляет таймаутами и другими параметрами для повышения производительности и стабильности приложений, работающих с HTTP-соединениями. Модуль содержит классы `Agent`, `HttpsAgent` и константы для управления соединениями.

## Оглавление

* [Модуль agentkeepalive](#модуль-agentkeepalive)
* [Обзор](#обзор)
* [Классы](#классы)
    * [`Agent`](#agent)
    * [`HttpsAgent`](#httpsagent)
* [Функции](#функции)
    * [`(rsc)/./node_modules/agentkeepalive/index.js`](#rsc-node_modulesagentkeepaliveindexjs)

## Классы

### `Agent`

**Описание**: Класс `Agent` расширяет базовый класс `http.Agent`, предоставляя расширенные возможности для управления соединениями.  Реализует keep-alive механизм, позволяет настраивать таймауты и обрабатывает исключения при работе с сокетами.

**Методы**:
- `constructor(options)`: Конструктор класса `Agent`. Настраивает параметры агента, включая keepAlive, freeSocketTimeout, timeout. Поддерживает человекочитаемые форматы таймаутов (`humanize-ms`).
- `calcSocketTimeout(socket)`: Вычисляет таймаут для сокета на основе настроек `freeSocketTimeout` и `socketActiveTTL`.
- `keepSocketAlive(socket)`:  Управляет keep-alive для сокета, учитывая настраиваемые таймауты.
- `reuseSocket(socket, req)`: Переиспользует сокет для нового запроса.
- `[CREATE_ID]()`: Генерирует уникальный идентификатор для сокета.
- `[INIT_SOCKET](socket, options)`: Инициализирует сокет с опциями. Добавляет слушатели событий для работы с таймаутами, ошибками и закрытием сокета.
- `createConnection(options, oncreate)`: Создает новое соединение.
- `get statusChanged()`: Проверяет, изменились ли параметры агента.
- `getCurrentStatus()`: Возвращает текущий статус агента.

### `HttpsAgent`

**Описание**: Класс `HttpsAgent` расширяет `Agent` для работы с HTTPS-соединениями. Наследуется от `http.Agent`.

**Методы**:
- `constructor(options)`: Конструктор класса `HttpsAgent`.
- `createConnection(options, oncreate)`: Создает новое HTTPS-соединение.


## Функции

### `(rsc)/./node_modules/agentkeepalive/index.js`

**Описание**: Экспортирует классы `Agent`, `HttpsAgent` и константы из соответствующих файлов.

**Возвращает**:
- `module.exports`: Объект, содержащий классы `Agent` и `HttpsAgent`, а также константы.


```
```
