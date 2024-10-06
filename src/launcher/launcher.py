## \file src/launcher/launcher.py
""" @namespace src.launcher """
## \file ../src/launcher/launcher.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Лончер. Запуск кода в автоматическом режиме на исполнение сценатиев
"""
...
from typing import List, Dict, Any

from src import gs
from .threads import Thread4Supplier
from src.suppliers import Supplier
from src.logger import logger


def launcher (supplier_prefix: list | str = None,
                active_clients_list:list = None,
                scenarios_any: dict = None,
                scenario_files: list = None,
                locale: list | str = None,
                threads: bool = False,
                gui: str = None) -> bool:
    """  
         <b>функция стартер программы</b>
        @details 
        Функция получает на вход параметры запуска инстанса `Supplier` и корректно запускает инстaнс поставщика коммадой `run()`        
       
        @image html 'func_launcher.png'
                
        Функция принимает на вход:
       - список поставщиков `supplier_prefix`. <sub>[Опционально]</sub> Если аргумент не задан - то берется дефолтный из `gs.supplier_prefix`.
       - список сценариев <sub>[Опционально]</sub>
       - список файлов сценариев <sub>[Опционально]</sub>
       - язык исполнения сценариев <sub>[Опционально]</sub>
       - Флаг многопоточности `threads` (`gs.threads`) <sub>[Опционально]</sub>
       - Выбор пользовательского интерфейса <sub>[Опционально]</sub>

       
       По умолчанию функция создаст очередь поставщиков на исполнение. 
        Порядок такой: 
        - supplier_1 -> lang_1 -> scenario_1
        - supplier_1 -> lang_1 -> scenario_2
        - supplier_1 -> lang_2 -> scenario_1
        - supplier_1 -> lang_2 -> scenario_2
        - supplier_2 -> lang_1 -> scenario_1
        - supplier_2 -> lang_1 -> scenario_2
        - supplier_2 -> lang_2 -> scenario_1
        - supplier_2 -> lang_2 -> scenario_2
        - ...
        
        @todo не обработана ситуация, когда заказчик устанавливает настройку `threads = True` для запуска единственного поставщика в `supplier_prefix`
        @todo Сделать возможность запускать сценарий/ии, без указания поставщика. 
        - Извлекать поставщика из сценария
        - упорядочить полученные сценарии по поставщику

        @param supplier_prefix `str | list[str]` : <sub>[Опционально]</sub>  Префикс поставщика. Для каждого поставщика существует набор действий и настроек, расположенных в папке 
                с именем <supplier_prefix>. Если supplier_prefix не указан, программа запускает поставщиков, определенных в файле 
                <b>настроек по умолчанию </b>  в разделе suppliers. `src/settings/settings.json['suppliers']`

                current defined suppliers:
                    * aliexpress
                    * amazon
                    * bangood
                    * cdata
                    * ebay
                    * etzmaleh
                    * gearbest
                    * grandadvance
                    * hb
                    * ksp
                    * kualastyle
                    * morlevi
                    * visualdg
                    * wallashop
                    * wallmart
                    
        @param active_clients_list `list[str]` : <sub>[Опционально]</sub>  
        Список клиентов (получателей данных). Если не указан берется из ключа `active_clients_list` файла `settings.json`
        
        @param scenarios_any `dict` <sub>[Опционально]</sub>  сценарий (список сценариев) исполнения.  
        Сценарий! НЕ ФАЙЛ! Опция позволяет составлять свои наборы сценариев из разных файлов сценариев.    
        
        
        @param  scenario_files `str | list[str]`  <sub>[Опционально]</sub>  Список файлов сценария к исполнению. По умолчанию список сценарив выполнения находится в установках поставщика по адресу   
                                            `src/suppliers/<supplier_prefix>/<supplier_prefix>.json`       
                                     
         locator_description `scenario` и `scenario_files` Позволяют осуществить все варианты сбора товара. Можно задать один из параметров, 
        оба параметра или вовсе их не задавать, тогда программа возьмет параметры из файла настроек.
        
        @param locale `str | list[str]` <sub>[Опционально]</sub> Язык на котором исполняется сценарий. Выбирается из ISO 639-1 двухбуквенного кода. Может получать строку или список. 
                                            Список будет обрабатыавться по очереди в таком порядке:  
                                            - suppliers_list_1 -> scenario_language_1 
                                            - suppliers_list_1 -> scenario_language_2
                                            - suppliers_list_2 -> scenario_language_1
                                            - suppliers_list_2 -> scenario_language_2
                                            
                                            
        @param gui `str` <sub>[Опционально]</sub> Пользовательский тип интерфейса. Возможные значения: 
        - `cmd` (командная строка)
        - `window` (оконный режим)
        - `jupyter`
        - `None` 
        Если этот аргумент не предоставлен, по умолчанию используется интерфейс командной строки `cmd`.
            
        
        @returns `True` в случае успешного завершения сценариев поставщиком, иначе `False`
        
        
        ---
        
        ## Примеры

        
        @code
        > ./python
        >>> import main
        >>> main.main()
        @endcode
        
        @code
        # Запускает все сценарии по умолчанию у поставщика `supplier1`, затем `supplier2`
        # парамерт supplier_prefix может принимать имя одного поставщика или список 
        # поставщиков для запуска парсера/ов
        
        >>> supplier_prefix : list = ['supplier1', 'supplier2', ...]
        >>> main(supplier_prefix = supplier_prefix)
        @endcode
        @code
        ''' определяет язык сбора сценариев. Стандартный двухбуквенный код языка ISO 639-1 '''
        
        >>> launcher( locale = 'ru')
        @endcode
        @code
        ''' Запускает один / несколько сценариев. В этом случает поставщик определяется из сценария '''  
        
        scenarios_list : list = ['scenario1', 'scenario2', ...]
        >>> launcher(scenario = scenarios_list)
        ```
        @endcode
        @code
        ''' запуск в графическом интерфейсе '''
        
        >>> launcher(window_mode = 'window')
        # Не реализован
        @endcode
        @code
        '''Запуск в Jupyter notebook. Удобно для экспериментов '''
        
        >>> launcher(window_mode = 'jupyter') 
        @endcode
        
        
        
        src.suppliers.supplier.Supplier.run()
        
        glish    
         Based on the `supplier_prefix`, creates an instance of the supplier and launches it.  
        If multithreading is defined, control is ...ed to the `Thread4Supplier` class; otherwise,  
        each supplier is launched sequentially from `supplier_prefix`. If `supplier_settings` are not ...ed as a function parameter,
        `supplier_settings` are taken from the global settings `gs.supplier_prefix`
 
        """
        
    ...
    # ~~ debug ~~
    supplier_prefix = 'aliexpress'
    #supplier_prefix = input("Supplier prefix: ")
    ...
    
    #suppliers_list = [supplier_prefix] if supplier_prefix else gs.default_suppliers_list
    locale = ['en'] if locale is None else locale 
     
    ...
    # 3. потоки
    if gs.threads:
        """  Многопоточный режим  """
        threads: list = []
        """ @var threads `(list)` Список потоков """
        for supplier_prefix in suppliers_list:
            for locale in locale:
                thrd: Thread4Supplier = Thread4Supplier (supplier_prefix, locale, threads )
                threads.append (thrd)
                thrd.start ()  ## <- точка старта многопоточного режима

        for thrd in threads:
            thrd.join()
    else:
        # """ Одним потоком """
        # for supplier_prefix in suppliers_list:
        #     for lang in locale:
        #         supplier: Supplier  = Supplier ( supplier_prefix = supplier_prefix, locale = lang )
        #         supplier.run (scenarios_any) ## <- точка старта одного потока
        #         logger.success (f'''Supplier {supplier.supplier_prefix} FINISHED!''')   
                
        # if gui and gui == 'qt':
        #     gs.main_window: MainWindow = launch_main_window()
            
        ...