# Модуль валидации TinyPerson

## Обзор

Модуль `tiny_person_validator.py` предназначен для валидации экземпляров класса `TinyPerson` с использованием OpenAI LLM. Он содержит класс `TinyPersonValidator` с методом `validate_person`, который оценивает соответствие экземпляра `TinyPerson` заданным ожиданиям.

## Подробней

Этот модуль играет важную роль в проекте `hypotez`, обеспечивая механизм для проверки и подтверждения поведения и характеристик виртуальных личностей, созданных с использованием класса `TinyPerson`. Валидация осуществляется путем отправки серии вопросов экземпляру `TinyPerson` и оценки его ответов с использованием OpenAI LLM. Результатом валидации является оценка достоверности и обоснование этой оценки.

## Классы

### `TinyPersonValidator`

**Описание**: Класс, предоставляющий статический метод для валидации экземпляров `TinyPerson`.

**Принцип работы**: Класс `TinyPersonValidator` содержит один статический метод `validate_person`, который использует OpenAI LLM для оценки соответствия экземпляра `TinyPerson` заданным ожиданиям.

**Методы**:
- `validate_person`: Статический метод для валидации экземпляра `TinyPerson`.

## Функции

### `validate_person`

```python
    @staticmethod
    def validate_person(person, expectations=None, include_agent_spec=True, max_content_length=default_max_content_display_length) -> tuple[float, str]:
        """
        Validate a TinyPerson instance using OpenAI\'s LLM.

        This method sends a series of questions to the TinyPerson instance to validate its responses using OpenAI\'s LLM.\n
        The method returns a float value representing the confidence score of the validation process.\n
        If the validation process fails, the method returns None.\n

        Args:\n
            person (TinyPerson): The TinyPerson instance to be validated.\n
            expectations (str, optional): The expectations to be used in the validation process. Defaults to None.\n
            include_agent_spec (bool, optional): Whether to include the agent specification in the prompt. Defaults to False.\n
            max_content_length (int, optional): The maximum length of the content to be displayed when rendering the conversation.\n

        Returns:\n
            float: The confidence score of the validation process (0.0 to 1.0), or None if the validation process fails.\n
            str: The justification for the validation score, or None if the validation process fails.\n
        """
        # Initiating the current messages
        current_messages = []
        
        # Generating the prompt to check the person
        check_person_prompt_template_path = os.path.join(os.path.dirname(__file__), \'prompts/check_person.mustache\')
        with open(check_person_prompt_template_path, \'r\') as f:\n
            check_agent_prompt_template = f.read()\n
        \n
        system_prompt = chevron.render(check_agent_prompt_template, {"expectations": expectations})\n

        # use dedent\n
        import textwrap\n
        user_prompt = textwrap.dedent(\\\n
        """\n
        Now, based on the following characteristics of the person being interviewed, and following the rules given previously, \n
        create your questions and interview the person. Good luck!\n\n
        """)\n

        if include_agent_spec:\n
            user_prompt += f"\\n\\n{json.dumps(person._persona, indent=4)}"\n
        else:\n
            user_prompt += f"\\n\\nMini-biography of the person being interviewed: {person.minibio()}"\n\n\n

        logger = logging.getLogger("tinytroupe")\n

        logger.info(f"Starting validation of the person: {person.name}")\n

        # Sending the initial messages to the LLM\n
        current_messages.append({"role": "system", "content": system_prompt})\n
        current_messages.append({"role": "user", "content": user_prompt})\n

        message = openai_utils.client().send_message(current_messages)\n

        # What string to look for to terminate the conversation\n
        termination_mark = "```json"\n

        while message is not None and not (termination_mark in message["content"]):\n
            # Appending the questions to the current messages\n
            questions = message["content"]\n
            current_messages.append({"role": message["role"], "content": questions})\n
            logger.info(f"Question validation:\\n{questions}")\n

            # Asking the questions to the person\n
            person.listen_and_act(questions, max_content_length=max_content_length)\n
            responses = person.pop_actions_and_get_contents_for("TALK", False)\n
            logger.info(f"Person reply:\\n{responses}")\n

            # Appending the responses to the current conversation and checking the next message\n
            current_messages.append({"role": "user", "content": responses})\n
            message = openai_utils.client().send_message(current_messages)\n

        if message is not None:\n
            json_content = utils.extract_json(message[\'content\'])\n
            # read score and justification\n
            score = float(json_content["score"])\n
            justification = json_content["justification"]\n
            logger.info(f"Validation score: {score:.2f}; Justification: {justification}")\n
            \n
            return score, justification\n
        \n
        else:\n
            return None, None\n
```

**Назначение**: Валидация экземпляра `TinyPerson` с использованием OpenAI LLM.

**Параметры**:
- `person` (TinyPerson): Экземпляр `TinyPerson`, который необходимо валидировать.
- `expectations` (str, optional): Ожидания, используемые в процессе валидации. По умолчанию `None`.
- `include_agent_spec` (bool, optional): Флаг, указывающий, следует ли включать спецификацию агента в запрос. По умолчанию `False`.
- `max_content_length` (int, optional): Максимальная длина контента для отображения при рендеринге разговора. По умолчанию значение берется из конфигурации `config["OpenAI"].getint("MAX_CONTENT_DISPLAY_LENGTH", 1024)`.

**Возвращает**:
- `tuple[float, str]`: Кортеж, содержащий оценку достоверности (от 0.0 до 1.0) и обоснование оценки. Возвращает `None, None`, если процесс валидации завершается неудачно.

**Как работает функция**:

1. **Инициализация**:
   - Инициализируется список `current_messages` для хранения сообщений в процессе валидации.

2. **Подготовка запроса**:
   - Загружается шаблон запроса из файла `prompts/check_person.mustache`.
   - Рендерится системный запрос `system_prompt` с использованием шаблона и заданных ожиданий (`expectations`).
   - Формируется пользовательский запрос `user_prompt` на основе характеристик `TinyPerson`, которого необходимо проинтервьюировать. В зависимости от значения `include_agent_spec`, в запрос включается либо полная персона агента, либо мини-биография.

3. **Взаимодействие с LLM**:
   - Системный и пользовательский запросы добавляются в `current_messages`.
   - Отправляется запрос в OpenAI LLM с использованием `openai_utils.client().send_message(current_messages)`.
   - В цикле происходит обмен сообщениями с LLM до тех пор, пока в ответе не появится маркер завершения `termination_mark` (```json).

4. **Обработка ответов**:
   - Вопросы, полученные от LLM, добавляются в `current_messages`.
   - `TinyPerson` "слушает" вопросы и "действует" на них (`person.listen_and_act`).
   - Ответы `TinyPerson` извлекаются и добавляются в `current_messages`.

5. **Извлечение результатов**:
   - После получения сообщения с маркером завершения извлекается JSON-контент из сообщения.
   - Из JSON-контента извлекаются оценка (`score`) и обоснование (`justification`).
   - Результаты логируются с использованием `logger.info`.

6. **Возврат результатов**:
   - Функция возвращает кортеж, содержащий оценку и обоснование. Если в процессе валидации произошла ошибка (например, не был получен маркер завершения), функция возвращает `None, None`.

**ASCII Flowchart**:

```
    Начало
     ↓
  Загрузка шаблона и рендеринг запроса
     ↓
  Формирование запроса пользователю
     ↓
  Отправка запроса в OpenAI LLM
     ↓
  Цикл (пока нет маркера завершения):
   ├── Получение вопросов от LLM
   │    ↓
   │  Ответы TinyPerson на вопросы
   │    ↓
   └── Отправка ответов в OpenAI LLM
     ↓
  Извлечение JSON-контента из ответа
     ↓
  Извлечение оценки и обоснования
     ↓
    Конец
```

**Примеры**:

```python
# Пример использования функции validate_person
from tinytroupe.agent import TinyPerson
from tinytroupe.tinytroupe import StoryTeller
from tinytroupe.world import World
from tinytroupe.location import Location
from tinytroupe.item import Item
from src.logger import logger

# Создание экземпляра TinyPerson (в данном примере параметры сокращены для краткости)
world = World()
storyteller = StoryTeller(world=world)
location = Location(storyteller=storyteller, name="Название локации", description="Описание локации")
item = Item(name="Название предмета", description="Описание предмета")

tiny_person_data = {
    "name": "Тестовый персонаж",
    "description": "Описание тестового персонажа",
    "world": world.ref(),
    "location": location.ref(),
    "inventory": [item.ref()],
    "occupation": "Тестировщик",
    "persona": "Характер тестового персонажа",
    "goals": "Цели тестового персонажа",
    "current_action": "Тестирование",
}
person = TinyPerson(**tiny_person_data)

# Валидация персонажа без ожиданий и без включения спецификации агента
score, justification = TinyPersonValidator.validate_person(person)
if score is not None:
    print(f"Оценка: {score:.2f}, Обоснование: {justification}")
else:
    print("Валидация не удалась")

# Валидация персонажа с ожиданиями и с включением спецификации агента
expectations = "Персонаж должен быть дружелюбным и отзывчивым"
score, justification = TinyPersonValidator.validate_person(person, expectations=expectations, include_agent_spec=True)
if score is not None:
    print(f"Оценка: {score:.2f}, Обоснование: {justification}")
else:
    print("Валидация не удалась")