# Документация модуля `test_control.py`

## Обзор

Модуль содержит набор модульных тестов для проверки функциональности управления симуляциями в `tinytroupe`. Тесты включают проверку корректного запуска, создания контрольных точек и завершения симуляций с использованием агентов, мира и фабрики персонажей.

## Оглавление

1.  [Функции](#Функции)
    *   [`test_begin_checkpoint_end_with_agent_only`](#test_begin_checkpoint_end_with_agent_only)
    *   [`test_begin_checkpoint_end_with_world`](#test_begin_checkpoint_end_with_world)
    *   [`test_begin_checkpoint_end_with_factory`](#test_begin_checkpoint_end_with_factory)

## Функции

### `test_begin_checkpoint_end_with_agent_only`

**Описание**: Тестирует последовательность запуска симуляции, создания контрольной точки и завершения симуляции с использованием агентов. Проверяет корректность создания и наличия кешированного следа и следа выполнения, а также статуса симуляции.

**Параметры**:
- `setup` (pytest.fixture): Фикстура для настройки тестового окружения.

**Возвращает**:
- None

**Вызывает исключения**:
- AssertionError: Если состояние симуляции не соответствует ожидаемому или не создан файл контрольной точки.

### `test_begin_checkpoint_end_with_world`

**Описание**: Тестирует последовательность запуска симуляции, создания контрольной точки и завершения симуляции с использованием мира. Проверяет корректность создания и наличия кешированного следа и следа выполнения, а также статуса симуляции.

**Параметры**:
- `setup` (pytest.fixture): Фикстура для настройки тестового окружения.

**Возвращает**:
- None

**Вызывает исключения**:
- AssertionError: Если состояние симуляции не соответствует ожидаемому или не создан файл контрольной точки.

### `test_begin_checkpoint_end_with_factory`

**Описание**: Тестирует последовательность запуска симуляции, создания контрольной точки и завершения симуляции с использованием фабрики персонажей. Проверяет корректность создания и наличия кешированного следа и следа выполнения, а также статуса симуляции. Тестирует повторяемость генерации агентов на основе фабрики персонажей.

**Параметры**:
- `setup` (pytest.fixture): Фикстура для настройки тестового окружения.

**Возвращает**:
- None

**Вызывает исключения**:
- AssertionError: Если состояние симуляции не соответствует ожидаемому или не создан файл контрольной точки, или атрибуты созданных агентов не совпадают.