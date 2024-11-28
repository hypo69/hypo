# Инструкция по установке ChromeDriver для тестирования

## Обзор

Данный документ описывает шаги по установке ChromeDriver для выполнения автотестов с использованием Selenium WebDriver.  ChromeDriver необходим для взаимодействия с браузером Chrome.

## Оглавление

* [Установка ChromeDriver](#установка-chromedriver)
* [Проверка установки](#проверка-установки)


## Установка ChromeDriver

1. **Загрузите ChromeDriver:** Перейдите на страницу загрузки ChromeDriver [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)  и выберите версию, соответствующую вашей версии Chrome.
2. **Выберите версию:** Найдите версию Chrome, которую вы используете. Выберите соответствующий ChromeDriver.
3. **Загрузите файл:** Скачайте загруженный файл ChromeDriver в удобное для вас место.
4. **Разместите ChromeDriver:** Разместите загруженный файл ChromeDriver в папку, которая будет доступна вашему скрипту Python. Например, в папку `./drivers` или `./tools/drivers`.
5. **Добавьте путь к ChromeDriver в переменные окружения (рекомендуется):**
    * Откройте переменные среды вашей операционной системы.
    * Найдите переменную `PATH`.
    * Добавьте путь к папке, куда вы поместили ChromeDriver, в переменную `PATH`, разделив пути точкой с запятой.
6. **Проверьте работоспособность:** Запустите скрипт Python, использующий ChromeDriver. Если скрипт работает корректно, то ChromeDriver установлен правильно.


## Проверка установки

Для проверки правильности установки ChromeDriver, выполните следующий код Python:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def check_chromedriver():
    """
    Проверяет установку ChromeDriver.

    Returns:
        bool: True, если ChromeDriver установлен и работает корректно, иначе False.
    """
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.quit()
        return True
    excep
    t Exception as e:
        print(f"Ошибка при установке ChromeDriver: {e}")
        return False

if __name__ == "__main__":
    if check_chromedriver():
        print("ChromeDriver установлен и работает корректно!")
    else:
        print("Произошла ошибка при установке ChromeDriver.")

```

Этот код загрузит ChromeDriver с помощью `webdriver_manager`, запустит браузер Chrome и проверит работоспособность.  Если ChromeDriver установлен корректно, будет выведено сообщение "ChromeDriver установлен и работает корректно!". В противном случае, вы увидите сообщение об ошибке.  Этот код следует запускать перед выполнением остальных тестов.