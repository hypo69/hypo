# Модуль `src.suppliers.wallashop.graber`

## Обзор

Модуль `src.suppliers.wallashop.graber` представляет класс `Graber`, предназначенный для сбора значений полей со страниц товаров сайта `wallashop.co.il`.  Класс наследуется от `Graber` и содержит функции для обработки полей. Если требуется нестандартная обработка, функция может быть переопределена в этом классе. Перед отправкой запроса к веб-драйверу можно совершить предварительные действия через декоратор.

## Оглавление

1.  [Класс `Graber`](#класс-graber)
    *   [Метод `__init__`](#метод-__init__)

## Классы

### `Graber`

**Описание**: Класс для операций захвата данных с сайта `wallashop.co.il`.

**Наследует от**: `src.suppliers.graber.Graber`

#### Метод `__init__`

**Описание**: Инициализирует класс `Graber`, устанавливает префикс поставщика и вызывает конструктор родительского класса.

**Параметры**:
-   `driver` (`src.webdriver.driver.Driver`): Экземпляр веб-драйвера для управления браузером.

**Возвращает**:
- `None`: Метод ничего не возвращает

**Пример:**
```python
from src.webdriver.driver import Driver
driver_instance = Driver()
graber = Graber(driver_instance)
```