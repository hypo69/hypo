# Шаги по настройке профиля Firefox для Selenium WebDriver

## Обзор

Данный документ содержит инструкцию по настройке пользовательского профиля Firefox для использования с Selenium WebDriver.  Это необходимо для более надежной и управляемой автоматизации тестирования.

## Оглавление

* [Шаги по настройке профиля Firefox для Selenium WebDriver](#шаги-по-настройке-профиля-firefox-для-selenium-webdriver)
* [Обзор](#обзор)
* [Что такое профиль](#что-такое-профиль)
* [Зачем нужен новый профиль](#зачем-нужен-новый-профиль)
* [Как найти папку профиля](#как-найти-папку-профиля)
* [Создание нового профиля](#создание-нового-профиля)
    * [Шаг 1: Запуск менеджера профилей](#шаг-1-запуск-менеджера-профилей)
    * [Шаг 2: Создание нового профиля](#шаг-2-создание-нового-профиля)
* [Использование пользовательского профиля в Selenium](#использование-пользовательского-профиля-в-selenium)


## Что такое профиль

Профиль Firefox — это набор файлов, содержащих личную информацию пользователя, такую как закладки, пароли и настройки.  Каждый профиль хранится отдельно от файлов программы Firefox. Можно создавать несколько профилей для разных целей.

## Зачем нужен новый профиль

Стандартный профиль Firefox не подходит для автоматизации.  Для надежного автоматического тестирования с помощью Selenium рекомендуется создать отдельный профиль. Такой профиль должен быть легким и содержать необходимые настройки (например, прокси) для стабильного выполнения тестов.

Следует использовать один и тот же профиль на всех машинах разработки и тестирования.  Использование разных профилей может привести к различиям в сертификатах SSL и установленных плагинах, что повлияет на поведение тестов.

## Как найти папку профиля

Расположение папки профиля зависит от операционной системы.  Ниже приведена таблица типичных путей:

| Операционная система | Путь к папке профиля |
|---|---|
| Windows XP/2000/Vista/7 | `%AppData%\Mozilla\Firefox\Profiles\xxxxxxxx.default` |
| Linux | `~/.mozilla/firefox/xxxxxxxx.default/` |
| Mac OS X | `~/Library/Application Support/Firefox/Profiles/xxxxxxxx.default/` |

`xxxxxxxx` — случайная строка, которая гарантирует уникальность профиля. Firefox автоматически генерирует её для новых профилей.

## Создание нового профиля

### Шаг 1: Запуск менеджера профилей

1. Закройте Firefox.
2. Используйте диалог "Выполнить" (Win+R) для запуска Firefox с параметром `-p`. На Windows 32-бит: `"C:Program FilesMozilla Firefoxfirefox.exe" -p`, а на 64-бит: `"C:Program Files (x86)Mozilla Firefoxfirefox.exe" -p`.

### Шаг 2: Создание нового профиля

1. В окне менеджера профилей нажмите "Создать профиль...".
2. Нажмите "Далее" в появившемся окне мастера создания профиля.
3. Введите имя нового профиля (например, "profileToolsQA") и нажмите "Готово".

## Использование пользовательского профиля в Selenium

После создания профиля необходимо указать его при инициализации драйвера Firefox в скриптах Selenium:

```java
ProfilesIni profile = new ProfilesIni();
FirefoxProfile myprofile = profile.getProfile("profileToolsQA");
WebDriver driver = new FirefoxDriver(myprofile);
```

**Примечание:**  Код на Java приведен в качестве примера,  могут быть использованы и другие языки программирования с соответствующей библиотекой для Selenium.  Убедитесь, что профиль с именем "profileToolsQA" существует.