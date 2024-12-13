# Документация для `hypotez/src/webdriver/chrome/extentions/try_path_1.3.5/pages/options.html`

## Обзор

Файл `options.html` представляет собой HTML-страницу, используемую для настроек расширения `try_path_1.3.5` для браузера Chrome. Эта страница позволяет пользователю задавать атрибуты для различных элементов, стили для вставки, а также размеры всплывающего окна.

## Оглавление

1. [Обзор](#обзор)
2. [Структура HTML](#структура-html)
    - [Раздел "Attributes"](#раздел-attributes)
    - [Раздел "Style to be inserted"](#раздел-style-to-be-inserted)
    - [Раздел "Popup styles"](#раздел-popup-styles)
    - [Кнопки](#кнопки)
    - [Сообщение](#сообщение)
3. [Используемые скрипты](#используемые-скрипты)

## Структура HTML

### Раздел "Attributes"

Этот раздел содержит текстовые поля для ввода атрибутов элементов.

-   **Результативные элементы (`Resulted elements`)**: `input` с `id="element-attribute"`
-   **Контекстный элемент (`Context element`)**: `input` с `id="context-attribute"`
-   **Фокусированный элемент (`Focused element`)**: `input` с `id="focused-attribute"`
-   **Предки фокусированного элемента (`Ancestors of the focused element`)**: `input` с `id="ancestor-attribute"`
-   **Фреймовые элементы (`Frame elements`)**: `input` с `id="frame-attribute"`
-   **Предки фреймов (`Ancestors of the frames`)**: `input` с `id="frame-ancestor-attribute"`

### Раздел "Style to be inserted"

Этот раздел содержит текстовое поле для ввода стилей CSS, которые будут вставлены.

-   **Стиль (`Style`)**: `textarea` с `id="style"`

### Раздел "Popup styles"

Этот раздел содержит текстовые поля для задания размеров всплывающего окна.

-   **Ширина тела (`Body width(auto or px)`)**: `input` с `id="popup-body-width"`
-   **Высота тела (`Body height(auto or px)`)**: `input` с `id="popup-body-height"`

### Кнопки

-   **Сохранить (`Save`)**: `button` с `id="save"`. Используется для сохранения настроек.
-   **Показать по умолчанию (`Show default`)**: `button` с `id="show-default"`. Используется для сброса настроек к значениям по умолчанию.

### Сообщение

-   **Сообщение (`Message`)**: `div` с `id="message"`. Используется для отображения сообщений пользователю.

## Используемые скрипты

-   `../scripts/try_xpath_functions.js`: JavaScript-файл, содержащий вспомогательные функции для работы с XPath.
-   `options.js`: JavaScript-файл, содержащий логику для обработки настроек на странице `options.html`.