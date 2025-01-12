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

**1. `contains_action_type(actions, action_type)`:**
   - **Вход:** Список `actions` (список словарей, представляющих действия) и строка `action_type` (тип действия).
   - **Процесс:**
     - Итерируется по каждому `action` в списке `actions`.
     - Для каждого `action`, проверяет, если ключ "action" существует, и если  `action["action"]["type"]` равно `action_type`.
     - Если условие истинно, возвращает `True`.
   - **Выход:** `True`, если действие с заданным типом найдено, иначе `False`.
   - **Пример:** 
     `actions` = `[{"action": {"type": "chat", "content": "Hello"}}, {"action": {"type": "plan", "content": "Go to the store"}}]`, `action_type` = `"plan"`. Вернет `True`.

**2. `contains_action_content(actions, action_content)`:**
   - **Вход:** Список `actions` и строка `action_content` (содержание действия).
   - **Процесс:**
     - Итерируется по каждому `action` в списке `actions`.
     - Для каждого `action`, проверяет, если ключ "action" существует, и если `action_content` (в нижнем регистре) содержится в `action["action"]["content"]` (в нижнем регистре).
     - Если условие истинно, возвращает `True`.
   - **Выход:** `True`, если действие с заданным содержанием найдено, иначе `False`.
   - **Пример:** 
     `actions` = `[{"action": {"type": "chat", "content": "Hello world"}}, {"action": {"type": "plan", "content": "Go to the store"}}], `action_content` = "hello". Вернет `True`.

**3. `contains_stimulus_type(stimuli, stimulus_type)`:**
   - **Вход:** Список `stimuli` (список словарей, представляющих стимулы) и строка `stimulus_type` (тип стимула).
   - **Процесс:**
     - Итерируется по каждому `stimulus` в списке `stimuli`.
     - Проверяет, если `stimulus["type"]` равно `stimulus_type`.
     - Если условие истинно, возвращает `True`.
   - **Выход:** `True`, если стимул с заданным типом найден, иначе `False`.
   - **Пример:** 
     `stimuli` = `[{"type": "message", "content": "Hello"}, {"type": "event", "content": "Start"}], `stimulus_type` = `"event"`. Вернет `True`.

**4. `contains_stimulus_content(stimuli, stimulus_content)`:**
   - **Вход:** Список `stimuli` и строка `stimulus_content` (содержание стимула).
   - **Процесс:**
     - Итерируется по каждому `stimulus` в списке `stimuli`.
      - Проверяет, если `stimulus_content` (в нижнем регистре) содержится в `stimulus["content"]` (в нижнем регистре).
     - Если условие истинно, возвращает `True`.
   - **Выход:** `True`, если стимул с заданным содержанием найден, иначе `False`.
  - **Пример:**
     `stimuli` = `[{"type": "message", "content": "Hello World"}, {"type": "event", "content": "Start"}], `stimulus_content` = "world". Вернет `True`.

**5. `terminates_with_action_type(actions, action_type)`:**
   - **Вход:** Список `actions` и строка `action_type` (тип действия).
   - **Процесс:**
     - Проверяет, если список `actions` пустой, возвращает `False`.
     - Проверяет, если тип последнего действия в `actions` ( `actions[-1]["action"]["type"]` ) равен `action_type`.
   - **Выход:** `True`, если последнее действие соответствует заданному типу, иначе `False`.
   - **Пример:**
     `actions` = `[{"action": {"type": "chat", "content": "Hello"}}, {"action": {"type": "plan", "content": "Go to the store"}}], `action_type` = `"plan"`. Вернет `True`.

**6. `proposition_holds(proposition)`:**
   - **Вход:** Строка `proposition` (предложение для проверки).
   - **Процесс:**
     - Формирует системное и пользовательское сообщения для LLM.
     - Вызывает LLM через `openai_utils.client().send_message()`.
     - Извлекает содержимое ответа LLM.
     - Очищает ответ от не-алфанумерических символов с помощью `only_alphanumeric()`.
     - Проверяет, начинается ли очищенный ответ со слов "true" или "false" (в нижнем регистре).
   - **Выход:** `True`, если ответ начинается с "true", `False`, если с "false", в противном случае вызывает исключение.
   - **Пример:**
     `proposition` = `"The text contains an idea for a product"`. Может вернуть `True` или `False` в зависимости от ответа LLM.

