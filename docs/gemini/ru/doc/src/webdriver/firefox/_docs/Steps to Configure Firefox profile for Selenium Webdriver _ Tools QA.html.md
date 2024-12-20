# Настройка профиля Firefox для Selenium WebDriver

## Обзор

Этот HTML-файл содержит статью с пошаговыми инструкциями по настройке пользовательского профиля Firefox для использования с Selenium WebDriver. Статья объясняет, что такое профиль Firefox, почему может потребоваться создать новый профиль для автоматизации, как найти папку профиля, как создать новый профиль и как использовать этот профиль в скриптах Selenium.

## Содержание

- [Что такое профиль?](#что-такое-профиль)
- [Зачем нужен новый профиль?](#зачем-нужен-новый-профиль)
- [Поиск папки профиля](#поиск-папки-профиля)
- [Создание нового профиля](#создание-нового-профиля)
    - [Шаг 1: Запуск менеджера профилей](#шаг-1-запуск-менеджера-профилей)
    - [Шаг 2: Создание профиля](#шаг-2-создание-профиля)
- [Шаг 3: Использование пользовательского профиля в Selenium](#шаг-3-использование-пользовательского-профиля-в-selenium)

## Что такое профиль?

Firefox сохраняет вашу личную информацию, такую как закладки, пароли и пользовательские настройки, в наборе файлов, называемом вашим **профилем**. Профиль хранится отдельно от файлов программы Firefox. Вы можете иметь несколько профилей Firefox, каждый из которых содержит отдельный набор пользовательской информации. Менеджер профилей позволяет создавать, удалять, переименовывать и переключать профили.

## Зачем нужен новый профиль?

Стандартный профиль Firefox не очень удобен для автоматизации. Когда вы хотите надежно запускать автоматизацию в браузере Firefox, рекомендуется создать отдельный профиль. Профиль автоматизации должен быть легким для загрузки и иметь специальные настройки прокси и другие параметры для запуска хорошего теста.

Необходимо использовать один и тот же профиль на всех машинах разработки и исполнения тестов. Использование разных профилей приведет к тому, что принятые SSL-сертификаты или установленные плагины будут разными, что сделает поведение тестов непредсказуемым.

*   В некоторых случаях вам может понадобиться что-то особенное в вашем профиле, чтобы сделать выполнение тестов надежным. Наиболее распространенным примером являются настройки SSL-сертификатов или плагины браузера, которые обрабатывают самозаверяющие сертификаты. Имеет смысл создать профиль, который обрабатывает эти особые потребности тестирования, а также упаковать и развернуть его вместе с кодом выполнения тестов.
*   Необходимо использовать очень легкий профиль только с теми настройками и плагинами, которые вам нужны для выполнения. Каждый раз, когда Selenium запускает новый сеанс, управляющий экземпляром Firefox, он копирует весь профиль во временный каталог, и если профиль большой, это делает его не только медленным, но и ненадежным.

## Поиск папки профиля

Расположение папки вашего профиля зависит от используемой операционной системы. В следующей таблице показано типичное расположение профиля по умолчанию:

| Операционная система         | Путь к папке профиля                                                    |
| --------------------------- | ----------------------------------------------------------------------- |
| Windows XP / 2000 / Vista / 7 | `%AppData%MozillaFirefoxProfilesxxxxxxxx.default`                      |
| Linux                       | `~/.mozilla/firefox/xxxxxxxx.default/`                                |
| Mac OS X                    | `~/Library/Application Support/Firefox/Profiles/xxxxxxxx.default/` |

В этой таблице есть два интересных момента. Первый - это строка `xxxxxxxx`, предшествующая каждому имени профиля. Эта строка представляет собой набор из 8 случайных чисел и символов, используемых для обеспечения уникальности каждого профиля. Firefox автоматически добавляет случайную строку к любому новому профилю, поэтому вам никогда не нужно беспокоиться о создании этой части имени.

Второй интересный момент заключается в путях Windows XP / 2000 / Vista / 7. Строка `%AppData%` на самом деле является специальной переменной Windows, указывающей на ваш путь к «Данным приложений». Обычно это выглядит так:

`C:Documents and Settings{Имя пользователя}Application Data.`

## Создание нового профиля

Создание новых профилей Firefox и использование их в тестовом скрипте включает в себя трехэтапный процесс. Сначала вам нужно запустить Profile Manager, во-вторых - создать новый профиль и в-третьих - использовать тот же профиль в тестовых скриптах.

### Шаг 1: Запуск менеджера профилей

1.  В верхней части окна Firefox щелкните меню **Файл**, а затем выберите **Выход**.
    
    ![FF-Profile-1](Steps to Configure Firefox profile for Selenium Webdriver _ Tools QA_files/1.FF-Profile-1.png)
    
2.  Нажмите ' `Win + R` ' или нажмите на меню Пуск Windows (кнопка внизу слева), а затем выберите **Выполнить**.
    
    ![FF-Profile-2](Steps to Configure Firefox profile for Selenium Webdriver _ Tools QA_files/2.FF-Profile-2.png)
    
3.  В диалоговом окне **Выполнить** введите: '`firefox.exe -p`', а затем нажмите **OK**.
    
    ![FF-Profile-3](Steps to Configure Firefox profile for Selenium Webdriver _ Tools QA_files/3.FF-Profile-3.png)
    
    **Примечание:** Если окно Profile Manager не появляется, оно может быть открыто в фоновом режиме. Его нужно правильно закрыть, вы можете использовать программу Ctrl+Alt+Del, чтобы убить его. Если он по-прежнему не открывается, возможно, вам потребуется указать полный путь к программе Firefox, заключив его в кавычки; например:
    
    *   В 32-разрядной версии Windows: `"C:Program FilesMozilla Firefoxfirefox.exe" -p`
    *   В 64-разрядной версии Windows: `"C:Program Files (x86)Mozilla Firefoxfirefox.exe" -p`
        
4.  Окно Выбор пользовательского профиля будет выглядеть так.
    
    ![FF-Profile-4](Steps to Configure Firefox profile for Selenium Webdriver _ Tools QA_files/4.FF-Profile-4.png)

### Шаг 2: Создание профиля

1.  Нажмите кнопку **Создать профиль...** в окне **Firefox - Выберите пользовательский профиль**.
    
    ![FF-Profile-5](Steps to Configure Firefox profile for Selenium Webdriver _ Tools QA_files/5.FF-Profile-5.png)
    
2.  Нажмите **Далее >** во всплывающем окне **Мастер создания профиля**.
    
    ![FF-Profile-6](Steps to Configure Firefox profile for Selenium Webdriver _ Tools QA_files/6.FF-Profile-6.png)
    
3.  Введите новое имя '`profileToolsQA`' в поле **Введите имя нового профиля** и нажмите **Готово**.
    
    ![FF-Profile-7](Steps to Configure Firefox profile for Selenium Webdriver _ Tools QA_files/7.FF-Profile-7.png)
    
4.  Окно **Выберите пользовательский профиль** отобразит вновь созданный профиль в списке.
    
    ![FF-Profile-8](Steps to Configure Firefox profile for Selenium Webdriver _ Tools QA_files/8.FF-Profile-8.png)
    
5.  Нажмите на поле **Запустить Firefox**. Firefox запустится с новым профилем.

**Примечание:** Вы заметите, что в новом окне Firefox не будет отображаться ни одна из ваших закладок и значков «Избранное».

**Примечание:** Последний выбранный профиль будет автоматически запускаться при следующем запуске Firefox, и вам потребуется снова запустить Profile Manager, чтобы переключить профили.

## Шаг 3: Использование пользовательского профиля в Selenium

После создания профиля автоматизации его нужно вызвать в тестовых скриптах. Теперь вы можете добавить следующий код в свои тестовые скрипты для создания экземпляра драйвера Firefox:

```java
ProfilesIni profile = new ProfilesIni();

FirefoxProfile myprofile = profile.getProfile("profileToolsQA");

WebDriver driver = new FirefoxDriver(myprofile);