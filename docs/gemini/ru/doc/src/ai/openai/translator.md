# Модуль `hypotez/src/ai/openai/translator.py`

## Обзор

Модуль `translator.py` предоставляет функцию для перевода текста с использованием API OpenAI.  Он использует настройки из файла конфигурации `gs.credentials` для доступа к API.


## Функции

### `translate`

**Описание**: Функция переводит текст с одного языка на другой с помощью модели OpenAI.

**Параметры**:

- `text` (str): Текст для перевода.
- `source_language` (str): Язык исходного текста.
- `target_language` (str): Язык для перевода.

**Возвращает**:

- `str`: Переведённый текст. Возвращает `None` в случае ошибки.

**Вызывает исключения**:

- `Exception`: Любые исключения, возникающие при взаимодействии с OpenAI API.  Ошибки логируются с помощью модуля `logger`.


## Использование

Пример использования функции `translate`:

```python
from hypotez.src.ai.openai import translator

source_text = "Привет, как дела?"
source_language = "Russian"
target_language = "English"

translation = translator.translate(source_text, source_language, target_language)

if translation:
    print(f"Translated text: {translation}")
else:
    print("Translation failed.")
```

**Примечания**:

- Убедитесь, что в файле `gs.credentials` указан корректный ключ API OpenAI.
- Модель `text-davinci-003` используется по умолчанию.  Можно изменить ее, если нужно использовать другую модель.
- Обработка ошибок (в блоке `except`) жизненно важна для устойчивости кода, так как запросы к внешним сервисам (API OpenAI) могут завершиться ошибкой.  В данном случае, ошибка логируется, и функция возвращает `None`, чтобы программа не прервалась.