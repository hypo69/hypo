# ИНСТРУКЦИЯ по установке Chrome для тестирования

## Обзор

Этот документ описывает шаги по установке Google Chrome для автоматизированного тестирования веб-приложений с использованием Selenium WebDriver.

## Требования

- Установленная операционная система (например, Windows, macOS или Linux).
- Установленный Python.
- Установленный пакет `selenium`.

## Установка Chrome

1. **Загрузка Chrome:** Перейдите на [сайт загрузки Chrome](https://www.google.com/chrome/) и загрузите последнюю версию стабильной сборки.  Выберите соответствующий установочный пакет для вашей операционной системы (например, `.exe` для Windows).

2. **Установка Chrome:** Запустите загруженный установочный файл и следуйте инструкциям мастера установки. Примите условия лицензионного соглашения и выберите папку для установки, если необходимо.

3. **Установка WebDriver:**
    - Откройте командную строку или терминал.
    - Перейдите в каталог, где установлен Chrome.
    - Откройте папку `chromedriver`.
    - В этой папке должен быть исполняемый файл ChromeDriver (например, `chromedriver.exe` для Windows, `chromedriver` для macOS/Linux).

4. **Установка Selenium:**
   - Убедитесь, что у вас установлен Python.
   - В командной строке или терминале используйте pip:
     ```bash
     pip install selenium
     ```

5. **Добавление пути к ChromeDriver:**
   - Для корректной работы Selenium необходимо добавить путь к папке с ChromeDriver в переменные среды вашей операционной системы. Это позволит WebDriver обнаружить исполняемый файл.
   - **Windows:**
     - Нажмите правой кнопкой мыши на «Этот компьютер» и выберите «Свойства».
     - Откройте «Переменные среды».
     - Найдите переменную `Path` и дважды щелкните по ней.
     - В новом окне нажмите «Новое» и введите путь к папке с `chromedriver.exe`.
   - **macOS/Linux:**
     - Добавьте путь к `chromedriver` в переменную окружения `PATH`.


## Использование

После установки ChromeDriver и добавления пути в переменные среды вы можете использовать его в своих скриптах Python с помощью Selenium.


##  Возможные ошибки

- **Ошибка `ModuleNotFoundError`:** Убедитесь, что Selenium установлен.
- **Ошибка `chromedriver`:**  Проверьте, что `chromedriver` находится в указанном пути.  Убедитесь, что вы указали версию драйвера соответствующую вашей версии Chrome.
- **Ошибка установки:** Проверьте доступность интернета.
- **Разные версии Chrome и WebDriver:** Убедитесь, что версия WebDriver соответствует версии Chrome.

## Пример использования в Python

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def initialize_webdriver(chrome_driver_path: str) -> webdriver.Chrome:
    """
    Инициализирует вебдрайвер Chrome.

    Args:
        chrome_driver_path (str): Путь к исполняемому файлу ChromeDriver.

    Returns:
        webdriver.Chrome: Объект вебдрайвера.

    Raises:
        FileNotFoundError: Если ChromeDriver не найден по указанному пути.
    """
    try:
        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        return driver
    except FileNotFoundError as ex:
        raise FileNotFoundError(f"Ошибка: ChromeDriver не найден по пути {chrome_driver_path}.") from ex

# Пример использования:
# driver = initialize_webdriver("/path/to/chromedriver")

```

## Дополнительная информация

Дополнительная информация о работе с Selenium WebDriver доступна в [документации Selenium](https://selenium-python.readthedocs.io/).