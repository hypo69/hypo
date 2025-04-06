# Модуль для тестирования импортов `unittest`

## Обзор

Модуль предназначен для тестирования корректности импортов в библиотеке `g4f`. Он содержит класс `TestImport`, который проверяет, что псевдонимы функций и классов соответствуют оригинальным именам.

## Подробнее

Данный модуль использует фреймворк `unittest` для автоматизированного тестирования. Он проверяет, что функция `get_cookies` из модуля `g4f.cookies` может быть импортирована как `get_cookies_alias` из модуля `g4f`, и что `StreamSession` является типом данных.

## Классы

### `TestImport`

**Описание**: Класс `TestImport` наследует класс `unittest.TestCase` и содержит методы для тестирования импортов.

**Наследует**:

- `unittest.TestCase`: Базовый класс для создания тестовых случаев.

**Методы**:

- `test_get_cookies()`: Проверяет, что функция `get_cookies` из модуля `g4f.cookies` может быть импортирована как `get_cookies_alias` из модуля `g4f`.
- `test_requests()`: Проверяет, что `StreamSession` является типом данных.

### `test_get_cookies`

```python
 def test_get_cookies(self):
        from g4f import get_cookies as get_cookies_alias
        from g4f.cookies import get_cookies
        self.assertEqual(get_cookies_alias, get_cookies)
```

**Назначение**: Проверяет, что функция `get_cookies` из модуля `g4f.cookies` может быть импортирована как `get_cookies_alias` из модуля `g4f`, и что они ссылаются на один и тот же объект.

**Параметры**:

- Отсутствуют

**Возвращает**:

- Отсутствует

**Вызывает исключения**:

- Отсутствуют

**Как работает функция**:

1.  Импортирует `get_cookies` из `g4f` как `get_cookies_alias`.
2.  Импортирует `get_cookies` из `g4f.cookies`.
3.  Проверяет, что `get_cookies_alias` и `get_cookies` ссылаются на один и тот же объект, используя `self.assertEqual`.

```
Импорт get_cookies as get_cookies_alias
↓
Импорт get_cookies from g4f.cookies
↓
Проверка: get_cookies_alias == get_cookies
```

**Примеры**:

```python
import unittest

class TestImport(unittest.TestCase):

    def test_get_cookies(self):
        from g4f import get_cookies as get_cookies_alias
        from g4f.cookies import get_cookies
        self.assertEqual(get_cookies_alias, get_cookies)
```

### `test_requests`

```python
def test_requests(self):
    from g4f.requests import StreamSession
    self.assertIsInstance(StreamSession, type)
```

**Назначение**: Проверяет, что `StreamSession` является типом данных (классом).

**Параметры**:

- Отсутствуют

**Возвращает**:

- Отсутствует

**Вызывает исключения**:

- Отсутствуют

**Как работает функция**:

1.  Импортирует `StreamSession` из `g4f.requests`.
2.  Проверяет, что `StreamSession` является типом данных, используя `self.assertIsInstance`.

```
Импорт StreamSession
↓
Проверка: StreamSession - тип данных
```

**Примеры**:

```python
import unittest

class TestImport(unittest.TestCase):
    def test_requests(self):
        from g4f.requests import StreamSession
        self.assertIsInstance(StreamSession, type)
```

## Функции

### `if __name__ == '__main__':`

```python
if __name__ == '__main__':
    unittest.main()
```

**Назначение**: Запускает тесты, если скрипт запущен как основной.

**Параметры**:

- Отсутствуют

**Возвращает**:

- Отсутствует

**Вызывает исключения**:

- Отсутствуют

**Как работает функция**:

1. Проверяет, является ли текущий модуль главным модулем, запущенным в Python.
2. Если это так, запускает все тесты, определенные в модуле, используя `unittest.main()`.

```
Проверка: __name__ == '__main__'
↓
Запуск тестов unittest.main()
```

**Примеры**:

```python
if __name__ == '__main__':
    unittest.main()