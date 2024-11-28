# Структура проекта PrestaShop

Этот документ описывает структуру проекта `PrestaShop`, предназначенного для взаимодействия с API платформы PrestaShop.  Документ содержит описание основных директорий, модулей и их функций.

## Структура папок

* **`PrestaShop`:** Основной каталог модуля.
    * `__init__.py`: Инициализирует модуль.
    * `category.py`: Управление категориями.
    * `customer.py`: Управление клиентами.
    * `language.py`: Управление языками.
    * `pricelist.py`: Управление ценовыми списками.
    * `product.py`: Управление продуктами.
    * `shop.py`: Управление магазинами.
    * `supplier.py`: Управление поставщиками.
    * `version.py`: Управление информацией о версии модуля.
    * `warehouse.py`: Управление складами.

* **`_examples`:** Каталог с примерами использования модуля и документацией.
    * `__init__.py`: Инициализирует модуль примеров.
    * `header.py`: Пример скрипта заголовка.
    * `version.py`: Пример скрипта версии.

* **`api`:** Каталог с файлами, связанными с API PrestaShop.
    * `__init__.py`: Инициализирует модуль API.
    * `_dot`: Каталог с DOT-файлами для графических представлений.
    * `_examples`: Примеры использования API.
    * `api.py`: Основной файл для взаимодействия с API PrestaShop.
    * `version.py`: Управление информацией о версии модуля API.

* **`api_schemas`:** Каталог со схемами JSON для API.
    * `__init__.py`: Инициализирует модуль схем.
    * `api_resourses_list.py`: Список доступных ресурсов API.
    * `api_schema_category.json`: Схема JSON для категорий.
    * `api_schema_language.json`: Схема JSON для языков.
    * `api_schema_product.json`: Схема JSON для продуктов.
    * `api_schemas_builder.py`: Скрипт для построения схем API.
    * `api_suppliers_schema.json`: Схема JSON для поставщиков.
    * `csv_product_schema.json`: Схема CSV для продуктов.
    * `PrestaShop_product_combinations_fields.json`: JSON файл для полей комбинаций продуктов.
    * `PrestaShop_product_combinations_sysnonyms_he.json`: JSON файл с синонимами комбинаций продуктов на иврите.

* **`domains`:** Каталог с настройками для разных доменных имён.
    * `__init__.py`: Инициализирует модуль доменов.
    * `ecat_co_il`: Настройки для `ecat.co.il`.
        * `__init__.py`: Инициализирует домен `ecat.co.il`.
        * `settings.json`: Файл настроек для `ecat.co.il`.
    * `emildesign_com`: Настройки для `emildesign.com`.
        * `__init__.py`: Инициализирует домен `emildesign.com`.
        * `settings.json`: Файл настроек для `emildesign.com`.
    * `sergey_mymaster_co_il`: Настройки для `sergey.mymaster.co.il`.
        * `__init__.py`: Инициализирует домен `sergey.mymaster.co.il`.
        * `settings.json`: Файл настроек для `sergey.mymaster.co.il`.


## Основные компоненты

Документ описывает функциональность основных модулей, связанных с PrestaShop API.  Каждый модуль отвечает за определенные операции, связанные с соответствующими ресурсами платформы PrestaShop.

## Пример использования

Пример использования модуля `product`:

```python
from PrestaShop.product import Product

# Инициализация Product
product = Product()

# Пример операции получения данных о продукте
product_data = product.get_product_data(product_id="12345")

print(product_data)
```

## Документация

Каталог `_examples` содержит примеры скриптов и документацию, которые помогают разработчикам эффективно понимать и использовать модуль.

Этот обзор предоставляет всестороннее понимание функциональности модуля `PrestaShop`.  Если у вас есть дополнительные вопросы, задавайте их.