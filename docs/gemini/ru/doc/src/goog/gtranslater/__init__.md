# Модуль goog.gtranslater

## Обзор

Модуль `goog.gtranslater` предоставляет функцию для перевода текста с использованием API Google Translate.  Функция поддерживает автоматическое определение языка входного текста, если оно не указано.

## Функции

### `translate`

**Описание**: Переводит текст с одного языка на другой с использованием Google Translate. Поддерживает автоматическое определение языка входного текста.

**Параметры**:

- `text` (str): Текст, который необходимо перевести.
- `locale_in` (str, необязательно): Код языка входного текста. Если не указан, язык будет определён автоматически.
- `locale_out` (str, по умолчанию 'EN'): Код языка выходного текста. По умолчанию английский ('EN').

**Возвращает**:

- str: Переведённый текст. Возвращает пустую строку (`""`) в случае ошибки перевода.

**Обрабатывает исключения**:

- `Exception`: Выводит сообщение об ошибке в лог и возвращает пустую строку.


## Функции (продолжение)

### `main`

**Описание**: Функция, запускаемая при выполнении скрипта как основной. Запрашивает у пользователя текст для перевода, исходный язык и целевой язык, вызывая функцию `translate` для перевода и отображает результат.

**Обрабатывает исключения**:

- Нет обработки исключений.

## Использование

Чтобы использовать модуль, импортируйте его и вызовите функцию `translate`, передавая ей текст и (необязательно) кодировки входного и выходного языков.  Например:

```python
from goog.gtranslater import translate

text_to_translate = "Hello, world!"
translated_text = translate(text_to_translate, locale_out='RU')
print(translated_text)
```

```python
from goog.gtranslater import translate

text_to_translate = "Hola, mundo!"
translated_text = translate(text_to_translate)
print(translated_text)
```

В последнем примере язык входного текста будет определён автоматически.

## Модули, используемые в этом модуле

- `googletrans`: Для взаимодействия с API Google Translate.
- `langdetect`: Для автоматического определения языка.
- `src.logger`: Для логирования сообщений об ошибках и информации.


```