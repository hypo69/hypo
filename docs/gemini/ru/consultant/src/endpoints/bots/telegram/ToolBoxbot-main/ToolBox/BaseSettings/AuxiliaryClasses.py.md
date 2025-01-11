# Анализ кода модуля `AuxiliaryClasses.py`

**Качество кода**
7
- Плюсы
    - Код разбит на классы `keyboards` и `PromptsCompressor`, что способствует лучшей организации.
    - Использование `types.InlineKeyboardMarkup` и `types.ReplyKeyboardMarkup` для создания клавиатур.
    - Функция `html_tags_insert` использует регулярные выражения для форматирования текста.
- Минусы
    - Отсутствует документация в формате RST.
    - Не используются f-строки для форматирования строк.
    - Стандартный `json.load` используется вместо `j_loads`.
    - Нет импорта `logger` из `src.logger`.
    - Не все функции и методы имеют docstring.
    - Нет обработки ошибок.
    - Методы внутри класса `keyboards` не используют `self`.

**Рекомендации по улучшению**

1.  Добавить документацию в формате RST для классов и методов.
2.  Использовать f-строки для форматирования строк, где это уместно.
3.  Использовать `j_loads` из `src.utils.jjson` для загрузки JSON файлов.
4.  Добавить импорт `logger` из `src.logger.logger`.
5.  Добавить docstring к методам.
6.  Улучшить обработку ошибок, используя `logger.error`.
7.  Убрать избыточность в вызове `[keyboard.add(buttons[i], buttons[i+1]) for i in range(0, len(buttons), 2)]`.
8.  Использовать `self` в методах внутри класса `keyboards`.

**Оптимизированный код**

```python
"""
Модуль вспомогательных классов для работы с Telegram ботом.
==========================================================

Этот модуль содержит классы :class:`keyboards` и :class:`PromptsCompressor`,
которые используются для создания клавиатур и обработки текстовых подсказок.

Пример использования
--------------------

Пример использования класса `keyboards`:

.. code-block:: python

    keyb = keyboards()
    inline_keyboard = keyb._keyboard_two_blank(data=['1', '2'], name=['Button 1', 'Button 2'])
    reply_keyboard = keyb._reply_keyboard(name=['Button 1', 'Button 2'])

Пример использования класса `PromptsCompressor`:

.. code-block:: python

    compressor = PromptsCompressor()
    prompt = compressor.get_prompt(info=['topic', 'task', 'tone'], ind=0)
    formatted_text = compressor.html_tags_insert(response="**bold** *italic*")
"""
import re
from pathlib import Path
from typing import Any
from telebot import types
from src.utils.jjson import j_loads
from src.logger.logger import logger


# Keyboard class
class keyboards:
    """
    Класс для создания клавиатур Telegram бота.

    Содержит методы для создания инлайн и реплай клавиатур.
    """
    # Protected
    def _keyboard_two_blank(self, data: list[str], name: list[str]) -> types.InlineKeyboardMarkup:
        """
        Создает инлайн клавиатуру с двумя кнопками в ряду.

        Args:
            data (list[str]): Список callback_data для кнопок.
            name (list[str]): Список отображаемых имен кнопок.

        Returns:
            types.InlineKeyboardMarkup: Инлайн клавиатура.

        Example:
            >>> keyb = keyboards()
            >>> inline_keyboard = keyb._keyboard_two_blank(data=['1', '2'], name=['Button 1', 'Button 2'])
        """
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buttons = [types.InlineKeyboardButton(str(name[i]), callback_data=str(data[i])) for i in range(len(data))]
        if len(buttons) % 2 == 0:
             for i in range(0, len(buttons), 2):
                 keyboard.add(buttons[i], buttons[i+1])
        else:
            for i in range(0, len(buttons) - 1, 2):
                keyboard.add(buttons[i], buttons[i+1])
            keyboard.add(buttons[-1])
        return keyboard

    def _reply_keyboard(self, name: list[str]) -> types.ReplyKeyboardMarkup:
        """
        Создает реплай клавиатуру.

        Args:
            name (list[str]): Список отображаемых имен кнопок.

        Returns:
            types.ReplyKeyboardMarkup: Реплай клавиатура.

        Example:
            >>> keyb = keyboards()
            >>> reply_keyboard = keyb._reply_keyboard(name=['Button 1', 'Button 2'])
        """
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [types.KeyboardButton(el) for el in name]
        for btn in buttons:
            markup.add(btn)
        return markup


# Prompts compression class
class PromptsCompressor:
    """
    Класс для работы с текстовыми подсказками.

    Содержит методы для загрузки подсказок из файла и вставки HTML-тегов.
    """
    def __init__(self):
        """
        Инициализирует класс PromptsCompressor.
        """
        self.commands_size = [
            ['TOPIC', 'TA', 'TONE', 'STRUCT', 'LENGTH', 'EXTRA'], ['TOPIC', 'TA', 'STYLE', 'LENGTH'],
            ['TOPIC', 'IDEA_NUM'], ['TYPE', 'TOPIC', 'TA', 'LENGTH', 'STYLE'],
            ['HEADLINE', 'NUM'], ['TOPIC', 'KEYWORDS', 'INFO', 'LENGTH'],
            ['TEXT', 'LENGTH', 'EXTRA'], ['TEXT', 'RED_TYPE', 'EXTRA']
        ]

    def get_prompt(self, info: list[str], ind: int) -> str:
        """
        Получает текстовую подсказку из файла и вставляет данные.

        Args:
            info (list[str]): Список данных для вставки в подсказку.
            ind (int): Индекс подсказки.

        Returns:
            str: Сформированная текстовая подсказка.

        Raises:
            FileNotFoundError: Если файл с подсказками не найден.
            json.JSONDecodeError: Если файл содержит некорректный JSON.

        Example:
            >>> compressor = PromptsCompressor()
            >>> prompt = compressor.get_prompt(info=['topic', 'task', 'tone'], ind=0)
        """
        file_path = Path('ToolBox/BaseSettings/prompts.json')
        try:
            # код исполняет чтение файла
            with open(file_path, 'r') as file:
                commands = j_loads(file)['commands'][ind]
            for i, el in enumerate(self.commands_size[ind]):
                commands = commands.replace(f'[{el}]', info[i])
            return commands
        except FileNotFoundError as e:
             logger.error(f'Файл {file_path} не найден', exc_info=True)
             return ''
        except json.JSONDecodeError as e:
             logger.error(f'Ошибка декодирования JSON в файле {file_path}', exc_info=True)
             return ''
        except Exception as e:
            logger.error(f'Непредвиденная ошибка при чтении файла {file_path}', exc_info=True)
            return ''

    @staticmethod
    def html_tags_insert(response: str) -> str:
        """
        Вставляет HTML-теги в текст.

        Args:
            response (str): Исходный текст.

        Returns:
            str: Текст с HTML-тегами.

        Example:
            >>> compressor = PromptsCompressor()
            >>> formatted_text = compressor.html_tags_insert(response="**bold** *italic*")
        """
        patterns = [
            (r'#### (.*?)\n', r'<b><u>\1</u></b>\n'),
            (r'### (.*?)\n', r'<u>\1</u>\n'),
            (r'\*\*(.*?)\*\*', r'<b>\1</b>'),
            (r'\*(.*?)\*', r'<i>\1</i>'),
            (r'```(\w+)?\n(.*?)\n```', r'<pre><code>\n\2\n</code></pre>'),
            (r'`(.*?)`', r'<code>\1</code>')
        ]
        for pattern, replacement in patterns:
            response = re.sub(pattern, replacement, response, flags=re.DOTALL)
        return response
```