

import header
#from header import j_dumps, j_loads,  logger, Category, Product, Supplier, gs, start_supplier
from header import start_supplier
s = start_supplier('amazon')
""" s - на протяжении всего кода означает класс `Supplier` """

from dict_scenarios import scenario
s.run_scenario(scenario['Murano Glass'])

k = list(s.current_scenario['presta_categories']['default_category'].keys())[0]

