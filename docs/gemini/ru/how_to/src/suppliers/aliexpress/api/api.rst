Как использовать метод retrieve_product_details
========================================================================================

Описание
-------------------------
Метод `retrieve_product_details` позволяет получить информацию о продуктах AliExpress. Он использует API AliExpress для поиска и возвращает детали продуктов, соответствующие заданным параметрам.  Метод принимает список идентификаторов продуктов, опционально фильтры по полям и стране.

Шаги выполнения
-------------------------
1. **Инициализация объекта `AliexpressApi`:** Создайте экземпляр класса `AliexpressApi`, передав в конструктор API ключ, секретный ключ, код языка, код валюты и идентификатор отслеживания.
   ```python
   api = AliexpressApi(key='YOUR_API_KEY', secret='YOUR_API_SECRET', language='ru', currency='RUB', tracking_id='YOUR_TRACKING_ID')
   ```
2. **Подготовка идентификаторов продуктов:** Предоставьте один или несколько идентификаторов продуктов в виде строки или списка строк.
   ```python
   product_ids = ['12345', '67890']
   # Или
   product_ids = '12345,67890'
   ```
3. **Вызов метода `retrieve_product_details`:** Вызовите метод `retrieve_product_details`, передав в качестве аргумента список идентификаторов продуктов и опциональные параметры (fields, country).
   ```python
   products = api.retrieve_product_details(product_ids=product_ids, fields=['name', 'price'], country='RU')
   ```
4. **Обработка результатов:** Проверьте, удалось ли получить продукты. Если `products` не пустой список, то в нем хранятся объекты `model_Product`.
   ```python
   if products:
       for product in products:
           pprint(product.name)
           pprint(product.price)
   ```

Пример использования
-------------------------
```python
from src.suppliers.aliexpress.api import AliexpressApi
from src.utils import pprint
from src.logger import logger
import sys
# ... (импорты других необходимых модулей)

try:
    api = AliexpressApi(key='YOUR_API_KEY', secret='YOUR_API_SECRET', language='en', currency='USD', tracking_id='YOUR_TRACKING_ID')
    product_ids = ['12345', '67890']
    products = api.retrieve_product_details(product_ids=product_ids)
    if products:
        for product in products:
            pprint(product.__dict__)
    else:
        logger.warning('No products found.')
        sys.exit(1)

except Exception as e:
    logger.error(f"An error occurred: {e}")
    sys.exit(1)


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

**Важно:** Замените `YOUR_API_KEY`, `YOUR_API_SECRET`, `YOUR_TRACKING_ID` на ваши собственные значения.