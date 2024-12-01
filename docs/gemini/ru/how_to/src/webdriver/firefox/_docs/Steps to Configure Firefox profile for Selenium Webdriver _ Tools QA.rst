Как настроить профиль Firefox для Selenium WebDriver
========================================================================================

Описание
-------------------------
Этот документ описывает шаги по настройке пользовательского профиля Firefox для использования с Selenium WebDriver.  Это важно для создания надежных и стабильных автоматизированных тестов, особенно при работе с авторизацией, сертификатами SSL или плагинами.  Создание отдельного профиля позволяет изолировать настройки, используемые для автоматизации, от пользовательских настроек.

Шаги выполнения
-------------------------
1. **Закройте Firefox.**  Перед настройкой профиля необходимо закрыть текущую сессию Firefox.
2. **Запустите Firefox с параметром -p.**  Для этого, используя диалоговое окно "Выполнить" (например, сочетание клавиш `Windows` + `R` в Windows), введите `firefox.exe -p` (или полную директорию к файлу `firefox.exe` для 32/64 битной системы) и нажмите "ОК". Если диалоговое окно не отобразится, возможно, Firefox открылся в фоновом режиме, и необходимо закрыть его.
3. **Создайте новый профиль.** В открывшемся окне "Выбор профиля пользователя" нажмите кнопку "Создать профиль...".
4. **Настройте имя профиля.** В появившемся диалоге "Мастер создания профиля" введите имя для нового профиля (например, `profileToolsQA`) и нажмите "Готово".
5. **Запустите Firefox с новым профилем.** В окне выбора профиля выберите созданный профиль и нажмите кнопку "Запустить Firefox".
6. **Настройте необходимые настройки в новом профиле (необязательно).** В новом профиле можно настроить параметры, необходимые для ваших тестов (например, настройки прокси-сервера, установленные сертификаты).
7. **Используйте профиль в Selenium WebDriver.** В вашем скрипте Selenium WebDriver используйте следующий код для запуска драйвера Firefox с использованием созданного профиля:

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
    import org.openqa.selenium.support.events.EventFiringWebDriver;
    import org.openqa.selenium.support.ui.WebDriverWait;
    import org.openqa.selenium.support.ui.ExpectedConditions;
    import java.io.File;
    import org.apache.commons.io.FileUtils;
    import java.util.concurrent.TimeUnit;
    import org.apache.commons.lang3.time.StopWatch;

    // ... (другие импорты)

    public class MyTest {

        public static void main(String[] args) throws Exception {
            
            ProfilesIni profile = new ProfilesIni();
            FirefoxProfile myprofile = profile.getProfile("profileToolsQA");
            
            DesiredCapabilities capabilities = DesiredCapabilities.firefox();
            capabilities.setCapability(FirefoxDriver.PROFILE, myprofile);
            
            WebDriver driver = new FirefoxDriver(capabilities);
            // ... (ваш код для работы с драйвером)
        
            driver.quit();
        }
    }