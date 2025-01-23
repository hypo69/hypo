## \file /src/suppliers/chat_gpt/converstions_parser.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.chat_gpt 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
import header
from src import gs

from pathlib import Path
from bs4 import BeautifulSoup

def extract_conversations_from_html(file_path: Path):
    """Генератор, который читает один .html файл и извлекает все <div class="conversation">.

    :param file_path: Путь к .html файлу.
    """
    # Открываем файл и парсим его содержимое
    with file_path.open('r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Ищем все <div class="conversation">
        conversations = soup.find_all('div', class_='conversation')
        ...
    # Возвращаем каждую найденную conversation
    for conversation in conversations:
        yield conversation

# Пример использования
file_path = Path(gs.path.data / 'chat_gpt'  / 'chat.html')
for conversation in extract_conversations_from_html(file_path):
    print(conversation.prettify())  # Печатаем содержимое каждой найденной беседы
