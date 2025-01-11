# Файл конфигурации TinyTroupe

## Обзор

Данный файл (`config.ini`) содержит настройки для интеграции с сервисами OpenAI или Azure OpenAI. Он определяет тип API, параметры модели, ограничения времени, обработку ошибок и другие важные конфигурационные параметры.


## Параметры

### `API_TYPE`

**Описание**: Тип API, используемый для взаимодействия с OpenAI или Azure OpenAI.

**Возможные значения**: `openai`, `azure`.

**Значение по умолчанию**: `openai`.


### `AZURE_API_VERSION`

**Описание**: Версия API Azure OpenAI.


**Значение по умолчанию**: `2023-05-15`.  *Обратите внимание на ссылку в файле конфигурации для получения актуальной информации.*


### `MODEL`

**Описание**: Модель OpenAI, которая будет использоваться для обработки запросов.

**Значение по умолчанию**: `gpt-4o`.


### `MAX_TOKENS`

**Описание**: Максимальное количество токенов, которое может быть использовано моделью для ответа.

**Значение по умолчанию**: `4000`.


### `TEMPERATURE`

**Описание**: Параметр, влияющий на случайность генерируемого текста. Значение от 0 до 1.

**Значение по умолчанию**: `0.3`.


### `FREQ_PENALTY`

**Описание**: Штраф за повторение часто встречающихся токенов.

**Значение по умолчанию**: `0.0`.


### `PRESENCE_PENALTY`

**Описание**: Штраф за повторение ранее использованных токенов.

**Значение по умолчанию**: `0.0`.


### `TIMEOUT`

**Описание**: Максимальное время ожидания ответа от сервиса OpenAI, в секундах.

**Значение по умолчанию**: `60`.


### `MAX_ATTEMPTS`

**Описание**: Максимальное количество попыток запроса к сервису OpenAI в случае ошибки.

**Значение по умолчанию**: `5`.


### `WAITING_TIME`

**Описание**: Время ожидания между повторными попытками, в секундах, для экспоненциального возврата.

**Значение по умолчанию**: `1`.


### `EXPONENTIAL_BACKOFF_FACTOR`

**Описание**: Множитель для экспоненциального увеличения времени ожидания при повторных неудачах.

**Значение по умолчанию**: `5`.


### `EMBEDDING_MODEL`

**Описание**: Модель для создания встраиваний текстов.

**Значение по умолчанию**: `text-embedding-3-small`.


### `CACHE_API_CALLS`

**Описание**: Флаг, определяющий, нужно ли кэшировать вызовы API.

**Значение по умолчанию**: `False`.


### `CACHE_FILE_NAME`

**Описание**: Имя файла для кэширования вызовов API.

**Значение по умолчанию**: `openai_api_cache.pickle`.


### `MAX_CONTENT_DISPLAY_LENGTH`

**Описание**: Максимальная длина выводимого контента, в символах.

**Значение по умолчанию**: `1024`.


### `RAI_HARMFUL_CONTENT_PREVENTION`

**Описание**: Включить ли защиту от вредного контента.

**Значение по умолчанию**: `True`.


### `RAI_COPYRIGHT_INFRINGEMENT_PREVENTION`

**Описание**: Включить ли защиту от нарушения авторских прав.

**Значение по умолчанию**: `True`.


### `LOGLEVEL`

**Описание**: Уровень ведения журнала.


**Возможные значения**: `ERROR`, `WARNING`, `INFO`, `DEBUG`.

**Значение по умолчанию**: `ERROR`.

## Оглавление

* [Файл конфигурации TinyTroupe](#файл-конфигурации-tinytroupe)
* [Обзор](#обзор)
* [Параметры](#параметры)
    * [API_TYPE](#api_type)
    * [AZURE_API_VERSION](#azure_api_version)
    * [MODEL](#model)
    * [MAX_TOKENS](#max_tokens)
    * [TEMPERATURE](#temperature)
    * [FREQ_PENALTY](#freq_penalty)
    * [PRESENCE_PENALTY](#presence_penalty)
    * [TIMEOUT](#timeout)
    * [MAX_ATTEMPTS](#max_attempts)
    * [WAITING_TIME](#waiting_time)
    * [EXPONENTIAL_BACKOFF_FACTOR](#exponential_backoff_factor)
    * [EMBEDDING_MODEL](#embedding_model)
    * [CACHE_API_CALLS](#cache_api_calls)
    * [CACHE_FILE_NAME](#cache_file_name)
    * [MAX_CONTENT_DISPLAY_LENGTH](#max_content_display_length)
    * [RAI_HARMFUL_CONTENT_PREVENTION](#rai_harmful_content_prevention)
    * [RAI_COPYRIGHT_INFRINGEMENT_PREVENTION](#rai_copyright_infringement_prevention)
    * [LOGLEVEL](#loglevel)