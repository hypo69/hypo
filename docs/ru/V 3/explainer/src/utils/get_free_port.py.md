# Проект `hypotez`
# Роль `code explainer`
## ИНСТРУКЦИЯ  :

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:  

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.  
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости, 
    которые импортируются при создании диаграммы. 
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`, 
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!  
    
    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]
    
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] 
    ```

3. **<объяснение>**: Предоставь подробные объяснения:  
   - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.  
   - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.  
   - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.  
   - **Переменные**: Их типы и использование.  
   - Выдели потенциальные ошибки или области для улучшения.  

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).  

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)



## Твое поведение при анализе кода:
- всегда смотри системную инструкцию для обработки кода проекта `hypotez`;
- анализируй расположение файла в проекте. Это поможет понять его назначение и взаимосвязь с другими файлами. Расположение файла ты найдешь в самой превой строке кода, начинающейся с `## \\file /...`;
- запоминай предоставленный код и анализируй его связь с другими частями проекта `hypotez`;

**КОНЕЦ ИНСТРУКЦИИ**

```md
## Анализ кода `hypotez/src/utils/get_free_port.py`

### 1. <алгоритм>

```mermaid
graph LR
    A[Начало: get_free_port(host, port_range)] --> B{port_range is None?};
    B -- Да --> C[port = 1024];
    C --> D{_is_port_in_use(host, port)?};
    D -- Да --> E[port += 1];
    E --> F{port > 65535?};
    F -- Да --> G[raise ValueError("No free port found")];
    F -- Нет --> D;
    D -- Нет --> H[return port];
    B -- Нет --> I{isinstance(port_range, str)?};
    I -- Да --> J[min_port, max_port = _parse_port_range(port_range)];
    J --> K{Проверка корректности port_range};
    K -- Ошибка --> L[raise ValueError("Invalid port range")];
    K -- Успех --> M[for port in range(min_port, max_port + 1)];
    M --> N{_is_port_in_use(host, port)?};
    N -- Да --> M;
    N -- Нет --> O[return port];
    M --> P[raise ValueError("No free port found in range")];
    I -- Нет --> Q{isinstance(port_range, list)?};
    Q -- Да --> R[for item in port_range];
    R --> S{isinstance(item, str)?};
    S -- Да --> T[min_port, max_port = _parse_port_range(item)];
    S -- Нет --> U[raise ValueError("Invalid port range item")];
    T --> V{Проверка корректности item};
    V -- Ошибка --> W[logger.error, continue];
    V -- Успех --> X[for port in range(min_port, max_port + 1)];
    X --> Y{_is_port_in_use(host, port)?};
    Y -- Да --> X;
    Y -- Нет --> Z[return port];
    X --> AA[continue];
    R --> BB[raise ValueError("No free port found in specified ranges")];
    Q -- Нет --> CC[raise ValueError("Invalid port range type")];

    subgraph _parse_port_range(port_range_str)
        SA[Разбить port_range_str на min и max] --> SB{len(parts) == 2?};
        SB -- Нет --> SC[logger.error, raise ValueError];
        SB -- Да --> SD[min_port = int(parts[0]), max_port = int(parts[1])];
        SD --> SE{min_port >= max_port?};
        SE -- Да --> SF[logger.error, raise ValueError];
        SE -- Нет --> SG[return min_port, max_port];
    end

    subgraph _is_port_in_use(host, port)
        CA[Создать сокет] --> CB[Попытка привязать сокет к (host, port)];
        CB -- Успех --> CC[return False];
        CB -- Ошибка (OSError) --> CD[return True];
    end
```

### 2. <mermaid>

```mermaid
flowchart TD
    subgraph get_free_port
        Start(Начало) --> Input{Входные параметры: host, port_range}
        Input --> CheckPortRange{Проверка: port_range?}
        CheckPortRange -- port_range is None --> FindFirstAvailablePort(Поиск первого доступного порта)
        CheckPortRange -- port_range is str or list --> ParsePortRange(Разбор диапазона портов)
        ParsePortRange --> LoopThroughRange(Цикл по диапазону портов)
        LoopThroughRange --> IsPortInUse{Проверка: _is_port_in_use(host, port)?}
        IsPortInUse -- Да --> NextPort(Следующий порт)
        IsPortInUse -- Нет --> ReturnPort(Возврат: port)
        NextPort --> LoopThroughRange
        FindFirstAvailablePort --> FindPort(Поиск доступного порта начиная с 1024)
		FindPort --> IsPortInUse2{Проверка: _is_port_in_use(host, port)?}
        IsPortInUse2 -- Да --> IncrementPort(Увеличение port)
        IsPortInUse2 -- Нет --> ReturnPort
        IncrementPort --> FindPort
        ReturnPort --> End(Конец)
    end

    subgraph _is_port_in_use
        StartSub(Начало _is_port_in_use) --> CreateSocket(Создание сокета)
        CreateSocket --> BindSocket{Попытка bind сокета к (host, port)}
        BindSocket -- Успех --> ReturnFalse(Возврат: False)
        BindSocket -- Ошибка (OSError) --> ReturnTrue(Возврат: True)
        ReturnFalse --> EndSub(Конец _is_port_in_use)
        ReturnTrue --> EndSub
    end

    subgraph _parse_port_range
        StartParse(Начало _parse_port_range) --> SplitRange(Разделение строки диапазона "min-max")
        SplitRange --> ValidateParts{Проверка: len(parts) == 2?}
        ValidateParts -- Нет --> RaiseValueError(Выброс ValueError: "Invalid port range string format")
        ValidateParts -- Да --> ConvertToInt(Преобразование min и max в int)
        ConvertToInt --> ValidateRange{Проверка: min_port >= max_port?}
        ValidateRange -- Да --> RaiseValueError2(Выброс ValueError: "Invalid port range")
        ValidateRange -- Нет --> ReturnMinMax(Возврат: min_port, max_port)
        RaiseValueError --> EndParse(Конец _parse_port_range)
        RaiseValueError2 --> EndParse
        ReturnMinMax --> EndParse
    end
    
    Input --> Header[<code>header.py</code><br> Determine Project Root]
    
    Header --> import[Import Global Settings: <br><code>from src import logger</code>] 
