## <алгоритм>

**1. `contains_action_type(actions, action_type)`:**
   - **Вход:** Список `actions` (список словарей, где каждый словарь содержит информацию о действии, включая тип) и `action_type` (строка, представляющая тип действия).
   - **Процесс:**
     - Итерируется по списку `actions`.
     - Для каждого действия проверяет, равно ли значение ключа `"type"` в словаре `"action"` значению `action_type`.
     - Если найдено совпадение, возвращает `True`.
     - Если итерация завершена без совпадений, возвращает `False`.
   - **Выход:** `True`, если в списке есть действие заданного типа, иначе `False`.

**Пример:**
```
actions = [{"action": {"type": "move", "content": "go forward"}}, {"action": {"type": "talk", "content": "hello"}}]
action_type = "talk"
# Результат: True

action_type = "jump"
# Результат: False
```

**2. `contains_action_content(actions, action_content)`:**
   - **Вход:** Список `actions` и `action_content` (строка, представляющая текст, который нужно найти в содержании действия).
   - **Процесс:**
     - Итерируется по списку `actions`.
     - Для каждого действия проверяет, содержится ли `action_content` (приведенный к нижнему регистру) в содержимом действия (`action["action"]["content"]`, приведенном к нижнему регистру).
     - Если найдено совпадение, возвращает `True`.
     - Если итерация завершена без совпадений, возвращает `False`.
   - **Выход:** `True`, если найдено действие с заданным содержанием, иначе `False`.

**Пример:**
```
actions = [{"action": {"type": "talk", "content": "Hello there"}}, {"action": {"type": "think", "content": "I am hungry"}}]
action_content = "hello"
# Результат: True

action_content = "hungry"
# Результат: True

action_content = "goodbye"
# Результат: False
```

**3. `contains_stimulus_type(stimuli, stimulus_type)`:**
    - **Вход:** Список `stimuli` (список словарей, где каждый словарь содержит информацию о стимуле, включая тип) и `stimulus_type` (строка, представляющая тип стимула).
    - **Процесс:**
      - Итерируется по списку `stimuli`.
      - Для каждого стимула проверяет, равно ли значение ключа `"type"` значению `stimulus_type`.
      - Если найдено совпадение, возвращает `True`.
      - Если итерация завершена без совпадений, возвращает `False`.
    - **Выход:** `True`, если в списке есть стимул заданного типа, иначе `False`.

**Пример:**
```
stimuli = [{"type": "visual", "content": "red light"}, {"type": "sound", "content": "loud noise"}]
stimulus_type = "sound"
# Результат: True

stimulus_type = "olfactory"
# Результат: False
```

**4. `contains_stimulus_content(stimuli, stimulus_content)`:**
   - **Вход:** Список `stimuli` и `stimulus_content` (строка, представляющая текст, который нужно найти в содержании стимула).
   - **Процесс:**
     - Итерируется по списку `stimuli`.
     - Для каждого стимула проверяет, содержится ли `stimulus_content` (приведенный к нижнему регистру) в содержимом стимула (`stimulus["content"]`, приведенном к нижнему регистру).
     - Если найдено совпадение, возвращает `True`.
     - Если итерация завершена без совпадений, возвращает `False`.
   - **Выход:** `True`, если найдено стимул с заданным содержанием, иначе `False`.

**Пример:**
```
stimuli = [{"type": "visual", "content": "red car"}, {"type": "text", "content": "important message"}]
stimulus_content = "red"
# Результат: True

stimulus_content = "message"
# Результат: True

stimulus_content = "blue"
# Результат: False
```

**5. `terminates_with_action_type(actions, action_type)`:**
   - **Вход:** Список `actions` и `action_type`.
   - **Процесс:**
     - Проверяет, пуст ли список `actions`. Если пуст, возвращает `False`.
     - Если список не пуст, проверяет, равен ли тип действия последнего элемента списка (`actions[-1]["action"]["type"]`) значению `action_type`.
     - Возвращает `True`, если типы совпадают, иначе `False`.
   - **Выход:** `True`, если последнее действие имеет заданный тип, иначе `False`.

**Пример:**
```
actions = [{"action": {"type": "move", "content": "go forward"}}, {"action": {"type": "talk", "content": "hello"}}]
action_type = "talk"
# Результат: True

action_type = "move"
# Результат: False

actions = []
# Результат: False
```

