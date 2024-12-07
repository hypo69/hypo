Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот фрагмент кода реагирует на клик по иконке расширения в адресной строке браузера. При клике он выполняет скрипт `contentScript.js` в текущей вкладке.

Шаги выполнения
-------------------------
1. `browser.browserAction.onClicked.addListener((tab) => { ... });`: Этот код регистрирует обработчик события `onClicked` для иконки расширения.  При клике на иконку в текущем браузере вызывается функция, указанная в `addListener`. Внутри этой функции `tab` переменная содержит информацию о текущей вкладке, включая её идентификатор.
2. `browser.scripting.executeScript({ target: { tabId: tab.id }, files: ["contentScript.js"] });`:  Этот код выполняет скрипт `contentScript.js` в контексте текущей вкладки.  `target: { tabId: tab.id }` указывает на то, что скрипт должен быть выполнен во вкладке с идентификатором `tab.id`.  `files: ["contentScript.js"]` указывает имя файла скрипта для выполнения.

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


    // contentScript.js
    (function() {
        // код, который будет выполняться в контексте страницы
        console.log("Скрипт contentScript.js выполнен!");
        // Добавьте сюда код, который должен выполняться в текущей вкладке.
        // Например, можете получить и вывести содержимое текущей страницы.
    })();