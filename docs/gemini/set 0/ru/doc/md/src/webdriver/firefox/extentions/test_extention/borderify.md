# Модуль borderify.js

## Обзор

Данный скрипт устанавливает красную границу толщиной 5 пикселей вокруг всего документа. Также отображается диалоговое окно alert().

## Функции

### `document.body.style.border = "5px solid red";`

**Описание**: Устанавливает стили для тела документа, задавая красную границу толщиной 5 пикселей.

**Параметры**:

-  Нет явных параметров.


**Возвращает**:

-  Не возвращает никакого значения. Изменение происходит непосредственно на DOM-элементе.


**Вызывает исключения**:

-  Возможны исключения, связанные с недоступностью элемента `document.body` или ошибками в работе с CSS.  Они не описаны явно в коде, но могут возникать.


### `alert()`

**Описание**: Выводит диалоговое окно с сообщением.

**Параметры**:

- Нет явных параметров. Возможен необязательный параметр текста для диалогового окна.


**Возвращает**:

- Не возвращает никакого значения, но изменяет поведение браузера, вызывая диалоговое окно.


**Вызывает исключения**:

- Возможны исключения, связанные с ошибками в работе с функцией `alert()`. Они не описаны явно в коде, но могут возникать.