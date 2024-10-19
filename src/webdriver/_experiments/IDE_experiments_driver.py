## \file ../src/webdriver/_experiments/IDE_experiments_driver.py
## \file src/webdriver/_experiments/IDE_experiments_driver.py
import sys, os
from pathlib import Path
# ----------------
dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7])
sys.path.append (str (dir_root) )  # Добавляю корневую папку в sys.path
dir_src = Path (dir_root, 'src')
sys.path.append (str (dir_root) ) 
# ----------------

from src.webdriver import Driver

d = Driver()

...