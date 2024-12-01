Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код реагирует на клик по значку расширения браузера Firefox. При нажатии на значок, он выполняет скрипт `contentScript.js` в текущей вкладке.

Шаги выполнения
-------------------------
1. Функция `browser.browserAction.onClicked.addListener` регистрирует обработчик события клика по значку расширения.
2. Когда пользователь кликает по значку расширения, вызывается функция `browser.scripting.executeScript`.
3. `browser.scripting.executeScript` выполняет скрипт `contentScript.js` в текущей вкладке, идентификатор которой (`tab.id`) передается в качестве параметра.
4. В качестве параметра `files` функция `browser.scripting.executeScript` получает массив путей к файлам скриптов, которые необходимо выполнить. В данном случае, `contentScript.js`

Пример использования
-------------------------
.. code-block:: javascript
    // background.js
    
    browser.browserAction.onClicked.addListener((tab) => {
        browser.scripting.executeScript({
            target: { tabId: tab.id },
            files: ["contentScript.js"],
        });
    });
    
    // contentScript.js (должен находиться в той же директории, что и background.js)
    
    (function() {
        console.log("Скрипт contentScript.js успешно выполнен!");
        // Здесь должен быть код, который выполняется в контексте страницы
    })();