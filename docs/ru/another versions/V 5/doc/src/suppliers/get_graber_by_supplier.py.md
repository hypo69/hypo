# Модуль для получения граббера по URL поставщика

## Обзор

Модуль предоставляет функциональность для получения соответствующего объекта граббера для заданного URL поставщика. У каждого поставщика есть свой собственный граббер, который извлекает значения полей из целевой HTML-страницы.

## Подробней

Этот модуль является важной частью системы, предназначенной для сбора данных о товарах с различных сайтов электронной коммерции. Он определяет, какой именно граббер следует использовать, исходя из URL-адреса сайта, что позволяет правильно извлекать информацию о товарах, адаптируясь к различным структурам сайтов поставщиков. Функция `get_graber_by_supplier_url` является центральной в этом процессе, она анализирует URL и возвращает соответствующий объект граббера.

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
```

**Как работает функция**:

Функция `get_graber_by_supplier_url` принимает URL страницы поставщика, индекс языка для Prestashop и объект драйвера WebDriver. Она определяет, какой граббер следует использовать, на основе начальной части URL. Если URL соответствует одному из известных поставщиков (например, Aliexpress, Amazon, Bangood и т. д.), функция возвращает экземпляр соответствующего класса граббера. Если совпадение не найдено, функция логирует отладочное сообщение и возвращает `None`.

**Параметры**:

- `driver` (`'Driver'`): Объект веб-драйвера, используемый для взаимодействия с веб-страницей.
- `url` (`str`): URL страницы поставщика.
- `lang_index` (`int`): Индекс языка в магазине Prestashop.

**Возвращает**:

- `Graber | None`: Возвращает экземпляр класса `Graber` или одного из его подклассов, если URL соответствует известному поставщику. В противном случае возвращает `None`.

**Примеры**:

```python
from src.suppliers.get_graber_by_supplier import get_graber_by_supplier_url
from selenium import webdriver

# Пример с Aliexpress
driver = webdriver.Chrome()
url = 'https://aliexpress.com/item/1234567890.html'
lang_index = 1
graber = get_graber_by_supplier_url(driver, url, lang_index)
if graber:
    print(f'Используется граббер: {type(graber).__name__}')
else:
    print('Граббер не найден')

# Пример с Amazon
url = 'https://amazon.com/item/1234567890.html'
graber = get_graber_by_supplier_url(driver, url, lang_index)
if graber:
    print(f'Используется граббер: {type(graber).__name__}')
else:
    print('Граббер не найден')

# Пример с неизвестным сайтом
url = 'https://unknown-site.com/item/1234567890.html'
graber = get_graber_by_supplier_url(driver, url, lang_index)
if graber:
    print(f'Используется граббер: {type(graber).__name__}')
else:
    print('Граббер не найден')
driver.quit()
```