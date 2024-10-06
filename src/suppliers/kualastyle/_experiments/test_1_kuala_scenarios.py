## \file ../src/suppliers/kualastyle/_experiments/test_1_kuala_scenarios.py
## \file src/suppliers/kualastyle/_experiments/test_1_kuala_scenarios.py
import header
from header import Product, ProductFields, start_supplier
s = start_supplier('kualastyle')
""" s - на протяжении всего кода означает класс `Supplier` """
s.run()

#from dict_scenarios import scenarios
#for key,scenario in scenarios.items(): 
#    s.current_scenario = scenario
#    s.run_scenario(s.current_scenario))