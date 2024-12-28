## ИНСТРУКЦИЯ:

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

3. **<объяснение>**: Предоставьте подробные объяснения:  
   - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.  
   - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.  
   - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.  
   - **Переменные**: Их типы и использование.  
   - Выделите потенциальные ошибки или области для улучшения.  

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).  

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**
```markdown
## <алгоритм>

1.  **Инициализация `Games101Basic`:**
    *   Создается экземпляр класса `Games101Basic` с указанием языка (`lang`).
    *   Загружается конфигурация из JSON файла (`101_basic_computer_games.json`).
    *   Читается системная инструкция из файла `fts.txt`.
    *   Инициализируется `GoogleGenerativeAI` (модель `bob`).
    *   _Пример:_ `g101 = Games101Basic('en')`

2.  **Получение списка игр (`games_list`):**
    *   Функция `games_list` извлекает имена файлов из каталога `rules` для заданного языка.
    *   Имена игр формируются путем обрезки лишних частей из имен файлов и преобразования их в верхний регистр с заменой подчеркиваний на пробелы.
    *   _Пример:_ Файл `ru/rules/game_01_guess_number.md`  становится  игрой `"GUESS NUMBER"`.
    *   _Результат:_ Список имен игр: `['GUESS NUMBER', 'TIC TAC TOE', ...]`.

3.  **Генерация Python кода (`generate_python_code`):**
    *   Для каждой игры в списке `games_list`:
        *   Читается инструкция для генерации кода из файла (`101_basic_computer_games_write_code.{lang}.md`).
        *   Подставляется имя игры в инструкцию.
        *   Отправляется запрос в `GoogleGenerativeAI` (модель `bob`).
        *   Если ответ начинается и заканчивается кодовыми блоками (```), то обрезаются эти блоки.
        *   Сохраняется сгенерированный код в файл.
        *   Задержка перед следующим запросом.
     *   _Пример:_ Для игры `"GUESS NUMBER"` создается запрос в Gemini с инструкцией, содержащей `<GUESS NUMBER>`, и сохраняется результат.

4.  **Сохранение кода (`save_code`):**
    *   Получает имя игры и код.
    *   Создается директория для сохранения кода, если ее нет.
    *   Сохраняет код в файл `<имя_игры>.py`.
    *   _Пример:_ Код для игры `"GUESS NUMBER"` сохраняется в файл `ru/guess number/guess_number.py`.

5.  **Генерация TOC (`generate_repository_toc`):**
    *   Читается инструкция для генерации TOC (оглавления) из файла (`101_basic_computer_games_create_toc.{lang}.md`).
    *   К инструкции добавляется список игр.
    *   Отправляется запрос в `GoogleGenerativeAI` (модель `bob`).
    *   Сохраняется сгенерированный TOC в файл `TOC.MD`.
    *   _Пример:_ Создается файл `ru/TOC.MD` с оглавлением для всех игр.

6.  **Основная программа (`if __name__ == '__main__':`)**
    *   Задается список языков.
    *   Для каждого языка:
        *   Создается экземпляр `Games101Basic`.
        *   Запускается асинхронная генерация TOC.
        *   Запускается асинхронная генерация кода (закомментирована).

**Поток данных:**

1.  **Инициализация:** Данные конфигурации из `*.json` файлов, системные инструкции из `*.txt` файлов, и настройки языка передаются в класс `Games101Basic`.
2.  **`games_list`:** Имена файлов из директорий,  обрабатываются и возвращается список игр.
3.  **`generate_python_code`:** Список игр из `games_list`, инструкции из файлов, и экземпляр `GoogleGenerativeAI`, все это вместе используется для генерации кода на Python.
4.  **`save_code`:** Сгенерированный код и имена игр передаются для сохранения кода в файлы.
5.  **`generate_repository_toc`:** Список игр из `games_list`, инструкции из файлов, и экземпляр `GoogleGenerativeAI`, все это вместе используется для генерации TOC.
6.  **Основная программа:** Инициирует работу для заданных языков.

## <mermaid>

