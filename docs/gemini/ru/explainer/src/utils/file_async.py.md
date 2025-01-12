## АНАЛИЗ КОДА `hypotez/src/utils/file_async.py`

### 1. <алгоритм>

**save_text_file**
1.  Принимает `file_path` (путь к файлу), `data` (данные для записи) и `mode` (режим записи).
    *   Пример: `save_text_file("test.txt", "Hello world!", "w")`
2.  Преобразует `file_path` в объект `Path`.
3.  Создает родительские директории для файла, если они не существуют.
    *   Пример: если `file_path` - `folder/subfolder/test.txt`, то создается `folder` и `subfolder`.
4.  Открывает файл в асинхронном режиме с указанным `mode` и кодировкой `utf-8`.
5.  Проверяет тип данных `data`:
    *   Если `data` - список (`list`), записывает каждую строку в файл с новой строки.
        *   Пример: `data` = `["line1", "line2"]` запишет в файл `line1\nline2\n`.
    *   Если `data` - словарь (`dict`), записывает `data` в файл в формате JSON.
        *   Пример: `data` = `{"key": "value"}` запишет в файл `{"key": "value"}`.
    *   Если `data` - строка (`str`), записывает `data` в файл.
        *   Пример: `data` = `"text"` запишет в файл `text`.
6.  Закрывает файл и возвращает `True` при успешной записи, `False` в случае ошибки.
    *   Пример: `True` или `False`.
    

**read_text_file**
1.  Принимает `file_path` (путь к файлу/директории), `as_list` (возвращать ли список/генератор), `extensions` (список расширений), `chunk_size` (размер чанка), `recursive` (рекурсивный поиск), `patterns` (шаблоны для фильтрации).
    *   Пример: `read_text_file("test.txt", as_list=True)` или `read_text_file("folder", recursive=True, patterns="*.txt")`
2.  Преобразует `file_path` в объект `Path`.
3.  Проверяет, является ли путь файлом или директорией:
    *   Если это файл:
        *   Если `as_list` - `True`, возвращает асинхронный генератор строк через `_read_file_lines_generator`.
        *   Если `as_list` - `False`, возвращает содержимое файла как строку через `_read_file_content`.
    *   Если это директория:
        *   Если `recursive` - `True`:
            *   Если `patterns` заданы, получает список файлов, соответствующих шаблонам, через `recursively_get_file_path`.
            *   Иначе, получает список всех файлов в директории и её поддиректориях с фильтрацией по расширениям.
            *   Если `as_list` - `True`, возвращает генератор строк из всех файлов через `yield_text_from_files`.
            *   Если `as_list` - `False`, возвращает объединенное содержимое всех файлов как строку.
        *   Если `recursive` - `False`:
            *   Получает список файлов в директории с фильтрацией по расширениям.
            *   Если `as_list` - `True`, возвращает генератор строк из всех файлов через `read_text_file`.
            *   Если `as_list` - `False`, возвращает объединенное содержимое всех файлов как строку.
    *   Если это не файл и не директория, возвращает `None` и логирует ошибку.
4.  Возвращает результат в зависимости от условий или `None` в случае ошибки.
    

**yield_text_from_files**
1.  Принимает `file_path`, `as_list`, `chunk_size`.
    *   Пример: `yield_text_from_files("test.txt", as_list=True)`
2.  Преобразует `file_path` в объект `Path`.
3.  Проверяет, является ли путь файлом.
    *   Если это файл:
        *   Если `as_list` - `True`, возвращает асинхронный генератор строк через `_read_file_lines_generator`.
        *   Если `as_list` - `False`, возвращает содержимое файла как строку через `_read_file_content`.
4.  Если путь не является файлом, логирует ошибку.
5.  Возвращает результат или `None` в случае ошибки.
    

**_read_file_content**
1.  Принимает `file_path`, `chunk_size`.
    *   Пример: `_read_file_content(Path("test.txt"), 4096)`
2.  Открывает файл в асинхронном режиме для чтения с кодировкой `utf-8`.
3.  Читает файл по чанкам, добавляя их к результирующей строке.
4.  Возвращает содержимое файла как строку.
    

**_read_file_lines_generator**
1.  Принимает `file_path`, `chunk_size`.
    *   Пример: `_read_file_lines_generator(Path("test.txt"), 4096)`
