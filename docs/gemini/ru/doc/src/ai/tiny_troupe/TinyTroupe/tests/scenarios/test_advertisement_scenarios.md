# Модуль `test_advertisement_scenarios.py`

## Обзор

Этот модуль содержит тесты сценариев, связанных с рекламой.  Он проверяет, как агенты (TinyPerson) реагируют на различные объявления о путешествиях и как они выбирают лучшие варианты. Также включает сценарий фокус-группы по рекламе квартиры и сценарий потребительского профилирования для оценки спроса на гаспачо.

## Тесты

### `test_ad_evaluation_scenario`

**Описание**: Тест проверяет способность агентов оценивать объявления и выбирать наиболее привлекательный вариант, предоставляя обоснование своего выбора.

**Параметры**:
- `setup`: Набор данных и конфигурации для запуска теста.

**Возвращает**:
- Нет явного возвращаемого значения. Тест проверяет корректность результатов и не возвращает значение.

**Вызывает исключения**:
- `AssertionError`: Возникает, если результаты агентов не соответствуют ожидаемым значениям (например, выбран неверный номер объявления, отсутствует необходимая информация).


### `test_ad_creation_scenario`

**Описание**: Тест сценария фокус-группы по созданию рекламы для аренды квартиры.

**Параметры**:
- `setup`: Набор данных и конфигурации для запуска теста.
- `focus_group_world`: Объект, представляющий фокус-группу.

**Возвращает**:
- Нет явного возвращаемого значения. Тест проверяет наличие предложений по рекламе квартиры.

**Вызывает исключения**:
- `AssertionError`: Возникает, если результат фокус-группы не соответствует ожидаемому содержанию.


### `test_consumer_profiling_scenario`

**Описание**: Тест сценария потребительского профилирования для оценки спроса на гаспачо.

**Параметры**:
- `setup`: Набор данных и конфигурации для запуска теста.

**Возвращает**:
- Нет явного возвращаемого значения. Тест проверяет создание и обработку профилей потребителей и создание файла чекпоинта.

**Вызывает исключения**:
- `AssertionError`: Возникает, если файл чекпоинта не был создан.



## Вспомогательные функции (в других модулях)

Этот модуль использует функции из других модулей, которые не описаны здесь.  Их документация доступна в соответствующих модулях.


## Структура

- Импорты необходимых библиотек и классов.
- Определены константы для тестовых данных (тексты объявлений, описание ситуации).
- Определены тестовые функции для каждого сценария.
- Использование `ResultsExtractor` для извлечения результатов от агентов.
- Использование `TinyPersonFactory` для создания и настройки агентов.
- Использование `TinyWorld`, `TinySocialNetwork` и `Simulation` для моделирования взаимодействия.
- Утверждения `assert` для проверки корректности результатов.
- Обработка исключений с использованием `ex` (примеры: `ex ValueError`).
- Создание и проверка файла кеша (`test_consumer_profiling_scenario.cache.json`).