Как использовать модуль валидации строк
========================================================================================

Описание
-------------------------
Модуль `validator.py` предоставляет набор статических методов для валидации строк. Он предназначен для проверки различных типов строк, таких как цены, веса, артикулы и URL-адреса, на соответствие определенным критериям.  Включает в себя проверку на наличие числового значения, длины, корректного формата и т.д.

Шаги выполнения
-------------------------
1. **Импортируйте класс `ProductFieldsValidator`:**
   ```python
   from hypotez.src.utils.string.validator import ProductFieldsValidator
   ```

2. **Выберите метод для валидации:**  Модуль предоставляет методы для проверки различных типов данных. Выберите метод, соответствующий типу строки, которую вы хотите валидировать.

3. **Передайте строку в качестве параметра:**  Передайте строку, которую нужно валидировать, в соответствующий метод в качестве аргумента.

4. **Получите результат:**  Метод вернет `True`, если строка соответствует критериям валидации, и `None` (или `False`, в случае, если код не обрабатывает исключения), если не соответствует. Обратите внимание на возвращаемый тип данных.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.utils.string.validator import ProductFieldsValidator

    # Пример проверки цены
    price_string = "123.45"
    is_valid_price = ProductFieldsValidator.validate_price(price_string)

    if is_valid_price:
        print("Цена валидна")
    else:
        print("Цена не валидна")

    # Пример проверки веса
    weight_string = "5,5 kg"
    is_valid_weight = ProductFieldsValidator.validate_weight(weight_string)

    if is_valid_weight:
        print("Вес валиден")
    else:
        print("Вес не валиден")


    # Пример проверки артикула
    sku_string = "ABC12345"
    is_valid_sku = ProductFieldsValidator.validate_sku(sku_string)

    if is_valid_sku:
        print("Артикул валиден")
    else:
        print("Артикул не валиден")

    # Пример проверки URL
    url_string = "https://www.example.com"
    is_valid_url = ProductFieldsValidator.validate_url(url_string)

    if is_valid_url:
        print("URL валиден")
    else:
        print("URL не валиден")

    #Пример невалидного URL (только адрес, без протокола)
    url_string = "www.example.com"
    is_valid_url = ProductFieldsValidator.validate_url(url_string)

    if is_valid_url:
        print("URL валиден")
    else:
        print("URL не валиден")

    # Пример проверки на целое число
    int_string = "123"
    is_integer = ProductFieldsValidator.isint(int_string)

    if is_integer:
        print(f"Строка '{int_string}' - целое число")
    else:
        print(f"Строка '{int_string}' - не целое число")

    # Пример проверки на целое число - НЕЧИСЛЕННОЕ значение
    int_string = "abc"
    is_integer = ProductFieldsValidator.isint(int_string)
    if is_integer:
        print(f"Строка '{int_string}' - целое число")
    else:
        print(f"Строка '{int_string}' - не целое число")