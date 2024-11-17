

import header
from src.webdriver import Driver, Firefox, Chrome, Edge


d = Driver(Chrome)
...

url = 'https://google.com'

d.get_url(url)

...