2.  Открывает файл в асинхронном режиме для чтения с кодировкой `utf-8`.
3.  Читает файл по чанкам.
4.  Разделяет каждый чанк на строки и возвращает их через `yield`.
5.  Обрабатывает случай, когда последняя строка не заканчивается символом новой строки и читает дополнительный байт, чтобы правильно завершить строку.
6.  Возвращает строки файла через генератор.
    

**get_filenames_from_directory**
1.  Принимает `directory` и `extensions` (опционально).
    *   Пример: `get_filenames_from_directory("folder", [".txt", ".md"])`
2.  Преобразует `directory` в объект `Path`.
3.  Если `extensions` - строка, преобразует её в список.
4.  Получает список имен файлов из директории, фильтруя по расширениям.
5.  Возвращает список имен файлов.
    

**recursively_yield_file_path**
1.  Принимает `root_dir` и `patterns` (опционально).
    *   Пример: `recursively_yield_file_path("folder", ["*.txt", "*.md"])`
2.  Преобразует `patterns` в список, если это строка.
3.  Итерируется по всем шаблонам, получает все файлы из указанной директории и её поддиректорий, соответствующие шаблонам, и возвращает их через генератор.
4.  Возвращает пути к файлам через генератор.
    

**recursively_get_file_path**
1.  Принимает `root_dir` и `patterns` (опционально).
    *   Пример: `recursively_get_file_path("folder", ["*.txt", "*.md"])`
2.  Преобразует `patterns` в список, если это строка.
3.  Итерируется по всем шаблонам, получает все файлы из указанной директории и её поддиректорий, соответствующие шаблонам, и добавляет их в список.
4.  Возвращает список путей к файлам.
    

**recursively_read_text_files**
1.  Принимает `root_dir`, `patterns`, `as_list`.
    *   Пример: `recursively_read_text_files("folder", ["*.txt"], as_list=True)`
2.  Проверяет, является ли `root_dir` директорией, и если нет, возвращает пустой список.
3.  Преобразует `patterns` в список, если это строка.
4.  Рекурсивно обходит директорию, фильтруя файлы по шаблонам.
5.  Открывает каждый найденный файл, читает его содержимое и добавляет в список.
6.  Если `as_list` - `True`, добавляет список строк файла. Иначе добавляет всю строку содержимого файла.
7.  Возвращает список содержимого файлов или список строк.
    

**get_directory_names**
1.  Принимает `directory`.
    *   Пример: `get_directory_names("folder")`
2.  Получает список имен всех директорий в `directory`.
3.  Возвращает список имен директорий.
    

**remove_bom**
1.  Принимает `path`.
    *   Пример: `remove_bom("test.txt")` или `remove_bom("folder")`
2.  Преобразует `path` в объект `Path`.
3.  Проверяет, является ли путь файлом или директорией.
    *   Если это файл, открывает его для чтения и записи, удаляет BOM, сохраняет изменения.
    *   Если это директория, рекурсивно обходит её, находит все файлы Python (с расширением `.py`) и удаляет BOM в каждом файле.
    *   Если путь не является ни файлом, ни директорией, логирует ошибку.
    

**main**
1.  Определяет корневую директорию.
2.  Запускает функцию `remove_bom` для удаления BOM из файлов в корневой директории.
    

