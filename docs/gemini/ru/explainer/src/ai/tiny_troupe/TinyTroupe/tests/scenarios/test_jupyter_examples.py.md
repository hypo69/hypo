## Анализ кода `test_jupyter_examples.py`

### 1. <алгоритм>

**1. Инициализация:**
   - Импортируются необходимые библиотеки: `os`, `nbformat`, `ExecutePreprocessor` из `nbconvert`, `pytest` и `sys`.
   - Устанавливаются пути для импорта: `sys.path.insert(0, ...)`.  Добавляются директории для поиска пакетов TinyTroupe.
   - Определяется путь к папке с ноутбуками: `NOTEBOOK_FOLDER`.
   - Определяется таймаут для выполнения ноутбуков: `TIMEOUT`.
   - Определяется имя ядра Jupyter: `KERNEL_NAME`.

**2. Функция `get_notebooks(folder)`:**
   - **Пример:** `get_notebooks("../examples/")`
   - Получает список всех файлов в указанной папке.
   - Фильтрует файлы, оставляя только те, которые:
     - Заканчиваются на `.ipynb`.
     - Не содержат в имени `.executed.`
     - Не содержат в имени `.local.`
   - Возвращает список полных путей к найденным Jupyter ноутбукам.

**3. Функция `test_notebook_execution(notebook_path)`:**
   - **Пример:** `test_notebook_execution("../examples/example1.ipynb")`
   - Принимает путь к Jupyter ноутбуку.
   - Открывает ноутбук в режиме чтения, используя кодировку UTF-8.
   - Читает содержимое ноутбука с помощью `nbformat.read()` и создает объект ноутбука.
   - Инициализирует объект `ExecutePreprocessor` с заданным тайм-аутом и именем ядра.
   - **Обработка исключений:**
     - Пытается выполнить ноутбук при помощи `ep.preprocess()`.
       - Передает метаданные, содержащие путь к папке с ноутбуками.
     - Если при выполнении возникает исключение, то тест завершается с ошибкой, используя `pytest.fail()`.
   - **Блок finally:**
     - Сохраняет копию выполненного ноутбука.
       - Создает новый путь к файлу, заменяя `.ipynb` на `.executed.local.ipynb`.
       - Записывает выполненный ноутбук в новый файл.
   - Выводит сообщение об успешном выполнении или ошибке и сохранении.

**4. `pytest.mark.parametrize`:**
   - Декоратор `pytest.mark.parametrize` запускает функцию `test_notebook_execution` для каждого пути к ноутбуку, возвращенного функцией `get_notebooks()`.

### 2. <mermaid>

```mermaid
flowchart TD
    subgraph Initialization
        A[Set Notebook Folder Path: <br><code>NOTEBOOK_FOLDER = "../examples/"</code>]
        B[Set Timeout: <br><code>TIMEOUT = 600</code>]
        C[Set Kernel Name: <br><code>KERNEL_NAME = "python3"</code>]
    end
     Start --> A
    A --> B
    B --> C
    C --> GetNotebooksFunctionCall

    subgraph Get Notebooks Function 
        GetNotebooksFunctionCall[<code>get_notebooks(folder)</code><br> Retrieve Notebooks ]
        D[Get files in folder]
        E[Filter files by extension and name]
        F[Return list of notebook paths]
    end
    GetNotebooksFunctionCall-->D
    D-->E
    E-->F
    F-->TestNotebookExecutionCall
    subgraph Test Notebook Execution Function
        TestNotebookExecutionCall[<code>test_notebook_execution(notebook_path)</code><br> Test each notebook]
        G[Open Notebook]
        H[Read Notebook with <code>nbformat.read</code>]
        I[Init <code>ExecutePreprocessor</code>]
        J[Execute Notebook: <code>ep.preprocess</code>]
        K[Handle Exception]
        L[Save executed notebook: <code>nbformat.write</code>]
        M[Print Success message]
        N[Print Error message]
    end
    TestNotebookExecutionCall-->G
    G-->H
    H-->I
    I-->J
    J-->K
    K--Exception-->N
    K--Success-->L
    L-->M

```
#### Пояснения к `mermaid` диаграмме:

- **Initialization**: Блок, описывающий начальную настройку переменных.
  - `A`: Установка пути к папке с ноутбуками.
  - `B`: Установка таймаута для выполнения ноутбуков.
  - `C`: Установка имени ядра Jupyter.
- **Get Notebooks Function**: Блок, описывающий логику функции `get_notebooks`.
  - `GetNotebooksFunctionCall`: Вызов функции `get_notebooks(folder)`.
  - `D`: Получение списка файлов в указанной папке.
  - `E`: Фильтрация файлов по расширению `.ipynb` и исключение файлов с `.executed.` и `.local.` в имени.
  - `F`: Возвращение списка полных путей к файлам Jupyter notebook.
