# Модуль `validation.py`

## Обзор

Модуль `validation.py` содержит класс `TinyPersonValidator` для валидации экземпляров `TinyPerson` с использованием OpenAI LLM.  Он задает вопросы `TinyPerson` через чат-ботовую сессию, анализируя ответы и возвращая оценку доверия.

## Классы

### `TinyPersonValidator`

**Описание**: Класс для валидации экземпляров `TinyPerson`.

**Методы**

#### `validate_person`

**Описание**:  Проводит валидацию `TinyPerson` с использованием OpenAI LLM.

**Параметры**:

- `person` (TinyPerson): Экземпляр `TinyPerson`, подлежащий валидации.
- `expectations` (str, необязательно): Критерии для валидации. По умолчанию `None`.
- `include_agent_spec` (bool, необязательно): Включать ли спецификацию агента в запрос. По умолчанию `True`.
- `max_content_length` (int, необязательно): Максимальная длина контента, отображаемого при рендеринге диалога. По умолчанию `default_max_content_display_length`.

**Возвращает**:

- `float`: Оценка доверия (от 0.0 до 1.0). `None`, если валидация не удалась.
- `str`: Обоснование оценки доверия. `None`, если валидация не удалась.

**Обрабатываемые исключения**:

- Любые исключения, которые могут быть вызваны методами `openai_utils.client().send_message()` или `person.listen_and_act()`.
- Возможные исключения, возникающие при работе с файлом `prompts/check_person.mustache` или при парсинге JSON.



## Переменные

### `default_max_content_display_length`

**Описание**:  Максимальная длина контента для отображения в процессе диалога. Значение задается конфигурацией из файла `config.ini` (раздел `OpenAI`, опция `MAX_CONTENT_DISPLAY_LENGTH`).


## Подключаемые модули

- `os`
- `json`
- `chevron`
- `logging`
- `tinytroupe.openai_utils`
- `tinytroupe.agent`
- `tinytroupe.config`
- `tinytroupe.utils`