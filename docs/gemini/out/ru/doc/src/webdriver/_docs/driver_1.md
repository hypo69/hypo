# Модуль driver_1

## Обзор

Данный модуль определяет метакласс `DriverMeta`, предназначенный для динамического создания класса `Driver`, который наследуется как от базового класса `Driver`, так и от указанного класса Selenium WebDriver (`Chrome`, `Firefox` или `Edge`). Метакласс отвечает за создание правильного сочетания этих классов.

## Метакласс `DriverMeta`

### Описание

Метакласс в Python – это класс для классов, определяющий поведение класса. Здесь `DriverMeta` используется для управления созданием нового класса `Driver`.

### Метод `__call__`

Метод `__call__` в метаклассе вызывается при создании экземпляра класса. В данном случае он используется для создания нового класса `Driver`, который наследуется от базового класса `Driver` и одного из классов Selenium WebDriver (`Chrome`, `Firefox` или `Edge`).

- `cls`: Класс, который создается, в данном случае `Driver`.
- `webdriver_cls`: Класс Selenium WebDriver, от которого наследуется (`Chrome`, `Firefox` или `Edge`).
- `*args` и `**kwargs`: Аргументы и ключевые аргументы для передачи в конструктор класса `Driver`.

### Проверки

- `assert isinstance(webdriver_cls, type)`: Гарантирует, что `webdriver_cls` на самом деле является классом.
- `assert issubclass(webdriver_cls, Chrome | Firefox | Edge)`: Гарантирует, что `webdriver_cls` является подклассом одного из разрешённых классов WebDriver (`Chrome`, `Firefox` или `Edge`).

### Динамическое создание класса

Внутри метода `__call__` динамически определяется новый класс с именем `Driver`. Этот новый класс наследуется как от `cls` (базового класса `Driver`), так и от `webdriver_cls` (указанного класса WebDriver).

#### Класс `Driver`

##### Конструктор `__init__`

- `__init__`: Конструктор динамически созданного класса `Driver`.
  - Записывает в логи информацию об инициализации WebDriver с его именем и аргументами.
  - Вызывает конструкторы родительских классов с помощью `super()`.
  - Вызывает метод `driver_payload`.

##### Метод `driver_payload`

Этот метод определен внутри динамически созданного класса `Driver` и вызывает метод `driver_payload` из родительского класса `Driver`. Это гарантирует, что будут выполнены любые дополнительные инициализации, необходимые классу `Driver`.

### Возвращение динамического класса

Созданный класс `Driver` инстанцируется и возвращается с предоставленными аргументами.

## Пример использования

При создании экземпляра класса `Driver` с метаклассом `DriverMeta` и передачей класса WebDriver, он динамически создаст новый класс, который наследуется как от базового класса `Driver`, так и от указанного класса WebDriver (`Chrome`, `Firefox` или `Edge`).

Например:

```python
# Создание экземпляра Driver с Chrome в качестве класса WebDriver
chrome_driver = Driver(Chrome, *args, **kwargs)

# Создание экземпляра Driver с Firefox в качестве класса WebDriver
firefox_driver = Driver(Firefox, *args, **kwargs)
```

Это позволяет создать класс `Driver`, который имеет все методы и свойства как базового класса `Driver`, так и указанного класса Selenium WebDriver (`Chrome`, `Firefox` или `Edge`), обеспечивая гибкую и динамическую инициализацию WebDriver с дополнительной кастомизацией.