**6. `proposition_holds(proposition)`:**
   - **Вход:** `proposition` (строка, представляющая утверждение).
   - **Процесс:**
     - Создает системное сообщение (system_prompt), указывающее LLM проверять истинность или ложность утверждения.
     - Создает пользовательское сообщение (user_prompt) с утверждением.
     - Отправляет запрос LLM с использованием `openai_utils.client().send_message()`.
     - Извлекает ответ LLM и удаляет из него все не буквенно-цифровые символы.
     - Проверяет, начинается ли очищенный ответ со строк `"true"` или `"false"` (без учета регистра).
     - Возвращает `True`, если начинается с `"true"`, `False`, если начинается с `"false"`. В противном случае вызывает исключение.
   - **Выход:** `True` или `False` в зависимости от результата LLM или исключение.

**Пример:**
```
proposition = "The sky is blue."
# Результат: (зависит от ответа LLM, ожидается True)

proposition = "The moon is made of cheese"
# Результат: (зависит от ответа LLM, ожидается False)
```

**7. `only_alphanumeric(string)`:**
   - **Вход:** Строка `string`.
   - **Процесс:**
     - Создает новую строку, содержащую только буквенно-цифровые символы из входной строки.
     - Возвращает новую строку.
   - **Выход:** Строка, содержащая только буквенно-цифровые символы.

**Пример:**
```
string = "Hello, world! 123"
# Результат: "Helloworld123"
```

**8. `create_test_system_user_message(user_prompt, system_prompt)`:**
   - **Вход:** `user_prompt` (строка с текстом сообщения пользователя) и `system_prompt` (строка с текстом системного сообщения, по умолчанию "You are a helpful AI assistant.").
   - **Процесс:**
     - Создает список `messages` с первым элементом в виде системного сообщения.
     - Если `user_prompt` не является `None`, то добавляет в список `messages` пользовательское сообщение.
     - Возвращает список `messages`.
   - **Выход:** Список сообщений для LLM.

**Пример:**
```
user_prompt = "Tell me a joke."
system_prompt = "You are a comedian."
# Результат: [{"role": "system", "content": "You are a comedian."}, {"role": "user", "content": "Tell me a joke."}]

user_prompt = None
# Результат: [{"role": "system", "content": "You are a helpful AI assistant."}]
```

**9. `agents_configs_are_equal(agent1, agent2, ignore_name)`:**
   - **Вход:** Два объекта `agent1` и `agent2`, `ignore_name` (логическое значение, указывающее, нужно ли игнорировать имя агента при сравнении).
   - **Процесс:**
     - Создает список `ignore_keys`.
     - Если `ignore_name` равно `True`, добавляет в список `ignore_keys` ключ `"name"`.
     - Итерирует по ключам конфигурации первого агента (`agent1._configuration`).
     - Если текущий ключ есть в списке `ignore_keys`, пропускает итерацию.
     - Сравнивает значения конфигураций агентов по текущему ключу.
     - Если значения не равны, возвращает `False`.
     - Если все значения совпадают, возвращает `True`.
   - **Выход:** `True`, если конфигурации агентов равны (с учетом флага `ignore_name`), иначе `False`.

**Пример:**
```
agent1 = MockAgent(configuration={"name": "agent1", "age": 30, "role": "engineer"})
agent2 = MockAgent(configuration={"name": "agent2", "age": 30, "role": "engineer"})
ignore_name = False
# Результат: False

ignore_name = True
# Результат: True
```

**10. `remove_file_if_exists(file_path)`:**
    - **Вход:** `file_path` (строка с путём к файлу).
    - **Процесс:**
        - Проверяет, существует ли файл по указанному пути.
        - Если файл существует, удаляет его.
    - **Выход:** None

**Пример:**
```
file_path = "temp.txt"
# если temp.txt существует, он будет удален.
```

**11. `get_relative_to_test_path(path_suffix)`:**
    - **Вход:** `path_suffix` (строка с суффиксом пути относительно файла теста).
    - **Процесс:**
        - Получает абсолютный путь к директории файла теста.
        - Объединяет путь к директории теста с `path_suffix` с помощью `os.path.join`.
    - **Выход:** Строка с абсолютным путём до файла теста с указанным суффиксом.

**Пример:**
```
path_suffix = "test_file.txt"
# Результат: (путь к файлу test_file.txt в той же директории, что и текущий файл)
```

**12. `focus_group_world()` (fixture):**
    - **Вход:** Нет
    - **Процесс:**
        - Создаёт `TinyWorld` с именем "Focus group"
        - Инициализирует `TinyPerson` Lisa, Oscar и Marcos используя example методы
        - Добавляет созданных `TinyPerson` в мир `TinyWorld`.
    - **Выход:** `TinyWorld` с тремя агентами внутри.

