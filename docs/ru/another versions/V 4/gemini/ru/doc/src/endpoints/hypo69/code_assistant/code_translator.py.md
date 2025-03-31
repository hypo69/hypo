# Модуль `code_translator`

## Обзор

Модуль `code_translator` предназначен для перевода кода с использованием AI-моделей. Он наследуется от класса `CodeAssistant` и специализируется на задачах перевода кода.

## Подробней

Этот модуль является частью проекта `hypotez` и используется для автоматического перевода кодовой базы проекта. Он читает файлы с кодом, передает код в AI-модели (например, Google Gemini), получает переведенный код обратно и сохраняет результаты в директории `docs/gemini`. В зависимости от заданной роли, файлы сохраняются в соответствующих поддиректориях.

## Классы

### `CodeTranslator`

**Описание**: Класс `CodeTranslator` наследуется от `CodeAssistant` и предназначен для перевода кода.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `CodeTranslator`.

**Параметры**:
- `role` (str): Роль, выполняемая экземпляром класса, по умолчанию `'code_translator'`.
- `models` (Optional[list], optional): Список моделей, используемых для перевода. По умолчанию `['gemini']`.

**Примеры**
```python
translator = CodeTranslator(role='code_translator', models=['gemini'])
```

## Функции

### `__init__`

```python
def __init__(self, role:str, models:Optional[list] = ['gemini']):
    """"""
    super().__init__(role=self.role)
```

**Описание**: Инициализирует экземпляр класса `CodeTranslator`, вызывая конструктор родительского класса `CodeAssistant`.

**Параметры**:
- `role` (str): Роль, выполняемая экземпляром класса.
- `models` (Optional[list], optional): Список моделей для использования. По умолчанию `['gemini']`.

**Возвращает**: # если есть возвращаемое значение
- None

**Примеры**:
```python
translator = CodeTranslator(role='code_translator')
```
```python
translator = CodeTranslator(role='code_translator', models=['gemini', 'openai'])