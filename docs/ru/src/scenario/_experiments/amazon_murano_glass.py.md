# Модуль src.scenario._experiments.amazon_murano_glass

## Обзор

Модуль `amazon_murano_glass.py` предназначен для запуска сценария, связанного с категорией "Murano Glass" (Муранское стекло) для поставщика "amazon". Он использует функциональность, предоставляемую модулем `header` и сценарии из `dict_scenarios`.

## Подробней

Этот модуль является частью экспериментов в рамках проекта `hypotez`. Он инициализирует поставщика "amazon", запускает сценарий "Murano Glass" и извлекает ключ из категорий PrestaShop по умолчанию. Модуль демонстрирует использование класса `Supplier` для автоматизации процесса загрузки и обработки данных о товарах.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_name: str) -> Supplier:
    """ This if example function
    Args:
        supplier_name (str): Имя поставщика.

    Returns:
        Supplier: Возвращает объект класса `Supplier`.

     Raises:
         Ошибка выполнение

     Example:
         Примеры вызовов

    """
```

**Описание**: Инициализирует поставщика с заданным именем.

**Как работает функция**: Функция `start_supplier` создает и возвращает экземпляр класса `Supplier` для указанного имени поставщика. В данном коде она вызывается с именем `'amazon'`, что означает инициализацию поставщика Amazon.

**Параметры**:
- `supplier_name` (str): Имя поставщика, которое будет использовано для создания экземпляра класса `Supplier`.

**Возвращает**:
- `Supplier`: Объект класса `Supplier`, представляющий инициализированного поставщика.

**Примеры**:
```python
s = start_supplier('amazon')
```

## Переменные

- `s`: Экземпляр класса `Supplier`, созданный с использованием функции `start_supplier('amazon')`. Представляет поставщика "amazon".
- `scenario`: Словарь сценариев, импортированный из модуля `dict_scenarios`.
- `k`: Ключ, извлеченный из словаря категорий PrestaShop по умолчанию в текущем сценарии.

## Код

```python
s = start_supplier('amazon')
s.run_scenario(scenario['Murano Glass'])
k = list(s.current_scenario['presta_categories']['default_category'].keys())[0]
```

**Описание**:
1.  Инициализация поставщика `amazon` с использованием функции `start_supplier`.
2.  Запуск сценария "Murano Glass" для поставщика `s`.
3.  Извлечение первого ключа из словаря `default_category` в `presta_categories` текущего сценария и присвоение его переменной `k`.