**Пример:**
```
# Результат: TinyWorld("Focus group", [lisa, oscar, marcos])
```

**13. `setup()` (fixture):**
    - **Вход:** Нет
    - **Процесс:**
        - Очищает список агентов с помощью `TinyPerson.clear_agents()`
        - Очищает список окружений с помощью `TinyWorld.clear_environments()`
    - **Выход:** None

**Пример:**
```
# Результат: пустые списки TinyPerson и TinyWorld
```

## <mermaid>

```mermaid
flowchart TD
    subgraph Testing Utilities
    A[contains_action_type] --> B{Iterate through actions}
    B -- Action found --> C[Return True]
    B -- No action found --> D[Return False]

    E[contains_action_content] --> F{Iterate through actions}
    F -- Action found --> G[Return True]
    F -- No action found --> H[Return False]

    I[contains_stimulus_type] --> J{Iterate through stimuli}
    J -- Stimulus found --> K[Return True]
    J -- No stimulus found --> L[Return False]

    M[contains_stimulus_content] --> N{Iterate through stimuli}
    N -- Stimulus found --> O[Return True]
    N -- No stimulus found --> P[Return False]

    Q[terminates_with_action_type] --> R{Check if actions is empty}
    R -- Yes --> S[Return False]
    R -- No --> T{Check last action type}
    T -- Type matches --> U[Return True]
    T -- Type does not match --> V[Return False]

    W[proposition_holds] --> X{Prepare messages}
    X --> Y[Call LLM: openai_utils.client().send_message()]
    Y --> Z{Process LLM response}
    Z --> AA{Check if response starts with "true"}
    AA -- Yes --> AB[Return True]
     Z --> AC{Check if response starts with "false"}
    AC -- Yes --> AD[Return False]
     AA -- No --> AC
    AC -- No --> AE[Raise Exception]
 
     AF[only_alphanumeric] --> AG{Create new string with only alphanumeric characters}
    AG --> AH[Return new string]

    AI[create_test_system_user_message] --> AJ{Create System Message}
    AJ --> AK{Add User message if exist}
    AK --> AL[Return messages list]
     
    AM[agents_configs_are_equal] --> AN{Create ignore_keys}
    AN --> AO{Iterate through agent1 configuration keys}
    AO -- Key in ignore_keys --> AO
    AO -- Key not in ignore_keys --> AP{Compare agent1 and agent2 configurations}
    AP -- Configuration different --> AQ[Return False]
     AP -- Configuration equal --> AO
      AO -- All keys checked --> AR[Return True]

      AS[remove_file_if_exists] --> AT{Check if file exists}
      AT -- File Exists --> AU[Remove file]
      AU --> AV
      AT -- File not Exists --> AV
     AV --> AW[Return]

    AX[get_relative_to_test_path] --> AY{Get absolute path to test dir}
    AY --> AZ[Join with path suffix]
    AZ --> BA[Return absolute path]


    BB[focus_group_world] --> BC{Create TinyWorld}
    BC --> BD{Create Lisa, Oscar, Marcos TinyPerson}
    BD --> BE{Add persons to TinyWorld}
    BE --> BF[Return TinyWorld with agents]

     BG[setup] --> BH{Clear TinyPerson}
    BH --> BI{Clear TinyWorld}
    BI --> BJ[Return None]

    end
```

## <объяснение>

### Импорты:
- **`os`**: Модуль для взаимодействия с операционной системой, используется для работы с файловой системой (удаление файлов, получение пути к директории).
- **`sys`**: Модуль для работы с интерпретатором Python, используется для добавления путей поиска модулей (`sys.path.append`).
- **`time.sleep`**: Используется для приостановки выполнения программы на заданное количество секунд.
- **`tinytroupe.openai_utils`**: Модуль, содержащий утилиты для работы с OpenAI API, например `force_api_cache` для кэширования запросов и `client` для вызова LLM.
- **`tinytroupe.agent.TinyPerson`**: Класс, представляющий агента в системе, используется для создания и управления агентами.
- **`tinytroupe.environment.TinyWorld`**: Класс, представляющий окружение, в котором действуют агенты, используется для создания и управления окружениями.
- **`tinytroupe.environment.TinySocialNetwork`**: Класс, представляющий социальную сеть агентов.
-   **`pytest`**: Фреймворк для тестирования.
-   **`importlib`**: Модуль для динамического импорта модулей.

