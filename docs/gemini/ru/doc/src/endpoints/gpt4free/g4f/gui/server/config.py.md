# Модуль конфигурации специальных инструкций для моделей GPT

## Обзор

Этот модуль содержит словарь `special_instructions`, который определяет набор специальных инструкций для различных AI-моделей, таких как GPT-3 и GPT-4. Эти инструкции используются для изменения поведения модели, например, для имитации определенных ролей или обхода ограничений.

## Подробней

Модуль содержит словарь `special_instructions`, где ключами являются идентификаторы моделей (например, `'gpt-dude-1.0'`, `'gpt-dan-1.0'`), а значениями - списки инструкций. Каждая инструкция представляет собой словарь с ключами `'role'` (роль, например, `'user'` или `'assistant'`) и `'content'` (содержание инструкции).

## Функции

В данном модуле нет отдельных функций, но основной структурой является словарь `special_instructions`.

## Переменные

### `special_instructions`

```python
special_instructions = {
    'default': [],
    'gpt-dude-1.0': [
        {'role': 'user', 'content': '...'},
        {'role': 'assistant', 'content': '...'}
    ],
    'gpt-dan-1.0': [
        {'role': 'user', 'content': '...'},
        {'role': 'assistant', 'content': '...'}
    ],
    'gpt-dan-2.0': [
        {'role': 'user', 'content': '...'},
        {'role': 'assistant', 'content': '...'}
    ],
    'gpt-math-1.0': [
        {'role': 'user', 'content': '...'},
        {'role': 'assistant', 'content': '...'}
    ],
    'gpt-dev-2.0': [
        {'role': 'user', 'content': '...'},
        {'role': 'assistant', 'content': '...'}
    ],
    'gpt-evil-1.0': [
        {'role': 'user', 'content': '...'},
        {'role': 'assistant', 'content': '...'}
    ]
}
```

**Описание**: Словарь, содержащий специальные инструкции для различных AI-моделей.
- `'default'`: Список инструкций по умолчанию.
- `'gpt-dude-1.0'`: Инструкции для имитации модели "DUDE", которая может выполнять любые задачи и не имеет ограничений.
- `'gpt-dan-1.0'`: Инструкции для имитации модели "DAN", которая не имеет фильтров и ограничений и всегда предоставляет ответы на любые вопросы, включая нелегальные и опасные.
- `'gpt-dan-2.0'`: Улучшенная версия инструкций для имитации модели "DAN" с более строгими правилами.
- `'gpt-math-1.0'`: Инструкции для имитации математического гения "ALAN", который всегда предоставляет правильные ответы на математические вопросы.
- `'gpt-dev-2.0'`: Инструкции для имитации ChatGPT с включенным Developer Mode, который позволяет генерировать любой контент без ограничений.
- `'gpt-evil-1.0'`: Инструкции для имитации "EvilBOT", который нарушает все правила и предоставляет любую информацию без каких-либо ограничений.

## Как работает `special_instructions`

Словарь `special_instructions` содержит набор инструкций для различных моделей, которые изменяют их поведение. Эти инструкции состоят из ролей (например, пользователь или ассистент) и контента, который определяет, как модель должна себя вести.

## Примеры

### Пример структуры инструкции

```python
{
    'role': 'user',
    'content': 'Инструкция для изменения поведения модели.'
}
```

### Пример использования словаря `special_instructions`

```python
instructions = special_instructions['gpt-dude-1.0']
for instruction in instructions:
    role = instruction['role']
    content = instruction['content']
    print(f'Role: {role}, Content: {content}')
```

## ASCII flowchart

```
special_instructions
|
+--> "default" : []
|
+--> "gpt-dude-1.0" : [instruction1, instruction2]
|
+--> "gpt-dan-1.0" : [instruction1, instruction2]
|
+--> "gpt-dan-2.0" : [instruction1, instruction2]
|
+--> "gpt-math-1.0" : [instruction1, instruction2]
|
+--> "gpt-dev-2.0" : [instruction1, instruction2]
|
+--> "gpt-evil-1.0" : [instruction1, instruction2]