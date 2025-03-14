## \file /src/utils/string/ai_response_normalizer.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль для нормализации ответа модели
=========================================================================================


Пример использования
--------------------

.. code-block:: python

    from src.utils.string.ai_response_normalizer import normilize_answer

    normalized_str = normalize_answer("```html Пример строки <b>с HTML</b> ```")
    print(normalized_str)  # Пример строки <b>с HTML</b>

"""

prefixes:list = [ 
    '```md\n',
    '```md',
    '```markdown\n',
    '```markdown',
    '```html\n',
    '```html',
    '```\n',
    '```',
    ]

def normalize_answer(text:str) -> str:
    """"""
    for prefix in prefixes:
        if text.startswith(prefix):
            return text.removeprefix(prefix).removesuffix('```')

    return text
