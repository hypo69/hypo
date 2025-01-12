## АНАЛИЗ КОДА: `src/suppliers/amazon/login.py`

### 1. <алгоритм>

**Пошаговый процесс авторизации на Amazon:**

1.  **Начало:** Функция `login(s)` принимает объект поставщика `s` в качестве аргумента.

2.  **Получение данных:**
    *   Извлекает локаторы элементов (`_l`) для процесса авторизации из `s.locators_store['login']`. 
        *   Пример: `_l` может содержать локаторы для кнопки входа, поля ввода email, поля ввода пароля и т.д.
        *  `_l = {'open_login_inputs': {'by': 'css', 'value': '#nav-link-accountList'}, 'email_input': {'by': 'id', 'value': 'ap_email'}, 'continue_button': {'by': 'id', 'value': 'continue'}, 'password_input': {'by': 'id', 'value': 'ap_password'}, 'keep_signed_in_checkbox': {'by': 'id', 'value': 'rememberMe'}, 'success_login_button': {'by': 'id', 'value': 'signInSubmit'}}`
    *   Получает объект веб-драйвера `_d` из `s.driver`.

3.  **Подготовка браузера:**
    *   Фокусируется на окне браузера: `_d.window_focus()`.
    *   Открывает главную страницу Amazon: `_d.get_url('https://amazon.com/')`.

4.  **Клик по кнопке открытия формы входа:**
    *   Пытается кликнуть на кнопку открытия формы входа, используя локатор `_l['open_login_inputs']`: `_d.click(_l['open_login_inputs'])`.
    *   Если клик не удался, обновляет страницу, фокусируется на окне и пробует еще раз.
        *   Если клик всё ещё не удался,  логирует отладочное сообщение о необходимости поиска кнопки входа в другом месте.

5.  **Ввод Email:**
    *   Выполняет действие ввода email, используя локатор `_l['email_input']`: `_d.execute_locator(_l['email_input'])`.
    *   Если ввод не удался, возвращает `None`.

6.  **Клик по кнопке "Продолжить":**
    *   Выполняет клик по кнопке "Продолжить", используя локатор `_l['continue_button']`: `_d.execute_locator(_l['continue_button'])`.
    *    Если клик не удался,  не выполняет никаких действий.

7.  **Ввод Пароля:**
    *   Выполняет ввод пароля, используя локатор `_l['password_input']`: `_d.execute_locator(_l['password_input'])`.
    *   Если ввод не удался, не выполняет никаких действий.

8.  **Клик по чекбоксу "Оставаться в системе":**
    *   Пытается кликнуть по чекбоксу "Оставаться в системе", используя локатор `_l['keep_signed_in_checkbox']`: `_d.execute_locator(_l['keep_signed_in_checkbox'])`.
    *  Если клик не удался, не выполняет никаких действий.

9.  **Клик по кнопке "Войти":**
    *   Выполняет клик по кнопке "Войти", используя локатор `_l['success_login_button']`: `_d.execute_locator(_l['success_login_button'])`.
   *   Если клик не удался,  не выполняет никаких действий.

10. **Проверка успешности входа:**
    *   Проверяет, остался ли текущий URL "https://www.amazon.com/ap/signin", если да, то логирует ошибку и возвращается из функции.

11. **Завершение:**
    *   Максимизирует окно браузера: `_d.maximize_window()`.
    *   Логирует информационное сообщение об успешном входе.
    *   Возвращает `True`.

### 2. <mermaid>

