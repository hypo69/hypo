## \file src/launcher/threads.py
## \file src/launcher/threads.py
# -*- coding: utf-8 -*-
""" @namespace src.launcher """
# /path/to/interpreter/python
""" """

from pathlib import Path
from typing import List, Dict, Any
from threading import Thread


class Thread4Supplier(Thread):
    """  Класс запуска списка поставщиков в отдельных потоках (<i> не тестировал </i>)
     Программу можно запустить в многопоточном режиме. Поскольку поставщики 
    не зависят друг от друга их вполне можно запускать каждого в своем потоке. \n Класс `Thread4Supplier` (src.main.Thread4Supplier) реализует механизм многопоточности
    Режим многопоточности задается в файле `settings.json` ключ: `threads`:`True` включает режим многопоточности.
    
     Запуск многопоточности нагружает цпу

    @todo 
        1. не тестирован

    """
    ...
    def __init__ (self, supplier_prefix: str, locale: str = 'en', threads : Thread = []):
        """
         конструктор класса
        @param self `(pointer)`
        @param supplier_prefix `(str)` Префикс поставщика
        @param locale `(locale)` локаль - язык на котором будет испонянтся сценарий, по умолчанию `en` 
        @var threads_list `(locale)` Список запущенных потоков   
        """  
        # 1.
        self.supplier : Supplier = Supplier ( supplier_prefix = supplier_prefix, locale = locale )
        self.threads = threads
        # 2.
        Thread.__init__(self)
        
    
    def run(self, supplier_prefix, scenario: str | list[str ]  = None):
        """ Запуск потока     
        @param supplier `Supplier` - Supplier class instance
        @param scenario `str | list[str]`  the list of scenarios for execution. None by default
        """
        
        # 1. Заношу поставщика в список потоков
        # 2. Запускаю поставщика на исполнение
        # 3. Финиш. Поставщик закончил исполнение
        
        
        # 1.
        self.threads.append (self.supplier)

        # 2.
        try:
            self.supplier.run(scenario)
            # The suppliers.__init__.py file is run here
        except Exception as ex:
            logger.error (f"""Oшибка запуска потока {ex.with_traceback(ex.__traceback__)}""")

        # 3.
        self.supplier.driver.close()
         