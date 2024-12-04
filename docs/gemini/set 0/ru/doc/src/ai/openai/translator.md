# Модуль `hypotez/src/ai/openai/translator.py`

## Обзор

Этот модуль предоставляет функцию `translate` для перевода текста с использованием API OpenAI. Он использует конфигурацию из файла `gs.credentials.openai` для аутентификации. Модуль также использует логирование из модуля `src.logger`.

## Функции

### `translate`

**Описание**: Функция переводит текст с одного языка на другой с помощью API OpenAI.

**Параметры**:
- `text` (str): Текст для перевода.
- `source_language` (str): Язык исходного текста.
- `target_language` (str): Язык для перевода.

**Возвращает**:
- `str`: Переведённый текст.  Возвращает `None` в случае ошибки.

**Обрабатывает исключения**:
- `Exception`: Логирует ошибку во время выполнения запроса к OpenAI API и возвращает `None`.


## Использование

Пример использования функции `translate`:

```python
source_text = "Привет, как дела?"
source_language = "Russian"
target_language = "English"
translation = translate(source_text, source_language, target_language)
if translation:
  print(f"Translated text: {translation}")
else:
  print("Translation failed.")
```

## Конфигурация

Ключ API OpenAI должен быть сохранён в файле `gs.credentials.openai`.

## Зависимости

Этот модуль использует следующие библиотеки:
- `openai`
- `src.gs`
- `src.logger`

```