```mermaid
flowchart TD
    Start[Start login(s)] --> GetLocators[Get locators from s.locators_store['login']\n(_l: dict)]
    GetLocators --> GetDriver[Get driver from s.driver\n(_d)]
    GetDriver --> FocusWindow[Focus on browser window\n_d.window_focus()]
    FocusWindow --> OpenAmazon[Open Amazon homepage\n_d.get_url('https://amazon.com/')]
    OpenAmazon --> ClickOpenLogin[Click open login button\n_d.click(_l['open_login_inputs'])]
    ClickOpenLogin -- Fail --> RefreshPage[Refresh page\n_d.refresh()]
    RefreshPage --> FocusWindow2[Focus on window\n_d.window_focus()]
    FocusWindow2 --> ClickOpenLogin2[Click open login button\n_d.click(_l['open_login_inputs'])]
    ClickOpenLogin -- Success --> EmailInput[Execute email input\n_d.execute_locator(_l['email_input'])]
    ClickOpenLogin2 -- Fail --> LogDebug[Log debug message\nlogger.debug('...')]
    EmailInput -- Fail --> ReturnNone[Return from function]
    EmailInput -- Success --> ContinueButton[Execute click continue button\n_d.execute_locator(_l['continue_button'])]
    ContinueButton -- Success --> PasswordInput[Execute password input\n_d.execute_locator(_l['password_input'])]
    ContinueButton -- Fail --> PasswordInput
    PasswordInput -- Success --> KeepSignedIn[Execute click keep signed in checkbox\n_d.execute_locator(_l['keep_signed_in_checkbox'])]
    PasswordInput -- Fail --> KeepSignedIn
    KeepSignedIn -- Success --> SuccessLogin[Execute click success login button\n_d.execute_locator(_l['success_login_button'])]
    KeepSignedIn -- Fail --> SuccessLogin
    SuccessLogin -- Success --> CheckLogin[Check if login failed\n_d.current_url == "https://www.amazon.com/ap/signin"]
    SuccessLogin -- Fail --> CheckLogin
     CheckLogin -- LoginFailed --> LogError[Log error message\nlogger.error('Неудачный логин')]
    LogError --> ReturnNone2[Return from function]
    CheckLogin -- LoginSuccess --> MaximizeWindow[Maximize window\n_d.maximize_window()]
    MaximizeWindow --> LogSuccess[Log success message\nlogger.info('Залогинился ... ')]
    LogSuccess --> ReturnTrue[Return True]
    ReturnNone --> End
    ReturnNone2 --> End
    ReturnTrue --> End
    End[End]

```
**Объяснение `mermaid`:**

*   `Start`: Начало функции `login`.
*   `GetLocators`: Извлекает локаторы элементов из `s.locators_store['login']` и сохраняет в `_l` (словарь).
*   `GetDriver`: Получает объект веб-драйвера из `s.driver` и сохраняет в `_d`.
*   `FocusWindow`: Фокусируется на окне браузера с помощью `_d.window_focus()`.
*  `OpenAmazon`: Открывает главную страницу Amazon (`https://amazon.com/`) с помощью `_d.get_url()`.
*   `ClickOpenLogin`: Пытается кликнуть на кнопку открытия формы входа с помощью `_d.click(_l['open_login_inputs'])`.
* `RefreshPage`: Обновляет страницу в случае неудачи с первым кликом.
* `FocusWindow2`: Снова фокусируется на окне после обновления.
* `ClickOpenLogin2`: Повторно пытается кликнуть на кнопку открытия формы входа.
*  `LogDebug`: Выводит отладочное сообщение в случае если не удалось кликнуть на кнопку открытия формы входа ни один раз.
*  `EmailInput`: Выполняет ввод email, используя `_d.execute_locator(_l['email_input'])`.
*   `ContinueButton`: Выполняет клик по кнопке "Продолжить" с помощью `_d.execute_locator(_l['continue_button'])`.
*   `PasswordInput`: Выполняет ввод пароля с помощью `_d.execute_locator(_l['password_input'])`.
*   `KeepSignedIn`: Пытается кликнуть по чекбоксу "Оставаться в системе"  с помощью `_d.execute_locator(_l['keep_signed_in_checkbox'])`.
* `SuccessLogin`: Пытается кликнуть на кнопку "Войти"  с помощью `_d.execute_locator(_l['success_login_button'])`.
*   `CheckLogin`: Проверяет, не остался ли текущий URL "https://www.amazon.com/ap/signin", что указывает на неудачный вход.
*   `LogError`: Выводит сообщение об ошибке, если вход не удался.
*   `MaximizeWindow`: Максимизирует окно браузера с помощью `_d.maximize_window()`.
*   `LogSuccess`: Выводит сообщение об успешном входе.
*   `ReturnNone`, `ReturnNone2`, `ReturnTrue`: Возвращает значения `None` или `True` из функции.
*   `End`: Конец выполнения функции.

