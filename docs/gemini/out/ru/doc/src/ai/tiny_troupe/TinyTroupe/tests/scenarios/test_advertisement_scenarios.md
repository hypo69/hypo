# Модуль `test_advertisement_scenarios.py`

## Обзор

Этот модуль содержит тесты сценариев, связанных с рекламой.  Тесты проверяют поведение агентов при оценке рекламных объявлений и создании рекламных кампаний.

## Тесты

### `test_ad_evaluation_scenario`

**Описание**: Этот тест оценивает способность агентов выбрать наиболее убедительное рекламное объявление из набора, связанного с турами по Европе.

**Параметры**:

* `setup`: Набор данных, необходимый для запуска сценария.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:

- `AssertionError`: Возникает, если результаты агентов не соответствуют ожидаемым значениям. Сообщения об ошибках проверяют корректность идентификатора объявления (`ad_id`), заголовка (`ad_title`) и обоснования выбора (`justification`). Проверяется корректность количества полученных результатов (2).


### `test_ad_creation_scenario`

**Описание**: Этот тест имитирует фокус-группу для обсуждения лучшего способа рекламы квартиры для сдачи в аренду.

**Параметры**:

* `setup`: Набор данных, необходимый для запуска сценария.
* `focus_group_world`: Объект, представляющий фокус-группу.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:

- `AssertionError`: Возникает, если результат не соответствует ожидаемой структуре. В данном случае проверяется наличие предложений по рекламе квартиры.


### `test_consumer_profiling_scenario`

**Описание**: Этот тест моделирует сбор данных о потребительских предпочтениях для продвижения газированного газпачо.

**Параметры**:

* `setup`: Набор данных, необходимый для запуска сценария.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:

- `AssertionError`: Возникает, если файл с данными о пользователях не был создан (`test_consumer_profiling_scenario.cache.json`).


## Функции

### `interview_consumer_batch`

**Описание**: Функция для моделирования опроса группы потребителей.

**Параметры**:

* `n` (int): Количество потребителей для опроса.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- Нет.


##  Использование дополнительных модулей

Этот модуль использует следующие модули и классы:

* `pytest`: Для выполнения тестов.
* `logging`: Для ведения журнала.
* `tinytroupe`, `TinyPerson`, `TinyWorld`, `TinySocialNetwork`, `TinyPersonFactory`, `ResultsExtractor`:  Классы и модули для работы с агентами и средой TinyTroupe.
* `create_lisa_the_data_scientist`, `create_oscar_the_architect`, `create_marcos_the_physician`:  Функции для создания агентов с заданными характеристиками.
* `default_extractor`:  Возможный вариант `extractor`.
* `tinytroupe.control`, `Simulation`: Модуль для управления симуляцией.
* `testing_utils`:  Возможно, модуль для вспомогательных функций тестирования.


## Поддержка файла

Этот модуль использует временные файлы (`.cache.json`) для сохранения результатов.