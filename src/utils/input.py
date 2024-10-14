## \file ../src/utils/input.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import header 
# ANSI escape codes
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

def input(prompt: str, color: str = RESET) -> str:
    """Prompts the user for input with colored text."""
    return input(f"{color}{prompt}{RESET}")