# Модуль hypotez/src/suppliers/ivory/__morlevi__.py

## Обзор

Данный модуль предоставляет функции для работы с поставщиком Morlevi, включая логин на сайт, получение данных о продуктах и список категорий.

## Функции

### `login`

**Описание**: Функция осуществляет вход на сайт Morlevi. При неудачном входе, пытается закрыть модальные окна и повторно выполнить вход.

**Параметры**:
- `supplier` (объект): Объект, представляющий поставщика. Должен содержать драйвер браузера, локаторы и другие необходимые данные для взаимодействия с сайтом.

**Возвращает**:
- `bool`: `True`, если вход успешен; `None`, если вход не удался после попыток закрыть модальные окна.


**Вызывает исключения**:
- Любые исключения, возникающие при взаимодействии с веб-драйвером (например, `NoSuchElementException`, `TimeoutException`).  Эти исключения обрабатываются, и соответствующее сообщение выводится в лог.


### `_login`

**Описание**: Вспомогательная функция для входа на сайт Morlevi.

**Параметры**:
- `_s` (объект): Объект, представляющий поставщика.  Должен содержать драйвер браузера, локаторы и другие необходимые данные для взаимодействия с сайтом.

**Возвращает**:
- `bool`: `True`, если вход успешен; `None`, если вход не удался.


**Вызывает исключения**:
- Любые исключения, возникающие при взаимодействии с веб-драйвером.  Эти исключения обрабатываются, и соответствующее сообщение выводится в лог.

### `grab_product_page`

**Описание**: Функция для извлечения данных о продукте с сайта Morlevi.

**Параметры**:
- `s` (объект): Объект, представляющий поставщика. Должен содержать драйвер браузера, локаторы и другие необходимые данные для взаимодействия с сайтом.


**Возвращает**:
- `Product`: Объект класса `Product`, содержащий данные о продукте.

**Вызывает исключения**:
- Любые исключения, возникающие при работе с веб-драйвером или при сборе данных о продукте.


### `list_products_in_category_from_pagination`

**Описание**: Функция для получения списка ссылок на продукты в заданной категории, обрабатывая все страницы пагинации.

**Параметры**:
- `supplier` (объект): Объект, представляющий поставщика. Должен содержать драйвер браузера, локаторы и другие необходимые данные для взаимодействия с сайтом.


**Возвращает**:
- `list`: Список ссылок на продукты. Возвращает пустой список, если в категории нет продуктов.

**Вызывает исключения**:
- Любые исключения, возникающие при взаимодействии с веб-драйвером или при работе с ссылками на продукты.


### `get_list_products_in_category`

**Описание**: Функция для получения списка продуктов в категории,  принимает объекты Supplier, сценарий и PrestaShopWebServiceDict.

**Параметры**:
- `s` (Supplier): Объект поставщика.
- `scenario` (JSON): JSON-данные сценария.
- `presath` (PrestaShopWebServiceDict): Данные PrestaShopWebService.

**Возвращает**:
- `list`: Список продуктов.

**Вызывает исключения**:
- Любые исключения, возникающие в `list_products_in_category_from_pagination`.


### `get_list_categories_from_site`

**Описание**: Функция для получения списка категорий с сайта.  (Не детализируется в этом фрагменте).


**Параметры**:
- `s` (Supplier): Объект поставщика.
- `scenario_file` (строка): Имя файла сценария.
- `brand` (строка, опционально): Название бренда.

**Возвращает**:
- Возвращаемое значение не указано. (Потребуется уточнение из исходного кода).

**Вызывает исключения**:
- Любые исключения, возникающие при работе с сайтом или файлами.


## Классы

(Нет определённых классов в этом коде)


## Замечания

- Код использует `logger` из модуля `settings` для регистрации событий и ошибок.
- Код предполагает наличие классов/модулей `Product`, `StringFormatter`, `settings` в проекте.
- Необходимо определить `Product`, `StringFormatter` и `settings` для полной работоспособности модуля.
- Дополнительные функции (например, `set_images`, `set_combinations`)  требуют большей детализации для полного понимания функциональности.
- Обработка исключений (`ex`) выполнена с использованием `...`, что требует дополнительного анализа и уточнения обработанных исключений.
-  В коде существуют TODO-заметки, которые требуют дальнейшего кодирования.