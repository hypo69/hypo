# ИНСТРУКЦИЯ по установке ChromeDriver для тестирования

## Обзор

Данный документ описывает процесс установки ChromeDriver для автоматизированного тестирования с помощью Selenium WebDriver на платформе Chrome.

## Оглавление

* [Установка ChromeDriver](#Установка-ChromeDriver)
* [Проверка установки](#Проверка-установки)


## Установка ChromeDriver

1. **Скачивание:** Перейдите на страницу загрузки ChromeDriver на сайте [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).
2. **Выбор версии:** Выберите версию ChromeDriver, соответствующую вашей версии браузера Chrome.  Важно выбрать версию, которая совместима с вашей версией Chrome, иначе возможны ошибки.
3. **Загрузка:** Скачайте подходящий архив с установщиком.
4. **Установка:**  Разместите скачанный архив ChromeDriver в удобном для вас месте (например, в папке с проектом).
5. **Добавление в PATH (рекомендуется):**  Для удобства работы, добавьте путь к папке с ChromeDriver в переменную среды PATH. Это позволит запускать ChromeDriver из любой точки вашей системы.  Подробная инструкция по добавлению в PATH зависит от вашей операционной системы.

## Проверка установки

1. **Откройте командную строку (или терминал).**
2. **Введите команду:**
   ```bash
   chromedriver --version
   ```
3. **Если вывод содержит информацию о версии ChromeDriver, установка прошла успешно.**  Если вы получаете ошибку, проверьте правильность шагов установки и корректность пути к исполняемому файлу ChromeDriver.