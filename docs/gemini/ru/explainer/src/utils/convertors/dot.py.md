## <алгоритм>

1. **Начало**:
    - Программа запускается.
    
2. **Проверка аргументов командной строки**:
    - Проверяется, передано ли ровно два аргумента командной строки (имя входного DOT файла и имя выходного PNG файла).
    - Если количество аргументов не равно двум, выводится сообщение об использовании и программа завершается.
    - *Пример*:
        ```bash
        #Правильное использование
        python dot.py input.dot output.png
        
        #Неправильное использование
        python dot.py input.dot
        ```
3. **Получение аргументов**:
    - Если количество аргументов равно двум, то из `sys.argv` извлекаются:
        - `input_dot_file`: путь к входному DOT файлу.
        - `output_png_file`: путь к выходному PNG файлу.
     - *Пример*: `input_dot_file` = "graph.dot", `output_png_file` = "graph.png"

4. **Вызов функции `dot2png`**:
    - Вызывается функция `dot2png` с аргументами `input_dot_file` и `output_png_file`.

5. **Внутри `dot2png`**:
    - **Чтение DOT файла**:
        - Пытается открыть файл по пути `dot_file` в режиме чтения ('r').
        - Если файл не найден, выбрасывается исключение `FileNotFoundError`.
        - *Пример*: Если `dot_file` = "graph.dot", то читается содержимое этого файла.
    - **Создание объекта `Source`**:
        - Если файл успешно открыт, содержимое файла сохраняется в переменную `dot_content`.
        - Из содержимого DOT файла создается объект `Source`.
        - *Пример*: `dot_content` = "digraph { A -> B; }" -> `source` = `graphviz.Source` объект
    - **Настройка формата и рендеринг**:
        - Устанавливается формат выходного файла для объекта `source` в 'png'.
        - Вызывается метод `render` объекта `source` для рендеринга PNG файла с именем `png_file`,  с включенным удалением временных файлов (`cleanup=True`).
        - *Пример*: `source` рендерит  "graph.png" на основе DOT содержимого.
    - **Обработка ошибок**:
         - Если происходит `FileNotFoundError`, выводится сообщение об ошибке, и исключение передается дальше.
         - Если происходит любое другое исключение (общая ошибка), то выводится сообщение об ошибке и исключение передается дальше.

6. **Завершение**:
    - После завершения функции `dot2png`, программа завершается.

## <mermaid>

```mermaid
flowchart TD
    Start[Start] --> CheckArgs{Check Command-Line Arguments}
    CheckArgs -- Incorrect Number of Arguments --> UsageMessage[Print Usage Message]
    UsageMessage --> Exit1[Exit (1)]
    CheckArgs -- Correct Number of Arguments --> GetFilePaths[Get Input and Output File Paths from Command-Line Arguments]
    GetFilePaths --> CallDot2Png[Call dot2png Function]

    subgraph dot2png Function
        CallDot2Png --> ReadDotFile[Read Input DOT File]
        ReadDotFile -- File Not Found --> FileNotFoundError[Handle FileNotFoundError]
        FileNotFoundError --> PrintFileNotFoundError[Print File Not Found Error Message]
        PrintFileNotFoundError --> RaiseException1[Raise FileNotFoundError]
        ReadDotFile -- File Found --> CreateSourceObj[Create Graphviz Source Object]
        CreateSourceObj --> SetFormat[Set Output Format to PNG]
        SetFormat --> RenderPng[Render PNG File]
        RenderPng -- Exception --> ExceptionHandler[Handle Generic Exception]
        ExceptionHandler --> PrintGenericError[Print Generic Error Message]
        PrintGenericError --> RaiseException2[Raise Exception]
        RenderPng --> EndDot2Png[End dot2png Function]
    end
    
    EndDot2Png --> End[End]
    RaiseException1 --> End
    RaiseException2 --> End
```
**Анализ зависимостей `mermaid`:**
- `Start`: Начало выполнения программы.
- `CheckArgs`: Проверка количества аргументов командной строки.
- `UsageMessage`: Вывод сообщения об использовании.
- `Exit1`: Выход из программы с кодом 1.
- `GetFilePaths`: Получение путей входного и выходного файлов из аргументов командной строки.
- `CallDot2Png`: Вызов функции `dot2png` для преобразования DOT в PNG.
- `ReadDotFile`: Чтение содержимого входного DOT-файла.
- `FileNotFoundError`: Обработка ошибки, когда файл не найден.
- `PrintFileNotFoundError`: Вывод сообщения об ошибке "Файл не найден".
- `RaiseException1`: Возбуждение исключения `FileNotFoundError`.
- `CreateSourceObj`: Создание объекта `graphviz.Source` на основе содержимого DOT файла.
- `SetFormat`: Установка формата вывода объекта `Source` в PNG.
- `RenderPng`: Рендеринг PNG файла.
- `ExceptionHandler`: Обработка общего исключения.
- `PrintGenericError`: Вывод сообщения об общей ошибке.
- `RaiseException2`: Возбуждение общего исключения.
- `EndDot2Png`: Конец работы функции `dot2png`.
- `End`: Завершение программы.

