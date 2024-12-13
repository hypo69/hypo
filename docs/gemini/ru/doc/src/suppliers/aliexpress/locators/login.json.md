# Документация для locators/login.json

## Обзор

Данный файл содержит JSON-объект с локаторами для веб-страницы логина и настроек языка/валюты/доставки AliExpress. Локаторы определены для элементов страницы, используемых при автоматизации тестирования или скрапинга.

## Содержание
- [Раздел "login"](#login)
  - [Локатор `close banner`](#close-banner)
  - [Локатор `open_login`](#open_login)
  - [Локатор `email_locator`](#email_locator)
  - [Локатор `password_locator`](#password_locator)
  - [Локатор `loginbutton_locator`](#loginbutton_locator)
  - [Локатор `cookies_accept`](#cookies_accept)
- [Раздел "currency_language_shipto_locators"](#currency_language_shipto_locators)
  - [Локатор `currency_language_shipto_block_opener_locator`](#currency_language_shipto_block_opener_locator)
  - [Локатор `shipto_locator`](#shipto_locator)
  - [Локатор `language_locator`](#language_locator)
  - [Локатор `currency_locator`](#currency_locator)
  - [Локатор `save_button_locator`](#save_button_locator)

## Раздел "login"

### Локатор `close banner`

**Описание**: Локатор для кнопки закрытия баннера, если он появляется.

**Параметры**:
- `attribute` (str):  `text` - атрибут, по которому ищем.
- `by` (str):  `XPATH` - тип локатора.
- `selector` (str):  `//div[contains(text(), \'אפשר\')]` - XPATH селектор.
- `timeout` (int):  `0` - таймаут для поиска элемента.
- `timeout_for_event` (str):  `presence_of_element_located` - событие, при котором элемент должен быть найден.
- `event` (str):  `send_keys(Key.RETURN)` - событие, которое должно произойти с элементом.
- `if_list` (str): `first` - если найдено несколько элементов, использовать первый.
- `use_mouse` (bool):  `false` - не использовать мышь для взаимодействия.
- `mandatory` (bool):  `true` - элемент обязательный.
- `locator_description` (str): "" - описание локатора.

### Локатор `open_login`

**Описание**: Локатор для кнопки открытия формы логина.

**Параметры**:
- `attribute` (str):  `null` - атрибут не задан.
- `by` (str):  `XPATH` - тип локатора.
- `selector` (str):  `//div[@class = \'account-main\']//span[. = \'Sign in\'] | //div[@class = \'account-main\']//span[. = \'Se connecter\'] | //div[@class = \'account-main\']//span[. = \'כניסה\'] ` - XPATH селектор.
- `timeout` (int):  `0` - таймаут для поиска элемента.
- `timeout_for_event` (str):  `presence_of_element_located` - событие, при котором элемент должен быть найден.
- `event` (str):  `click()` - событие, которое должно произойти с элементом.
- `if_list` (str): `first` - если найдено несколько элементов, использовать первый.
- `use_mouse` (bool):  `false` - не использовать мышь для взаимодействия.
- `mandatory` (bool):  `true` - элемент обязательный.
- `locator_description` (str): "" - описание локатора.

### Локатор `email_locator`

**Описание**: Локатор для поля ввода электронной почты.

**Параметры**:
- `attribute` (str):  `null` - атрибут не задан.
- `by` (str):  `XPATH` - тип локатора.
- `selector` (str):  `//input[@id=\'fm-login-id\']` - XPATH селектор.
- `timeout` (int):  `0` - таймаут для поиска элемента.
- `timeout_for_event` (str):  `presence_of_element_located` - событие, при котором элемент должен быть найден.
- `event` (str):  `send_keys(\'one.last.bit@gmail.com\')` - событие, которое должно произойти с элементом.
- `if_list` (str): `first` - если найдено несколько элементов, использовать первый.
- `use_mouse` (bool):  `false` - не использовать мышь для взаимодействия.
- `mandatory` (bool):  `true` - элемент обязательный.
- `locator_description` (str): "" - описание локатора.

### Локатор `password_locator`

**Описание**: Локатор для поля ввода пароля.

**Параметры**:
- `attribute` (str):  `null` - атрибут не задан.
- `by` (str):  `XPATH` - тип локатора.
- `selector` (str):  `//input[@id=\'fm-login-password\']` - XPATH селектор.
- `timeout` (int):  `0` - таймаут для поиска элемента.
- `timeout_for_event` (str):  `presence_of_element_located` - событие, при котором элемент должен быть найден.
- `event` (str):  `send_keys(\'7p3ato9kijsosw7\')` - событие, которое должно произойти с элементом.
- `if_list` (str): `first` - если найдено несколько элементов, использовать первый.
- `use_mouse` (bool):  `false` - не использовать мышь для взаимодействия.
- `mandatory` (bool):  `true` - элемент обязательный.
- `locator_description` (str): "" - описание локатора.

### Локатор `loginbutton_locator`

**Описание**: Локатор для кнопки входа в систему.

**Параметры**:
- `attribute` (str):  `null` - атрибут не задан.
- `by` (str):  `XPATH` - тип локатора.
- `selector` (str):  `//button[@type=\'submit\']` - XPATH селектор.
- `timeout` (int):  `0` - таймаут для поиска элемента.
- `timeout_for_event` (str):  `presence_of_element_located` - событие, при котором элемент должен быть найден.
- `event` (str):  `click()` - событие, которое должно произойти с элементом.
- `if_list` (str): `first` - если найдено несколько элементов, использовать первый.
- `use_mouse` (bool):  `false` - не использовать мышь для взаимодействия.
- `mandatory` (bool):  `true` - элемент обязательный.
- `locator_description` (str): "" - описание локатора.

### Локатор `cookies_accept`

**Описание**: Локатор для кнопки принятия cookie.

**Параметры**:
- `attribute` (str):  `null` - атрибут не задан.
- `by` (str):  `XPATH` - тип локатора.
- `selector` (str):  `//button[contains(@data-role,\'gdpr-accept\')]` - XPATH селектор.
- `timeout` (int):  `0` - таймаут для поиска элемента.
- `timeout_for_event` (str):  `presence_of_element_located` - событие, при котором элемент должен быть найден.
- `event` (str):  `click()` - событие, которое должно произойти с элементом.
- `if_list` (str): `first` - если найдено несколько элементов, использовать первый.
- `use_mouse` (bool):  `false` - не использовать мышь для взаимодействия.
- `mandatory` (bool):  `true` - элемент обязательный.
- `locator_description` (str): "" - описание локатора.

## Раздел "currency_language_shipto_locators"

### Локатор `currency_language_shipto_block_opener_locator`

**Описание**: Локатор для кнопки открытия блока выбора валюты, языка и доставки.

**Параметры**:
- `attribute` (str):  `null` - атрибут не задан.
- `by` (str):  `XPATH` - тип локатора.
- `selector` (str):  `//div[@data-role = \'region-pannel\']/a` - XPATH селектор.
- `timeout` (int):  `0` - таймаут для поиска элемента.
- `timeout_for_event` (str):  `presence_of_element_located` - событие, при котором элемент должен быть найден.
- `event` (str):  `click()` - событие, которое должно произойти с элементом.
- `if_list` (str): `first` - если найдено несколько элементов, использовать первый.
- `use_mouse` (bool):  `false` - не использовать мышь для взаимодействия.
- `mandatory` (bool):  `true` - элемент обязательный.
- `locator_description` (str): "" - описание локатора.

### Локатор `shipto_locator`

**Описание**: Локатор для выбора страны доставки.
    
**Параметры**:
- `attribute` (list[str]):  `[null, null, null]` - атрибуты не заданы.
- `by` (list[str]):  `["XPATH", "XPATH", "XPATH"]` - типы локаторов.
- `selector` (list[str]):  `["//a[contains(@class,\'address-select-trigger\') and contains(@data-role,\'country\')]", "//div[@class = \'filter-list-container\']", "//li[contains(@data-code,\'il\')]"]` - XPATH селекторы.
- `timeout` (int):  `0` - таймаут для поиска элемента.
- `timeout_for_event` (str):  `presence_of_element_located` - событие, при котором элемент должен быть найден.
- `event` (list[str]):  `["click()", "click()", "click()"]` - события, которые должны произойти с элементами.
- `if_list` (str): `first` - если найдено несколько элементов, использовать первый.
- `use_mouse` (bool):  `false` - не использовать мышь для взаимодействия.
- `mandatory` (bool):  `true` - элемент обязательный.
- `locator_description` (str): "" - описание локатора.

### Локатор `language_locator`

**Описание**: Локатор для выбора языка.
    
**Параметры**:
- `attribute` (list[str]):  `[null, null, null]` - атрибуты не заданы.
- `by` (list[str]):  `["XPATH", "XPATH", "XPATH"]` - типы локаторов.
- `selector` (list[str]):  `["//span[contains( @data-role , \'language-input\')]", "//input[contains(@data-role,\'language-search\')]", "//a[contains(@data-locale,\'en-US\')]"]` - XPATH селекторы.
- `timeout` (int):  `0` - таймаут для поиска элемента.
- `timeout_for_event` (str):  `presence_of_element_located` - событие, при котором элемент должен быть найден.
- `event` (list[str]):  `["click()", "click()", "click()"]` - события, которые должны произойти с элементами.
- `if_list` (str): `first` - если найдено несколько элементов, использовать первый.
- `use_mouse` (bool):  `false` - не использовать мышь для взаимодействия.
- `mandatory` (bool):  `true` - элемент обязательный.
- `locator_description` (str): "" - описание локатора.

### Локатор `currency_locator`

**Описание**: Локатор для выбора валюты.

**Параметры**:
- `attribute` (list[str]):  `[null, null, null]` - атрибуты не заданы.
- `by` (list[str]):  `["XPATH", "XPATH", "XPATH"]` - типы локаторов.
- `selector` (list[str]):  `["//div[contains(@class , \'switcher-currency-c language-selector\')]", "//span[contains(@class , \'select-item\')]", "//a[contains(@data-currency , \'ILS\')]"]` - XPATH селекторы.
- `timeout` (int):  `0` - таймаут для поиска элемента.
- `timeout_for_event` (str):  `presence_of_element_located` - событие, при котором элемент должен быть найден.
- `event` (list[str]):  `["click()", "click()", "click()"]` - события, которые должны произойти с элементами.
- `if_list` (str): `first` - если найдено несколько элементов, использовать первый.
- `use_mouse` (bool):  `false` - не использовать мышь для взаимодействия.
- `mandatory` (bool):  `true` - элемент обязательный.
- `locator_description` (str): "" - описание локатора.

### Локатор `save_button_locator`

**Описание**: Локатор для кнопки сохранения выбранных настроек.

**Параметры**:
- `attribute` (str):  `null` - атрибут не задан.
- `by` (str):  `XPATH` - тип локатора.
- `selector` (str):  `//div[contains(@class , \'switcher-btn\')]` - XPATH селектор.
- `timeout` (int):  `0` - таймаут для поиска элемента.
- `timeout_for_event` (str):  `presence_of_element_located` - событие, при котором элемент должен быть найден.
- `event` (str):  `click()` - событие, которое должно произойти с элементом.
- `if_list` (str): `first` - если найдено несколько элементов, использовать первый.
- `use_mouse` (bool):  `false` - не использовать мышь для взаимодействия.
- `mandatory` (bool):  `true` - элемент обязательный.
- `locator_description` (str): "" - описание локатора.