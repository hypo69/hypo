Как использовать этот блок кода
=========================================================================================\n\nОписание
-------------------------
Данный код служит обработчиком события клика на значок расширения в браузере Firefox.  При клике он выполняет скрипт `contentScript.js` в текущей вкладке.

Шаги выполнения
-------------------------
1. `browser.browserAction.onClicked.addListener((tab) => { ... });`:  Этот код регистрирует обработчик события `onClicked` для значка расширения.  Функция `addListener` ожидает функцию, которая будет вызвана при клике на значок.  Переменная `tab` содержит информацию о текущей вкладке.
2. `browser.scripting.executeScript({ ... });`:  Эта функция выполняет скрипт `contentScript.js` в текущей вкладке (`tab.id`).  Параметр `files` указывает на то, что нужно выполнить скрипт, указанный в файле `contentScript.js`.
3. `{ target: { tabId: tab.id }, files: ["contentScript.js"] }`:  Объект конфигурации для `browser.scripting.executeScript`:
    - `target.tabId`:  Указывает, что скрипт нужно выполнить в текущей вкладке, идентификатор которой извлекается из переменной `tab`.
    - `files`: Массив путей к скриптам, которые нужно выполнить. В данном случае, только `contentScript.js`.


Пример использования
-------------------------
.. code-block:: javascript
\n
// background.js
browser.browserAction.onClicked.addListener((tab) => {\n    browser.scripting.executeScript({\n        target: { tabId: tab.id },\n        files: ["contentScript.js"],\n    });\n});\n\n// contentScript.js (Примерный скрипт, который будет выполняться)\n\n(function() {\n  console.log(\"Выполняется скрипт contentScript.js\");\n  document.body.style.backgroundColor = \"yellow\";\n})();\n