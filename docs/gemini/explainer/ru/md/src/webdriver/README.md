# Модуль `Driver` (webdriver)

## Обзор

Модуль `Driver` предоставляет реализацию WebDriver, интегрирующую стандартные функциональности WebDriver с дополнительными методами для работы с веб-страницами, обработки JavaScript и управления куки. Он использует возможности Selenium WebDriver и собственные расширения для поддержки различных задач автоматизации веб-приложений.

## Основные особенности:

* Наследуется от указанного класса WebDriver (например, Chrome, Firefox, Edge) и добавляет дополнительную функциональность.
* Содержит методы для прокрутки, управления куки, взаимодействия с веб-элементами и выполнения JavaScript.
* Предоставляет утилиты для управления окнами браузера и взаимодействия со страницами.

## Компоненты:

1. **Класс `DriverBase`:**
   * **Атрибуты:**
     * `previous_url`: Хранит предыдущий URL.
     * `referrer`: Хранит URL referrer.
     * `page_lang`: Хранит язык страницы.
     * Различные атрибуты, связанные с взаимодействием с веб-элементами и выполнением JavaScript.
   * **Методы:**
     * `scroll`: Прокручивает веб-страницу в заданном направлении. Поддерживает прокрутку вперед, назад или в обе стороны.
     * `locale`: Пытается определить язык страницы, проверяя мета-теги или используя JavaScript.
     * `get_url`: Загружает указанный URL.
     * `extract_domain`: Извлекает домен из URL.
     * `_save_cookies_localy`: Сохраняет куки в локальный файл.
     * `page_refresh`: Обновляет текущую страницу.
     * `window_focus`: Фокусирует окно браузера с помощью JavaScript.
     * `wait`: Ожидает указанный интервал.
     
2. **Класс `DriverMeta`:**
   * **Методы:**
     * `__call__`: Создает новый класс `Driver`, объединяющий указанный класс WebDriver (Chrome, Firefox, Edge) с `DriverBase`. Инициализирует методы JavaScript и функциональности выполнения локаторов.

3. **Класс `Driver`:**
   * **Описание:** Динамически созданный класс WebDriver, наследующий от `DriverBase` и указанного класса WebDriver.
   * **Пример использования:**
     ```python
     from src.webdriver import Driver, Chrome, Firefox, Edge
     d = Driver(Chrome)
     ```

## Использование:

* **Инициализация:** Создайте экземпляр `Driver` с конкретным классом WebDriver.
* **Функциональность:** Используйте методы, такие как `scroll`, `get_url`, `extract_domain`, `page_refresh`, для взаимодействия с веб-страницами.  Класс также предоставляет методы для выполнения JavaScript и управления куками.


## Зависимости:

* **Selenium:** Используется для операций WebDriver, включая поиск элементов, прокрутку и взаимодействие с веб-страницами.
* **Встроенные библиотеки Python:** Используются для обработки исключений, управления временем и других задач.


## Примеры использования:

Примеры, представленные в исходном коде, демонстрируют различные методы класса `Driver`.  Они включают навигацию по URL, извлечение домена, сохранение куки, обновление страницы, прокрутку, получение языка страницы, настройку пользовательского агента, поиск элемента, получение текущего URL и фокусировку окна.


## Модуль `ExecuteLocator` (executor.py):

Этот модуль содержит класс `ExecuteLocator`, предназначенный для выполнения различных действий над элементами веб-страницы с использованием Selenium WebDriver.

## Общий Структура и Цель:

* **Основное назначение:** `ExecuteLocator` выполняет навигацию и взаимодействие с веб-страницей, используя данные из словарей локаторов.


## Основные компоненты:

* **Импорты:** Импортирует необходимые библиотеки Selenium и внутренние модули для работы с настройками, логированием и обработкой исключений.

* **Класс `ExecuteLocator`:**
    * **Атрибуты:**
        * `driver`: Экземпляр WebDriver для взаимодействия с браузером.
        * `actions`: Экземпляр `ActionChains` для выполнения сложных действий над веб-элементами.
        * `by_mapping`: Словарь для сопоставления строк локаторов с объектами Selenium `By`.

    * **Методы:**
        * `__init__`: Инициализирует WebDriver и `ActionChains`.
        * `execute_locator`: Основной метод для выполнения действий, основанных на словаре локаторов.
        * `get_webelement_by_locator`: Возвращает веб-элемент, найденный по локатору.
        * `get_attribute_by_locator`: Возвращает атрибут веб-элемента.
        * `send_message`: Отправляет текстовое сообщение веб-элементу.
        * `evaluate_locator`: Оценивает атрибуты локатора (обработка замены параметров).
        * Другие вспомогательные методы для поиска и взаимодействия с элементами.

## Примечания:

* Обратите внимание на примеры локаторов в json формате, которые содержат информацию о способе нахождения и взаимодействии с элементами.

* Файл содержит примеры использования различных методов и  обработку ошибок.


Этот расширенный ответ предоставляет более подробное и структурированное объяснение модулей `Driver` и `ExecuteLocator`.