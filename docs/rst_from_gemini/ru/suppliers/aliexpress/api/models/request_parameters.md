```markdown
# Файл: `hypotez/src/suppliers/aliexpress/api/models/request_parameters.py`

**Расположение:** `C:\Users\user\Documents\repos\hypotez\src\suppliers\aliexpress\api\models\request_parameters.py`

**Роль:** `doc_creator` (генератор документации)

**Описание:**

Данный файл определяет константы для параметров запросов к API AliExpress.  Он содержит перечисления (классы `ProductType`, `SortBy`, `LinkType`), представляющие различные типы данных, используемых при формировании запросов.

**Константы:**

* **`ProductType`:**
    * `ALL`:  Представляет все типы продуктов.
    * `PLAZA`: Представляет продукты из PLAZA.
    * `TMALL`: Представляет продукты из TMALL.

* **`SortBy`:**
    * `SALE_PRICE_ASC`: Сортировка по цене продажи по возрастанию.
    * `SALE_PRICE_DESC`: Сортировка по цене продажи по убыванию.
    * `LAST_VOLUME_ASC`: Сортировка по последнему объему продаж по возрастанию.
    * `LAST_VOLUME_DESC`: Сортировка по последнему объему продаж по убыванию.

* **`LinkType`:**
    * `NORMAL`: Обычный тип ссылки.
    * `HOTLINK`: Тип ссылки "Горячая ссылка".


**Примечание:**

В коде присутствует дублирование строки `MODE = 'debug'`. Это может указывать на ошибку в исходном коде и требует исправления.
```