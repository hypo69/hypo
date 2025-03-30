## \file /src/endpoints/kazarinov/main.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.endpoints.kazarinov 
	:platform: Windows, Unix
	:synopsis:

"""
import asyncio
from urllib import response
import header
from src.endpoints.math_challenges.minibot import main
from src.endpoints.math_challenges.scenarios.scenario import Scenario
from src.utils.printer import pprint as print

def run_scenario():
	"""Запускает сценарий."""
	s = Scenario()
	response = s.ask_question()
	print( response )

if __name__ == "__main__":
	#main()
	run_scenario()
	...
	