**7. `only_alphanumeric(string)`:**
    - **Вход:** Строка `string`.
    - **Процесс:**
        - Создаёт новую строку, содержащую только алфанумерические символы из входной строки.
    - **Выход:** Строка, содержащая только алфанумерические символы.
    - **Пример:**
        `string` = "Hello, world! 123". Вернет `"Helloworld123"`.

**8. `create_test_system_user_message(user_prompt, system_prompt)`:**
   - **Вход:** Строка `user_prompt` (сообщение пользователя, может быть `None`) и строка `system_prompt` (системное сообщение, по умолчанию "You are a helpful AI assistant.").
   - **Процесс:**
     - Создает список, содержащий системное сообщение.
     - Если `user_prompt` не `None`, добавляет пользовательское сообщение в список.
   - **Выход:** Список словарей, представляющих сообщения.
   - **Пример:**
     `user_prompt` = `"What is the capital of France?"`, `system_prompt` = `"You are an expert in geography"`. Вернет `[{"role": "system", "content": "You are an expert in geography"}, {"role": "user", "content": "What is the capital of France?"}]`.

**9. `agents_configs_are_equal(agent1, agent2, ignore_name)`:**
   - **Вход:** Два объекта агента `agent1`, `agent2` и булев флаг `ignore_name` (по умолчанию `False`).
   - **Процесс:**
     - Создает список `ignore_keys` и, если `ignore_name` равен `True`, добавляет в него "name".
     - Проходит по ключам конфигурации `agent1`.
     - Если ключ есть в `ignore_keys`, пропускает его.
     - Сравнивает значения по текущему ключу в конфигурациях `agent1` и `agent2`.
     - Если значения не совпадают, возвращает `False`.
   - **Выход:** `True`, если конфигурации равны (с учетом игнорирования имени), иначе `False`.
   - **Пример:**
        `agent1` = `_configuration={"name":"John", "age":30, "role": "engineer"}`,
        `agent2` = `_configuration={"name":"Jane", "age":30, "role": "engineer"}`.
         `ignore_name` = `True`. Вернет `True`.
        `ignore_name` = `False`. Вернет `False`.

**10. `remove_file_if_exists(file_path)`:**
    - **Вход:** Строка `file_path` (путь к файлу).
    - **Процесс:**
        - Проверяет, существует ли файл по указанному пути.
        - Если файл существует, удаляет его.
    - **Выход:** None.
    - **Пример:** Если по пути `"test.txt"` существует файл, он будет удален.

**11. `get_relative_to_test_path(path_suffix)`:**
    - **Вход:** Строка `path_suffix` (суффикс пути).
    - **Процесс:**
        - Получает путь к текущему файлу.
        - Соединяет путь к текущему файлу с предоставленным суффиксом пути.
    - **Выход:** Строка, представляющая абсолютный путь к файлу, полученному из суффикса.
    - **Пример:**
        `path_suffix` = `"data/test.json"`. Если текущий файл находится в директории `/home/user/project/tests`, вернет `/home/user/project/tests/data/test.json`.

**12. `focus_group_world()`:**
    - **Вход:** Нет.
    - **Процесс:**
        - Создает экземпляр `TinyWorld` с тремя агентами из `tinytroupe.examples`.
    - **Выход:** Экземпляр класса `TinyWorld`.
    - **Пример:** Возвращает игровой мир, содержащий Лизу, Оскара и Маркоса.

**13. `setup()`:**
    - **Вход:** Нет.
    - **Процесс:**
        - Очищает список агентов и список миров.
        - Использует `yield` для последующего выполнения тестов.
    - **Выход:** None. Этот фикстура используется для настройки тестов pytest.

## <mermaid>

