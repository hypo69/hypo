# Модуль hypotez/src/product/product_fields/product_fields.py

## Обзор

Этот модуль содержит класс `ProductFields`, предназначенный для работы с полями товаров в базе данных PrestaShop. Класс предоставляет методы для загрузки, доступа и изменения значений полей товара, включая как основные поля, так и мультиязычные.  Документация описывает структуру полей в базе данных PrestaShop и предоставляет API для взаимодействия с ними, включая обработку исключений и логирование.


## Классы

### `ProductFields`

**Описание**: Класс `ProductFields` предоставляет методы для работы с полями товаров в базе данных PrestaShop.  Он загружает список полей, значения по умолчанию и обрабатывает мультиязычные поля.


**Методы**:

- `__init__(self)`: Инициализирует класс. Загружает список полей из файла `fields_list.txt`, значения по умолчанию из `product_fields_default_values.json`, инициализирует словарь языков и служебные поля.

- `_load_product_fields_list(self) -> List[str]`: Загружает список имен полей из файла `fields_list.txt`.

- `_payload(self) -> bool`: Загружает значения полей по умолчанию из файла `product_fields_default_values.json`. Возвращает `True`, если загрузка успешна, и `False` в противном случае.

- `associations(self) -> Optional[Dict]`: Возвращает словарь ассоциаций.

- `associations(self, value: Dict[str, Optional[str]])`: Устанавливает значение словаря ассоциаций.

- `id_product(self) -> Optional[int]`:  Возвращает значение поля `id_product`.

- `id_product(self, value: int = None) -> bool`: Устанавливает значение поля `id_product`. Обрабатывает исключения `ProductFieldException`.

- `id_supplier(self) -> int | None`: Возвращает значение поля `id_supplier`.

- `id_supplier(self, value: int = None) -> bool`: Устанавливает значение поля `id_supplier`. Обрабатывает исключения `ProductFieldException`.

- `id_manufacturer(self) -> int | None`: Возвращает значение поля `id_manufacturer`.

- `id_manufacturer(self, value: int = None) -> bool`: Устанавливает значение поля `id_manufacturer`. Обрабатывает исключения `ProductFieldException`.

-(и другие методы для каждого поля товара, например, `id_category_default`, `price`, `ean13`, `isbn`, `upc`, и т.д.) ... все остальные методы по аналогии


**Обрабатывает исключения**:

- `ProductFieldException`: Обрабатывает возможные ошибки при работе с полями товаров.



## Функции


(Нет функций в данном модуле)


## Описание полей в базе данных PrestaShop

(Подробное описание структуры таблиц `ps_product` и `ps_product_lang` с примерами типов данных и описаний.)



## Служебные поля

(Описание служебных полей, хранящихся в словаре `assist_fields_dict`, например, URL изображений, код языка страницы и т.д.)


## Дополнительные замечания

- Модуль использует Pydantic для валидации входных данных.
- Модуль использует библиотеку `langdetect` для определения языка текста.
-  В комментариях к методам содержатся подробные описания, параметры, возвращаемые значения и возможные исключения.
- Используются `Enum` для удобства работы с перечислениями.

```