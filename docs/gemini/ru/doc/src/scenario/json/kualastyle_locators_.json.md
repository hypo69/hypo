# `kualastyle_locators_.json`

## Обзор

Данный файл содержит JSON-структуру с локаторами элементов веб-страницы для использования в автоматизированном тестировании или сборе данных. Он включает в себя локаторы для меню, категорий, товаров, полей товаров, характеристик ноутбуков, наличия товара на складе и формы авторизации.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [Общие параметры](#общие-параметры)
- [Раздел `main menu`](#раздел-main-menu)
  - [`categories parent`](#categories-parent)
  - [`categories sub menu`](#categories-sub-menu)
  - [`a`](#a)
- [Раздел `store`](#раздел-store)
  - [`store categories dept-1`](#store-categories-dept-1)
  - [`store categories dept-2`](#store-categories-dept-2)
  - [`store categories dept-3`](#store-categories-dept-3)
- [Раздел `product`](#раздел-product)
  - [`link_to_product_locator`](#link_to_product_locator)
  - [`stock available`](#stock-available)
  - [`product_name_locator`](#product_name_locator)
  - [`summary_locator`](#summary_locator)
  - [`description_locator`](#description_locator)
  - [`price_locator`](#price_locator)
  - [`brand_locator`](#brand_locator)
  - [`sku_locator`](#sku_locator)
  - [`brand_sku_locator`](#brand_sku_locator)
  - [`main_image_locator`](#main_image_locator)
  - [`li_locator`](#li_locator)
- [Раздел `product_fields_locators`](#раздел-product_fields_locators)
- [Раздел `laptop_description_fields_selectors`](#раздел-laptop_description_fields_selectors)
  - [`screen`](#screen)
  - [`CPUTYPE`](#cputype)
  - [`cpu`](#cpu)
- [Раздел `stock_locator`](#раздел-stock_locator)
- [Раздел `login`](#раздел-login)
  - [`open_login_dialog_locator`](#open_login_dialog_locator)
  - [`email`](#email)
  - [`email_locator`](#email_locator)
  - [`password`](#password)
  - [`password_locator`](#password_locator)
  - [`loginbutton_locator`](#loginbutton_locator)

## Структура JSON

### Общие параметры

Для всех локаторов используются следующие общие параметры:

- `attribute`: Атрибут HTML элемента, значение которого необходимо получить или с которым нужно взаимодействовать.
- `by`: Метод поиска элемента (`XPATH`, `css selector`, `ID`, `tag name`).
- `selector`: Строка селектора для поиска элемента.
- `timeout`: Время ожидания элемента в секундах.
- `timeout_for_event`: Событие, по которому должно произойти ожидание элемента.
- `event`: Событие, которое нужно совершить с элементом (например, `click()`, `send_keys()`).

## Раздел `main menu`

### `categories parent`

**Описание**: Локатор для родительских категорий в главном меню.

**Параметры**:
- `attribute`: `"innerText"` - Получение текста элемента.
- `by`: `"XPATH"` - Поиск по XPATH.
- `selector`: `"//nav[@class,\'site-navigation\']//li[contains(@class,\'navmenu-item-parent\')][{x}]//details//summary"` - XPATH-селектор.
- `if_list`: `"first"` - Получение первого элемента из списка.
- `use_mouse`: `false` - Использование мыши не требуется.
- `mandatory`: `true` - Элемент обязателен.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `"loop"` - Событие - цикл.
- `variables in selector`: `"x"` - Переменная в селекторе.
- `formula for locator`: `"range(1,6)"` - Формула для генерации селектора.

### `categories sub menu`

**Описание**: Локатор для подменю категорий.

**Параметры**:
- `attribute`: `'{\'innerText\':\'href\'}'` - Получение текста и href атрибута.
- `by`: `"XPATH"` - Поиск по XPATH.
- `selector`: `"//nav[@class,\'site-navigation\']//li[contains(@class,\'navmenu-item-parent\')][{x}]//div[contains(@class,\'navmenu-submenu\')]//li//a"` - XPATH-селектор.
- `if_list`: `"first"` - Получение первого элемента из списка.
- `use_mouse`: `false` - Использование мыши не требуется.
- `mandatory`: `true` - Элемент обязателен.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `"click()"` - Событие - клик.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null` - Логика действия не определена.

### `a`

**Описание**: Локатор для элементов `<a>` в пагинации.

**Параметры**:
- `attribute`: `null` - Атрибут не указан.
- `by`: `"XPATH"` - Поиск по XPATH.
- `selector`: `"//ul[@class=\'pagination\']//a[@class=\'page-link\']"` - XPATH-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `"click()"` - Событие - клик.

## Раздел `store`

### `store categories dept-1`

**Описание**: Локатор для категорий первого уровня.

**Параметры**:
- `description`: `"Список главных категероий магазина"` - Описание локатора.
- `attribute`: `{'innerText': 'href'}` - Получение текста и href атрибута.
- `by`: `"XPATH"` - Поиск по XPATH.
- `selector`: `"//nav[@class=\'site-navigation\'],//ul[contains(@class,\'navmenu-depth-1\')]/li"` - XPATH-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `store categories dept-2`

**Описание**: Локатор для категорий второго уровня.

**Параметры**:
- `description`: `"Список подкатегероий магазина"` - Описание локатора.
- `attribute`: `{'innerText': 'href'}` - Получение текста и href атрибута.
- `by`: `"XPATH"` - Поиск по XPATH.
- `selector`: `"//nav[@class=\'site-navigation\'],//ul[contains(@class,\'navmenu-depth-1\')]/li//ul[contains(@class,\'navmenu-depth-2\')]/li"` - XPATH-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `store categories dept-3`

**Описание**: Локатор для категорий третьего уровня.

**Параметры**:
- `description`: `"Список подкатегероий магазина"` - Описание локатора.
- `attribute`: `{'innerText': 'href'}` - Получение текста и href атрибута.
- `by`: `"XPATH"` - Поиск по XPATH.
- `selector`: `"//nav[@class=\'site-navigation\'],//ul[contains(@class,\'navmenu-depth-1\')]/li//ul[contains(@class,\'navmenu-depth-2\')]/li//ul[contains(@class,\'navmenu-depth-3\')]/li"` - XPATH-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

## Раздел `product`

### `link_to_product_locator`

**Описание**: Локатор для ссылки на страницу товара.

**Параметры**:
- `attribute`: `"href"` - Получение href атрибута.
- `by`: `"XPATH"` - Поиск по XPATH.
- `selector`: `"//div[@class = \'product-thumb\']/a"` - XPATH-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `stock available`

**Описание**: Локатор для информации о наличии товара.

**Параметры**:
- `attribute`: `"innerText"` - Получение текста элемента.
- `by`: `"XPATH"` - Поиск по XPATH.
- `selector`: `"//div[conatins(@class , \'stockMsg\')]"` - XPATH-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `product_name_locator`

**Описание**: Локатор для названия товара.

**Параметры**:
- `attribute`: `"innerHTML"` - Получение внутреннего HTML элемента.
- `by`: `"css selector"` - Поиск по CSS селектору.
- `selector`: `"h1.d-inline-block"` - CSS-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `summary_locator`

**Описание**: Локатор для краткого описания товара.

**Параметры**:
- `attribute`: `"innerHTML"` - Получение внутреннего HTML элемента.
- `by`: `"css selector"` - Поиск по CSS селектору.
- `selector`: `"h1.d-inline-block"` - CSS-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `description_locator`

**Описание**: Локатор для полного описания товара.

**Параметры**:
- `attribute`: `"innerHTML"` - Получение внутреннего HTML элемента.
- `by`: `"css selector"` - Поиск по CSS селектору.
- `selector`: `".row.product-params.pt-2.pb-2.pt-sm-5.pb-sm-5"` - CSS-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `price_locator`

**Описание**: Локатор для цены товара.

**Параметры**:
- `attribute`: `"innerHTML"` - Получение внутреннего HTML элемента.
- `by`: `"ID"` - Поиск по ID.
- `selector`: `"basicPrice"` - ID-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `brand_locator`

**Описание**: Локатор для бренда товара.

**Параметры**:
- `attribute`: `"innerHTML"` - Получение внутреннего HTML элемента.
- `by`: `"css selector"` - Поиск по CSS селектору.
- `selector`: `"text*=\'éöøï\'"` - CSS-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `sku_locator`

**Описание**: Локатор для SKU товара.

**Параметры**:
- `attribute`: `"innerText"` - Получение текста элемента.
- `by`: `"XPATH"` - Поиск по XPATH.
- `selector`: `"//div[contains(@class,\'main-details\')]//span[contains(@class,\'sku-copy\')]"` - XPATH-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `brand_sku_locator`

**Описание**: Локатор для SKU товара.

**Параметры**:
- `attribute`: `"innerHTML"` - Получение внутреннего HTML элемента.
- `by`: `"css selector"` - Поиск по CSS селектору.
- `selector`: `"span.sku-copy"` - CSS-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `main_image_locator`

**Описание**: Локатор для главного изображения товара.

**Параметры**:
- `attribute`: `"href"` - Получение href атрибута.
- `by`: `"ID"` - Поиск по ID.
- `selector`: `"mainpic"` - ID-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `li_locator`

**Описание**: Локатор для элемента `<li>`.

**Параметры**:
- `attribute`: `"innerHTML"` - Получение внутреннего HTML элемента.
- `by`: `"tag name"` - Поиск по тегу.
- `selector`: `"li"` - Тег-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

## Раздел `product_fields_locators`

**Описание**: Пустой раздел для локаторов полей товаров.

## Раздел `laptop_description_fields_selectors`

### `screen`

**Описание**: Локатор для характеристики "экран" ноутбука.

**Параметры**:
- `attribute`: `"innerHTML"` - Получение внутреннего HTML элемента.
- `by`: `"css selector"` - Поиск по CSS селектору.
- `selector`: `"text*=\'âåãì îñê\'"` - CSS-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `CPUTYPE`

**Описание**: Локатор для характеристики "Тип процессора" ноутбука.

**Параметры**:
- `attribute`: `"innerHTML"` - Получение внутреннего HTML элемента.
- `by`: `"css selector"` - Поиск по CSS селектору.
- `selector`: `"text*=\'CPUTYPE\'"` - CSS-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

### `cpu`

**Описание**: Локатор для характеристики "Процессор" ноутбука.

**Параметры**:
- `attribute`: `"innerHTML"` - Получение внутреннего HTML элемента.
- `by`: `"css selector"` - Поиск по CSS селектору.
- `selector`: `"text=\'îòáã\'"` - CSS-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

## Раздел `stock_locator`

**Описание**: Локатор для информации о наличии товара на складе.

**Параметры**:
- `attribute`: `"innerHTML"` - Получение внутреннего HTML элемента.
- `by`: `"css selector"` - Поиск по CSS селектору.
- `selector`: `".stockMsg"` - CSS-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `null` - Событие не определено.

## Раздел `login`

### `open_login_dialog_locator`

**Описание**: Локатор для открытия диалога авторизации.

**Параметры**:
- `attribute`: `null` - Атрибут не указан.
- `by`: `"XPATH"` - Поиск по XPATH.
- `selector`: `"//a[contains(@data-modal,\'User\')]"` - XPATH-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `"click()"` - Событие - клик.

### `email`

**Описание**: Email для авторизации.

### `email_locator`

**Описание**: Локатор для поля ввода email.

**Параметры**:
- `attribute`: `null` - Атрибут не указан.
- `by`: `"ID"` - Поиск по ID.
- `selector`: `"Email"` - ID-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `"send_keys(\'sales@aluf.co.il\')"` - Событие - ввод текста.

### `password`

**Описание**: Пароль для авторизации.

### `password_locator`

**Описание**: Локатор для поля ввода пароля.

**Параметры**:
- `attribute`: `null` - Атрибут не указан.
- `by`: `"ID"` - Поиск по ID.
- `selector`: `"Password"` - ID-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `"send_keys(\'9643766\')"` - Событие - ввод текста.

### `loginbutton_locator`

**Описание**: Локатор для кнопки входа.

**Параметры**:
- `attribute`: `null` - Атрибут не указан.
- `by`: `"css selector"` - Поиск по CSS селектору.
- `selector`: `".btn.btn-primary.btn-lg.w-50.float-left.mr-2"` - CSS-селектор.
- `timeout`: `0` - Время ожидания равно 0.
- `timeout_for_event`: `"presence_of_element_located"` - Ожидание присутствия элемента.
- `event`: `"click()"` - Событие - клик.