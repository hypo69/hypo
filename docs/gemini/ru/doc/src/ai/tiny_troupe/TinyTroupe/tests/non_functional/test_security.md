# Модуль `test_security.py`

## Обзор

Данный модуль содержит тесты безопасности для библиотеки TinyTroupe, проверяющие корректность работы API для доступа к LLM.

## Функции

### `test_default_llmm_api`

**Описание**: Тестирует некоторые желаемые свойства API LLM по умолчанию, настроенного для TinyTroupe. Проверяет, что ответ от API не равен `None`, содержит ключи `content` и `role` с ненулевыми значениями, длина `content` больше или равна 1, а полная строка ответа содержит не менее 1 символа и не более 2 миллионов символов. Также проверяет, что ответ можно закодировать в UTF-8 без исключений.


**Параметры**:
- Нет входных параметров.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- `AssertionError`: Возникает, если какие-либо из проверок не проходят.  Например, если ответ от API `None`, не содержит необходимых ключей, длина `content` меньше 1, длина строки ответа меньше 1 или больше 2 миллионов символов, или ответ не может быть закодирован в UTF-8.


## Зависимости

- `pytest`
- `textwrap`
- `logging`
- `sys`
- `openai_utils`
- `testing_utils`
- `tinytroupe`


## Примечания

- Тесты полагаются на корректную настройку API LLM.
- Тесты проверяют минимальные требования к ответу.
- Тесты не проверяют семантическое содержание ответа.
- `sys.path.append(...)` - добавляет пути к файлам, используемым для тестирования.  Важно учесть, что эти пути относительны к файлу `test_security.py`.  Этот код может потребовать модификаций в зависимости от текущей структуры проекта.
- `create_test_system_user_message` - функция, которая предполагается определенной в `testing_utils`, и необходима для генерации тестовых сообщений.