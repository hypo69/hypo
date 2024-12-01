Как использовать модуль валидации строк (validator.py)
========================================================================================

Описание
-------------------------
Модуль `validator.py` предоставляет набор статических методов для валидации различных типов строк, таких как цена, вес, артикул и URL.  Он проверяет соответствие строк определенным критериям, например, правильный формат цены (число с плавающей точкой), валидный артикул, корректный URL.

Шаги выполнения
-------------------------
1. **Импортирование модуля:**  Для использования функций валидации необходимо импортировать класс `ProductFieldsValidator`.

   ```python
   from hypotez.src.utils.string.validator import ProductFieldsValidator
   ```

2. **Выбор функции валидации:**  Выберите необходимую функцию для проверки конкретного типа строки (например, `validate_price`, `validate_weight`, `validate_url`).

3. **Передача значения:** Передайте строку, которую нужно валидировать, в качестве аргумента функции.

4. **Обработка результата:** Результат функции – булевое значение (`True`, если строка валидна, иначе `None` или `False` в зависимости от функции).  Необходимо обработать возвращаемое значение. Пример:

   ```python
   price = "123.45"
   is_valid_price = ProductFieldsValidator.validate_price(price)
   if is_valid_price:
       print("Цена валидна")
   else:
       print("Цена невалидна")
   ```

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.utils.string.validator import ProductFieldsValidator

    # Пример валидации цены
    price = "1234.56"
    is_price_valid = ProductFieldsValidator.validate_price(price)
    if is_price_valid:
        print("Цена валидна")
    else:
        print("Цена невалидна")

    # Пример валидации веса
    weight = "10.5кг"
    is_weight_valid = ProductFieldsValidator.validate_weight(weight)
    if is_weight_valid:
        print("Вес валиден")
    else:
        print("Вес невалиден")

    # Пример валидации артикула
    sku = "ABC123"
    is_sku_valid = ProductFieldsValidator.validate_sku(sku)
    if is_sku_valid:
        print("Артикул валиден")
    else:
        print("Артикул невалиден")


    # Пример валидации URL
    url = "https://example.com"
    is_url_valid = ProductFieldsValidator.validate_url(url)
    if is_url_valid:
        print("URL валиден")
    else:
        print("URL невалиден")