```mermaid
flowchart TD
    subgraph Testing Utilities
    
        Start[Начало] --> containsActionTypeCall[<code>contains_action_type</code><br>Проверка наличия действия по типу]
        Start --> containsActionContentCall[<code>contains_action_content</code><br>Проверка наличия действия по содержанию]
        Start --> containsStimulusTypeCall[<code>contains_stimulus_type</code><br>Проверка наличия стимула по типу]
        Start --> containsStimulusContentCall[<code>contains_stimulus_content</code><br>Проверка наличия стимула по содержанию]
        Start --> terminatesWithActionTypeCall[<code>terminates_with_action_type</code><br>Проверка последнего действия по типу]
        Start --> propositionHoldsCall[<code>proposition_holds</code><br>Проверка истинности утверждения с LLM]
        Start --> onlyAlphanumericCall[<code>only_alphanumeric</code><br>Удаление не-алфанумерических символов]
        Start --> createTestSystemUserMessageCall[<code>create_test_system_user_message</code><br>Создание сообщения для LLM]
        Start --> agentsConfigsAreEqualCall[<code>agents_configs_are_equal</code><br>Сравнение конфигураций агентов]
        Start --> removeFileIfExistsCall[<code>remove_file_if_exists</code><br>Удаление файла по пути]
        Start --> getRelativeToTestPathCall[<code>get_relative_to_test_path</code><br>Получение относительного пути]
        Start --> focusGroupWorldCall[<code>focus_group_world</code><br>Создание игрового мира]
        Start --> setupCall[<code>setup</code><br>Настройка тестов]

        containsActionTypeCall --> containsActionTypeCheck[<code>contains_action_type</code><br>Возврат True/False]
        containsActionContentCall --> containsActionContentCheck[<code>contains_action_content</code><br>Возврат True/False]
        containsStimulusTypeCall --> containsStimulusTypeCheck[<code>contains_stimulus_type</code><br>Возврат True/False]
        containsStimulusContentCall --> containsStimulusContentCheck[<code>contains_stimulus_content</code><br>Возврат True/False]
        terminatesWithActionTypeCall --> terminatesWithActionTypeCheck[<code>terminates_with_action_type</code><br>Возврат True/False]
        propositionHoldsCall --> propositionHoldsCheck[<code>proposition_holds</code><br>Возврат True/False, Exception]
        onlyAlphanumericCall --> onlyAlphanumericReturn[<code>only_alphanumeric</code><br>Возврат строки]
        createTestSystemUserMessageCall --> createTestSystemUserMessageReturn[<code>create_test_system_user_message</code><br>Возврат списка сообщений]
        agentsConfigsAreEqualCall --> agentsConfigsAreEqualCheck[<code>agents_configs_are_equal</code><br>Возврат True/False]
        removeFileIfExistsCall --> removeFileIfExistsAction[<code>remove_file_if_exists</code><br>Удаление файла или нет]
        getRelativeToTestPathCall --> getRelativeToTestPathReturn[<code>get_relative_to_test_path</code><br>Возврат абсолютного пути]
        focusGroupWorldCall --> focusGroupWorldReturn[<code>focus_group_world</code><br>Возврат TinyWorld]
        setupCall --> setupReturn[<code>setup</code><br>Очистка агентов и сред, yield]

        
    end
    
    subgraph TinyTroupe Imports
        importOpenAI[<code>openai_utils</code><br>Взаимодействие с OpenAI API]
        importTinyPerson[<code>TinyPerson</code><br>Агент]
        importTinyWorld[<code>TinyWorld</code><br>Игровой мир]
        importTinySocialNetwork[<code>TinySocialNetwork</code><br>Социальная сеть]
        importPyTest[<code>pytest</code><br>Фреймворк для тестирования]
        importImportLib[<code>importlib</code><br>Импорт модулей]
        importExamples[<code>examples</code><br>Примеры агентов]
    end
    
    Testing Utilities --> importOpenAI
    Testing Utilities --> importTinyPerson
    Testing Utilities --> importTinyWorld
    Testing Utilities --> importTinySocialNetwork
    Testing Utilities --> importPyTest
    Testing Utilities --> importImportLib
    Testing Utilities --> importExamples
```

## <объяснение>

**Импорты:**

- **`os`**: Предоставляет функции для взаимодействия с операционной системой, используется для работы с файловой системой, например, для проверки существования файла и его удаления (`os.path.exists`, `os.remove`, `os.path.join`, `os.path.dirname`).
- **`sys`**: Предоставляет доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором Python. Здесь используется для добавления путей в `sys.path`, что позволяет импортировать модули из других директорий.
- **`time.sleep`**:  Используется для приостановки выполнения кода на заданное количество секунд (не используется напрямую в коде, но может использоваться в тестах).
- **`tinytroupe.openai_utils`**: Модуль, отвечающий за взаимодействие с OpenAI API, содержит функции для отправки запросов LLM. Он включает функцию `force_api_cache` для управления кэшированием ответов.
- **`tinytroupe.agent.TinyPerson`**: Класс, представляющий агента (персонажа) в симуляции.
- **`tinytroupe.environment.TinyWorld`**: Класс, представляющий игровой мир.
- **`tinytroupe.environment.TinySocialNetwork`**: Класс, представляющий социальную сеть (не используется напрямую).
- **`pytest`**: Библиотека для написания и запуска тестов.
- **`importlib`**: Библиотека для динамического импорта модулей (не используется напрямую).
- **`tinytroupe.examples`**: Модуль, содержащий примеры агентов для использования в тестах.

