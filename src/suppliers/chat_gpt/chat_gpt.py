## \file /src/suppliers/chat_gpt/chat_gpt.py
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
from pathlib import Path
from src import gs
from src.utils.file import recursively_read_text_files
class ChatGpt:

    def yeld_conversations_htmls(self) -> str:
        """"""
        ...
        conversation_directory = Path(gs.path.data / 'chat_gpt' / 'conversations')
        html_files = conversation_directory.glob("*.html")

