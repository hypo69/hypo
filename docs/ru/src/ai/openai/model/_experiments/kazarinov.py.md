# Модуль для экспериментов с OpenAI (kazarinov.py)

## Обзор

Модуль предназначен для экспериментов с моделью OpenAI, включая инициализацию модели, отправку запросов и обработку ответов. Он также включает функцию для интерактивного чата с моделью.

## Подробней

Этот модуль предоставляет класс `OpenAIChat` для взаимодействия с OpenAI API. Он загружает системную инструкцию из файла и использует её для инициализации модели. Модуль также содержит функцию `chat` для организации интерактивного чата с пользователем через консоль. Этот код является экспериментальным и может использоваться для тестирования различных параметров и подходов к взаимодействию с OpenAI.

## Классы

### `OpenAIChat`

**Описание**: Класс для взаимодействия с моделью OpenAI Chat.

**Принцип работы**:
Класс инициализируется с API-ключом и системной инструкцией. Он поддерживает историю сообщений для контекста беседы. Метод `ask` отправляет запрос в OpenAI и возвращает ответ, обрабатывая возможные ошибки.

**Атрибуты**:
- `api_key` (str): API-ключ для доступа к OpenAI.
- `system_instruction` (str): Системная инструкция для модели.
- `messages` (list): Список сообщений для поддержания контекста диалога.

**Методы**:

- `__init__(self, api_key: str, system_instruction: str = None)`:
    - **Описание**: Инициализирует класс `OpenAIChat` с заданным API-ключом и системной инструкцией.
- `ask(self, prompt: str) -> str`:
    - **Описание**: Отправляет запрос в модель OpenAI и получает ответ.

### `__init__(self, api_key: str, system_instruction: str = None)`

```python
    def __init__(self, api_key: str, system_instruction: str = None):
        """Инициализация OpenAI модели"""
        openai.api_key = gs.credentials
        self.system_instruction = system_instruction
        self.messages = []

        if self.system_instruction:
            self.messages.append({"role": "system", "content": self.system_instruction})
```

**Назначение**: Инициализация экземпляра класса `OpenAIChat`.

**Параметры**:
- `api_key` (str): API-ключ для доступа к OpenAI.
- `system_instruction` (str, optional): Системная инструкция для модели. По умолчанию `None`.

**Как работает функция**:

1. **Установка API-ключа**: Устанавливает API-ключ для доступа к OpenAI, используя `gs.credentials`.
2. **Инициализация атрибутов**: Инициализирует атрибуты экземпляра класса: `system_instruction` и `messages`.
3. **Добавление системной инструкции**: Если предоставлена системная инструкция, она добавляется в список сообщений как сообщение от системы.

```
Установка API-ключа --> Инициализация атрибутов --> Добавление системной инструкции
```

**Примеры**:

```python
ai = OpenAIChat(api_key="your_api_key", system_instruction="You are a helpful assistant.")
```

### `ask(self, prompt: str) -> str`

```python
    def ask(self, prompt: str) -> str:
        """Отправка вопроса в модель OpenAI и получение ответа"""
        self.messages.append({"role": "user", "content": prompt})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                max_tokens=150,
                temperature=0.7
            )
            answer = response['choices'][0]['message']['content']
            self.messages.append({"role": "assistant", "content": answer})
            return answer
        except Exception as ex:
            logger.error(f"Ошибка: {ex}")
            return "Произошла ошибка при обработке запроса."
```

**Назначение**: Отправка вопроса в модель OpenAI и получение ответа.

**Параметры**:
- `prompt` (str): Текст вопроса, который необходимо отправить в модель.

**Возвращает**:
- `str`: Ответ от модели OpenAI или сообщение об ошибке.

**Вызывает исключения**:
- `Exception`: В случае ошибки при взаимодействии с OpenAI API.

**Как работает функция**:

1. **Добавление сообщения пользователя**: Добавляет сообщение пользователя в список сообщений.
2. **Отправка запроса в OpenAI**: Отправляет запрос в OpenAI с использованием `openai.ChatCompletion.create`.
3. **Обработка ответа**: Извлекает ответ из полученного ответа и добавляет его в список сообщений.
4. **Обработка ошибок**: В случае возникновения ошибки логирует её и возвращает сообщение об ошибке.

```
Добавление сообщения пользователя --> Отправка запроса в OpenAI --> Обработка ответа --> Обработка ошибок
```

**Примеры**:

```python
ai = OpenAIChat(api_key="your_api_key", system_instruction="You are a helpful assistant.")
response = ai.ask(prompt="What is the capital of France?")
print(response)
```

## Функции

### `chat()`

```python
def chat():
    print("Добро пожаловать в чат с OpenAI!")
    print("Чтобы завершить чат, напишите \'exit\'.\n")
    
    # Ввод ключа API и инициализация модели
    api_key = input("Введите ваш OpenAI API ключ: ")
    ai = OpenAIChat(api_key=api_key, system_instruction=system_instruction)

    while True:
        # Получаем вопрос от пользователя
        user_input = input("> вопрос\n> ")
        
        if user_input.lower() == 'exit':
            print("Чат завершен.")
            break
        
        # Отправляем запрос модели и получаем ответ
        response = ai.ask(prompt=user_input)
        
        # Выводим ответ
        print(f">> ответ\n>> {response}\n")
```

**Назначение**: Функция для организации интерактивного чата с пользователем через консоль.

**Как работает функция**:

1. **Приветствие**: Выводит приветственное сообщение и инструкцию по завершению чата.
2. **Ввод API-ключа**: Запрашивает у пользователя OpenAI API-ключ.
3. **Инициализация модели**: Инициализирует модель `OpenAIChat` с введенным API-ключом и системной инструкцией.
4. **Цикл чата**: В цикле запрашивает вопросы у пользователя, отправляет их в модель и выводит ответы до тех пор, пока пользователь не введет "exit".

```
Приветствие --> Ввод API-ключа --> Инициализация модели --> Цикл чата
```

**Примеры**:

```python
chat()
```

### `system_instruction_path`
```python
system_instruction_path = Path('../src/ai/openai/model/_experiments/system_instruction.txt')
```

**Назначение**: Определяет путь к файлу, содержащему системную инструкцию для модели OpenAI.

### `system_instruction`
```python
system_instruction = read_text_file(system_instruction_path)
```

**Назначение**: Считывает системную инструкцию из файла, указанного в `system_instruction_path`.