### 2. <mermaid>
```mermaid
flowchart TD
    subgraph save_text_file
        A[<code>save_text_file</code><br> (file_path, data, mode)]
        B[Path(file_path)]
        C[os.makedirs<br>(file_path.parent, exist_ok=True)]
        D[aiofiles.open<br>(file_path, mode, encoding='utf-8')]
        E{isinstance(data, list)?}
        F{isinstance(data, dict)?}
        G[file.write(line+'\n')]
        H[json.dumps(data, ensure_ascii=False, indent=4)]
        I[file.write(data)]
        J[return True]
        K[logger.error]
        L[return False]

        A --> B --> C --> D
        D --> E
        E -- Yes --> F
        F -- Yes --> H --> I
        F -- No --> I
        E -- No --> I
        I --> J
        D -- Exception --> K --> L
    end
    
    subgraph read_text_file
        M[<code>read_text_file</code><br>(file_path, as_list, extensions, chunk_size, recursive, patterns)]
        N[path = Path(file_path)]
        O{path.is_file()?}
        P{as_list?}
        Q[_read_file_lines_generator(path, chunk_size)]
        R[_read_file_content(path, chunk_size)]
        S{path.is_dir()?}
        T{recursive?}
        U{patterns?}
        V[recursively_get_file_path(path, patterns)]
        W[path.rglob('*')]
        X{extensions?}
        Y[yield_text_from_files]
        Z[asyncio.gather]
        AA[Join Contents]
        AB[path.iterdir()]
        AC[logger.error]
        AD[return None]


        M --> N --> O
        O -- Yes --> P
        P -- Yes --> Q
        P -- No --> R
        O -- No --> S
        S -- Yes --> T
        T -- Yes --> U
        U -- Yes --> V
        U -- No --> W
        W --> X
         X -- Yes-->Y
         X -- No-->Y
        T-- No--> AB-->X
        S -- No --> AC --> AD
        V --> X
         X -- Yes-->Y
         X -- No-->Y

        Y -- as_list=True -->  Z
        Z-- as_list=True -->  AA

    end

    subgraph yield_text_from_files
      AE[<code>yield_text_from_files</code><br>(file_path, as_list, chunk_size)]
        AF[path = Path(file_path)]
        AG{path.is_file()?}
        AH{as_list?}
        AI[_read_file_lines_generator(path, chunk_size)]
        AJ[_read_file_content(path, chunk_size)]
        AK[logger.error]

        AE --> AF --> AG
        AG -- Yes --> AH
        AH -- Yes --> AI
        AH -- No --> AJ
       AG -- No --> AK
       AI--> AE
       AJ--> AE
    end

    subgraph _read_file_content
        AL[<code>_read_file_content</code><br>(file_path, chunk_size)]
        AM[aiofiles.open<br>(file_path, 'r', encoding='utf-8')]
        AN[file.read(chunk_size)]
        AO{not chunk?}
        AP[content += chunk]
        AQ[return content]
        AR[return '']
        AS[logger.error]

        AL --> AM
        AM --> AN
        AN --> AO
        AO -- Yes --> AQ
        AO -- No --> AP --> AN
        AM--Exception-->AS-->AR
    end

     subgraph _read_file_lines_generator
        AT[<code>_read_file_lines_generator</code><br>(file_path, chunk_size)]
        AU[aiofiles.open<br>(file_path, 'r', encoding='utf-8')]
        AV[file.read(chunk_size)]
        AW{not chunk?}
        AX[lines = chunk.splitlines()]
        AY{len(lines) > 0 and not chunk.endswith('\n')?}
         AZ[next_chunk = await f.read(1)]
        BA{next_chunk != ''?}
         BB[lines[-1] = lines[-1] + next_chunk]
        BC[yield line]
        BD[logger.error]
         
        AT --> AU
        AU --> AV
        AV --> AW
        AW -- Yes -->  BC
         AW -- No --> AX
         AX-->AY
         AY--Yes-->AZ
        AZ-->BA
        BA--Yes-->BB
        BA--No-->BC
         AY--No-->BC
        AU--Exception-->BD
        BC-->AT

    end
    
    subgraph get_filenames_from_directory
        BE[<code>get_filenames_from_directory</code><br>(directory, extensions)]
        BF[Path(directory)]
        BG{isinstance(extensions, str)?}
        BH[extensions = [extensions]]
        BI[extensions = [ext...]]
        BJ[file.is_file() and ...]
        BK[return list[file.name]]
         BL[logger.error]
          BM[return []]
           BE-->BF-->BG
          BG -- Yes-->BH
          BH-->BI
            BG -- No-->BI
          BI-->BJ
          BJ-->BK
           BF--Exception-->BL-->BM
    end
     subgraph recursively_yield_file_path
         BN[<code>recursively_yield_file_path</code><br>(root_dir, patterns)]
        BO{isinstance(patterns, str)?}
        BP[patterns = [patterns]]
        BQ[Path(root_dir).rglob(pattern)]
         BR[yield path]
        BS[logger.error]
           BN-->BO
          BO -- Yes-->BP
          BO -- No-->BQ
          BP-->BQ
          BQ-->BR
         BQ--Exception-->BS
         BR-->BN
    end
    subgraph recursively_get_file_path
      BT[<code>recursively_get_file_path</code><br>(root_dir, patterns)]
      BU[file_paths = []]
      BV{isinstance(patterns, str)?}
      BW[patterns = [patterns]]
      BX[Path(root_dir).rglob(pattern)]
      BY[file_paths.append(path)]
      BZ[return file_paths]
      CA[logger.error]
        CB[return []]
    
      BT-->BU
      BU-->BV
       BV--Yes-->BW
       BV--No-->BX
        BW-->BX
      BX-->BY
      BY-->BX
      BX-->BZ
        BT--Exception-->CA-->CB
    end
    subgraph recursively_read_text_files
        CC[<code>recursively_read_text_files</code><br>(root_dir, patterns, as_list)]
        CD[matches = []]
        CE[Path(root_dir)]
        CF{CE.is_dir()?}
        CG[logger.debug]
        CH[return []]
        CI{isinstance(patterns, str)?}
        CJ[patterns = [patterns]]
        CK[os.walk(root_path)]
        CL{any(fnmatch.fnmatch(filename, pattern) for pattern in patterns)?}
        CM[file_path = Path(root) / filename]
        CN[aiofiles.open(file_path, 'r', encoding='utf-8')]
        CO{as_list?}
        CP[matches.extend(await file.readlines())]
        CQ[matches.append(await file.read())]
        CR[logger.error]
        CS[return matches]

        CC --> CD --> CE --> CF
        CF -- No --> CG --> CH
        CF -- Yes --> CI
        CI -- Yes --> CJ
        CJ --> CK
         CI -- No --> CK
         CK-->CL
        CL -- Yes --> CM --> CN
        CN --> CO
        CO -- Yes --> CP
        CO -- No --> CQ
         CL -- No --> CK
        CN--Exception-->CR
         CK-->CS
    end
     subgraph get_directory_names
      CT[<code>get_directory_names</code><br>(directory)]
        CU[Path(directory).iterdir()]
        CV[entry.is_dir()]
       CW[return list[entry.name]]
       CX[logger.error]
        CY[return []]

        CT-->CU
         CU-->CV
        CV-->CW
      CU--Exception-->CX-->CY
    end
    
    subgraph remove_bom
        CZ[<code>remove_bom</code><br>(path)]
        DA[Path(path)]
        DB{DA.is_file()?}
         DC[aiofiles.open<br>(path, 'r+', encoding='utf-8')]
        DD[content = await file.read()]
        DE[content = content.replace('\ufeff', '')]
         DF[await file.seek(0)]
         DG[await file.write(content)]
         DH[await file.truncate()]
        DI[logger.error]
        DJ{DA.is_dir()?}
        DK[os.walk(path)]
         DL{file.endswith('.py')?}
        DM[file_path = Path(root) / file]
         DN[aiofiles.open<br>(file_path, 'r+', encoding='utf-8')]
          DO[content = await f.read()]
        DP[content = content.replace('\ufeff', '')]
         DQ[await f.seek(0)]
         DR[await f.write(content)]
         DS[await f.truncate()]
        DT[logger.error]
      DU[logger.error]
    CZ --> DA
    DA --> DB
    DB -- Yes --> DC --> DD --> DE --> DF --> DG --> DH
    DC--Exception-->DI
    DB--No-->DJ
    DJ--Yes-->DK-->DL
    DL--Yes-->DM-->DN-->DO-->DP-->DQ-->DR-->DS
        DN--Exception-->DT
    DJ--No-->DU
        
    end
    subgraph main
        DV[<code>main</code>]
        DW[remove_bom]
        DX[logger.info]
         DV-->DX-->DW
    end
     
    

```

