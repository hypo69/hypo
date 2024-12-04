Настройка профиля Firefox для Selenium WebDriver
=================================================

Описание
-------------------------
Данный документ описывает шаги по настройке пользовательского профиля Firefox для использования в тестах Selenium WebDriver.  Это позволяет создать отдельный профиль, содержащий необходимые настройки для стабильной работы автотестов, избегая проблем с сертификатами и плагинами.  Такой подход обеспечивает более надежные и воспроизводимые результаты тестов на различных машинах.

Шаги выполнения
-------------------------
1. **Закройте Firefox.**  Прежде чем начать, убедитесь, что браузер Firefox закрыт.
2. **Запустите командную строку (или терминал).**
3. **Введите команду для запуска менеджера профилей Firefox.**  Используйте команду `firefox.exe -p` (или аналогичную для вашей системы).  Для Windows x64, возможно, потребуется указать полный путь к исполняемому файлу Firefox, например: `"C:\Program Files (x86)\Mozilla Firefox\firefox.exe" -p`
4. **Создайте новый профиль.** В появившемся окне менеджера профилей Firefox, нажмите кнопку "Создать профиль...".
5. **Назовите новый профиль.** Введите имя для нового профиля (например, "profileToolsQA") в соответствующем поле и нажмите "Далее >".
6. **Завершите создание профиля.** Нажмите "Готово".  Новый профиль будет добавлен в список менеджера профилей.
7. **Запустите Firefox с новым профилем.** В окне менеджера профилей, выберите созданный профиль и нажмите "Запустить Firefox". Это запустит Firefox с новым профилем, без ваших обычных настроек (закладок, паролей).
8. **Настройка в коде Selenium.**  В вашем коде Selenium WebDriver необходимо использовать созданный профиль.  Для этого, загрузите библиотеку `ProfilesIni`. Затем используйте метод `getProfile()` для получения нужного профиля по его имени:

.. code-block:: java

    ProfilesIni profile = new ProfilesIni();
    FirefoxProfile myprofile = profile.getProfile("profileToolsQA");
    WebDriver driver = new FirefoxDriver(myprofile);


Пример использования
-------------------------
.. code-block:: java

    import org.openqa.selenium.WebDriver;
    import org.openqa.selenium.firefox.FirefoxDriver;
    import org.openqa.selenium.firefox.FirefoxProfile;
    import org.openqa.selenium.remote.DesiredCapabilities;
    import java.io.File;
    import org.apache.commons.io.FileUtils;
    import org.openqa.selenium.support.events.EventFiringWebDriver;


    public class MyFirstTest {
        public static void main(String[] args) {

            // ... (other imports)

            ProfilesIni profile = new ProfilesIni();
            FirefoxProfile myprofile = profile.getProfile("profileToolsQA");

            // ... (other code if required)

            // Option 1: Initialize driver directly
            WebDriver driver = new FirefoxDriver(myprofile);


            // Option 2: Use EventFiringWebDriver to catch events
            EventFiringWebDriver eventDriver = new EventFiringWebDriver(driver);


            // ... rest of your test code ...

        }
    }