```mermaid
flowchart TD
    subgraph Header
        Start --> Header[<code>header.py</code><br> Determine Project Root]
        Header --> ImportGlobalSettings[Import Global Settings: <br><code>from src import gs</code>]
    end

    subgraph Games101Basic
        Init(Init Games101Basic) --> LoadConfig[Load config: <code>j_loads_ns(config.json)</code>]
        LoadConfig --> LoadInstructions[Load system instruction: <code>Path(fts.txt).read_text()</code>]
        LoadInstructions --> InitGemini[Init GoogleGenerativeAI (bob)]
        
        InitGemini --> GamesList(Get games list: <code>games_list</code>)

        GamesList --> GenerateCode[Generate python code: <code>generate_python_code</code>]

        GenerateCode -->  LoopThroughGames[Loop through games]
        LoopThroughGames --> LoadCodeInstruction[Load instruction: <code>read_text(md)</code>]
        LoadCodeInstruction --> ReplaceGameName[Replace: <code>replace('<GAME>', f'<game>')</code>]
        ReplaceGameName --> SendToGemini[Send to GoogleGenerativeAI (bob): <code>ask(q)</code>]
        SendToGemini --> ProcessResponse[Process response]

        ProcessResponse --> SaveCodeCall[Call: <code>save_code(game, response)</code>]
    
        SaveCodeCall --> SaveCode(Save Code to File)
    
        GamesList --> GenerateTOC[Generate Repository TOC: <code>generate_repository_toc</code>]

        GenerateTOC --> LoadTOCInstruction[Load instruction: <code>read_text(md)</code>]
        LoadTOCInstruction --> ConcatGamesList[Concat games_list]
        ConcatGamesList --> SendTOCtoGemini[Send to GoogleGenerativeAI (bob): <code>ask(q)</code>]
        SendTOCtoGemini --> SaveTOC(Save TOC to File)

    end
    
    subgraph Main
    StartMain(Start Main) --> LoopLanguages[Loop through languages]
        LoopLanguages --> CreateGameInstance(Create <code>Games101Basic</code> instance)
        CreateGameInstance --> CallGenerateTOC(Call <code>generate_repository_toc</code>)
        CreateGameInstance --> CallGenerateCode(Call <code>generate_python_code</code> - optional)
    end

```

**Описание зависимостей `mermaid`:**

1.  **`header.py`**:
    *   `Start`: Начало процесса.
    *   `Header`: Определяет корень проекта.
    *   `ImportGlobalSettings`: Импортирует глобальные настройки из `src.gs`.

2.  **`Games101Basic`**:
    *   `Init`: Инициализация класса `Games101Basic`, загружает конфигурации.
    *   `LoadConfig`: Загружает JSON-конфигурацию.
    *   `LoadInstructions`: Загружает системную инструкцию из файла.
    *   `InitGemini`: Инициализирует объект `GoogleGenerativeAI`.
    *  `GamesList`: Получает список имен игр из файлов правил.
    *   `GenerateCode`: Генерирует Python код для каждой игры.
    * `LoopThroughGames`: Цикл по списку игр.
        * `LoadCodeInstruction`: Загружает инструкцию для генерации кода.
        *   `ReplaceGameName`: Подставляет имя игры в инструкцию.
        *   `SendToGemini`: Отправляет запрос в `GoogleGenerativeAI`.
        *  `ProcessResponse`: Обрабатывает ответ от Google Gemini
        *   `SaveCodeCall`: Вызывает функцию для сохранения кода.
    * `SaveCode`: Сохраняет сгенерированный код в файл.
    *   `GenerateTOC`: Генерирует оглавление репозитория.
        * `LoadTOCInstruction`: Загружает инструкцию для генерации TOC.
        *   `ConcatGamesList`: Объединяет список игр в строку для запроса.
        *   `SendTOCtoGemini`: Отправляет запрос в `GoogleGenerativeAI`.
        *   `SaveTOC`: Сохраняет сгенерированное оглавление в файл.

3.  **`Main`**:
    *   `StartMain`: Начало основной программы.
    *  `LoopLanguages`: Цикл по списку языков.
    *   `CreateGameInstance`: Создает экземпляр `Games101Basic` для каждого языка.
    *   `CallGenerateTOC`: Вызывает функцию генерации TOC.
    *   `CallGenerateCode`: Вызывает функцию генерации кода (опционально).

## <объяснение>

**Импорты:**

*   `asyncio`: Используется для асинхронного программирования, что позволяет выполнять несколько задач параллельно.
*   `time`: Используется для добавления задержек между запросами к API.
*   `pathlib.Path`: Используется для работы с путями к файлам и директориям.
*   `header`: Предположительно, модуль, устанавливающий корень проекта и содержащий общие функции.
*   `src.gs`: Глобальные настройки проекта, такие как пути, учетные данные и т.д.
*   `src.ai.gemini.GoogleGenerativeAI`: Класс для взаимодействия с моделью Gemini от Google.
*   `src.ai.openai.OpenAIModel`: Класс для взаимодействия с моделью OpenAI, не используется в этом коде, но импортируется.
*   `src.utils.jjson.j_loads`, `src.utils.jjson.j_loads_ns`: Функции для загрузки данных из JSON файлов.
*   `src.utils.file.get_filenames`: Функция для получения списка имен файлов в директории.
*   `src.utils.printer.pprint`: Функция для удобной печати данных.

**Классы:**

