Настройка параметров OpenAI и Azure OpenAI сервиса
========================================================================================

Описание
-------------------------
Этот файл `config.ini` содержит настройки для работы с API OpenAI или Azure OpenAI. Он определяет тип API, параметры модели, время ожидания, количество попыток и другие важные настройки. Настройки также определяют параметры для предотвращения вредного контента и нарушения авторских прав.  Он включает  опции кеширования API-вызовов и настройку уровня ведения журнала.

Шаги выполнения
-------------------------
1. **Выбор типа API**: Настройка `API_TYPE` определяет, какой API использовать: `openai` (для OpenAI) или `azure` (для Azure).
2. **Указание параметров модели**: Настройки `MODEL`, `MAX_TOKENS`, `TEMPERATURE`, `FREQ_PENALTY`, `PRESENCE_PENALTY`,  `TIMEOUT`,  `MAX_ATTEMPTS` и `WAITING_TIME`  определяют модель, максимальное количество токенов,  температуру, штрафы за частоту и присутствие, время ожидания, количество попыток и время ожидания.
3. **Указание параметров модели встраивания**: Параметр `EMBEDDING_MODEL` определяет модель, используемую для встраивания текста.
4. **Кеширование API-вызовов**: Настройка `CACHE_API_CALLS` и `CACHE_FILE_NAME` определяют, нужно ли кешировать API-вызовы и, если да, то имя файла кеша.
5. **Настройка отображения контента**: Настройка `MAX_CONTENT_DISPLAY_LENGTH` определяет максимальную длину отображаемого контента.
6. **Предотвращение вредного контента**: Настройки `RAI_HARMFUL_CONTENT_PREVENTION` и `RAI_COPYRIGHT_INFRINGEMENT_PREVENTION` включают защиту от вредного контента и нарушения авторских прав.
7. **Уровень ведения журнала**: Настройка `LOGLEVEL` определяет уровень подробности в журнале (ERROR, WARNING, INFO, DEBUG).

Пример использования
-------------------------
.. code-block:: ini

    [OpenAI]
    API_TYPE=openai
    MODEL=gpt-4o
    MAX_TOKENS=4000
    TEMPERATURE=0.3
    FREQ_PENALTY=0.0
    PRESENCE_PENALTY=0.0
    TIMEOUT=60
    MAX_ATTEMPTS=5
    WAITING_TIME=1
    EXPONENTIAL_BACKOFF_FACTOR=5
    EMBEDDING_MODEL=text-embedding-3-small
    CACHE_API_CALLS=True
    CACHE_FILE_NAME=openai_api_cache.pickle
    MAX_CONTENT_DISPLAY_LENGTH=1024
    RAI_HARMFUL_CONTENT_PREVENTION=True
    RAI_COPYRIGHT_INFRINGEMENT_PREVENTION=True
    [Logging]
    LOGLEVEL=INFO