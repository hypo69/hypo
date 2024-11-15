## \file hypotez/src/suppliers/kualastyle/_experiments/test_1_kuala_scenarios.py
# -*- coding: utf-8 -*-

""" module: src.suppliers.kualastyle._experiments """
MODE = 'debug'
""" module: src.suppliers.kualastyle._experiments """
MODE = 'debug'
import header
from header import Product, ProductFields, start_supplier
s = start_supplier('kualastyle')
""" s - на протяжении всего кода означает класс `Supplier` """
s.run()

#from dict_scenarios import scenarios
#for key,scenario in scenarios.items(): 
#    s.current_scenario = scenario
#    s.run_scenario(s.current_scenario))