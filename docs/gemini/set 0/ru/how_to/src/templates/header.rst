Как использовать hypotez/src/templates/header.py
========================================================================================

Описание
-------------------------
Этот файл содержит функцию `set_project_root`, которая определяет корневую директорию проекта. Функция ищет директории вверх от текущего файла, пока не найдёт директорию, содержащую один из файлов-маркеров (pyproject.toml, requirements.txt, .git). Если корневой каталог найден, он добавляется в системный путь `sys.path`.  Файл также инициализирует глобальную переменную `__root__`, хранящую путь к корню проекта, и импортирует модуль `gs` из директории `src`.

Шаги выполнения
-------------------------
1. **Определение корневой директории проекта:** Функция `set_project_root` принимает кортеж `marker_files` с именами файлов, которые служат маркерами корневой директории.
2. **Поиск корня проекта:** Функция начинается с текущего директория файла и перебирает родительские директории, проверяя существование файлов-маркеров в каждом родительском каталоге.
3. **Добавление в системный путь:** Если корневой каталог найден, он добавляется в переменную `sys.path`  для последующего импорта модулей из других директорий проекта.
4. **Возврат пути:** Функция возвращает путь к найденному корневому каталогу.
5. **Инициализация глобальной переменной:** Результат работы функции `set_project_root` сохраняется в глобальной переменной `__root__`.
6. **Импорт модуля:** Файл импортирует модуль `gs` из директории `src`.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.templates.header import set_project_root

    # Пример использования функции set_project_root
    root_dir = set_project_root()
    print(f"Корневой каталог проекта: {root_dir}")

    # Далее, в вашем коде, вы можете использовать путь к корневому каталогу
    # для импорта других модулей проекта.

    # Пример импорта модуля gs
    import src.gs as gs_module  # Замените gs на правильное имя модуля
    # ... дальнейшее использование gs_module