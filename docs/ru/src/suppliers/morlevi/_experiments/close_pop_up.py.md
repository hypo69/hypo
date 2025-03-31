# Модуль `close_pop_up`

## Обзор

Модуль `close_pop_up` предназначен для проверки локатора закрытия всплывающего окна на веб-сайте поставщика Morlevi. Он использует Selenium WebDriver для управления браузером и взаимодействия с веб-страницей.

## Подробней

Этот модуль является экспериментальным и предназначен для тестирования и отладки процесса закрытия всплывающих окон на сайте Morlevi. Он использует классы `Driver`, `Firefox` и `MorleviGraber` для автоматизации действий браузера и извлечения необходимой информации со страницы.

## Классы

### `MorleviGraber`

**Описание**: Класс `MorleviGraber` используется для взаимодействия с веб-сайтом Morlevi, включая извлечение информации о продуктах и выполнение других задач.

**Как работает класс**:
Класс наследуется от базового класса `Graber` и предоставляет методы для работы с сайтом Morlevi. В данном контексте он используется для извлечения идентификатора продукта (`id_product`) после загрузки страницы.

**Методы**:
- `id_product`: Возвращает идентификатор продукта, полученный со страницы.

**Параметры**:
- `driver` (Driver): Экземпляр класса `Driver`, представляющий управляемый браузер.

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox
from src.suppliers.morlevi.graber import Graber as MorleviGraber

driver = Driver(Firefox)
graber = MorleviGraber(driver)
```

## Функции

### `Driver`

```python
driver = Driver(Firefox)
```

**Описание**: Инициализирует драйвер для управления браузером Firefox.

**Как работает функция**:
Создает экземпляр класса `Driver` с указанием `Firefox` в качестве типа браузера. Это позволяет использовать Selenium WebDriver для автоматизации действий в браузере Firefox.

**Параметры**:
- `Firefox`: Указывает на использование браузера Firefox.

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox

driver = Driver(Firefox)
```

### `MorleviGraber`

```python
graber = MorleviGraber(driver)
```

**Описание**: Создает экземпляр класса `MorleviGraber` для взаимодействия с сайтом Morlevi.

**Как работает функция**:
Создает экземпляр класса `MorleviGraber`, передавая ему экземпляр `driver`. Это позволяет использовать методы класса `MorleviGraber` для работы с веб-страницей, управляемой драйвером.

**Параметры**:
- `driver` (Driver): Экземпляр класса `Driver`, представляющий управляемый браузер.

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox
from src.suppliers.morlevi.graber import Graber as MorleviGraber

driver = Driver(Firefox)
graber = MorleviGraber(driver)
```

### `driver.get_url`

```python
driver.get_url('https://www.morlevi.co.il/product/19041')
```

**Описание**: Открывает указанный URL в браузере, управляемом драйвером.

**Как работает функция**:
Использует метод `get_url` класса `Driver` для загрузки веб-страницы по указанному URL.

**Параметры**:
- `url` (str): URL веб-страницы для загрузки.

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox
from src.suppliers.morlevi.graber import Graber as MorleviGraber

driver = Driver(Firefox)
graber = MorleviGraber(driver)
driver.get_url('https://www.morlevi.co.il/product/19041')
```

### `graber.id_product`

```python
product_id = graber.id_product
```

**Описание**: Извлекает идентификатор продукта с загруженной веб-страницы.

**Как работает функция**:
Использует свойство `id_product` класса `MorleviGraber` для получения идентификатора продукта, который был извлечен со страницы.

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox
from src.suppliers.morlevi.graber import Graber as MorleviGraber

driver = Driver(Firefox)
graber = MorleviGraber(driver)
driver.get_url('https://www.morlevi.co.il/product/19041')
product_id = graber.id_product
```