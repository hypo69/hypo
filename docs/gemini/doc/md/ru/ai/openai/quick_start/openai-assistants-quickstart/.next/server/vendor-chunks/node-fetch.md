```markdown
# Модуль node-fetch

## Обзор

Этот модуль предоставляет интерфейс для работы с HTTP запросами в Node.js, используя API Fetch.  Он предоставляет классы `Request`, `Response`, `Headers`, а также обработку ошибок и исключений.

## Оглавление

- [Классы](#классы)
    - [`AbortError`](#aborterror)
    - [`FetchError`](#fetcherror)
    - [`Headers`](#headers)
    - [`Request`](#request)
    - [`Response`](#response)
    - [`Blob`](#blob)
- [Функции](#функции)
    - [`fetch`](#fetch)
    - [`getNodeRequestOptions`](#getnoderequestoptions)
    - [`extractContentType`](#extractcontenttype)
    - [`getTotalBytes`](#gettotalbytes)
    - [`writeToStream`](#writetostream)
    - [`convertBody`](#convertbody)
    - [`isURLSearchParams`](#isurlsearchparams)
    - [`isBlob`](#isblob)
    - [`clone`](#clone)
    - [`fixResponseChunkedTransferBadEnding`](#fixresponsechunkedtransferbadending)
    - [`destroyStream`](#destroystream)
    - [`isDomainOrSubdomain`](#isdomainorsubdomain)
    - [`isSameProtocol`](#issameprotocol)


## Классы

### `AbortError`

**Описание**: Класс представляет ошибку, возникающую при прерывании запроса.

**Конструктор**:
```python
AbortError(message: str)
```

**Описание**: Создаёт новый экземпляр `AbortError` с указанным сообщением об ошибке.


### `FetchError`

**Описание**: Класс представляет собой базовый класс для ошибок, возникающих при работе с запросами Fetch.


**Конструктор**:
```python
FetchError(message: str, type: str, systemError: Optional[str] = None)
```


**Описание**: Создаёт новый экземпляр `FetchError` с указанным сообщением об ошибке, типом ошибки и (необязательным) системным кодом ошибки.


### `Headers`

**Описание**: Класс для работы с заголовками HTTP.  Он предоставляет методы для добавления, получения и удаления заголовков.


**Конструктор**:
```python
Headers(headers: Optional[dict | Iterable])
```

**Описание**: Создает новый экземпляр `Headers`. Принимает необязательный объект `headers` (словарь или итерируемый объект) для инициализации заголовков.

**Методы**:
- `get(name: str) -> str | None`: Возвращает значение заголовка с указанным именем.
- `forEach(callback: Callable, thisArg: Optional[Any] = None) -> None`: Итерирует по всем заголовкам.
- `set(name: str, value: str) -> None`: Задает значение заголовка.
- `append(name: str, value: str) -> None`: Добавляет значение заголовка.
- `has(name: str) -> bool`: Проверяет существование заголовка.
- `delete(name: str) -> None`: Удаляет заголовок.
- `raw() -> dict`: Возвращает заголовки в виде объекта.
- `keys()`: Возвращает итератор по именам заголовков.
- `values()`: Возвращает итератор по значениям заголовков.
- `[Symbol.iterator]()`: Возвращает итератор по парам имя-значение заголовков.


### `Request`

**Описание**: Представляет HTTP запрос.

**Конструктор**:
```python
Request(url: Union[str, Request], init?: Object)
```
**Описание**: Создаёт новый экземпляр `Request` с указанным URL или экземпляром `Request`, и (необязательными) опциями.


### `Response`

**Описание**: Представляет HTTP ответ.

**Конструктор**:
```python
Response(body: Optional[Stream], opts: Object)
```

**Описание**: Создает новый экземпляр `Response`, принимая body и опции.



### `Blob`

**Описание**: Представляет собой фрагмент данных, часто используемый для работы с файлами.

**Конструктор**:
```python
Blob(blobParts: Optional[Array], opts: Optional[Object])
```

**Описание**: Создаёт новый экземпляр `Blob`.  Принимает массив `blobParts` с данными и опции `opts`.

**Свойства**:
- `size`: Размер объекта Blob.
- `type`: Тип объекта Blob.
- `slice()`: Метод для создания фрагмента из объекта Blob.

**Методы**:
- `text()`: Возвращает промис, содержащий текст объекта Blob.
- `arrayBuffer()`: Возвращает промис, содержащий ArrayBuffer объект Blob.
- `stream()`: Возвращает объект Readable Stream, представляющий объект Blob.


## Функции

### `fetch`

**Описание**:  Асинхронная функция для выполнения HTTP запросов.

**Параметры**:
- `url` (Union[str, Request]): URL или объект Request.
- `opts` (Object): Опции запроса.


**Возвращает**: Промис, содержащий объект Response.

### `getNodeRequestOptions`

**Описание**: Преобразует объект `Request` в объект, подходящий для использования с `http.request` в Node.js.

### `extractContentType`

**Описание**: Извлекает тип содержимого из объекта `body`.

### `getTotalBytes`

**Описание**:  Получает общее количество байтов для объекта Body.

### `writeToStream`

**Описание**: Записывает объект Body в поток Writable.

### `convertBody`

**Описание**: Преобразует буфер в текст с автоматическим определением кодировки.


### `isURLSearchParams`

**Описание**: Проверяет, является ли объект экземпляром `URLSearchParams`.

### `isBlob`

**Описание**: Проверяет, является ли объект экземпляром `Blob`.

### `clone`

**Описание**: Создает копию объекта Response или Request.

### `fixResponseChunkedTransferBadEnding`

**Описание**:  Решает потенциальную проблему с некорректным завершением запроса с кодировкой chunked.

### `destroyStream`

**Описание**: Метод для разрушения потока.


### `isDomainOrSubdomain`

**Описание**:  Проверяет, является ли домен поддоменом.

### `isSameProtocol`

**Описание**: Проверяет, используют ли URL одинаковый протокол.


```
```