## <объяснение>

**Импорты:**

- `sys`: Модуль `sys` используется для доступа к параметрам командной строки (`sys.argv`) и для завершения программы (`sys.exit`).
- `graphviz`: Из модуля `graphviz` импортируется класс `Source`. Этот класс используется для представления графа, заданного в формате DOT, и для его рендеринга в различные форматы (в данном случае в PNG).
  
**Функции:**

-   `dot2png(dot_file: str, png_file: str) -> None`:
    -   **Аргументы**:
        -   `dot_file` (`str`): Путь к входному DOT-файлу.
        -   `png_file` (`str`): Путь, куда будет сохранен выходной PNG-файл.
    -   **Возвращаемое значение**: `None`, функция не возвращает значения.
    -   **Назначение**: Читает содержимое DOT-файла, создает на его основе объект `graphviz.Source`, устанавливает формат вывода в PNG и рендерит изображение в файл.
    -   **Пример**: `dot2png("input.dot", "output.png")` преобразует `input.dot` в `output.png`.
    -   **Возможные ошибки**:
        -   `FileNotFoundError`: Возникает, если файл, указанный в `dot_file`, не существует.
        -   `Exception`: Возникает при любых других ошибках, возникающих в процессе конвертации.

**Переменные:**

-   `dot_file` (`str`): Имя файла с расширением .dot, который нужно преобразовать.
-   `png_file` (`str`): Имя файла с расширением .png, в который будет сохранён результат.
-   `dot_content` (`str`): Содержимое DOT-файла, считанное из файла.
-   `source` (`graphviz.Source`): Объект, представляющий граф из DOT-содержимого, созданный на основе данных из `dot_content`.
-   `input_dot_file` (`str`): Путь к входному DOT файлу, полученный из аргументов командной строки.
-   `output_png_file` (`str`): Путь к выходному PNG файлу, полученный из аргументов командной строки.

**Объяснение кода:**

-   Код предназначен для преобразования файлов в формате DOT в изображения PNG с использованием библиотеки `graphviz`.
-   Функция `dot2png` является основной частью скрипта, которая выполняет преобразование, обрабатывая ошибки.
-   Условие `if __name__ == "__main__":` гарантирует, что код внутри него будет выполнен только при непосредственном запуске скрипта, а не при его импорте как модуля.
-   Код обрабатывает возможные исключения, такие как `FileNotFoundError` и общие ошибки `Exception`, выводя сообщения об ошибках в консоль и передавая исключение дальше.
-   Функция `sys.argv` получает аргументы командной строки, где `sys.argv[0]` – имя скрипта, `sys.argv[1]` – первый аргумент (путь к dot файлу), а `sys.argv[2]` – второй аргумент (путь к png файлу).
-   Если количество аргументов не равно 3, то выводится сообщение об использовании скрипта.
-   Внутри блока `try` происходит чтение файла и создание `Source` объекта, затем устанавливается формат и происходит рендеринг.
-   Блоки `except` обрабатывают ошибки, если они возникают.
-   Код простой, функциональный и выполняет свою задачу, но не имеет дополнительных настроек.

**Цепочка взаимосвязей с другими частями проекта (если применимо):**

-   Этот модуль, предположительно, является частью более крупного проекта `hypotez`, где используется для визуализации каких-либо графовых структур. 
-   Модуль `dot.py` входит в пакет `src.utils.convertors` что означает он может быть вызван другими компонентами проекта, где требуется преобразование DOT-файлов в PNG.
-   На данный момент не видно связей с `header.py` или глобальными настройками (`gs`).