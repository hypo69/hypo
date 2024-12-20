# ИНСТРУКЦИЯ ПО ОБРАБОТКЕ КОМПОНЕНТОВ КОМПЬЮТЕРА

## Обзор

Данный модуль предназначен для анализа JSON-данных о компонентах компьютера, классификации типа сборки (например, игровой, рабочая станция), генерации заголовков и описаний на иврите и русском языках, перевода деталей компонентов и возврата структурированного JSON-выхода. Модуль сохраняет правильный формат, включает оценки уверенности и следует подробным рекомендациям по описаниям и обработке компонентов.

## Функции

### `process_components`

**Описание**: Обрабатывает входные данные JSON, содержащие информацию о компонентах компьютера, и генерирует выходной JSON в соответствии с шаблоном.

**Параметры**:

- `input_json` (dict): Входные данные в формате JSON. Должен соответствовать описанному в шаблоне формату.

**Возвращает**:

- `dict`: Выходные данные в формате JSON, соответствующие шаблону. Возвращает `None`, если входные данные некорректны.

**Вызывает исключения**:

- `ValueError`: Если входные данные не соответствуют ожидаемому формату.
- `TypeError`: Если входные данные имеют неверный тип.
- `Exception`: Если возникла любая другая ошибка.



```
```python
def process_components(input_json: dict) -> dict | None:
    """
    Args:
        input_json (dict): Входные данные в формате JSON. Должен соответствовать описанному в шаблоне формату.

    Returns:
        dict: Выходные данные в формате JSON, соответствующие шаблону. Возвращает None, если входные данные некорректны.

    Raises:
        ValueError: Если входные данные не соответствуют ожидаемому формату.
        TypeError: Если входные данные имеют неверный тип.
        Exception: Если возникла любая другая ошибка.
    """
    try:
        # Ваша логика обработки входных данных
        # ...
        return processed_json
    except ValueError as ex:
        print(f"Ошибка валидации: {ex}")
        return None
    except TypeError as ex:
        print(f"Ошибка типа: {ex}")
        return None
    except Exception as ex:
        print(f"Непредвиденная ошибка: {ex}")
        return None
```

## Шаблон ответа

### Описание шаблона

Шаблон ответа предоставляет структурированный формат для возвращаемых данных. Он содержит поля `he` (иврит) и `ru` (русский), каждый из которых включает заголовок (`title`), описание (`description`), типы сборки (`build_types`), а также список компонентов (`products`). Каждый компонент имеет поля `product_id`, `product_title`, `product_description`, `product_specification`, и `image_local_saved_path`.  Поля  `product_description` и `product_specification` могут быть пустыми, если не удалось получить информацию.

## Требования к входным данным

Входной JSON должен соответствовать шаблону, описанному в разделе "Шаблон ответа".


## Примеры

```json
// Пример входных данных
// ...
```

```json
// Пример выходных данных
// ...
```
```
```

##  Описание обработанных данных

Здесь необходимо подробное описание того, как обрабатываются входные данные, какие алгоритмы используются, и как формируется итоговый JSON.