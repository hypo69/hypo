# Модуль openai.js

## Обзор

Данный модуль предоставляет класс `OpenAI`, позволяющий взаимодействовать с API OpenAI.  Он содержит методы для создания диалоговых сессий (`chat`) и транскрибирования аудио (`transcription`).

## Оглавление

* [OpenAI](#openai)
    * [chat](#chat)
    * [transcription](#transcription)


## Классы

### `OpenAI`

**Описание**: Класс `OpenAI` предназначен для работы с API OpenAI. Он инициализируется API ключом и предоставляет методы для создания диалоговых сессий и транскрибирования аудио.

**Атрибуты**:

- `roles`: Объект, содержащий типы ролей для сообщений в чате (ASSISTANT, USER, SYSTEM).


**Методы**:

#### `constructor(apiKey)`

**Описание**: Конструктор класса `OpenAI`. Инициализирует экземпляр `OpenAIApi` с заданным API ключом.

**Параметры**:

- `apiKey` (строка): API ключ для доступа к OpenAI.

#### `chat(messages)`

**Описание**: Метод для создания диалоговой сессии с OpenAI.

**Параметры**:

- `messages` (массив): Массив объектов, каждый из которых содержит роль и текст сообщения в формате `{ role: string, content: string }`.

**Возвращает**:

- `dict | null`: Словарь с ответом от API OpenAI или `null`, если произошла ошибка.

**Вызывает исключения**:

- `Error`: Любые ошибки, возникающие при взаимодействии с API OpenAI.


#### `transcription(filepath)`

**Описание**: Метод для транскрибирования аудио из файла.

**Параметры**:

- `filepath` (строка): Путь к файлу аудио.

**Возвращает**:

- `string | null`: Текст транскрипции или `null`, если произошла ошибка.

**Вызывает исключения**:

- `Error`: Любые ошибки, возникающие при взаимодействии с API OpenAI или чтении файла.


## Переменные

### `openai`

**Описание**: Экземпляр класса `OpenAI`, инициализированный с API ключом из файла `config`.


```javascript