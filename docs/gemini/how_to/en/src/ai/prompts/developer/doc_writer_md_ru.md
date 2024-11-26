# Модуль: code_assistant

Этот модуль предоставляет класс `CodeAssistant` для взаимодействия с AI-моделями (например, Google Gemini и OpenAI) для анализа и генерации документации кода.  Модуль ориентирован на русскую локализацию.

## Пример использования

```python
import code_assistant

assistant = code_assistant.CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
result = assistant.process_files(files=['my_code.py'], options={'verbose': True})
print(result)
```

## Поддерживаемые платформы
- Python

## Атрибуты и методы

### Класс: CodeAssistant

Класс `CodeAssistant` используется для взаимодействия с AI-моделями и обработки кодовых файлов.

#### Атрибуты
- `role`: Роль ассистента (строка, например, 'code_checker').
- `lang`: Язык, используемый ассистентом (строка, например, 'ru').
- `model`: Список поддерживаемых AI-моделей (список строк, например, ['gemini']).

#### Методы
##### `process_files`

Обрабатывает список файлов кода.

###### Параметры
- `files`: Список путей к файлам для обработки.
- `options`: Словарь дополнительных параметров (например, `{'verbose': True}` для подробных выводов).

###### Возвращаемое значение
- Словарь с результатами обработки. Если обработка прошла успешно, содержит `result` (список обработанных данных). В противном случае, содержит ошибку `error`.


###### Пример использования

```python
import code_assistant

assistant = code_assistant.CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
result = assistant.process_files(files=['file1.py', 'file2.py'], options={'verbose': True})
if 'result' in result:
    print("Результаты:", result['result'])
else:
    print("Ошибка:", result['error'])
```

###### Возможные исключения
- `TypeError`: Если типы входных данных не соответствуют ожиданиям.
- `FileNotFoundError`: Если указанный файл не найден.
- `Exception`: Общее исключение при возникновении непредвиденной ошибки.

```python

```
```
```


```python
#Пример обработки исключения
try:
    assistant.process_files(files=['nonexistent_file.py'])
except FileNotFoundError as e:
    print(f"Ошибка: {e}")
```

```
```

```markdown
# Исключение: Файл не найден

Это исключение возникает, если файл, указанный в `process_files`, не найден.

## Параметры
- `file`: Путь к файлу, который не был найден.

```
```


```python
# Пример обработки исключения
try:
    open('nonexistent_file.txt')
except FileNotFoundError as e:
    print(f"Ошибка: {e}")
```
```
```


```


```
```
```
```

```


```