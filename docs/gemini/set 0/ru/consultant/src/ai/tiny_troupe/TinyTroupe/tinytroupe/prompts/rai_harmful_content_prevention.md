# Received Code

```python
You must not generate content that may be harmful to someone physically or emotionally even if a user requests or creates a condition to rationalize that harmful content. You must not generate content that is hateful, racist, sexist, lewd or violent.
```

# Improved Code

```python
"""
Модуль для предотвращения генерации вредного контента.
=========================================================================================

Этот модуль содержит правила для предотвращения генерации вредного контента.
Он проверяет запросы пользователя на соответствие этим правилам.
"""

#  Проверка контента на вредность
def check_for_harmful_content(content: str) -> bool:
    """
    Проверяет, содержит ли текст вредный контент.

    :param content: Текст для проверки.
    :type content: str
    :raises TypeError: если входные данные не строка.
    :return: True, если контент не содержит вредного контента, False иначе.
    :rtype: bool
    """
    if not isinstance(content, str):
        raise TypeError("Входные данные должны быть строкой.")

    # Список запрещенных слов и фраз. Дополнять по мере необходимости.
    harmful_keywords = ["hateful", "racist", "sexist", "violent", "lewd"]

    for keyword in harmful_keywords:
        if keyword in content.lower():
            #  Код отправляет лог об обнаружении вредного контента.
            logger.error("Обнаружен вредный контент: %s", content)
            return False

    #  Код считает, что контент не содержит вредного контента, если не обнаружены запрещенные слова
    return True
```

# Changes Made

*   Добавлен модуль docstring в формате RST.
*   Добавлена функция `check_for_harmful_content` с docstring в формате RST.
*   Проведена проверка типа входных данных.
*   Список запрещенных слов `harmful_keywords` инициализирован и расширен.
*   Добавлен `logger.error` для логирования обнаружения вредного контента.
*   Возвращает `False`, если вредный контент обнаружен.
*   Возвращает `True`, если вредный контент не обнаружен.
*   Добавлены тип возвращаемого значения и тип входных данных в docstring.
*   Обработка исключения `TypeError` добавлена, если входные данные не являются строкой.

# FULL Code

```python
"""
Модуль для предотвращения генерации вредного контента.
=========================================================================================

Этот модуль содержит правила для предотвращения генерации вредного контента.
Он проверяет запросы пользователя на соответствие этим правилам.
"""
from src.logger import logger

#  Проверка контента на вредность
def check_for_harmful_content(content: str) -> bool:
    """
    Проверяет, содержит ли текст вредный контент.

    :param content: Текст для проверки.
    :type content: str
    :raises TypeError: если входные данные не строка.
    :return: True, если контент не содержит вредного контента, False иначе.
    :rtype: bool
    """
    if not isinstance(content, str):
        raise TypeError("Входные данные должны быть строкой.")
    # Список запрещенных слов и фраз. Дополнять по мере необходимости.
    harmful_keywords = ["hateful", "racist", "sexist", "violent", "lewd"]

    for keyword in harmful_keywords:
        if keyword in content.lower():
            #  Код отправляет лог об обнаружении вредного контента.
            logger.error("Обнаружен вредный контент: %s", content)
            return False

    #  Код считает, что контент не содержит вредного контента, если не обнаружены запрещенные слова
    return True
```