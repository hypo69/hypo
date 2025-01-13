## \file /src/endpoints/kazarinov/main.py
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.kazarinov 
	:platform: Windows, Unix
	:synopsis:

"""
import asyncio
import header
from src.endpoints.kazarinov.kazarinov_bot import main

if __name__ == "__main__":
    asyncio.run( main()	)