# Модуль openai.js

## Обзор

Данный модуль предоставляет класс `OpenAI`, который позволяет взаимодействовать с API OpenAI, включая чат-боты и транскрипцию аудио.

## Классы

### `OpenAI`

**Описание**: Класс для взаимодействия с API OpenAI.

**Конструктор**:

```javascript
constructor(apiKey)
```

**Описание**: Инициализирует экземпляр класса `OpenAI` с заданным API ключом.

**Параметры**:

- `apiKey` (строка): API ключ для доступа к API OpenAI.

**Методы**:

#### `chat(messages)`

**Описание**: Отправляет запрос на создание чат-ботного ответа.

**Параметры**:

- `messages` (массив объектов): Массив объектов, представляющих сообщения для чат-бота.  Каждый объект должен содержать поля `role` (например, 'user', 'assistant') и `content` (сообщение).

**Возвращает**:

- `объект` | `null`: Объект с ответом чат-бота или `null` в случае ошибки.  Объект содержит поле `message` с текстом ответа.

**Вызывает исключения**:

- `ошибка`: Выводит сообщение об ошибке при запросе.


#### `transcription(filepath)`

**Описание**: Производит транскрипцию аудио из указанного файла.

**Параметры**:

- `filepath` (строка): Путь к аудио файлу для транскрипции.

**Возвращает**:

- `строка` | `null`: Текст транскрипции или `null` в случае ошибки.

**Вызывает исключения**:

- `ошибка`: Выводит сообщение об ошибке при запросе.


## Переменные

### `openai`

**Описание**: Экземпляр класса `OpenAI`, инициализированный с API ключом из файла `config`.


```