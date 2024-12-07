# Руководство по тестированию класса `ExecuteLocator`

## Обзор

Это руководство предоставляет инструкции по тестированию класса `ExecuteLocator` для работы с веб-элементами через Selenium WebDriver.  Оно описывает установку среды, написание тестов и их запуск.

## Оглавление

- [Руководство по тестированию класса `ExecuteLocator`](#руководство-по-тестированию-класса-executelocator)
- [Введение](#введение)
- [Подготовка окружения](#подготовка-окружения)
  - [Установка зависимостей](#установка-зависимостей)
  - [Настройка WebDriver](#настройка-webdriver)
- [Написание тестов](#написание-тестов)
  - [Структура тестов](#структура-тестов)
  - [Реализация тестов](#реализация-тестов)
- [Запуск тестов](#запуск-тестов)
- [Проверка результатов тестирования](#проверка-результатов-тестирования)
- [Обновление тестов](#обновление-тестов)
- [Документация](#документация)
- [Пример документации для тестов](#пример-документации-для-тестов)
- [Дополнительные ресурсы](#дополнительные-ресурсы)


## Введение

Класс `ExecuteLocator` предназначен для взаимодействия с веб-элементами через Selenium WebDriver. Он предоставляет методы для работы с элементами, такие как получение атрибутов и отправка сообщений.  Это руководство поможет вам написать тесты, покрывающие различные сценарии использования.

## Подготовка окружения

### Установка зависимостей

Убедитесь, что у вас установлены необходимые библиотеки. Выполните команду:

```bash
pip install -r requirements.txt
```

`requirements.txt` должен содержать следующие зависимости:

```
pytest==7.4.0
selenium==4.16.1
```

### Настройка WebDriver

Установите WebDriver для вашего браузера (например, ChromeDriver для Chrome).

## Написание тестов

### Структура тестов

Создайте файл `test_executor.py` в директории `tests`.  В нём будут находиться тесты для класса `ExecuteLocator`.  Пример:

```python
# ... (Импорты) ...

@pytest.fixture
def driver_mock():
    return MagicMock()

@pytest.fixture
def execute_locator(driver_mock):
    return ExecuteLocator(driver_mock)

# ... (Тесты) ...
```

### Реализация тестов

Ниже приведены примеры реализованных тестов для метода `get_webelement_by_locator`:

```python
# ... (Импорты) ...

def test_get_webelement_by_locator_single_element(execute_locator, driver_mock):
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]
    locator = {"by": "XPATH", "selector": "//div[@id='test']"}
    result = execute_locator.get_webelement_by_locator(locator)
    # Проверка вызова find_elements
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='test']")
    assert result == element
    
# ... (другие тесты) ...
```

(Аналогичные тесты для остальных методов: `get_attribute_by_locator`, `send_message`)

Обратите внимание на использование `MagicMock` для имитации поведения `WebDriver` и ассертов для проверки ожидаемых действий.  Все примеры тестов демонстрируют валидацию возвращаемых значений и вызовов.

## Запуск тестов

Для запуска тестов выполните команду в корневой директории проекта:

```bash
pytest tests/test_executor.py
```

## Проверка результатов тестирования

`pytest` выведет результаты в терминале. Проверьте, что все тесты прошли успешно.

## Обновление тестов

По мере изменения кода класса `ExecuteLocator`  обновляйте тесты, чтобы они отражали новые функции и функциональность.

## Документация

Создайте документацию, чтобы описать поведение и использование класса `ExecuteLocator`, а также логику и цель тестов.

## Пример документации для тестов

(Указанная в запросе документация уже приведена)


## Дополнительные ресурсы

- [Официальная документация pytest](https://docs.pytest.org/en/latest/)
- [Документация Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/)
- [Руководство по написанию тестов для Python](https://docs.python.org/3/library/unittest.html)


Следуйте этому руководству для эффективного тестирования класса `ExecuteLocator` и обеспечения его правильной работы.  Обращайтесь к разработчикам и тестировщикам при возникновении вопросов.