# Модуль для получения граббера на основе URL поставщика

## Обзор

Модуль предоставляет функциональность для получения соответствующего объекта граббера для заданного URL поставщика. У каждого поставщика есть свой граббер, который извлекает значения полей из целевой HTML-страницы.

## Подробней

Этот модуль является центральным местом для определения того, какой граббер следует использовать в зависимости от URL-адреса веб-сайта. Он содержит функцию `get_graber_by_supplier_url`, которая принимает URL и возвращает соответствующий объект граббера. Если соответствующий граббер не найден, возвращается `None`. Это позволяет динамически выбирать граббер в зависимости от поставщика, с которым вы работаете.

## Функции

### `get_graber_by_supplier_url`

```python
def get_graber_by_supplier_url(driver: 'Driver', url: str, lang_index: int) -> Graber | None:
    """
    Function that returns the appropriate grabber for a given supplier URL.

    Each supplier has its own grabber, which extracts field values from the target HTML page.

    :param url: Supplier page URL.
    :type url: str
    :param lang_index: Указывает индекс языка в магазине Prestashop
    :return: Graber instance if a match is found, None otherwise.
    :rtype: Optional[object]
    """
    # Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Функция возвращает соответствующий граббер для заданного URL поставщика.

**Параметры**:
- `driver` (Driver): Объект веб-драйвера, используемый для навигации по веб-страницам.
- `url` (str): URL-адрес страницы поставщика.
- `lang_index` (int): Индекс языка в магазине Prestashop.

**Возвращает**:
- `Graber | None`: Экземпляр граббера, если соответствие найдено, иначе `None`.

**Примеры**:

```python
from src.webdriver import WebDriver
from src.suppliers.get_graber_by_supplier import get_graber_by_supplier_url

driver = WebDriver()
url = 'https://www.aliexpress.com/item/1234567890.html'
lang_index = 1
graber = get_graber_by_supplier_url(driver, url, lang_index)

if graber:
    print(f'Используется граббер: {type(graber).__name__}')
else:
    print('Граббер не найден для данного URL.')
```

**Как работает функция**:

1.  Функция принимает URL-адрес страницы поставщика и индекс языка.
2.  Функция проверяет, начинается ли URL-адрес с известных URL-адресов поставщиков (например, AliExpress, Amazon и т.д.).
3.  Если URL-адрес соответствует известному поставщику, функция возвращает экземпляр соответствующего граббера (например, `AliexpressGraber`, `AmazonGraber` и т.д.), передавая ему драйвер и индекс языка.
4.  Если URL-адрес не соответствует ни одному из известных поставщиков, функция регистрирует отладочное сообщение и возвращает `None`.