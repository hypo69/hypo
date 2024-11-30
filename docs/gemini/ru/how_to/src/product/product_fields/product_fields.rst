Как использовать класс ProductFields
============================================================================================

Описание
-------------------------
Класс `ProductFields` предназначен для работы с полями товаров в формате API PrestaShop. Он предоставляет методы для доступа и изменения значений различных полей товаров, соответствующих таблицам базы данных PrestaShop.  Класс обрабатывает данные из файла `product_fields_default_values.json`,  использует нормализаторы строк и чисел, и содержит валидацию для корректного заполнения полей.  В нем хранятся данные о полях таблицы `ps_product` и `ps_product_lang`.  Для работы с мультиязычными полями `ps_product_lang` используется словарь `language`.  Также класс предоставляет методы для работы с дополнительными полями, такими как URL изображений.


Шаги выполнения
-------------------------
1. **Импортировать необходимый модуль:**  Импортируйте класс `ProductFields` из файла `product_fields.py`.

2. **Создать экземпляр класса:** Создайте объект `ProductFields`, вызвав конструктор `__init__`.
   ```python
   from hypotez.src.product.product_fields import ProductFields
   product_fields = ProductFields()
   ```

3. **Получить или установить значение поля:** Используйте свойства (properties) класса, например, `id_product`, для чтения или записи значений полей товара. Свойства имеют методы-сеттеры и геттеры, что позволяет валидировать данные перед записью.
   ```python
   # Чтение значения поля
   product_id = product_fields.id_product

   # Запись значения поля (убедитесь, что тип данных соответствует ожидаемому)
   product_fields.id_product = 123
   product_fields.ean13 = "1234567890123"
   ```


4. **Работа с мультиязычными полями:** Для работы с полями из таблицы `ps_product_lang`,  необходимо указать язык (например, 'en', 'ru', 'he').
   ```python
   # Пример установки значения для поля name на английском языке
   product_fields.name = "Product Name", "en"
   ```

5. **Работа с дополнительными полями:** Для работы с дополнительными полями (например, `images_urls`), используйте соответствующие свойства.

Пример использования
-------------------------
```python
from hypotez.src.product.product_fields import ProductFields
import datetime

# Создаем экземпляр класса
product_fields = ProductFields()

# Заполняем поля товара
product_fields.id_product = 1001
product_fields.name = "Example Product", 'ru'
product_fields.price = 19.99
product_fields.description = "This is a description for the product.", 'ru'
product_fields.available_date = datetime.date(2024, 10, 26)

# Вывод значений полей
print(f"ID товара: {product_fields.id_product}")
print(f"Название товара (ru): {product_fields.name}")
print(f"Цена: {product_fields.price}")
print(f"Описание товара (ru): {product_fields.description}")
print(f"Дата доступности: {product_fields.available_date}")

# Проверка, что заполнение полей выполнилось успешно
print("Поля заполнены успешно?", product_fields._payload())

```
```
```
```
```
```
```
```
```

```
```
```
```

```
```


```
```
```
```
```
```

```
```
```

```
```

```
```
```
```
```
```
```
```


```
```
```
```

```
```

```

```

```
```
```

```
```
```

```
```
```
```
```
```

```
```
```
```
```