```

В этой диаграмме `mermaid` показан основной поток управления функцией `get_free_port`, а также взаимодействие с подфункциями `_is_port_in_use` и `_parse_port_range`. Диаграмма наглядно демонстрирует логику проверки и поиска свободного порта в заданном диапазоне или начиная с порта 1024, если диапазон не указан.

### 3. <объяснение>

**Назначение файла:**
Файл `get_free_port.py` предоставляет функцию для поиска свободного TCP-порта на указанном хосте. Он может искать первый доступный порт, начиная с определенного значения, или искать порт в заданном диапазоне.

**Импорты:**
- `socket`: Используется для работы с сетевыми сокетами, что необходимо для проверки доступности порта.
- `typing.Optional, typing.Tuple, typing.List`: Используются для аннотации типов, что улучшает читаемость и помогает инструментам статического анализа кода.
- `header`: Импортируется, но не используется в коде. Возможно, это остаток от предыдущих версий или заготовка для будущего функционала.
- `src.logger.logger`: Используется для логирования ошибок и предупреждений.

**Функции:**
- `get_free_port(host: str, port_range: Optional[str | List[str]] = None) -> int`:
  - **Аргументы:**
    - `host` (str): Хост, на котором нужно искать свободный порт (например, `'localhost'`).
    - `port_range` (Optional[str | List[str]]): Необязательный аргумент, задающий диапазон портов для поиска. Может быть строкой в формате `'min-max'` (например, `'3000-3005'`) или списком таких строк (например, `['3000-3005', '8000-8010']`). Если `None`, функция ищет первый доступный порт, начиная с 1024.
  - **Возвращаемое значение:**
    - `int`: Свободный номер порта.
  - **Назначение:**
    - Находит свободный порт на указанном хосте. Если указан `port_range`, ищет в пределах этого диапазона. Если `port_range` не указан, ищет первый доступный порт, начиная с 1024.
  - **Пример:**
    ```python
    >>> get_free_port('localhost', '3000-3005')
    3001
    ```
- `_is_port_in_use(host: str, port: int) -> bool`:
  - **Аргументы:**
    - `host` (str): Хост, который нужно проверить.
    - `port` (int): Номер порта, который нужно проверить.
  - **Возвращаемое значение:**
    - `bool`: `True`, если порт занят, `False` в противном случае.
  - **Назначение:**
    - Проверяет, используется ли указанный порт на данном хосте. Для этого пытается привязать сокет к указанному адресу и порту. Если привязка удается, значит порт свободен, иначе — занят.
- `_parse_port_range(port_range_str: str) -> Tuple[int, int]`:
  - **Аргументы:**
    - `port_range_str` (str): Строка, представляющая диапазон портов в формате `'min-max'` (например, `'3000-3005'`).
  - **Возвращаемое значение:**
    - `Tuple[int, int]`: Кортеж, содержащий минимальный и максимальный номера портов (например, `(3000, 3005)`).
  - **Назначение:**
    - Разбирает строку с диапазоном портов и возвращает минимальный и максимальный номера портов. Проверяет корректность формата строки и убеждается, что минимальный порт меньше максимального. Если формат некорректный, выбрасывает исключение `ValueError`.

**Переменные:**
- В основном используются локальные переменные внутри функций для хранения промежуточных значений, таких как номера портов, диапазоны портов и результаты проверок.

**Потенциальные ошибки и области для улучшения:**
- **Обработка ошибок:** В случае, если ни один порт не найден в указанном диапазоне, выбрасывается исключение `ValueError`. Можно добавить обработку этого исключения на более высоком уровне, чтобы предоставить более информативное сообщение пользователю или предпринять другие действия.
- **Импорт `header`:** Импорт `header` не используется, следует его удалить.

**Взаимосвязи с другими частями проекта:**
- Функция `get_free_port` использует модуль логирования `src.logger.logger` для записи ошибок и предупреждений.  Это позволяет собирать информацию о работе программы и облегчает отладку.  Функция может быть использована в других модулях проекта, где требуется динамическое выделение портов, например, для запуска серверов или других сетевых служб.