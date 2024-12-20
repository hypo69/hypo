# Модуль hypotez/src/suppliers/cdata/login.py

## Обзор

Данный модуль содержит функцию `login`, предназначенную для авторизации на платформе c-data.  Функция использует локаторы для поиска элементов на странице входа и выполняет соответствующие действия.

## Функции

### `login`

**Описание**: Функция выполняет вход на сайт c-data.

**Параметры**:

* `self` (объект класса, наследующего от данного модуля): Объект класса, содержащий данные для авторизации.

**Возвращает**:

* `Truee`: Если авторизация успешна.

**Вызывает исключения**:

* Возможные исключения, связанные с поиском элементов на странице (например, `NoSuchElementException`) или ошибками взаимодействия с веб-драйвером, не перечислены в коде, но могут возникнуть.


**Детали**:

Функция `login` предполагает, что в объекте `self` (вероятно, экземпляре класса) доступны следующие атрибуты:

* `get_url(url: str)`: Метод для перехода на указанную URL-адрес.
* `locators`: Словарь, содержащий локаторы для элементов страницы входа.
* `find(locator)`: Метод для поиска элемента на странице по заданному локатору.
* `send_keys(text: str)`: Метод для ввода текста в найденный элемент.
* `click()`: Метод для нажатия на найденный элемент.
* `print(text: str)`: Метод для вывода информации в консоль.
* `log(message: str)`: Метод для логирования сообщений.

**Локаторы**: Функция использует локаторы для поиска элементов на странице входа.  Локаторы хранятся в словаре `self.locators['login']`.  Структура локейторов  должна быть следующей:

```
'email_locator': {'by': 'id', 'selector': 'email_input'},
'password_locator': {'by': 'name', 'selector': 'password_input'},
'loginbutton_locator': {'by': 'css', 'selector': 'button[type="submit"]'}
```

* `by`: Тип локатора (например, `id`, `name`, `css`, `xpath`).
* `selector`: Значение локатора.

В коде присутствуют переменные `email`, `password`,  которые предполагается получить извне.  Функция предполагает, что локаторы доступны через атрибут `self.locators['login']`.



```