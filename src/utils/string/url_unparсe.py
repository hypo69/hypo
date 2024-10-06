## \file ../src/utils/string/url_unparсe.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import header 
from urllib.parse import urlparse, parse_qs

def extract_url_params(url: str) -> dict:
    """Извлекает параметры из строки URL.

    Args:
        url (str): Строка URL для парсинга.

    Returns:
        dict: Словарь параметров запроса и их значений.
    """
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)
    
    # Преобразуем значения из списка в строку, если параметр имеет одно значение
    params = {k: v if len(v) > 1 else v[0] for k, v in params.items()}
    
    return params

if __name__ == "__main__":
    # Получаем строку URL от пользователя
    url = input("Введите URL: ")
    params = extract_url_params(url)
    
    # Выводим параметры
    print("Параметры URL:")
    for key, value in params.items():
        print(f"{key}: {value}")
