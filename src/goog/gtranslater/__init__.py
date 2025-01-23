## \file /src/goog/gtranslater/__init__.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.goog.gtranslater 
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
  
""" module: src.goog.gtranslater """


""" This module handles language translation using Google Translate API. It includes a function to translate text with automatic language detection for the input text if not specified."""



from googletrans import Translator
from langdetect import detect
from src.logger.logger import logger

def translate(text: str, locale_in: str = None, locale_out: str = 'EN') -> str:
    """ Translate text from one language to another using Google Translate.

    @param text: The text to be translated.
    @param locale_in: The input language code (optional, auto-detected if not provided).
    @param locale_out: The output language code (default is 'EN').
    @return: The translated text.
    """
    translator = Translator()

    try:
        if not locale_in:
            locale_in = detect(text)
            logger.info(f"Auto-detected input language: {locale_in}")

        result = translator.translate(text, src=locale_in, dest=locale_out)
        return result.text
    except Exception as ex:
        logger.error("Translation failed:", ex)
        return ""

def main():
    text = input("Enter the text to be translated: ")
    locale_in = input("Enter the source language code (leave blank for auto-detect): ")
    locale_out = input("Enter the target language code: ")

    translated_text = translate(text, locale_in, locale_out)
    print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()