**Функции:**

- **`contains_action_type(actions, action_type)`**: Проверяет, содержится ли в списке действий `actions` действие с типом `action_type`. Полезно для проверки, выполняют ли агенты действия определенного типа.
- **`contains_action_content(actions, action_content)`**: Проверяет, содержит ли список действий `actions` действие, чье содержание (в нижнем регистре) содержит `action_content`. Позволяет проверять действия по их содержанию.
- **`contains_stimulus_type(stimuli, stimulus_type)`**: Проверяет, содержится ли в списке стимулов `stimuli` стимул с типом `stimulus_type`.  Полезно для отслеживания возникновения стимулов определенного типа.
- **`contains_stimulus_content(stimuli, stimulus_content)`**: Проверяет, содержит ли список стимулов `stimuli` стимул, чье содержание (в нижнем регистре) содержит `stimulus_content`.  Полезно для проверки содержания стимулов.
- **`terminates_with_action_type(actions, action_type)`**: Проверяет, заканчивается ли список действий `actions` действием типа `action_type`.  
- **`proposition_holds(proposition)`**: Проверяет, истинно ли `proposition` с помощью LLM. Используется для проверок, которые нельзя легко автоматизировать (например, "есть ли в тексте какие-то идеи").
- **`only_alphanumeric(string)`**: Возвращает строку, содержащую только буквенно-цифровые символы. Используется для очистки ответа LLM.
- **`create_test_system_user_message(user_prompt, system_prompt)`**: Создает структуру сообщения для LLM, содержащую системное и пользовательское сообщения.
- **`agents_configs_are_equal(agent1, agent2, ignore_name)`**: Сравнивает конфигурации двух агентов, с возможностью игнорирования поля `name`. 
- **`remove_file_if_exists(file_path)`**: Удаляет файл по указанному пути, если он существует.
- **`get_relative_to_test_path(path_suffix)`**: Формирует абсолютный путь к файлу относительно пути текущего файла.
- **`focus_group_world()`**: Pytest фикстура, создающая игровой мир с тремя агентами для тестов.
- **`setup()`**: Pytest фикстура, очищающая списки агентов и миров перед тестами. Использует `yield` для настройки и очистки перед тестом.

**Переменные:**
- **`sys.path`**: Список путей, где Python ищет модули. В данном коде добавляются пути для импорта модулей из других директорий.
- **`messages`**:  Список словарей, представляющих сообщения для LLM, каждое сообщение имеет ключи "role" и "content".
- **`system_prompt`**:  Строка, представляющая системное сообщение для LLM.
- **`user_prompt`**:  Строка, представляющая пользовательское сообщение для LLM.
- **`cleaned_message`**:  Строка, содержащая очищенный от не-алфанумерических символов ответ от LLM.
- **`file_path`**: Строка, представляющая путь к файлу.
- **`path_suffix`**: Строка, представляющая суффикс пути.
- **`agent1`, `agent2`**: Объекты агентов, чьи конфигурации сравниваются.
- **`ignore_keys`**: Список ключей, которые нужно игнорировать при сравнении конфигураций агентов.
- **`world`**: Экземпляр класса `TinyWorld`.

**Взаимосвязи:**

- Этот файл является частью тестового пакета и предоставляет набор вспомогательных функций для упрощения написания тестов для TinyTroupe.
- Он использует модули `openai_utils`, `agent`, `environment` из `tinytroupe` для создания и проверки поведения агентов и их окружения.
- Функции, такие как `contains_action_type`, `contains_action_content`, и т.д., позволяют проверять различные аспекты работы агентов и мира.
- Фикстуры `focus_group_world` и `setup` используются pytest для настройки и очистки состояния перед тестами.
- `proposition_holds` использует LLM для проверки текстовых утверждений.
- Функции I/O (`remove_file_if_exists` и `get_relative_to_test_path`) используются для работы с файлами в тестах.

**Потенциальные ошибки и улучшения:**

- Функция `proposition_holds` полагается на LLM, поэтому ее результаты могут быть не всегда детерминированными и могут потребовать дополнительной обработки.
- В функциях `contains_action_content` и `contains_stimulus_content` используется `lower()` для сравнения, но это может не всегда быть идеальным решением, если нужно более точное сравнение.
- Использование `sys.path.append` может быть неудобным, если структура проекта меняется. Лучше использовать относительные импорты или переменные окружения.

Этот файл предоставляет набор утилит для написания тестов, что упрощает тестирование различных аспектов системы TinyTroupe.