### Функции:
- **`contains_action_type(actions, action_type)`**: Проверяет, содержится ли в списке действий `actions` действие с заданным типом `action_type`. Возвращает `True`, если такое действие есть, иначе `False`.
- **`contains_action_content(actions, action_content)`**: Проверяет, содержится ли в списке действий `actions` действие, в содержимом которого есть подстрока `action_content`. Возвращает `True`, если такое действие есть, иначе `False`.
- **`contains_stimulus_type(stimuli, stimulus_type)`**: Проверяет, содержится ли в списке стимулов `stimuli` стимул с заданным типом `stimulus_type`. Возвращает `True`, если такой стимул есть, иначе `False`.
- **`contains_stimulus_content(stimuli, stimulus_content)`**: Проверяет, содержится ли в списке стимулов `stimuli` стимул, в содержимом которого есть подстрока `stimulus_content`. Возвращает `True`, если такой стимул есть, иначе `False`.
- **`terminates_with_action_type(actions, action_type)`**: Проверяет, заканчивается ли список действий `actions` действием с типом `action_type`. Возвращает `True`, если это так, иначе `False`.
- **`proposition_holds(proposition)`**: Проверяет, истинно ли утверждение `proposition`, с помощью запроса к LLM. Возвращает `True`, если LLM считает утверждение истинным, `False`, если ложным, и вызывает исключение в случае невалидного ответа от LLM.
- **`only_alphanumeric(string)`**: Возвращает новую строку, содержащую только буквенно-цифровые символы из входной строки `string`.
- **`create_test_system_user_message(user_prompt, system_prompt="You are a helpful AI assistant.")`**: Создает список сообщений для LLM, содержащий системное сообщение и пользовательское сообщение, если оно есть.
- **`agents_configs_are_equal(agent1, agent2, ignore_name=False)`**: Проверяет, равны ли конфигурации двух агентов, с возможностью игнорировать ключ "name". Возвращает `True`, если конфигурации равны, иначе `False`.
- **`remove_file_if_exists(file_path)`**: Удаляет файл по указанному пути, если он существует.
- **`get_relative_to_test_path(path_suffix)`**: Возвращает путь к файлу относительно пути файла с тестами.

### Переменные:
- **`actions`**: Список словарей, каждый словарь представляет действие и содержит информацию о типе и содержании действия.
- **`action_type`**: Строка, представляющая тип действия.
- **`action_content`**: Строка, представляющая содержимое действия.
- **`stimuli`**: Список словарей, каждый словарь представляет стимул и содержит информацию о типе и содержании стимула.
- **`stimulus_type`**: Строка, представляющая тип стимула.
- **`stimulus_content`**: Строка, представляющая содержимое стимула.
-   **`file_path`**: Строка, представляющая путь к файлу.
-   **`path_suffix`**: Строка, представляющая суффикс пути.
-   **`proposition`**: Строка, представляющая утверждение, которое нужно проверить.
-   **`system_prompt`**: Строка, представляющая системное сообщение для LLM.
-   **`user_prompt`**: Строка, представляющая пользовательское сообщение для LLM.
-   **`agent1`, `agent2`**: Объекты агентов.
-   **`ignore_name`**: Логическая переменная, указывающая, нужно ли игнорировать имя агента при сравнении.

###  Fixtures:
-   **`focus_group_world()`**: Фикстура для создания тестового мира `TinyWorld` с тремя агентами.
-   **`setup()`**: Фикстура для очистки агентов и окружений перед каждым тестом.

### Потенциальные ошибки и области для улучшения:
- **Обработка ошибок LLM**: Функция `proposition_holds` вызывает исключение, если LLM возвращает неожиданный ответ. Можно добавить более точную обработку ошибок, например, повторить запрос или использовать стратегию отката.
- **Тестирование LLM**: Тесты, зависящие от вызовов LLM, могут быть нестабильными.
- **Кэширование LLM**: Кэширование результатов LLM-вызовов может привести к устаревшим результатам, если кэш не инвалидировать вовремя.
- **Сложность сравнения конфигураций агентов**: Функция `agents_configs_are_equal` сравнивает конфигурации агентов по ключам. Стоит добавить проверку на тип данных в конфигурации.

### Взаимосвязь с другими частями проекта:
- Этот файл используется в тестах для TinyTroupe.
- Использует `openai_utils` для взаимодействия с LLM.
- Использует классы `TinyPerson` и `TinyWorld` из пакета `tinytroupe` для создания и управления агентами и окружениями.
- Зависит от `pytest` для запуска тестов.

Этот файл предоставляет набор утилит, необходимых для тестирования функциональности агентов и окружений в TinyTroupe, включая проверку действий, стимулов и утверждений, а также для создания тестовых окружений и агентов.