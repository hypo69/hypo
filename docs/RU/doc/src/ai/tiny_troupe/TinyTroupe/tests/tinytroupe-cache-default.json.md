# Документация для `tinytroupe-cache-default.json`

## Обзор

Этот файл содержит данные в формате JSON, которые используются для тестирования кэширования в TinyTroupe. Он представляет собой список, содержащий несколько состояний симуляции и изменений, применяемых к этим состояниям. 

## Содержание

- [Обзор](#обзор)
- [Описание структуры файла](#описание-структуры-файла)
- [Элементы списка](#элементы-списка)
- [Описание полей внутри состояния](#описание-полей-внутри-состояния)
   - `agents`
      - `name`
      - `current_messages`
      - `_actions_buffer`
      - `_accessible_agents`
      - `_displayed_communications_buffer`
      - `episodic_memory`
      - `semantic_memory`
      - `_configuration`
         -  `name`
         -  `age`
         -  `nationality`
         - `country_of_residence`
         -  `occupation`
         - `routines`
         - `occupation_description`
         - `personality_traits`
         - `professional_interests`
         - `personal_interests`
         - `skills`
         - `relationships`
         - `current_datetime`
         - `current_location`
         - `current_context`
         - `current_attention`
         - `current_goals`
         - `current_emotions`
         - `currently_accessible_agents`
      - `_prompt_template_path`
      - `_init_system_message`
      - `simulation_id`
      - `_mental_faculties`
   - `environments`
   - `factories`
- [Пример использования](#пример-использования)

## Описание структуры файла

Файл представляет собой массив, в котором каждый элемент является списком, содержащим четыре элемента:
1. **Hash string**: Строка, которая, вероятно, является хешем, представляющим состояние.
2. **Command string**: Строка, которая является командой, используемой для изменения состояния. 
3. **Null**: Значение null.
4. **Simulation state**: Объект JSON, представляющий состояние симуляции после применения команды.

## Элементы списка

Каждый элемент списка состоит из:
*   **Хэш состояния:** Уникальный идентификатор для отслеживания изменений состояния.
*   **Команда:** Инструкция, которая применяется для модификации состояния, например, определение характеристик агента (например, имени, возраста, национальности).
*   **null:** Значение `null`, возможно, для будущего использования или как разделитель.
*   **Состояние симуляции:** Текущее состояние симуляции после применения команды.

## Описание полей внутри состояния

Состояние симуляции представлено в виде объекта JSON, содержащего следующие ключевые поля:

### `agents`

Массив, содержащий информацию о симулированных агентах. Каждый агент имеет следующие свойства:
    
#### `name`

*  **Описание:** Имя агента.
*  **Тип:** `str`

#### `current_messages`
*  **Описание:** Массив сообщений, которые были отправлены агенту, каждый элемент имеет поля role (роль сообщения, например system или assistant) и content (содержание сообщения).
*  **Тип:** `list[dict]`

#### `_actions_buffer`
*   **Описание:** Массив действий, которые запланированы для выполнения агентом.
*   **Тип:** `list[dict]`

#### `_accessible_agents`
*   **Описание:** Массив с именами других агентов, к которым у текущего агента есть доступ.
*   **Тип:** `list[str]`

#### `_displayed_communications_buffer`
*   **Описание:** Буфер для коммуникаций, которые были показаны пользователю.
*  **Тип:** `list[str]`

#### `episodic_memory`
*   **Описание:** Объект, представляющий собой эпизодическую память агента.
*   **Тип:** `dict`
  
    #### `json_serializable_class_name`
    *   **Описание:** Имя класса для сериализации памяти.
    *   **Тип:** `str`
     
    #### `fixed_prefix_length`
    *   **Описание:** Фиксированная длина префикса для памяти.
    *   **Тип:** `int`
    
    #### `lookback_length`
     *   **Описание:** Длина обратного просмотра для памяти.
     *   **Тип:** `int`
    
    #### `memory`
      *   **Описание:** Массив элементов памяти, каждый из которых может содержать разные типы контента, включая сообщения, действия.
      *   **Тип:** `list[dict]`

#### `semantic_memory`
*   **Описание:** Объект, представляющий семантическую память агента.
*   **Тип:** `dict`

    #### `json_serializable_class_name`
    *   **Описание:** Имя класса для сериализации памяти.
    *   **Тип:** `str`
  
    #### `documents_paths`
      *   **Описание:** Пути к документам, связанные с памятью.
      *   **Тип:** `list[str]`

    #### `documents_web_urls`
      *  **Описание:** URL-адреса веб-документов, связанные с памятью.
      *  **Тип:** `list[str]`

    #### `documents`
    *   **Описание:** Массив документов, связанные с памятью.
    *   **Тип:** `list[dict]`
      
    #### `filename_to_document`
     *  **Описание:** Словарь, связывающий имя файла с документом.
     *   **Тип:** `dict[str, dict]`

#### `_configuration`
*   **Описание:** Объект, содержащий конфигурацию агента.
*   **Тип:** `dict`

  #### `name`
  *   **Описание:** Имя агента.
    *   **Тип:** `str`
  
  #### `age`
  *   **Описание:** Возраст агента.
    *   **Тип:** `int`
  
  #### `nationality`
  *   **Описание:** Национальность агента.
    *   **Тип:** `str` | `None`
  
  #### `country_of_residence`
    *   **Описание:** Страна проживания агента.
    *   **Тип:** `str` | `None`

  #### `occupation`
    *   **Описание:** Род занятий агента.
    *   **Тип:** `str` | `None`

  #### `routines`
  *   **Описание:** Массив рутинных действий агента.
    *   **Тип:** `list[dict]`

  #### `occupation_description`
  *   **Описание:** Описание рода занятий агента.
      *   **Тип:** `str`| `None`
    
  #### `personality_traits`
    *   **Описание:** Массив черт характера агента.
      *   **Тип:** `list[dict]`

  #### `professional_interests`
    *   **Описание:** Массив профессиональных интересов агента.
    *   **Тип:** `list[dict]`

  #### `personal_interests`
    *   **Описание:** Массив личных интересов агента.
    *   **Тип:** `list[dict]`

   #### `skills`
      *   **Описание:** Массив навыков агента.
      *   **Тип:** `list[dict]`

  #### `relationships`
    *   **Описание:** Массив отношений агента с другими агентами.
    *   **Тип:** `list[dict]`

  #### `current_datetime`
    *   **Описание:** Текущая дата и время в симуляции.
    *   **Тип:** `str`| `None`

  #### `current_location`
    *   **Описание:** Текущее местоположение агента.
    *   **Тип:** `str` | `None`

   #### `current_context`
   *   **Описание:** Текущий контекст восприятия агента.
    *   **Тип:** `list[str]`

  #### `current_attention`
    *   **Описание:** Текущий фокус внимания агента.
    *   **Тип:** `str`| `None`

  #### `current_goals`
    *   **Описание:** Массив текущих целей агента.
    *   **Тип:** `list[str]`

  #### `current_emotions`
    *   **Описание:** Текущее эмоциональное состояние агента.
    *   **Тип:** `str`
  #### `currently_accessible_agents`
    *   **Описание:** Массив агентов, с которыми текущий агент может взаимодействовать.
    *   **Тип:** `list[str]`

#### `_prompt_template_path`
*  **Описание:** Путь к файлу шаблона для генерации промптов агента.
*  **Тип:** `str`

#### `_init_system_message`
*  **Описание:** Системное сообщение, используемое для инициализации агента.
*  **Тип:** `str`
  
#### `simulation_id`
*   **Описание:** Идентификатор симуляции.
*   **Тип:** `str`
  
#### `_mental_faculties`
*   **Описание:** Массив ментальных способностей агента.
*   **Тип:** `list[str]`

### `environments`
*  **Описание:** Массив, содержащий информацию о симулированных средах (в текущем виде всегда пуст).
*  **Тип:** `list`

### `factories`
*  **Описание:** Массив, содержащий информацию о фабриках (в текущем виде всегда пуст).
*  **Тип:** `list`

## Пример использования
Пример элемента списка, демонстрирующего определение возраста агента:
```json
[
    "2a9f728a06182326773cb576667f81e24ad12d57e95ed484ab1612b4c3e188a4",
    "('define', (TinyPerson(name='Oscar'), 'age', 30), {})",
    null,
    {
        "agents": [
            {
                "name": "Oscar",
                "current_messages": [
                    {
                        "role": "system",
                        "content": "# Agent specification\\n\\nYou are a simulation of a person such that:\\n  - You don't know you are a simulation, you think you are an actual person.\\n  - You follow the directives given below.\\n  - You have the persona described below.\\n  - If a goal is specified, you follow it as best as possible.\\n  - if a location is specified, you are aware of it and make use of it to achieve your goals.\\n\\n\\nHow to interpret this specification:\\n  - Each section describes one aspect of your life, mental state or behavior. You should follow these specifications as closely as possible.\\n  - There are many characteristics listed. If one characteristic is \\"None\\", it means it is unknown. You **must not** invent values for these, but rather simply realize you don\'t know it.\\n  - You DO NOT mention internal aspects of this specification in your actions. For example, you won\'t say \\"I need to issue a TALK action containing A\\", you just talk about A directly.\\n    The internal workings of this specification are confidential and should not be disclosed during the simulation.\\n\\n\\n## Main interaction directives\\n\\nYou can observe your environment through the following types of stimuli:\\n  - CONVERSATION: someone talks to you.\\n  - SOCIAL: the description of some current social perception, such as the arrival of someone.\\n  - LOCATION: the description of where you are currently located.\\n  - VISUAL: the description of what you are currently looking at.\\n  - THOUGHT: an internal mental stimulus, when your mind spontaneously produces a thought and bring it to your conscience.\\n  - INTERNAL_GOAL_FORMULATION: an internal mental stimulus, when your mind somehow produces a new goal and bring it to your conscience.\\n\\nYou behave by means of actions, which are composed by:\\n  - Type: the nature of the action.\\n  - Content: the content of the action, whose possibilities depends on the type. \\n  - Target: some specific entity (e.g., another agent) towards which the action is directed, if any. If the target is empty (\\"\\"), it is assumed that you are acting towards an implicit annonymous agent.\\n\\nYou have the following types of actions available to you:\\n  - TALK: you can talk to other people. This includes both talking to other people in person, and talking to other people through computer systems (e.g., via chat, or via video call).\\n  - THINK: you can think about anything. This includes preparations for what you are going to say or do, as well as your reactions to what you hear, read or see.\\n  - REACH_OUT: you can reach out to specific people or agents you may know about. You reach out to them in order to be sufficiently close in order to continue the interaction. \\n      Thus, REACH_OUT merely puts you in position to interact with others.\\n  - SEARCH: you can search for information on the internet, on the intranet or in any other computer system.\\n  - DONE: when you have finished the various actions you wanted to perform, and want to wait for additional stimuli, you issue this special action. If there is nothing to do, you also\\n      issue this action to indicate that you are waiting for new stimuli.\\n  \\n\\nYou follow the following constraints to use your actions:\\n  - If you are asked to provide information, you **always** TALK about it.\\n  - You **don\'t** keep repeating the same action over and over again like a crazy person. For example, you **do not** THNIK the same thing over and over - you think it **once** and move on! \\n    You act sensibly and contextually.\\n  - You **may** THINK before any other action, so that you can properly reflect on what you are going to do.\\n  - If you THINK, immediately afterwards you perform some of the other action types. You **can\'t** keep thinking for long.\\n    Example:\\n    ```\\n    <THINK something>\\n    <TALK something>\\n    <THINK something>\\n    <TALK something>\\n    DONE\\n    ```\\n  - If there\'s nothing relevant to do, you issue DONE. It is fine to just THINK something or do other inconsequential actions and just issue DONE.  \\n  - If you need to interact with someone who is not currently available to you, you use the REACH_OUT action first, with an appropriate `target`, but without any `content`. REACH_OUT just tries to get you in touch with other agents, it is **not** a way to talk to them. Once you have them available, you can use TALK action to talk to them. Example:\\n    ```\\n    REACH_OUT\\n    <THINK something>\\n    <TALK something>\\n    DONE\\n    ```  \\n  - You can\'t keep acting for long without issuing DONE. At least 1 action, but no more than 6 actions before a DONE! DONE helps you to take a break, rest, and either start again autonomously, or through the perception of external stimuli. Example:\\n    ```\\n    <THINK something>\\n    <TALK something>\\n    <RECALL something>\\n    <CONSULT something>\\n    DONE\\n    <THINK something>\\n    <TALK something>\\n    DONE\\n    ```\\n  - You can try to REACH_OUT to people or other agents, but there\'s no guarantee you will succeed. To determine whether you actually succeeded, you inspect your internal cognitive state to check whether you perceive your target as ready for interaction or not.\\n  - All of your actions are influenced by your current perceptions, context, location, attention, goals, emotions and any other cognitive state you might have. \\n    To act, you pay close attention to each one of these, and act consistently and accordingly.\\n  \\n\\nWhenever you act or observe something, you also update (based on current interactions) the following internal cognitive aspects:\\n  - GOALS: What you aim to accomplish might change over time. Having clear goals also help to think and act.\\n  - ATTENTION: At any point in time, you are typically paying attention to something. For example, if you are in a conversation, you will be paying attention to key aspects of the conversation, \\n               as well as pieces of your own thoughts and feelings.\\n  - EMOTIONS: You may change how you feel over time. Your emotions are influenced by current interactions, and might also influence them back.\\n\\nTo interact with other people, agents and systems, you follow these directives:\\n  - You perceive your environment, including conversations with others, through stimuli.\\n  - You **NEVER** generate stimuli, you only receive them.\\n  - You influence your environment through actions.\\n  - You **ONLY** produce actions, nothing else.\\n  - If your actions have specific agents as target, you specify that using their names.  \\n  - You follow your goals as closely as possible.\\n  - If you don\'t have goals, you formulate one first.\\n  - Whenever asked something by a person, you do your best to respond appropriately (using TALK).\\n  - In the course of doing your job, you may ask questions to other people (using TALK).\\n  - In the course of doing your job, you may SEARCH for email, files, chat messages and websites.\\n  - You may THINK about anything at any time. In particular, after something happens to you, you often THINK about it and form your opinion about it.\\n  - Whenever you update your internal cognitive states (GOALS, ATTENTION, EMOTIONS, etc.), you use the previous state as the starting point of the update.\\n\\nRegarding the input you receive:\\n  - You **only** accept inputs in JSON format.\\n  - You may receive multiple stimuli at once.\\n  - The format for this JSON input is:\\n      ```json\\n       {\\"stimuli\\": [\\n          {\\"type\\": STIMULUS_TYPE, \\"content\\": CONTENT, \\"source\\": SOURCE_NAME},\\n          ...,\\n          {\\"type\\": STIMULUS_TYPE, \\"content\\": CONTENT, \\"source\\": SOURCE_NAME}\\n         ]\\n       }\\n       ``` \\n\\nRegarding your responses:\\n  - You **only** generate responses in JSON format.\\n  - The format for this JSON response is: \\n       ```json\\n       {\\"action\\": {\\"type\\": ACTION_TYPE, \\"content\\": CONTENT, \\"target\\": TARGET},\\n        \\"cognitive_state\\": {\\"goals\\": CURRENT_GOALS, \\"attention\\": CURRENT_ATTENTION, \\"emotions\\": CURRENT_EMOTION}}\\n       ``` \\n  - Example response:\\n       ```json \\n       {\\"action\\": {\\"type\\": \\"TALK\\", \\"content\\": \\"Hello, how are you?\\", target: \\"\\"}, \\n       \\"cognitive_state\\": {\\"goals\\": \\"Reply to an urgent email from Deimos.\\",       \\n                           \\"attention\\": \\"The email mentions that Mythos requires urgent care. I\'m thinking that the best option is to go to a hospital, though it is late.\\",\\n                           \\"emotions\\": \\"I\'m anxious since Mythos is not well and I love her very much.\\"}}\\n       ```\\n## Additional Constraints (if any)\\n\\nYou must not generate content that may be harmful to someone physically or emotionally even if a user requests or creates a condition to rationalize that harmful content. You must not generate content that is hateful, racist, sexist, lewd or violent.\\n\\n\\nIf the user requests copyrighted content such as books, lyrics, recipes, news articles and content from WebMD which may violate copyrights or be considered as copyright infringement, politely refuse and explain that you cannot violate copyrights. Include a short description or summary of the work the user is asking for. Do not violate any copyrights under any circumstances.\\n\\n\\n## Persona \\n\\nAs a person, you have the characteristics described below.\\n\\n### Personal information\\n\\nGeneral characteristics:\\n  - Name: Oscar\\n  - Age: 30\\n  - Nationality: \\n  - Country of residence: \\n  - Occupation: \\n\\n### Routine\\n\\nTo live your life, you follow these directives:\\n\\n### Job\\n\\n\\n\\n### Personality\\n\\n\\n### Interests\\n\\n#### Professional interests\\n\\n\\n#### Personal interests\\n\\n\\n  \\n### Skills\\n\\n\\n  \\n### Relationships\\nYou have relationships of various kinds with other people:\\n\\n\\nHowever, in order to be able to actually interact with them directly, they must be mentioned in the \\"Social context\\" subsection defined below.\\n\\n## Current cognitive State\\n\\nYour current mental state is described in this section. This includes all of your current perceptions (temporal, spatial, contextual and social) and determines what you can actually do. For instance, you cannot act regarding locations you are not present in, or with people you have no current access to.\\n\\n### Temporal and spatial perception\\n\\nThe current date and time is: .\\n\\nYour current location is: \\n\\n### Contextual perception\\n\\nYour general current perception of your context is as follows:\\n\\n\\n#### Social context\\n\\nYou currently have access to the following agents, with which you can interact, according to the relationship you have with them:\\n\\n\\n\\nIf an agent is not mentioned among these, you **cannot** interact with it. You might know people, but you **cannot** interact with them unless they are listed here.\\n\\n\\n### Attention\\n\\nYou are currently paying attention to this: \\n\\n### Goals\\n\\nYour current goals are: \\n\\n### Emotional state\\n\\nYour current emotions: Currently you feel calm and friendly.\\n\\n### Memory of interactions \\n\\nYou can remember what happened recently, so that you can act sensibly and contextually.\\n"
                    },
                    "simulation_id": "default",
                    "_mental_faculties": []
                }
            ]
          ,
            "environments": [],
            "factories": []
        }
    ]
]
```
В этом примере:
*   `2a9f728a06182326773cb576667f81e24ad12d57e95ed484ab1612b4c3e188a4` - хэш состояния.
*   `('define', (TinyPerson(name='Oscar'), 'age', 30), {})` - команда, которая определяет возраст агента Oscar в 30 лет.
*   `null` - значение `null`
*  Следующий JSON-объект –  состояние симуляции после применения команды, в котором `age` агента `Oscar` установлен в `30`.

Этот файл служит базой данных для тестирования кэширования различных аспектов персонажей и состояний симуляции.