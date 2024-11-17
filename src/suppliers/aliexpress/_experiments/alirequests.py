

""" HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import header   

from src.webdriver import Driver, Chrome, Firefox

d = Driver(Firefox)
d.get_url(r"https://www.aliexpress.com")
...