# Руководство по тестированию класса `ExecuteLocator`

**Описание:**

Данное руководство предназначено для тестировщиков, чтобы они могли эффективно протестировать класс `ExecuteLocator` в проекте.  Оно охватывает все необходимые шаги от установки окружения до запуска и анализа результатов тестов.

## 1. Подготовка окружения

**1.1 Установка зависимостей:**

Убедитесь, что на вашей системе установлены необходимые библиотеки.  Выполните команду в терминале:

```bash
pip install -r requirements.txt
```

Файл `requirements.txt` должен содержать следующие зависимости:

```text
pytest==7.4.0
selenium==4.16.1
```

**1.2 Настройка WebDriver:**

Установите WebDriver для браузера, который вы будете использовать для тестирования. Например, для Chrome:

* Скачайте [ChromeDriver](https://sites.google.com/chromium.org/driver/) и поместите исполняемый файл в доступный для вашей системы путь (например, в директорию PATH).


## 2. Написание тестов

**2.1 Структура тестов:**

Создайте файл `test_executor.py` в директории `tests`. Этот файл будет содержать тесты для класса `ExecuteLocator`.

```python
import pytest
from unittest.mock import MagicMock, patch
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from src.webdriver.executor import ExecuteLocator
from src.logger.exceptions import ExecuteLocatorException
```

**2.2 Реализация тестов (Подробные примеры):**

Важно использовать патчинг для имитации работы WebDriver (чтобы не запускать реальный браузер в каждом тесте). Это ускоряет тестирование и делает его более стабильным.

```python
@pytest.fixture
def driver_mock():
    return MagicMock()

@pytest.fixture
def execute_locator(driver_mock):
    return ExecuteLocator(driver_mock)

def test_get_webelement_by_locator_single_element(execute_locator, driver_mock):
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]  # Возвращает список из одного элемента

    locator = {"by": "XPATH", "selector": "//div[@id='test']"}

    result = execute_locator.get_webelement_by_locator(locator)

    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='test']")
    assert result == element
    
# ... (Другие тесты аналогично) ...
```

**Ключевые моменты:**

* **Использование `MagicMock`:**  Используйте `MagicMock` из `unittest.mock` для имитации объектов веб-драйвера и веб-элементов. Это позволяет контролировать их поведение в тестах.
* **Патчинг методов WebDriver:**  Используйте `driver_mock.find_elements.return_value` для управления возвращаемым значением метода `find_elements`.
* **Проверка ожидаемого поведения:** Используйте методы `assert_called_once_with` и `assert_called_with` из `unittest.mock`, чтобы проверить, что методы `find_elements` и `get_attribute` были вызваны с ожидаемыми аргументами.
* **Обработка ошибок:**  В тестах нужно проверять ситуации, когда элемент не найден (`driver_mock.find_elements.return_value = []`).
* **Тестирование типов возвращаемых значений:**  Проверьте корректность типов (например, `assert isinstance(result, list)`).
* **Тестирование с `typing_speed`:** В тесте `test_send_message_typing_speed` важно использовать `patch('time.sleep', return_value=None)` для имитации задержки `time.sleep`. Это предотвращает реальные задержки и позволяет проверить только логику с задержками в коде.

## 3. Запуск тестов

В корневой директории проекта выполните:

```bash
pytest tests/test_executor.py
```

## 4. Анализ результатов

`pytest` выведет результаты выполнения тестов в терминал. Обратите внимание на сообщения об ошибках, чтобы понять, где есть проблемы и исправить код.


## 5. Обновление тестов и документации

После внесения изменений в код класса `ExecuteLocator`, обновите тесты, чтобы они соответствовали новым функциям.  Обновляйте документацию в соответствии с изменениями.


**Рекомендации:**

* **Дробление тестов:** Разбейте сложные тесты на более мелкие, специализированные тесты.
* **Использование fixture:** Используйте `pytest.fixture` для подготовки данных и объектов в тестах.
* **Управление окружением:** Используйте `pytest.ini` для конфигурации pytest.
* **Достаточная проверка:** Проверяйте все значимые сценарии использования (`single_element`, `multiple_elements`, `no_element`, обработка ошибок).


Этот расширенный ответ предоставляет более практичные и подробные рекомендации по написанию эффективных тестов, что значительно улучшает качество и надежность вашего кода.