**Зависимости:**
*  `src.logger.logger`:  Используется для логирования событий.
* `s` - это объект поставщика, который предоставляет доступ к локаторам и веб-драйверу. `s.locators_store` - словарь, который содержит локаторы для различных частей веб-страницы, а `s.driver` это объект вебдрайвера, с помощью которого осуществляется взаимодействие с браузером.

### 3. <объяснение>

**Импорты:**

*   `from src.logger.logger import logger`: Импортирует объект `logger` из модуля `src.logger.logger`. Этот объект используется для логирования различных событий (отладочных сообщений, ошибок, информационных сообщений).

**Функции:**

*   `login(s) -> bool`:
    *   **Аргументы:**
        *   `s`: Объект поставщика (`Supplier`), который должен содержать необходимые данные для работы, включая локаторы элементов и объект веб-драйвера.
    *   **Возвращаемое значение:**
        *   `True`: Если авторизация прошла успешно.
        *   `None`: если произошла ошибка в процессе авторизации.
    *   **Назначение:** Выполняет процесс авторизации на веб-сайте Amazon с помощью веб-драйвера.
    *   **Примеры:**
        *   Вызов: `login(my_supplier)`.
        *   Возвращает: `True`, если авторизация успешна; `None` если произошла ошибка.

**Переменные:**

*   `_l: dict`: Словарь, содержащий локаторы элементов для авторизации, полученный из `s.locators_store['login']`.
    *   Пример: `_l = {'open_login_inputs': {'by': 'css', 'value': '#nav-link-accountList'}, ...}`
*   `_d`: Объект веб-драйвера, полученный из `s.driver`.
    *   Пример: `_d` - объект, представляющий управление окном браузера.

**Подробное объяснение:**

*   Функция `login` принимает объект `s`, который должен предоставлять доступ к `locators_store` (словарь с локаторами) и `driver` (объект веб-драйвера).
*   Функция получает локаторы для элементов, связанных с процессом авторизации, из `s.locators_store['login']` и сохраняет их в переменной `_l`.
*   Получает объект веб-драйвера из `s.driver` и сохраняет в `_d`, который используется для управления браузером.
*   Функция выполняет следующие действия:
    *   Открывает страницу Amazon, кликает на кнопку входа, вводит email и пароль, нажимает кнопку "войти" .
    *   На каждом шаге происходит проверка того, что действие было выполнено, если действие не удается, то обрабатывается определенным способом, или заканчивает выполнение.
    *   Проверяет, произошел ли успешный вход, если нет, то выводит ошибку в лог, и выходит из функции.
    *   Если вход успешен, то максимизирует окно, логирует успешный вход, и возвращает `True`.
*   **Потенциальные ошибки/улучшения:**
    *   Обработка ошибок при вводе email и пароля, а также при клике по элементам, не достаточно проработана (только `return` без вывода сообщений и т.д.).
    *   Отсутствует обработка CAPTCHA и других возможных проблем.
    *   Код может быть более гибким, если локаторы будут браться не из словаря, а например, из файла или бд.
    *   В коде есть закомментированные строки, их можно удалить если они не используются.
    *   Можно использовать более информативное логирование с контекстом, чтобы отслеживать, на каком именно шаге произошла ошибка.
    *   В коде отсутствуют `docstring` для модуля.

**Взаимосвязи с другими частями проекта:**

*   **`src.logger.logger`**: Используется для записи информации о ходе выполнения авторизации, ошибок и информационных сообщений.
*   **`s` (объект поставщика)**: Является контейнером, который передаёт все необходимые данные для выполнения авторизации.
*   **Веб-драйвер:** Взаимодействие с браузером происходит через объект `_d`, который предоставляет методы для выполнения действий на веб-странице.