Как использовать этот блок кода
=========================================================================================\n\nОписание
-------------------------
Данный фрагмент кода служит обработчиком события установки расширения в браузере Chrome.  При установке расширения он выводит сообщение в консоль браузера.

Шаги выполнения
-------------------------
1. Функция `chrome.runtime.onInstalled.addListener` регистрирует обработчик для события `onInstalled`.
2. При установке расширения Chrome вызывает функцию, указанную в качестве обработчика.
3. Функция `console.log('OpenAI Model Interface Extension Installed');` выводит строку 'OpenAI Model Interface Extension Installed' в консоль разработчика браузера.

Пример использования
-------------------------
.. code-block:: javascript

    chrome.runtime.onInstalled.addListener(() => {
        console.log('OpenAI Model Interface Extension Installed');
    });