## \file ./src/goog/text_to_speech/__init__.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
""" Google TTS """
# /path/to/interpreter/python
import header   

from attr import attr, attrs

import pyttsx3


from gtts import gTTS


class TTS():
    """ Google text to speach """
    def __init__(self,*args,**kwards):
        tts = pyttsx3.init()
        voices = tts.getProperty('voices')
        for v in voices:
            print(v)
    ...


_tts = TTS()



