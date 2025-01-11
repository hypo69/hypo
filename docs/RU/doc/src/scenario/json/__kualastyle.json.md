# Документация для `kualastyle.json`

## Обзор

Файл `kualastyle.json` содержит конфигурационные данные для парсинга веб-сайта поставщика "kualastyle". Этот файл определяет основные параметры и настройки, необходимые для сбора данных о товарах, таких как категории, URL-адреса, правила ценообразования и другие настройки.

## Содержание

1.  [Обзор](#обзор)
2.  [Описание JSON-структуры](#описание-json-структуры)
    *   [Ключи верхнего уровня](#ключи-верхнего-уровня)
3.  [Использование](#использование)

## Описание JSON-структуры

### Ключи верхнего уровня

*   `supplier` (str): Название поставщика, в данном случае "kualastyle".
*   `supplier_id` (str): Идентификатор поставщика, "11028".
*   `supplier_prefix` (str): Префикс поставщика, используется для формирования уникальных идентификаторов, "kualastyle".
*   `start_url` (str): Начальный URL сайта поставщика, "https://kualastyle.com".
*   `login_url` (str): URL для входа на сайт поставщика, в данном случае совпадает с `start_url`.
*    `check categories on site` (bool): Флаг, указывающий на необходимость проверки категорий на сайте, `true`.
*   `if_login` (bool): Флаг, указывающий на необходимость входа на сайт, `true`.
*   `price_rule` (str): Правило для расчета цены, в данном случае "умножить на 1".
*    `if_list` (str): Определяет как брать список, значение "first".
*    `use_mouse` (bool): Флаг, указывающий на необходимость использовать мышь, `false`.
*    `mandatory` (bool): Флаг, указывающий является ли обязательным, `true`.
*   `parcing method [webdriver|api]` (str): Метод парсинга, используется "web".
*   `about method web scrapping [webdriver|api]` (str): Описание метода парсинга, "Если я работаю через API мне не нужен webdriver".
*   `collect_products_from_categorypage` (bool): Флаг, указывающий на необходимость собирать товары прямо со страницы категории, `false`.
*   `num_items_4_flush` (int): Количество элементов для сброса, 500.
*   `scenario_files` (list): Список файлов сценариев для сбора данных из различных категорий товаров, включает в себя:
    *   `kualastyle_categories_accessories.json`
    *   `kualastyle_categories_appliances.json`
    *   `kualastyle_categories_carpets.json`
    *   `kualastyle_categories_children_and_youth.json`
    *   `kualastyle_categories_furniture.json`
    *   `kualastyle_categories_lighting.json`
    *   `kualastyle_categories_mattresses.json`
    *   `kualastyle_categories_mirrors.json`
    *   `kualastyle_categories_photos.json`
    *   `kualastyle_categories_textile.json`
*   `last_runned_scenario` (str): Имя последнего запущенного сценария, пока не задано.
*   `excluded` (list): Список исключенных элементов, пока пуст.

## Использование

Этот файл используется для настройки процесса сбора данных с сайта `kualastyle.com`. Он определяет, как следует подключаться к сайту, какие категории товаров следует парсить, и какие правила следует применять к ценам. Файл является отправной точкой для запуска скриптов парсинга.