- **Test Notebook Execution Function**: Блок, описывающий логику функции `test_notebook_execution`.
  - `TestNotebookExecutionCall`: Вызов функции `test_notebook_execution(notebook_path)`.
  - `G`: Открытие файла Jupyter notebook в режиме чтения.
  - `H`: Чтение содержимого файла с помощью `nbformat.read`.
  - `I`: Инициализация объекта `ExecutePreprocessor` для выполнения ноутбука.
  - `J`: Выполнение ноутбука с помощью `ep.preprocess`.
  - `K`: Обработка исключений, которые могут возникнуть при выполнении ноутбука.
  - `L`: Сохранение выполненного ноутбука.
  - `M`: Вывод сообщения об успешном выполнении.
  - `N`: Вывод сообщения об ошибке при выполнении.

### 3. <объяснение>

#### Импорты:
-   **`os`**:  Используется для работы с операционной системой, в частности, для получения списка файлов в директории.
-   **`nbformat`**: Библиотека для работы с Jupyter notebook файлами (.ipynb). Используется для чтения и записи файлов.
-   **`nbconvert.preprocessors.ExecutePreprocessor`**: Класс из библиотеки `nbconvert`, который используется для выполнения ячеек кода в Jupyter ноутбуке.
-   **`pytest`**: Фреймворк для тестирования, используется для параметризации тестов и генерации отчетов о тестировании.
-   **`sys`**: Используется для модификации путей поиска модулей Python, чтобы убедиться, что импортируются необходимые модули из правильных директорий.
-    `sys.path.insert(0, '...')`: Эти вставки добавляют директории в начало пути поиска модулей Python. Это гарантирует, что при импорте, Python сначала будет искать модули в этих директориях, а не в стандартных местах.
    - `../../tinytroupe/`: добавляет путь к пакету `tinytroupe`.
    - `../../`: добавляет путь к родительской директории.
    - `../`: добавляет путь к родительской директории относительно текущего файла.

#### Переменные:
-   **`NOTEBOOK_FOLDER`**: Строка, содержащая путь к папке с Jupyter notebook файлами.
-   **`TIMEOUT`**: Целое число, устанавливающее таймаут в секундах для выполнения одного ноутбука.
-   **`KERNEL_NAME`**: Строка, задающая имя ядра Jupyter для выполнения ноутбуков.
-   **`notebook_path`**: Строка, содержащая путь к конкретному notebook файлу (используется в parametrize).

#### Функции:
-   **`get_notebooks(folder)`**:
    -   **Аргументы**: `folder` (строка) – путь к папке, в которой нужно искать notebook-и.
    -   **Возвращает**: Список строк, каждая из которых – путь к notebook файлу.
    -   **Назначение**: Находит все Jupyter notebook файлы (.ipynb) в заданной папке, которые не содержат `.executed.` или `.local.` в имени.
    -   **Пример:**
        ```python
        notebook_paths = get_notebooks("../examples/")
        # notebook_paths будет списком типа ["../examples/example1.ipynb", "../examples/example2.ipynb", ...]
        ```
-   **`test_notebook_execution(notebook_path)`**:
    -   **Аргументы**: `notebook_path` (строка) – путь к notebook файлу, который нужно выполнить.
    -   **Возвращает**: Ничего (None), но вызывает ошибку тестирования, если выполнение notebook-а завершилось с исключением.
    -   **Назначение**:
        -   Открывает, читает и выполняет Jupyter notebook.
        -   Сохраняет копию выполненного notebook-а с изменённым именем.
        -   Если при выполнении возникает ошибка, тест завершается неудачей с подробным сообщением.
    -   **Пример:**
        ```python
        test_notebook_execution("../examples/example1.ipynb") # выполнение пройдет успешно если example1.ipynb исполняется без ошибок
        ```
-   **`@pytest.mark.parametrize("notebook_path", get_notebooks(NOTEBOOK_FOLDER))`**:
    -   **Назначение**: Декоратор pytest, который параметризирует функцию `test_notebook_execution` так, чтобы она запускалась для каждого notebook-а из списка, возвращаемого `get_notebooks(NOTEBOOK_FOLDER)`.

#### Потенциальные ошибки и области для улучшения:

-   **Обработка исключений**: Хотя код обрабатывает исключения при выполнении ноутбуков, можно было бы добавить более детальную информацию об ошибке (например, номер ячейки, вызвавшей ошибку).
-   **Таймаут**: Большой таймаут может замедлить процесс тестирования, если один из ноутбуков зациклится. Можно было бы рассмотреть динамическое определение таймаута, исходя из размера или сложности ноутбука.
-   **Фильтрация файлов**: Фильтрация файлов с помощью `endswith` и `not in` может быть не очень гибкой. Если потребуется более сложная логика, возможно, стоит использовать регулярные выражения.
-   **Пути**: Зависимость от жестко закодированных путей к файлам и пакетам делает код менее переносимым. Можно было бы рассмотреть использование относительных путей или переменных окружения.

#### Взаимосвязи с другими частями проекта:
- Данный код тесно связан с папкой `../examples/`, где находятся Jupyter Notebook файлы, которые должны быть протестированы.
- Код использует `sys.path.insert` для того, чтобы подключить модули из `tinytroupe`.
- Этот код является частью тестового набора проекта и используется для проверки правильности работы Jupyter Notebook примеров.