# Модуль `background.js`

## Обзор

Этот файл содержит обработчик события `chrome.runtime.onInstalled`, который выполняется при установке расширения.  В нём выводится сообщение в консоль о том, что расширение установлено.

## Функции

### `chrome.runtime.onInstalled.addListener`

**Описание**:  Этот обработчик устанавливается для события `chrome.runtime.onInstalled`. Он выполняется, когда расширение устанавливается или обновляется.


**Параметры**:

- `callback`: функция, которая будет вызвана при наступлении события.

**Возвращает**:

- Не имеет возвращаемого значения.


**Вызывает исключения**:


- Любые ошибки, связанные с Chrome Runtime API.


```javascript
chrome.runtime.onInstalled.addListener(() => {
    console.log('OpenAI Model Interface Extension Installed');
});
```