## \file /src/endpoints/hypo69/code_assistant/__init__.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.endpoints.hypo69.code_assistant 
	:platform: Windows, Unix
	:synopsis:

"""


from .code_assistant import CodeAssistant

if __name__ == "main":
	from .code_assistant import main
	main()
	