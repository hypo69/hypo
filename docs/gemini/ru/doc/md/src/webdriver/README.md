# Модуль WebDriver Executor

## Обзор

Модуль `WebDriver Executor` предоставляет фреймворк для навигации и взаимодействия с веб-страницами с помощью WebDriver. Он обрабатывает скрипты и локеры для выполнения автоматизированных действий с веб-элементами.

## Основные возможности

- **Обработка локеров:**
    - **Инициализация:** Класс `ExecuteLocator` инициализируется экземпляром WebDriver и опциональным списком аргументов и ключевых аргументов. Он настраивает WebDriver и цепочки действий для взаимодействия с веб-элементами.
    - **Выполнение локеров:** Метод `execute_locator` обрабатывает словарь локера, содержащий информацию о том, как найти и взаимодействовать с веб-элементами. Он обрабатывает различные типы локеров и действий на основе предоставленной конфигурации.
    - **Получение элементов:** Метод `get_webelement_by_locator` получает веб-элементы на основе информации локера, такой как XPATH, ID или CSS-селекторы. Он ожидает, пока элементы появятся, и может вернуть один элемент, список элементов или `False`, если элементы не найдены.
    - **Получение атрибутов:** Метод `get_attribute_by_locator` получает атрибуты из найденных элементов, используя локер. Поддерживает как отдельные, так и множественные элементы.
    - **Отправка сообщений:** Метод `send_message` отправляет текстовый ввод веб-элементам. Поддерживает симуляцию набора текста с настраиваемой скоростью и опциональным взаимодействием с мышкой.

- **Скриншоты:**
    - **Скриншот элемента:** Метод `get_webelement_as_screenshot` делает скриншот веб-элемента и возвращает его в формате PNG. Поддерживает захват скриншотов нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.

- **Действие клика:**
    - **Клик по элементу:** Метод `click` выполняет клик по веб-элементу, идентифицированному по локеру. Обрабатывает случаи, когда клик приводит к переходу на новую страницу или открытию нового окна, и регистрирует ошибки, если клик не удался.

- **Оценка локеров:**
    - **Оценка атрибутов:** Метод `evaluate_locator` оценивает атрибуты локеров, включая обработку особых случаев, когда атрибуты представлены как плейсхолдеры (например, `%EXTERNAL_MESSAGE%`).


## Обработка ошибок

Модуль использует блоки `try-except` для перехвата и регистрации ошибок во время различных операций, таких как поиск элементов, отправка сообщений и создание скриншотов. Перехватываются специфические исключения, такие как `NoSuchElementException` и `TimeoutException`, чтобы обрабатывать случаи, когда элементы не найдены или истекло время ожидания.

## Использование

### Инициализация

Создайте экземпляр `ExecuteLocator` с экземпляром WebDriver.

### Выполнение локера

Вызовите метод `execute_locator` со словарем локера для выполнения действий или получения данных от веб-элементов.

### Обработка результатов

Используйте методы, такие как `get_webelement_by_locator`, `send_message` и `get_webelement_as_screenshot`, для взаимодействия с веб-элементами и обработки результатов.


## Зависимости

Модуль использует Selenium для операций WebDriver, включая поиск элементов, отправку ключей и взаимодействие с веб-страницами. Также используются встроенные библиотеки Python для обработки исключений и управления временем.

## Пример использования

```python
from src.webdriver import Driver, Chrome
from selenium.webdriver.common.by import By

def main():
    # Основная функция для демонстрации примеров использования Driver и Chrome
    
    # Пример 1: Создание экземпляра Chrome драйвера и навигация по URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Успешно перешли на URL")
    
    # ... (другие примеры использования)
    
if __name__ == "__main__":
    main()
```

## Класс `ExecuteLocator` (Подробное описание)

```markdown
(Здесь следует подробное описание класса `ExecuteLocator` в формате markdown, включая его атрибуты, методы и их описания, как описано в вашем входном коде. Используйте заголовки, списки и структурированные разделы для улучшения читабельности.  Не забудьте привести примеры использования методов.)
```
```