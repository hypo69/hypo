# borderify.js

## Обзор

Этот файл представляет собой JavaScript-код, который добавляет красную рамку шириной 5 пикселей вокруг всего содержимого веб-страницы и отображает предупреждение. Код предназначен для использования в качестве расширения браузера Firefox.

## Оглавление

- [Обзор](#обзор)
- [Код](#код)

## Код

### `document.body.style.border = "5px solid red";`

**Описание**: Эта строка кода устанавливает границу для элемента `body` веб-страницы.

**Детали**:
- `document.body`: Ссылка на элемент `body` HTML-документа.
- `style.border`: Свойство CSS для управления границей элемента.
- `"5px solid red"`: Значение свойства `border`, устанавливающее границу шириной 5 пикселей, сплошной линией и красного цвета.

### `alert()`

**Описание**: Эта строка кода отображает стандартное предупреждение в браузере.

**Детали**:
- `alert()`:  JavaScript-функция, которая выводит диалоговое окно с сообщением.
- В данном случае функция `alert()` не принимает никаких параметров, поэтому будет показано стандартное сообщение браузера.