### 3. <объяснение>

**Импорты:**
   - `os`:  Используется для работы с операционной системой, например, для рекурсивного обхода директорий через `os.walk`.
   - `json`:  Используется для работы с JSON-данными,  для сериализации словарей в строковый формат при сохранении в файл.
   - `fnmatch`: Используется для сравнения имен файлов с шаблонами.
   - `asyncio`: Используется для поддержки асинхронных операций, таких как чтение и запись файлов.
   - `aiofiles`: Библиотека для асинхронной работы с файлами. Позволяет выполнять файловые операции без блокировки основного потока.
   - `aiofiles.os`: Используется для асинхронного создания директорий.
   - `pathlib.Path`:  Используется для представления путей к файлам и директориям в объектно-ориентированном виде.
   - `typing`:  Используется для аннотации типов, повышая читаемость и помогая инструментам статического анализа.
   - `src.logger.logger`: Импортируется для логирования ошибок и другой информации. Обеспечивает централизованное логирование в проекте.
   
**Переменные:**
   - `MODE`: Глобальная константа, определяющая режим работы модуля (`'dev'` в данном случае).

**Функции:**
   - `save_text_file(file_path, data, mode='w')`:
        -   **Args:** `file_path` (путь к файлу), `data` (данные для записи - строка, список строк или словарь), `mode` (режим записи: `w` - перезапись, `a` - добавление).
        -   **Returns:** `True`, если файл успешно сохранен, `False` в случае ошибки.
        -   **Назначение:** Асинхронно сохраняет данные в текстовый файл. Поддерживает запись строк, списков строк и словарей (в формате JSON).
        -   **Пример:** `await save_text_file("output.txt", ["line1", "line2"], 'w')`
        -   **Взаимосвязи:** Использует `aiofiles` для асинхронной записи, `json` для обработки словарей,  `Path` для обработки путей. Логирует ошибки через `src.logger.logger`.
   - `read_text_file(file_path, as_list=False, extensions=None, chunk_size=8192, recursive=False, patterns=None)`:
        -   **Args:** `file_path` (путь к файлу или директории), `as_list` (возвращать ли список строк или генератор - True), `extensions` (список расширений для файлов), `chunk_size` (размер чанка), `recursive` (рекурсивный поиск), `patterns` (шаблоны для фильтрации).
        -   **Returns:** Асинхронный генератор строк, строку, список строк или `None`.
        -   **Назначение:** Асинхронно читает содержимое файла(ов) или директории. Может возвращать содержимое файла построчно (генератор), как строку или как список строк. Поддерживает рекурсивный поиск и фильтрацию.
        -   **Пример:** `await read_text_file("input.txt", as_list=True)` или `await read_text_file("folder", recursive=True, patterns="*.txt")`
        -   **Взаимосвязи:**  Использует `Path` для работы с путями. Вызывает `_read_file_lines_generator`, `_read_file_content`, `recursively_get_file_path`, `yield_text_from_files` для обработки файлов. Логирует ошибки через `src.logger.logger`.
   - `yield_text_from_files(file_path, as_list=False, chunk_size=8192)`:
        -   **Args:** `file_path` (путь к файлу), `as_list` (возвращать ли генератор строк), `chunk_size` (размер чанка).
        -   **Returns:** Асинхронный генератор строк или строка.
        -   **Назначение:** Асинхронно читает содержимое файла и возвращает его в виде генератора строк или строки. Используется для чтения файлов по частям.
        -  **Пример:** `async for line in yield_text_from_files("input.txt", as_list=True): print(line)`
        -   **Взаимосвязи:** Вызывает `_read_file_lines_generator` или `_read_file_content`. Логирует ошибки через `src.logger.logger`.
   - `_read_file_content(file_path, chunk_size)`:
        -   **Args:** `file_path` (путь к файлу), `chunk_size` (размер чанка).
        -   **Returns:** Строка с содержимым файла.
        -   **Назначение:** Асинхронно читает содержимое файла по чанкам и возвращает как одну строку.
        -   **Пример:**  `_read_file_content(Path("input.txt"), 4096)`
        -   **Взаимосвязи:**  Использует `aiofiles` для чтения файла. Логирует ошибки через `src.logger.logger`.
   - `_read_file_lines_generator(file_path, chunk_size)`:
        -   **Args:** `file_path` (путь к файлу), `chunk_size` (размер чанка).
        -   **Returns:** Асинхронный генератор строк из файла.
        -   **Назначение:** Асинхронно читает файл по строкам с помощью генератора, для экономии памяти.
        -  **Пример:** `async for line in _read_file_lines_generator(Path("input.txt"), 4096): print(line)`
        -   **Взаимосвязи:** Использует `aiofiles` для чтения файла. Логирует ошибки через `src.logger.logger`.
   - `get_filenames_from_directory(directory, extensions='*')`:
        -   **Args:** `directory` (путь к директории), `extensions` (список расширений).
        -   **Returns:** Список имен файлов в директории.
        -   **Назначение:** Асинхронно возвращает список имен файлов в директории, опционально фильтруя по расширениям.
        -   **Пример:** `await get_filenames_from_directory("folder", [".txt", ".md"])`
        -   **Взаимосвязи:** Использует `Path` для работы с путями. Логирует ошибки через `src.logger.logger`.
   - `recursively_yield_file_path(root_dir, patterns='*')`:
        -  **Args:** `root_dir` (путь к корневой директории), `patterns` (список шаблонов).
        -   **Returns:** Асинхронный генератор путей к файлам.
        -   **Назначение:** Асинхронно рекурсивно возвращает пути ко всем файлам, соответствующим шаблонам, в указанной директории.
        -   **Пример:** `async for path in recursively_yield_file_path("folder", ["*.txt", "*.md"]): print(path)`
        -   **Взаимосвязи:**  Использует `Path` для работы с путями. Логирует ошибки через `src.logger.logger`.
   - `recursively_get_file_path(root_dir, patterns='*')`:
        -   **Args:** `root_dir` (путь к корневой директории), `patterns` (список шаблонов).
        -   **Returns:** Список путей к файлам.
        -   **Назначение:** Асинхронно рекурсивно возвращает список путей ко всем файлам, соответствующим шаблонам, в указанной директории.
        -   **Пример:** `await recursively_get_file_path("folder", ["*.txt", "*.md"])`
        -   **Взаимосвязи:** Использует `Path` для работы с путями. Логирует ошибки через `src.logger.logger`.
   - `recursively_read_text_files(root_dir, patterns, as_list=False)`:
        -   **Args:** `root_dir` (путь к корневой директории), `patterns` (список шаблонов), `as_list` (возвращать ли список строк).
        -   **Returns:** Список содержимого файлов.
        -  **Назначение:** Асинхронно рекурсивно читает текстовые файлы из указанной директории, фильтруя по шаблонам.
        -   **Пример:** `await recursively_read_text_files("folder", ["*.txt"], as_list=True)`
        -   **Взаимосвязи:** Использует `os.walk` для рекурсивного обхода директорий, `fnmatch` для фильтрации файлов по шаблонам, `aiofiles` для чтения файлов,  `Path` для работы с путями.  Логирует ошибки через `src.logger.logger`.
   -  `get_directory_names(directory)`:
        -   **Args:** `directory` (путь к директории).
        -   **Returns:** Список имен директорий в указанной директории.
        -   **Назначение:** Асинхронно возвращает список имен директорий из указанной директории.
        -   **Пример:** `await get_directory_names("folder")`
        -   **Взаимосвязи:**  Использует `Path` для работы с путями. Логирует ошибки через `src.logger.logger`.
   - `remove_bom(path)`:
        -   **Args:** `path` (путь к файлу или директории).
        -   **Returns:** `None`
        -   **Назначение:** Асинхронно удаляет BOM (Byte Order Mark) из текстового файла или из всех файлов Python в директории.
        -   **Пример:** `await remove_bom("file.txt")` или `await remove_bom("folder")`
        -   **Взаимосвязи:**  Использует `aiofiles` для чтения и записи файлов. Рекурсивно обходит директории через `os.walk`. Логирует ошибки через `src.logger.logger`.

