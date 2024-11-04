## \file src/webdriver/_experiments/start_driver.py
## \file src/webdriver/_experiments/start_driver.py
import header
from src.webdriver import Driver, Firefox, Chrome, Edge


d = Driver(Chrome)
...

url = 'https://google.com'

d.get_url(url)

...



