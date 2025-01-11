# Модуль `header.py`

## Обзор

Данный модуль содержит настройки и импорты, необходимые для работы с веб-драйвером Edge. Он устанавливает пути к директориям, добавляет их в `sys.path` и импортирует необходимые библиотеки и модули. Также определена переменная `MODE`, указывающая на режим работы (в данном случае 'dev').

## Оглавление

1. [Обзор](#обзор)
2. [Переменные](#переменные)
3. [Импорты](#импорты)
4. [Вывод директории root](#вывод-директории-root)

## Переменные

### `MODE`
**Описание**: Определяет режим работы модуля. В данном случае установлен в `dev`.
Тип: `str`

## Импорты

### Системные импорты

- `sys`: Модуль для доступа к параметрам и функциям интерпретатора.
- `os`: Модуль для взаимодействия с операционной системой.
- `pathlib`: Модуль для работы с путями в файловой системе.
- `json`: Модуль для работы с данными в формате JSON.
- `re`: Модуль для работы с регулярными выражениями.

### Локальные импорты

- `src.gs`: Модуль `gs` из директории `src`.
- `src.suppliers.Supplier`: Класс `Supplier` из модуля `src.suppliers`.
- `src.product.Product`, `src.product.ProductFields`, `src.product.ProductFieldsLocators`: Классы `Product`, `ProductFields` и `ProductFieldsLocators` из модуля `src.product`.
- `src.category.Category`: Класс `Category` из модуля `src.category`.
- `src.utils.jjson.j_dumps`, `src.utils.jjson.j_loads`, `src.utils.jjson.pprint`, `src.utils.jjson.save_text_file`: Функции `j_dumps`, `j_loads`, `pprint` и `save_text_file` из модуля `src.utils.jjson`.
- `src.logger.logger`:  Объект `logger` из модуля `src.logger.logger`.
- `src.logger.logger.StringNormalizer`, `src.logger.logger.ProductFieldsValidator`: Классы `StringNormalizer` и `ProductFieldsValidator` из модуля `src.logger.logger`.

## Вывод директории root

В коде выполняется вывод значения переменной `dir_root`, представляющей корневую директорию проекта. Это полезно для отладки и понимания текущего контекста работы модуля.

```python
print(dir_root)