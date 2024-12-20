# Модуль login.py

## Обзор

Этот модуль содержит функцию `login`, предназначенную для авторизации на сайте Amazon с использованием веб-драйвера.  Функция использует локаторы из хранилища `locators_store` для взаимодействия с элементами страницы и выполняет последовательность действий для ввода данных, нажатия кнопок и проверки результата.


## Функции

### `login`

**Описание**: Функция для входа на сайт Amazon.

**Параметры**:

- `s` (Supplier): Объект, содержащий данные о поставщике, в том числе веб-драйвер и локаторы элементов.

**Возвращает**:

- `bool`: `True`, если вход успешен, иначе `False`.

**Вызывает исключения**:

- Возможные исключения, генерируемые методами веб-драйвера (например, `NoSuchElementException`, `TimeoutException` и т.д.) не явно указаны в документации, но должны быть обработаны внутри функции.


**Детали реализации**:

1. Получает локаторы для элементов страницы входа из `s.locators_store['login']`.
2. Получает веб-драйвер из `s.driver`.
3. Переходит на страницу входа `https://amazon.com/`.
4. Попытка кликнуть по элементу `open_login_inputs`. При неудаче перезагружает страницу и выполняет повторную попытку.  В случае повторной неудачи, логгирует сообщение о необходимости поиска кнопки в другом месте.
5. Выполняет последовательность действий, используя методы веб-драйвера для заполнения полей, нажатия кнопок и проверки результата.
6. Проверяет текущий URL. Если он соответствует странице входа, логгирует ошибку и возвращает `False`.
7. Если вход успешен, увеличивает окно до максимального размера, логгирует информацию и возвращает `True`.

**Важно**: Функция `login` содержит `...` в местах, где требуется добавить обработку случаев неудачной авторизации. Это необходимо реализовать для полноты и стабильности работы функции.  Использование `logger` для отслеживания успехов и ошибок.