# <input code>

```python
# ИНСТРУКЦИЯ
Для каждого входного Python файла создайте документацию в формате `rst` для последующей компиляции с Sphinx. Документация должна соответствовать следующим требованиям:

1. **Формат документации**:
   - Используйте стандарт `reStructuredText (rst)`.
   - Каждый файл должен начинаться с заголовка и краткого описания его содержимого.
   - Для всех классов и функций используйте следующий формат комментариев:
     ```python
     def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
         """
         Аргументы:
             param (str): Описание параметра `param`.
             param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию равно `None`.

         Возвращаемое значение:
             dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

         Исключения:
             SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
         """
     ```
   - Используйте `ex` вместо `e` в блоках обработки исключений.

2. **Дерево оглавлений (TOC)**:
   - Включите разделы в документации с использованием `.. toctree::`.
   - Структура файла `index.rst` должна содержать ссылки на все описания модулей.

3. **Форматирование документации**:
   - Все заголовки классов, функций и методов должны быть задокументированы с использованием директив Sphinx (`autoclass`, `autofunction`).
   - Пример:
     ```rst
     .. automodule:: module_name
         :members:
         :undoc-members:
         :show-inheritance:
     ```

4. **Заголовки разделов**:
   - Используйте заголовки первого уровня (`=`), второго уровня (`-`), третьего уровня (`~`) и четвертого уровня (`^`).

5. **Пример файла**:
   ```rst
   Название модуля
   ===============\n

   .. automodule:: module_name
       :members:
       :undoc-members:
       :show-inheritance:

   Функции
   --------

   .. autofunction:: module_name.function_name
   ```

Сгенерируйте соответствующую документацию для каждого входного Python файла в формате `rst`.
```

# <algorithm>

Эта инструкция описывает алгоритм генерации документации `reStructuredText` для Python-кода.  Алгоритм состоит из следующих шагов:

1. **Прочитать входной Python-файл**.
2. **Проанализировать структуру файла:** определить классы, функции, атрибуты.
3. **Сгенерировать заголовок:** создать заголовок RST файла, описывающий содержащийся в нем модуль.
4. **Сгенерировать секции для классов и функций:** создать секции для каждого класса и функции, используя `.. automodule::`, `.. autofunction::` и т.п.
5. **Сгенерировать секции для документации (Docstrings):** для каждой функции и класса вставить документацию из комментариев.
6. **Сохранить файл в формате RST**.


Пример: Для файла `my_module.py` с классом `MyClass` и функцией `my_function`, алгоритм создаст файл `my_module.rst` с заголовком, секцией для класса `MyClass` и функцией `my_function`, содержащими в себе документацию из `docstrings`.


# <mermaid>

```mermaid
graph LR
    A[Входной Python файл] --> B{Анализ структуры};
    B --> C[Генерация заголовка RST];
    B --> D{Генерация секций для классов и функций};
    D --> E[Вставка документации (docstrings)];
    C --> F[Сохранение RST файла];
    E --> F;
    F --> G[Выходной RST файл];
```

**Объяснение зависимостей:**

Эта инструкция не имеет явных зависимостей от других частей проекта. Она предоставляет алгоритм генерации RST-документации из Python-кода.  Ожидается, что инструмент для генерации документации (например, Sphinx) будет внешним.

# <explanation>

**Импорты:**

Инструкция не содержит импортов. Она описывает алгоритм генерации документации.


**Классы:**

Инструкция не определяет классы, она описывает, как должна быть создана документация для классов, содержащихся в входных Python файлах.

**Функции:**

Инструкция описывает, как должны быть задокументированы функции. Для этого используются комментарии внутри функций (docstrings) в соответствии со стандартом `reStructuredText`.


**Переменные:**

Инструкция не определяет переменные.  Она концентрируется на структурировании и документировании классов и функций, которые могут содержать переменные.


**Возможные ошибки и улучшения:**

* **Не указан язык:**  Инструкция не уточняет, какие инструменты или среды используются для обработки файлов.
* **Не указано входное/выходное:** Не указано, где хранятся входные и выходные файлы.
* **Нет деталей имплементации:** Не описан конкретный способ анализа Python-кода.
* **Не указаны инструменты:** Не указано, какие инструменты (например, Sphinx) используются для генерации документации.

Инструкция  дает высокую степень свободы в выборе инструментов и подходов. Это может быть полезным для адаптации к различным окружениям и потребностям.