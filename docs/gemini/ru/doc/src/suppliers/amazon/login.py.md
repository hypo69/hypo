# Модуль `login`

## Обзор

Модуль `login.py` предназначен для автоматизации процесса авторизации на сайте Amazon с использованием веб-драйвера. Он содержит функцию `login`, которая принимает объект поставщика (`Supplier`) в качестве аргумента и использует его для выполнения шагов авторизации, таких как ввод email, пароля и нажатие кнопок.

## Подробней

Этот модуль является частью системы автоматизации `hypotez` и отвечает за вход пользователя в аккаунт Amazon. Он использует локаторы, хранящиеся в объекте поставщика (`Supplier`), для поиска элементов на веб-странице и взаимодействия с ними. В случае неуспешной попытки входа, модуль регистрирует ошибку.
## Функции

### `login`

```python
def login(s) -> bool:
    """ Функция логин. 
   @param
        s - Supplier
    @returns
        True if login else False

   """
   ...
```

**Назначение**: Выполняет процесс авторизации на сайте Amazon.

**Параметры**:

-   `s` (Supplier): Объект поставщика, содержащий необходимые локаторы и драйвер для взаимодействия с веб-страницей.

**Возвращает**:

-   `bool`: `True`, если вход выполнен успешно, иначе `False`.

**Как работает функция**:

1.  **Извлечение локаторов**: Функция извлекает локаторы для элементов страницы входа из объекта поставщика `s`, используя ключ `'login'`.
2.  **Получение драйвера**: Получает драйвер из объекта поставщика `s`.
3.  **Фокусировка на окне**: Переводит фокус на окно браузера, управляемое драйвером.
4.  **Переход по URL**: Открывает страницу Amazon по адресу `https://amazon.com/`.
5.  **Клик по кнопке открытия формы входа**: Пытается нажать на кнопку, открывающую форму входа. Если не удается, обновляет страницу и повторяет попытку.
6.  **Ввод email**: Вводит email в поле ввода, используя локатор `email_input`. Если поле не найдено, завершает работу.
7.  **Нажатие кнопки "Продолжить"**: Нажимает кнопку "Продолжить", используя локатор `continue_button`.
8.  **Ввод пароля**: Вводит пароль в поле ввода, используя локатор `password_input`. Если поле не найдено, завершает работу.
9.  **Клик по чекбоксу "Оставаться в системе"**: Отмечает чекбокс "Оставаться в системе", используя локатор `keep_signed_in_checkbox`.
10. **Нажатие кнопки "Войти"**: Нажимает кнопку "Войти", используя локатор `success_login_button`.
11. **Проверка URL**: Проверяет, не произошла ли переадресация обратно на страницу входа. Если да, регистрирует ошибку и завершает работу.
12. **Разворачивание окна**: Разворачивает окно браузера на весь экран.
13. **Запись cookies**: Дампит cookies в файл.
14. **Логирование успеха**: Логирует сообщение об успешной авторизации.

```text
    Начало
    │
    ├── Получение локаторов и драйвера (locators, driver)
    │
    ├── Фокусировка на окне и открытие URL (window_focus, get_url)
    │
    ├── Попытка клика по кнопке "Войти" (open_login_inputs)
    │   └── Если неуспешно: Обновление страницы и повторная попытка (refresh)
    │
    ├── Ввод email (email_input)
    │   └── Если неуспешно: Завершение (return)
    │
    ├── Нажатие кнопки "Продолжить" (continue_button)
    │
    ├── Ввод пароля (password_input)
    │   └── Если неуспешно: Завершение (return)
    │
    ├── Клик по чекбоксу "Оставаться в системе" (keep_signed_in_checkbox)
    │
    ├── Нажатие кнопки "Войти" (success_login_button)
    │
    ├── Проверка URL на переадресацию (current_url)
    │   └── Если переадресация: Логирование ошибки и завершение (logger.error, return)
    │
    ├── Разворачивание окна (maximize_window)
    │
    ├── Логирование успеха (logger.info)
    │
    └── Завершение (return True)
```

**Примеры**:

Пример вызова функции `login` с объектом поставщика:

```python
from src.suppliers.amazon.login import login
from unittest.mock import Mock

# Создаем мок-объект поставщика
supplier_mock = Mock()
supplier_mock.locators_store = {'login': {'open_login_inputs': 'locator1', 'email_input': 'locator2', 'continue_button': 'locator3', 'password_input': 'locator4', 'keep_signed_in_checkbox': 'locator5', 'success_login_button': 'locator6'}}
supplier_mock.driver = Mock()
supplier_mock.driver.click.return_value = True
supplier_mock.driver.execute_locator.return_value = True
supplier_mock.driver.current_url = "https://www.amazon.com/homepage"

# Вызываем функцию login с мок-объектом
result = login(supplier_mock)

# Проверяем результат
print(result)  # Вывод: True
```

В данном примере создается мок-объект поставщика `supplier_mock` с необходимыми атрибутами и методами. Затем вызывается функция `login` с этим объектом, и проверяется возвращаемое значение.