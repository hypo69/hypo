# Модуль `amazon_murano_glass`

## Обзор

Модуль `amazon_murano_glass.py` предназначен для запуска сценария, связанного с товарами "Murano Glass" (Муранское стекло) от поставщика "amazon". Он использует модуль `header` для запуска поставщика и модуль `dict_scenarios` для получения сценария.

## Подробней

Этот модуль является частью экспериментов с различными сценариями для поставщиков. Он инициализирует поставщика "amazon" и запускает для него конкретный сценарий "Murano Glass".

## Функции

### `start_supplier`

```python
s = start_supplier('amazon')
```

**Описание**: Инициализирует поставщика 'amazon', используя функцию `start_supplier` из модуля `header`.

**Параметры**:
- Нет явных параметров, но функция `start_supplier` принимает строку с именем поставщика.

**Возвращает**:
- Объект класса `Supplier`.

**Примеры**:
```python
s = start_supplier('amazon')
```

### `run_scenario`

```python
s.run_scenario(scenario['Murano Glass'])
```

**Описание**: Запускает сценарий 'Murano Glass' для поставщика `s`.

**Параметры**:
- `scenario['Murano Glass']` (dict): Сценарий, который будет выполнен.

**Возвращает**:
- Нет явного возвращаемого значения.

**Примеры**:
```python
s.run_scenario(scenario['Murano Glass'])
```

## Переменные

### `s`

**Описание**: Объект класса `Supplier`, представляющий поставщика "amazon".

**Примеры**:
```python
s = start_supplier('amazon')
```

### `k`

```python
k = list(s.current_scenario['presta_categories']['default_category'].keys())[0]
```

**Описание**: Извлекает первый ключ из словаря `default_category` в сценарии поставщика.

**Параметры**:
- Нет явных параметров.

**Возвращает**:
- Строка, представляющая первый ключ из указанного словаря.

**Примеры**:
```python
k = list(s.current_scenario['presta_categories']['default_category'].keys())[0]