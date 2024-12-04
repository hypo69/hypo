Как использовать этот блок кода
========================================================================================

Описание
-------------------------
Этот код определяет переменные, представляющие информацию о проекте (название, версия, автор и т.д.). Он пытается загрузить настройки из файла `../settings.json` и использовать значения из него, если файл существует и содержимое валидное JSON. В противном случае, используется значение по умолчанию.

Шаги выполнения
-------------------------
1. **Открытие файла настроек:** Код пытается открыть файл `../settings.json` в режиме чтения (`'r'`):
   ```python
   with open('../settings.json', 'r') as settings_file:
       settings = json.load(settings_file)
   ```
2. **Загрузка настроек:** Если файл успешно открыт и содержит корректный JSON, код загружает данные из файла в переменную `settings`.
3. **Получение значений настроек:** Если `settings` содержит данные, код извлекает значения из словаря `settings` для переменных:
   ```python
   __project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
   __version__ = settings.get("version", '') if settings else ''
   __doc__ = ''
   __details__ = ''
   __author__ = settings.get("author", '') if settings else ''
   __copyright__ = settings.get("copyright", '') if settings else ''
   __cofee__ = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
   ```
4. **Обработка ошибок:** Если файл `../settings.json` не найден или содержит некорректный JSON, код обрабатывает исключения `FileNotFoundError` и `json.JSONDecodeError`, делая `settings` равным `None`.
5. **Использование значений по умолчанию:**  Если `settings` равно `None`, код использует значения по умолчанию для переменных, например, `'hypotez'` для `__project_name__`.


Пример использования
-------------------------
.. code-block:: python

    # Допустим, файл ../settings.json содержит
    # {
    #   "project_name": "MyAwesomeProject",
    #   "version": "1.2.3",
    #   "author": "John Doe"
    # }

    import sys
    from hypotez.src.templates import version

    print(version.__project_name__)  # Выведет MyAwesomeProject
    print(version.__version__)      # Выведет 1.2.3
    print(version.__author__)       # Выведет John Doe


    # Если файл ../settings.json не существует, или содержит ошибки, 
    # выведет значения по умолчанию.