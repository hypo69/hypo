# Модуль config.ini

## Обзор

Данный файл (`config.ini`) содержит конфигурационные параметры для работы с API OpenAI или Azure OpenAI.  В нём определены типы API, версии, модели, параметры запросов и другие настройки.

## Параметры

### `API_TYPE`

**Описание**:  Тип API, используемый для взаимодействия с OpenAI (по умолчанию `openai`).  Возможно использование `azure`.

**Значение**: `openai` или `azure`.

### `AZURE_API_VERSION`

**Описание**: Версия API Azure OpenAI.  Указывает на спецификацию API.

**Значение**: Строка, представляющая версию API (в примере `2023-05-15`).

### `MODEL`

**Описание**:  Модель OpenAI, используемая для обработки запросов.

**Значение**: Строка, представляющая имя модели (в примере `gpt-4o`).

### `MAX_TOKENS`

**Описание**: Максимальное количество токенов в ответе модели.

**Значение**: Целое число.

### `TEMPERATURE`

**Описание**:  Параметр, влияющий на вероятность выбора наиболее вероятного варианта ответа. Значение от 0 до 1.

**Значение**: Число с плавающей точкой.

### `FREQ_PENALTY`

**Описание**:  Штраф за частоту повторения слов.

**Значение**: Число с плавающей точкой.

### `PRESENCE_PENALTY`

**Описание**: Штраф за повторение последовательностей слов.

**Значение**: Число с плавающей точкой.

### `TIMEOUT`

**Описание**:  Таймаут для выполнения запросов к API, в секундах.

**Значение**: Целое число.

### `MAX_ATTEMPTS`

**Описание**: Максимальное количество попыток запроса к API.

**Значение**: Целое число.

### `WAITING_TIME`

**Описание**: Время ожидания между попытками запроса, в секундах.

**Значение**: Целое число.

### `EXPONENTIAL_BACKOFF_FACTOR`

**Описание**: Множитель для экспоненциального увеличения времени ожидания между попытками при ошибках.

**Значение**: Целое число.

### `EMBEDDING_MODEL`

**Описание**: Модель для создания векторных представлений текста.

**Значение**: Строка, представляющая имя модели (в примере `text-embedding-3-small`).

### `CACHE_API_CALLS`

**Описание**: Флаг, определяющий, использовать ли кэш для ответов API.

**Значение**: Булево значение (`True` или `False`).

### `CACHE_FILE_NAME`

**Описание**: Имя файла для кеширования ответов API.

**Значение**: Строка.

### `MAX_CONTENT_DISPLAY_LENGTH`

**Описание**: Максимальная длина текста для отображения (в символах).

**Значение**: Целое число.

### `RAI_HARMFUL_CONTENT_PREVENTION`

**Описание**:  Флаг, определяющий включение фильтрации вредного контента.

**Значение**: Булево значение (`True` или `False`).

### `RAI_COPYRIGHT_INFRINGEMENT_PREVENTION`

**Описание**: Флаг, определяющий включение фильтрации нарушений авторских прав.

**Значение**: Булево значение (`True` или `False`).

### `LOGLEVEL`

**Описание**: Уровень ведения журнала.

**Значение**: Строка (`ERROR`, `WARNING`, `INFO`, `DEBUG`).