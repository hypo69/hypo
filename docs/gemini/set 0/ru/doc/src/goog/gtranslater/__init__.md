# Модуль `hypotez/src/goog/gtranslater`

## Обзор

Модуль `gtranslater` предоставляет функции для перевода текста с использованием Google Translate API.  Включает автоматическое определение языка входного текста, если оно не задано явно.

## Функции

### `translate`

**Описание**: Переводит текст из одного языка в другой с использованием Google Translate. Автоматически определяет язык входного текста, если он не указан.

**Параметры**:

- `text` (str): Текст, который нужно перевести.
- `locale_in` (str, необязательно): Код языка входного текста.  Если не указан, язык определяется автоматически.
- `locale_out` (str, по умолчанию 'EN'): Код языка выходного текста. По умолчанию - английский ('EN').

**Возвращает**:

- str: Переведенный текст. Возвращает пустую строку (`""`) в случае ошибки перевода.

**Вызывает исключения**:

- Любые исключения, возникающие при использовании Google Translate API или при обнаружении языка (langdetect).  Подробная информация об ошибке выводится в лог.


### `main`

**Описание**: Функция для взаимодействия с пользователем. Запрашивает текст, входной и выходной языки, вызывает функцию `translate` и выводит результат.

**Параметры**:

- Не имеет параметров.

**Возвращает**:

- Не возвращает значения.

**Вызывает исключения**:

- Не вызывает исключения непосредственно.  Возможные исключения функции `translate` обрабатываются внутри.


## Использование

Для использования модуля, импортируйте его и вызовите функцию `translate`.

```python
from hypotez.src.goog.gtranslater import translate

text_to_translate = "Hello, world!"
translated_text = translate(text_to_translate, locale_out='RU')
print(translated_text)
```

## Логирование

Модуль использует модуль `src.logger` для ведения журнала операций.  Сообщения об ошибках и отладке записываются в соответствующие логи.


## Зависимости

Модуль использует библиотеки:

- `googletrans`: для доступа к Google Translate API.
- `langdetect`: для автоматического определения языка.
- `src.logger`: для логирования.


```
```
```
```
```
```
```