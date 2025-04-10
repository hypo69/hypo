# Модуль для работы с Poe (g4f)

## Обзор

Модуль `Poe.py` предназначен для взаимодействия с платформой Poe, предоставляющей доступ к различным моделям искусственного интеллекта, таким как Llama-2, CodeLlama, GPT-3.5, GPT-4 и Google-PaLM. Модуль использует веб-драйвер для автоматизации взаимодействия с веб-интерфейсом Poe.

## Подробнее

Модуль содержит класс `Poe`, который наследуется от `AbstractProvider` и реализует методы для создания запросов к моделям через веб-интерфейс Poe. Для работы требуется аутентификация и поддерживается потоковая передача данных.
Модуль использует `selenium` для управления браузером и взаимодействия с веб-страницей.

## Классы

### `Poe`

**Описание**: Класс для взаимодействия с платформой Poe.

**Наследует**:
- `AbstractProvider`: Абстрактный класс, определяющий интерфейс для провайдеров.

**Атрибуты**:
- `url` (str): URL платформы Poe ("https://poe.com").
- `working` (bool): Указывает, работает ли провайдер (False).
- `needs_auth` (bool): Указывает, требуется ли аутенентификация (True).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу (True).
- `models` (dict): Словарь с поддерживаемыми моделями и их именами.

**Методы**:
- `create_completion`: Создает запрос на завершение текста к выбранной модели.

## Функции

### `create_completion`

```python
@classmethod
def create_completion(
    cls,
    model: str,
    messages: Messages,
    stream: bool,
    proxy: str = None,
    webdriver: WebDriver = None,
    user_data_dir: str = None,
    headless: bool = True,
    **kwargs
) -> CreateResult:
    """Создает запрос на завершение текста к выбранной модели.

    Args:
        cls (Poe): Класс Poe.
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для отправки в модель.
        stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        webdriver (WebDriver, optional): Веб-драйвер для управления браузером. По умолчанию `None`.
        user_data_dir (str, optional): Путь к каталогу пользовательских данных браузера. По умолчанию `None`.
        headless (bool, optional): Флаг, указывающий, следует ли запускать браузер в безголовом режиме. По умолчанию `True`.
        **kwargs: Дополнительные аргументы.

    Returns:
        CreateResult: Результат создания запроса.

    Raises:
        ValueError: Если указанная модель не поддерживается.
        RuntimeError: Если не найдено поле ввода текста или пользователь не залогинен.
    """
```

**Назначение**: Создает запрос на завершение текста к выбранной модели через веб-интерфейс Poe.

**Параметры**:
- `cls` (Poe): Класс Poe.
- `model` (str): Название модели для использования. Если не указано, используется "gpt-3.5-turbo".
- `messages` (Messages): Список сообщений для отправки в модель.
- `stream` (bool): Флаг, указывающий, следует ли использовать потоковую передачу.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `webdriver` (WebDriver, optional): Веб-драйвер для управления браузером. По умолчанию `None`.
- `user_data_dir` (str, optional): Путь к каталогу пользовательских данных браузера. По умолчанию `None`.
- `headless` (bool, optional): Флаг, указывающий, следует ли запускать браузер в безголовом режиме. По умолчанию `True`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `CreateResult`: Результат создания запроса. В данном случае, генератор, возвращающий чанки текста.

**Вызывает исключения**:
- `ValueError`: Если указанная модель не поддерживается.
- `RuntimeError`: Если не найдено поле ввода текста или пользователь не залогинен.

**Как работает функция**:

1. **Подготовка**:
   - Если модель не указана, устанавливается значение по умолчанию "gpt-3.5-turbo".
   - Проверяется, поддерживается ли указанная модель. Если нет, вызывается исключение `ValueError`.
   - Форматируется промпт из списка сообщений.
   - Создается сессия веб-драйвера с использованием переданных параметров (веб-драйвер, каталог пользовательских данных, headless режим, прокси).
2. **Взаимодействие с веб-страницей**:
   - С помощью веб-драйвера открывается страница Poe для указанной модели.
   - Скрипт внедряется в страницу для перехвата сообщений WebSocket и извлечения текста ответа модели.
   - Ожидается появление элемента ввода текста. Если элемент не найден, происходит повторное открытие браузера для повторной попытки входа в систему.
   - В поле ввода текста вводится промпт, и нажимается кнопка отправки сообщения.
3. **Получение ответа**:
   - В цикле выполняется JavaScript-скрипт, который извлекает текст ответа модели из перехваченных сообщений WebSocket.
   - Скрипт возвращает чанк текста, если он доступен, или пустую строку, если ответ еще не завершен.
   - Если возвращается `None`, это означает, что ответ завершен.
   - Функция возвращает чанки текста с использованием `yield`, обеспечивая потоковую передачу.

**Внутренние функции**:
- Внутри `create_completion` используется анонимная функция в виде скрипта JavaScript, выполняемого в браузере через `driver.execute_script(script)`. Этот скрипт перехватывает сообщения WebSocket, чтобы получить текст ответа от модели Poe.

**ASCII Flowchart**:

```
    Начало
     ↓
   [Проверка модели]
     ↓
   [Форматирование промпта]
     ↓
   [Создание сессии WebDriver]
     ↓
   [Открытие страницы Poe]
     ↓
   [Внедрение скрипта WebSocket]
     ↓
   [Ожидание элемента ввода текста]
     ↓
   [Ввод текста и отправка сообщения]
     ↓
   [Цикл получения чанков текста]
     ↓
   [Выполнение JavaScript-скрипта]
     ↓
   [Извлечение чанка текста]
     ↓
   [Yield chunk] -→ [chunk == None?] -→  Конец
      ↑          ↓ Да
      -------------
```

**Примеры**:

```python
# Пример использования create_completion с потоковой передачей
messages = [{"role": "user", "content": "Напиши короткое стихотворение о весне."}]
for chunk in Poe.create_completion(model="gpt-3.5-turbo", messages=messages, stream=True):
    print(chunk, end="")
```
```python
# Пример использования create_completion с указанием прокси и каталога пользовательских данных
messages = [{"role": "user", "content": "Как называется столица Франции?"}]
for chunk in Poe.create_completion(model="gpt-3.5-turbo", messages=messages, stream=True, proxy="http://your_proxy:8080", user_data_dir="./user_data"):
    print(chunk, end="")