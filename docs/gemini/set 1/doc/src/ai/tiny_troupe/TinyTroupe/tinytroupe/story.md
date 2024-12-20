# Модуль `tinytroupe.story`

## Обзор

Этот модуль предоставляет инструменты для создания историй, связанных с симуляциями в TinyTroupe. Он позволяет описывать среду, агента или их взаимодействие, используя заданный контекст и цели.

## Классы

### `TinyStory`

**Описание**: Класс `TinyStory` предназначен для создания и управления историями, связанными с симуляциями. Он поддерживает описание среды, агента и заданную цель для генерации истории.

**Методы**:

- `__init__`: Инициализирует объект `TinyStory`.
- `start_story`: Запускает создание новой истории.
- `continue_story`: Продолжает уже начатую историю.
- `_current_story`: Возвращает текущее состояние истории.

**Параметры**:

- `environment` (TinyWorld, необязательно): Объект, представляющий среду симуляции. Должен быть указан либо `environment`, либо `agent`, но не оба одновременно.
- `agent` (TinyPerson, необязательно): Объект, представляющий агента в симуляции. Должен быть указан либо `environment`, либо `agent`, но не оба одновременно.
- `purpose` (str, необязательно): Цель или описание симуляции (по умолчанию "Be a realistic simulation.").
- `context` (str, необязательно): Текущий контекст истории (по умолчанию пустая строка).
- `first_n` (int, необязательно): Количество первых взаимодействий для включения в историю (по умолчанию 10).
- `last_n` (int, необязательно): Количество последних взаимодействий для включения в историю (по умолчанию 20).
- `include_omission_info` (bool, необязательно): Включать ли информацию об опущенных взаимодействиях (по умолчанию True).
- `requirements` (str, необязательно): Дополнительные требования к истории.
- `number_of_words` (int, необязательно): Желаемое количество слов в истории.
- `include_plot_twist` (bool, необязательно): Включать ли сюжетный твист в историю.

**Возвращает**:

- `__init__`: `None`
- `start_story`: Начальный текст истории (str).
- `continue_story`: Продолжение истории (str).
- `_current_story`: Текущее состояние истории (str).

**Вызывает исключения**:

- `Exception`: Если ни `environment`, ни `agent` не были указаны.
- `Exception`: Если одновременно указаны `environment` и `agent`.



## Функции

(Нет функций в этом модуле)