*   `Games101Basic`:
    *   **`lang: str`**: Язык, для которого генерируются игры.
    *   **`bob: GoogleGenerativeAI`**: Экземпляр класса `GoogleGenerativeAI` для взаимодействия с моделью Gemini.
    *   **`alice: GoogleGenerativeAI`**: Экземпляр класса `GoogleGenerativeAI`, не используется в этом коде.
    *   **`base: str`**: Базовое имя директории с играми.
    *   **`base_path: Path`**: Путь к директории с играми.
    *   **`__init__(self, lanf: str = 'en')`**:
        *   Конструктор класса.
        *   Загружает конфигурацию из `101_basic_computer_games.json`.
        *   Устанавливает язык (`self.lang`).
        *   Читает системную инструкцию.
        *   Инициализирует модель Gemini (`self.bob`).
    *   **`@property games_list(self)`**:
        *   Генерирует список имен игр.
        *   Получает список файлов в директории `rules`.
        *   Извлекает имя игры из имени файла, удаляя префиксы и расширения.
    *   **`async def generate_python_code(self)`**:
        *   Асинхронная функция для генерации Python кода для всех игр.
        *   Читает инструкцию для генерации кода.
        *   Заменяет плейсхолдер `<GAME>` именем игры.
        *   Отправляет запрос в Gemini для генерации кода.
        *   Сохраняет сгенерированный код.
        *   Добавляет паузу для соблюдения лимитов API.
    *   **`def save_code(self, game: str, code: str)`**:
        *   Сохраняет сгенерированный код в файл.
        *   Создает директорию для файла, если ее нет.
    *  **`async def generate_repository_toc(self)`**:
        * Асинхронная функция для генерации TOC (оглавления) для репозитория.
        * Читает инструкцию для генерации TOC.
        * Добавляет список игр в инструкцию.
        * Отправляет запрос в Gemini для генерации TOC.
        * Сохраняет сгенерированный TOC в файл.

**Функции:**

*   Все методы внутри класса `Games101Basic` рассмотрены выше.
*   Функции `j_loads`, `j_loads_ns`, `get_filenames`, `pprint` являются внешними утилитами и их функциональность описана в секции импорта.
*   `asyncio.run()`: Функция для запуска асинхронных функций.

**Переменные:**

*   `lang` (str): Язык, для которого генерируются игры.
*   `bob` (GoogleGenerativeAI): Экземпляр класса для взаимодействия с Google Gemini.
*   `base` (str): Имя базовой директории с играми.
*  `base_path` (pathlib.Path): Путь к директории с играми.
*  `config` (dict): Словарь с настройками загруженными из json.
*  `system_instruction` (str): Инструкция для Gemini модели.
*   `rules_files` (list): Список имен файлов правил.
*  `games` (list): Список названий игр.
* `file_name` (str): Название файла.
*  `game_name` (str): Название игры.
*   `command_instruction` (str): Инструкция для Gemini, загруженная из файла.
*   `q` (str): Запрос к Gemini.
*   `response` (str): Ответ от Gemini.
*  `output_file` (pathlib.Path): Путь к файлу для сохранения результата.
*   `langs_list` (list): Список языков.
*   `executed_langs_list` (list): Список языков, для которых выполняется генерация.
*  `g101` (Games101Basic): Экземпляр класса Games101Basic.

**Потенциальные ошибки и области для улучшения:**

*   Обработка ошибок: В коде не хватает обработки ошибок, например, при чтении файлов, запросах к API, парсинге ответов.
*   Логирование: Отсутствует логирование действий, что затрудняет отслеживание ошибок и процесса выполнения.
*   Обработка ответов от Gemini: Код предполагает, что ответ всегда будет корректным, но возможны случаи, когда Gemini не сможет сгенерировать код.
*   Код `save_code` можно упростить, убрав `...`, так как он не несет никакой нагрузки
*   Закомментированная строка  `#asyncio.run( g101.generate_python_code())` указывает на то, что эта функция не используется в данном варианте запуска, хотя она и предусмотрена в коде.
*   Используется  `time.sleep(20)` для задержки, что не очень эффективно и желательно использовать асинхронные задержки
*    `alice` не используется, что может быть удалено
*   Используется  `or` в условии `if file_name == ('README.MD' or 'TOC.MD'):`, что не дает желаемого результата. Следует использовать `in`

**Взаимосвязи с другими частями проекта:**

*   Код зависит от `src.gs` для получения глобальных настроек и учетных данных.
*   Использует `src.ai.gemini.GoogleGenerativeAI` для взаимодействия с моделью Gemini.
*   Использует `src.utils.jjson`, `src.utils.file`, `src.utils.printer` для обработки данных, работы с файлами и вывода информации.
*   Предполагается, что структура директорий с правилами игр ( `rules`) уже существует.

В целом, код предоставляет функциональность для генерации Python кода и оглавления для репозитория на основе инструкций и моделей AI.
```