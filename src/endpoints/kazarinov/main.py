## \file /src/endpoints/kazarinov/main.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
```rst
.. module:: src.endpoints.kazarinov 
```

Модуль обслуживания для Сергея Казаринова
==========================================
Казаринов собирает компоненты для сборки комьютеров с сайтов поставщиков,
объединяет их в onetab и отправляет ботy созданую ссылку.
Бот запускает сценарий сбора информации с вебстраниц.
Сценарий подключает quotation_builder для создания конечного прайслиста


[Документация `minibot`](https://github.com/hypo69/hypo/blob/master/docs/ru/src/endpoints/kazarinov/minibot.py.md)
[Документация `scenario`](https://github.com/hypo69/hypo/blob/master/docs/ru/src/endpoints/kazarinov/scenarios/scenario.py.md)
[Документация `quotation_builder`](https://github.com/hypo69/hypo/blob/master/docs/ru/src/endpoints/kazarinov/scenarios/quotation_builder.py.md)
"""
import asyncio
import header
from src.endpoints.kazarinov.minibot import main

if __name__ == "__main__":
	main()