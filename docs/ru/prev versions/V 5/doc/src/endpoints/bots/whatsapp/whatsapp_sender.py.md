# Модуль отправки сообщений в WhatsApp

## Обзор

Этот модуль предназначен для автоматической отправки сообщений в WhatsApp с использованием библиотеки `pywhatkit` и `pyautogui`. Он позволяет отправлять случайные сообщения из заданного списка в указанный период времени.

## Подробней

Модуль предоставляет функцию `send_whatsapp_message` для отправки сообщений и использует список `messages` в качестве банка сообщений с эмодзи. Пользователь вводит номер телефона, количество сообщений, начальный и конечный час отправки. Затем модуль отправляет случайные сообщения в случайное время в заданном интервале.

## Функции

### `send_whatsapp_message`

```python
def send_whatsapp_message(phone_number: str, message: str, hour: int, minutes: int) -> None:
    """Отправляет сообщение WhatsApp с использованием pywhatkit и pyautogui.
    
    Args:
        phone_number (str): Номер телефона получателя с кодом страны.
        message (str): Текст сообщения для отправки.
        hour (int): Час отправки сообщения (0-23).
        minutes (int): Минута отправки сообщения (0-59).
    
    Returns:
        None
    
    Raises:
        Exception: Если возникает ошибка при отправке сообщения.

    Example:
        >>> send_whatsapp_message('+1234567890', 'Hello!', 10, 30)
    """
```

**Как работает функция**:
1. Функция `send_whatsapp_message` принимает номер телефона, сообщение, час и минуты в качестве аргументов.
2. Использует `pywhatkit.sendwhatmsg` для отправки сообщения через WhatsApp Web. Параметры `wait_time` и `tab_close` настроены для ожидания загрузки страницы и закрытия вкладок.
3. После отправки сообщения, функция ждет 20 секунд для загрузки WhatsApp Web.
4. С помощью `pyautogui` и `pynput.keyboard`, функция имитирует нажатие клавиши Enter для отправки сообщения в активном чате.
5. В случае возникновения ошибки, выводит сообщение об ошибке.

**Параметры**:
- `phone_number` (str): Номер телефона получателя, включая код страны.
- `message` (str): Текст сообщения для отправки.
- `hour` (int): Час отправки сообщения (0-23).
- `minutes` (int): Минуты отправки сообщения (0-59).

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки при отправке сообщения, например, при проблемах с подключением или неправильном номере телефона.

**Примеры**:

```python
send_whatsapp_message('+1234567890', 'Hello!', 10, 30)
```

## Переменные

### `messages`

```python
messages: list[str]
```

**Описание**:
Список сообщений для отправки. Каждое сообщение может содержать эмодзи, добавленные с помощью библиотеки `emoji`.

**Пример**:

```python
messages = [
    "Hello! How are you? :slightly_smiling_face:",
    "Thinking of you! :heart:",
    "Just wanted to say hi! :waving_hand:",
    "I love you :heart_exclamation:",
    emoji.emojize("Have a wonderful day! :sun:")
]
```

**Как работает переменная**:
Переменная `messages` содержит список строк, представляющих собой различные сообщения, которые могут быть отправлены. Эмодзи добавляются непосредственно в строки или с использованием `emoji.emojize`.

## Логика работы

1. **Получение пользовательских данных**:
   - Запрашивает у пользователя номер телефона, количество сообщений для отправки, начальный и конечный час отправки.

2. **Отправка сообщений**:
   - В цикле, повторяющемся `num_messages` раз:
     - Генерирует случайный час и минуту в заданном диапазоне.
     - Выбирает случайное сообщение из списка `messages`.
     - Вызывает функцию `send_whatsapp_message` для отправки сообщения.

## Пример использования

```python
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import emoji
import random
import time

def send_whatsapp_message(phone_number, message, hour, minutes):
    """Sends a WhatsApp message using pywhatkit and pyautogui."""
    try:
        pywhatkit.sendwhatmsg(phone_number, message, hour, minutes, wait_time=25, tab_close=True)
        time.sleep(20)  # Give time for WhatsApp Web to load
        keyboard = Controller()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")


# Message bank with emojis
messages = [
    "Hello! How are you? :slightly_smiling_face:",
    "Thinking of you! :heart:",
    "Just wanted to say hi! :waving_hand:",
    "I love you :heart_exclamation:",
    emoji.emojize("Have a wonderful day! :sun:")
]

# Get user inputs
phone_number = input("Enter the phone number with country code: ")
num_messages = int(input("Enter the number of messages to send: "))
start_hour = int(input("Enter the start hour (0-23): "))
end_hour = int(input("Enter the end hour (0-23): "))

message_count = 0
while message_count < num_messages:
    random_hour = random.randint(start_hour, end_hour)
    random_minutes = random.randint(0, 59)
    random_message = random.choice(messages)

    send_whatsapp_message(phone_number, random_message, random_hour, random_minutes)
    message_count += 1
```