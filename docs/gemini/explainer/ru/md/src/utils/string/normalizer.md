# StringNormalizer.py - модуль для нормализации строковых полей

```markdown
## hypotez/src/utils/string/normalizer.py

Этот файл содержит класс `StringNormalizer`, предназначенный для нормализации данных, полученных из различных полей, например, при работе с продуктами. Он предоставляет статические методы для конвертации данных в различные типы (булевы, строки, целые числа, числа с плавающей точкой), обрабатывая возможные исключения и ошибки.


### Класс `StringNormalizer`

**Описание:**

Класс `StringNormalizer` содержит статические методы для нормализации данных.  Каждый метод предназначен для конкретного типа данных, обеспечивая корректную обработку различных входных значений.


**Методы:**

* **`normalize_boolean(input_data: Any) -> bool`**:
    Нормализует входные данные в булевое значение. Принимает различные типы данных (bool, str, int), преобразует их в строку и сравнивает с известными значениями, представляющими булевы значения. Возвращает `True` или `False`, а также `False` при ошибках и не распознанных значениях.  Логирование ошибок и предупреждений в `logger`.
* **`normalize_string(input_data: Union[str, List[str]]) -> str`**:
    Нормализует строку или список строк. Удаляет HTML-теги, переносы строк и спецсимволы,  преобразует список строк в одну строку, удаляет лишние пробелы. В случае ошибок возвращает пустую строку и записывает ошибку в лог.
* **`normalize_int(input_data: Union[str, int, float, Decimal]) -> int`**:
    Нормализует входные данные в целое число.  Поддерживает `Decimal`, `int`, `float` и строки, представляющие числа. Возвращает целочисленное значение или `None` при ошибках конвертации. Обратите внимание, что при ошибках возвращается `None`, а не пустая строка.
* **`normalize_float(value: Any) -> float | None`**:
    Преобразует входное значение в число с плавающей точкой или список таких чисел.  Рекурсивно обрабатывает списки.  Возвращает `float`, `List[float]` или `None` в случае ошибки.  Важно: обработка пустых значений (`value = None`, `value = ""`) и вложенных списков.  Возвращает 0 для пустых значений.  Добавлены предупреждающие сообщения в лог для случая некорректного ввода.


**Важно:**

* Методы используют `logger` для записи сообщений об ошибках и предупреждениях.
* Метод `normalize_int` возвращает `None` при ошибках, а не `''`.
* Метод `normalize_float` корректнее обрабатывает списки и возвращает список чисел с плавающей точкой или `None`, если преобразование невозможно.
* Добавлена более подробная документация для каждого метода.


Этот код улучшен благодаря более четким сообщениям об ошибках, обработке пустых и некорректных входных данных, а также более понятным возвращаемым значениям.
```