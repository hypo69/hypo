# Модуль config.ini

## Обзор

Этот файл содержит конфигурацию для взаимодействия с API OpenAI или Azure OpenAI, включая параметры модели, таймауты, ограничения и параметры кэширования.  Он также содержит параметры для предотвращения вредоносного и нарушающего авторские права контента, а также для логирования.


## Параметры

### `API_TYPE`

**Описание**: Тип используемого API.  Допустимые значения: `openai`, `azure`. По умолчанию `openai`.

**Возможные значения**:
- `openai`
- `azure`


### `AZURE_API_VERSION`

**Описание**: Версия API Azure OpenAI.  Необходимо обновлять в соответствии с актуальной документацией. По умолчанию `2023-05-15`.

**Примечание**:  Для использования `azure` API_TYPE, необходимо установить соответствующие библиотеки и настроить Azure OpenAI.


### `MODEL`

**Описание**: Идентификатор модели OpenAI для использования. По умолчанию `gpt-4o`.

**Возможные значения**: Список поддерживаемых моделей OpenAI.


### `MAX_TOKENS`

**Описание**: Максимальное количество токенов для запроса. По умолчанию `4000`.


### `TEMPERATURE`

**Описание**: Параметр температуры для генерации текста.  Влияет на случайность и разнообразие результата. По умолчанию `0.3`.


### `FREQ_PENALTY`

**Описание**: Наказание за частоту слов.  Уменьшает повторение слов в ответе. По умолчанию `0.0`.


### `PRESENCE_PENALTY`

**Описание**: Наказание за присутствие слов. Уменьшает повторение фрагментов текста. По умолчанию `0.0`.


### `TIMEOUT`

**Описание**: Таймаут для запроса в секундах. По умолчанию `60`.


### `MAX_ATTEMPTS`

**Описание**: Максимальное количество попыток запроса. По умолчанию `5`.


### `WAITING_TIME`

**Описание**: Время ожидания между попытками запроса в секундах. По умолчанию `1`.


### `EXPONENTIAL_BACKOFF_FACTOR`

**Описание**: Фактор экспоненциальной задержки для повторных попыток. По умолчанию `5`.


### `EMBEDDING_MODEL`

**Описание**: Модель для встраивания текстовых данных. По умолчанию `text-embedding-3-small`.


### `CACHE_API_CALLS`

**Описание**: Флаг включения кэширования вызовов API. По умолчанию `False`.


### `CACHE_FILE_NAME`

**Описание**: Имя файла для кэша вызовов API. По умолчанию `openai_api_cache.pickle`.


### `MAX_CONTENT_DISPLAY_LENGTH`

**Описание**: Максимальная длина отображаемого контента. По умолчанию `1024` символов.


### `RAI_HARMFUL_CONTENT_PREVENTION`

**Описание**: Включить предотвращение вредоносного контента. По умолчанию `True`.


### `RAI_COPYRIGHT_INFRINGEMENT_PREVENTION`

**Описание**: Включить предотвращение нарушения авторских прав. По умолчанию `True`.


### `LOGLEVEL`

**Описание**: Уровень ведения журнала. По умолчанию `ERROR`. Возможные значения: `ERROR`, `WARNING`, `INFO`, `DEBUG`.


## Ошибки (Raises)


Этот файл не предусматривает каких-либо специфических ошибок.  Возможные ошибки будут возникать при работе с API OpenAI или Azure OpenAI, в зависимости от используемого API.