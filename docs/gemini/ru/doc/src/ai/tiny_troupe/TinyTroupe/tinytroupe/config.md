# Модуль config.ini

## Обзор

Этот файл содержит конфигурацию для взаимодействия с API OpenAI или Azure OpenAI. Он определяет типы API, параметры моделей, таймауты, ограничения на количество попыток и другие параметры.  Также здесь настраиваются параметры для предотвращения вредоносного и нарушающего авторские права контента.

## Параметры

### `API_TYPE`

**Описание**: Тип используемого API. Может принимать значения `openai` или `azure`.

**Значение по умолчанию**: `openai`

### `AZURE_API_VERSION`

**Описание**: Версия API Azure OpenAI.

**Значение по умолчанию**: `2023-05-15`

**Примечание**: Для получения актуальной информации по версиям API, пожалуйста, обратитесь к документации Azure OpenAI.


### `MODEL`

**Описание**: Модель OpenAI, используемая для запросов.

**Значение по умолчанию**: `gpt-4o`

### `MAX_TOKENS`

**Описание**: Максимальное количество токенов в ответе модели.

**Значение по умолчанию**: `4000`

### `TEMPERATURE`

**Описание**: Параметр температуры, влияющий на вероятность выбора модели.

**Значение по умолчанию**: `0.3`

### `FREQ_PENALTY`

**Описание**: Наказание за частоту появления токенов.

**Значение по умолчанию**: `0.0`

### `PRESENCE_PENALTY`

**Описание**: Наказание за повторение токенов.

**Значение по умолчанию**: `0.0`

### `TIMEOUT`

**Описание**: Таймаут запроса к API в секундах.

**Значение по умолчанию**: `60`

### `MAX_ATTEMPTS`

**Описание**: Максимальное количество попыток запроса к API.

**Значение по умолчанию**: `5`

### `WAITING_TIME`

**Описание**: Время ожидания между попытками запроса в секундах.

**Значение по умолчанию**: `1`

### `EXPONENTIAL_BACKOFF_FACTOR`

**Описание**: Фактор экспоненциального увеличения времени ожидания между попытками.

**Значение по умолчанию**: `5`


### `EMBEDDING_MODEL`

**Описание**: Модель для создания векторных представлений (вложений) текста.

**Значение по умолчанию**: `text-embedding-3-small`


### `CACHE_API_CALLS`

**Описание**: Флаг, определяющий, следует ли кэшировать вызовы API.

**Значение по умолчанию**: `False`

### `CACHE_FILE_NAME`

**Описание**: Имя файла для кэша API вызовов.

**Значение по умолчанию**: `openai_api_cache.pickle`


### `MAX_CONTENT_DISPLAY_LENGTH`

**Описание**: Максимальная длина отображаемого содержимого в символах.

**Значение по умолчанию**: `1024`

## Раздел [Simulation]

### `RAI_HARMFUL_CONTENT_PREVENTION`

**Описание**: Включить или выключить предотвращение вредоносного контента.

**Значение по умолчанию**: `True`


### `RAI_COPYRIGHT_INFRINGEMENT_PREVENTION`

**Описание**: Включить или выключить предотвращение нарушения авторских прав.

**Значение по умолчанию**: `True`


## Раздел [Logging]

### `LOGLEVEL`

**Описание**: Уровень ведения журнала.

**Допустимые значения**: `ERROR`, `WARNING`, `INFO`, `DEBUG`

**Значение по умолчанию**: `ERROR`