**Взаимосвязь с другими частями проекта:**
   -  Модуль `src.utils.file_async.py` является частью утилитарного слоя (`src.utils`) и предоставляет общие функции для работы с файлами. 
   -  Использует  `src.logger.logger` для логирования, что обеспечивает централизованное управление логированием в проекте.
   -  Может быть использован другими модулями проекта для чтения и записи файлов, поиска и обработки данных в файлах.

**Потенциальные ошибки или области для улучшения:**
   -  Обработка исключений: во многих функциях используются общие блоки `try...except Exception`. Можно рассмотреть более детальную обработку исключений, чтобы ловить и обрабатывать конкретные ошибки.
   -  Улучшение производительности: некоторые операции с файлами могут быть оптимизированы, особенно при работе с большими файлами. Можно рассмотреть использование более эффективных способов чтения/записи файлов и более тонкую настройку параметров чанка.
   -  Более подробное документирование:  Документация для некоторых функций (особенно `_read_file_lines_generator` и `_read_file_content`) может быть более подробной, с описанием случаев использования и возможных подводных камней.
   -  Добавление тестов: Для повышения надежности кода следует добавить unit-тесты, чтобы проверить каждую функцию в различных условиях.
   -  Обработка ошибок кодировки: Можно добавить более явную обработку ошибок кодировки, которые могут возникнуть при чтении файлов.
   -   `recursively_read_text_files` читает файлы синхронно внутри цикла, что может замедлять работу, особенно при большом количестве файлов. Стоит переписать эту функцию с использованием асинхронных операций, для параллельного чтения файлов.
   - `remove_bom`  читает файл в память целиком, что не эффективно при работе с большими файлами. Стоит переписать с применением генераторов, для построчной обработки файла.