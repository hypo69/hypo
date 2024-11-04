""" <b> Module for launching the program. </b>

Here I set the order of launching suppliers (in threads or sequentially), the user interface (`GUI`, `JUPYTER`, `CMD`). \n 
            Extended launch parameters for suppliers can be specified when calling the `launcher()` function. See details 
            in the comments within the `launcher()` function (`src.main.launcher()`).
<pre>
main.py
│
├── sys
│
├── pathlib
│
├── typing
│   ├── List
│   ├── Dict
│
├── src
│   ├── settings.py
│   │   └── gs
│   │       └── ...
│   │           └── ...
│   │
│   ├── launcher.py
│       └── launcher
│           └── ...
│
└── ...
</pre>

@dotfile main.dot
@image html main.png
"""
...
## \file ../src/main.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
...
import sys
from pathlib import Path
from typing import List, Dict
from src import gs
from src.launcher import launcher

""" The code below is a workaround. """
dir_root: Path = Path.cwd().resolve().parent  # Root directory of the project
sys.path.append(str(dir_root))  # Adding the root directory to sys.path
dir_src = dir_root / 'src'
sys.path.append(str(dir_src))  # Adding the src directory to sys.path

def main(supplier_prefix: List[str] | str = None,
         active_clients_list: List[str] = None,
         scenario: Dict = None,
         scenario_files: List[str] | str = None,
         locale: List[str] | str = None,
         gui_mode: str = None
         ) -> bool:
    """ 
    When running python main.py, default values will be used,
    and when running python main.py arg1 arg2, the passed arguments will be used.
    """

    print("Supplier Prefix:", supplier_prefix)
    print("Active Clients List:", active_clients_list)
    print("Scenario:", scenario)
    print("Scenario Files:", scenario_files)
    print("Scenario Language:", locale)
    print("GUI Mode:", gui_mode)
    
    launcher(supplier_prefix, active_clients_list, scenario, scenario_files, locale, threads=False, gui='qt')

if __name__ == "__main__":
    # Check for command-line arguments
    if len(sys.argv) > 1:
        # The first argument is the script name, so we start with 1
        supplier_prefix = sys.argv[1]
        active_clients_list = sys.argv[2]
        # Set other command-line arguments as needed
    else:
        # Set default values if arguments were not provided
        supplier_prefix = "default_value"
        active_clients_list = ["1", "2", "3"]
        # Set other default values as needed

    # Launch the main function with the provided or default argument values
    main(supplier_prefix=supplier_prefix, active_clients_list=active_clients_list)

    """ Entry point. See launcher() for launch details.
    
    @param supplier_prefix `str | list[str]` <sub>[Optional]</sub> List of suppliers from whom I need to get info
    @param active_clients_list `list[str]` List of clients (to whom the content is delivered)
    @param scenario `dict` <sub>[Optional]</sub> Single execution scenario. Scenario! NOT A FILE! This option allows you to compose your own sets of scenarios from different scenario files
    @param scenario_files `list | str` <sub>[Optional]</sub> List of scenario files
    @param locale `(str | list[str])` <sub>[Optional]</sub> Scenario execution language(s) - two-letter ISO code
    @param gui_mode `(str)` <sub>[Optional]</sub> `['window' | 'jupyter lab' | 'jupyter notebook' | 'None']`
    
    @returns `True` if success, else `False`
    """"