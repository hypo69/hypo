## File hypotez/src/suppliers/aliexpress/campaign/ali_campaign_editor_jupyter_widgets.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""\n.. module: src.suppliers.aliexpress.campaign \n\t:platform: Windows, Unix\n\t:synopsis: Jupyter widgets for the AliExpress campaign editor.\n\nThis module contains widgets for managing AliExpress campaigns in Jupyter notebooks.\n\nTestfile:\n    file test_ali_campaign_editor_jupyter_widgets.py\n\n"""\nMODE = \'dev\'\n\n\nfrom types import SimpleNamespace\nimport header\nfrom pathlib import Path\nfrom ipywidgets import widgets\nfrom IPython.display import display\nimport webbrowser\n\nfrom src import gs\nfrom src.suppliers.aliexpress.campaign import AliCampaignEditor\nfrom src.suppliers.aliexpress.utils import locales\nfrom src.utils import pprint, get_directory_names\nfrom src.logger import logger\n\n\nclass JupyterCampaignEditorWidgets:\n    """Widgets for the AliExpress campaign editor.\n\n    This class provides widgets for interacting with and managing AliExpress campaigns,\n    including selecting campaigns, categories, and languages, and performing actions such as\n    initializing editors, saving campaigns, and showing products.\n\n    Example:\n        >>> editor_widgets: JupyterCampaignEditorWidgets = JupyterCampaignEditorWidgets()\n        >>> editor_widgets.display_widgets()\n    """\n\n    # Class attributes declaration\n    language: str = None\n    currency: str = None\n    campaign_name: str = None\n    category_name: str = None\n    category:SimpleNamespace = None\n    campaign_editor: AliCampaignEditor = None\n    products:list[SimpleNamespace] = None\n    def __init__(self):\n        """Initialize the widgets and set up the campaign editor.\n\n        Sets up the widgets for selecting campaigns, categories, and languages. Also sets up\n        default values and callbacks for the widgets.\n        """\n        self.campaigns_directory:str = Path(\n            gs.path.google_drive, "aliexpress", "campaigns"\n        )\n        \n        if not self.campaigns_directory.exists():\n            raise FileNotFoundError(\n                f"Directory does not exist: {self.campaigns_directory}"\n            )\n\n        #self.languages = {"EN": "USD", "HE": "ILS", "RU": "ILS"}\n        self.campaign_name_dropdown = widgets.Dropdown(\n            options = get_directory_names(self.campaigns_directory),\n            description = "Campaign Name:",\n        )\n        # ... (rest of the class definition)
```

```<algorithm>
**Workflow Diagram**

```mermaid
graph TD
    A[User Selects Campaign] --> B{Get Campaign Directories};
    B --> C[Initialize Widgets];
    C --> D[Initialize Campaign Editor];
    D --> E[Update Category Dropdown];
    E --> F[Display Widgets];
    F --> G[User Interacts (e.g., Select Category, Language)];
    G --> H[Trigger Callback];
    H --> D;
    D --> I[Save Campaign];
    I --> J[Save Categories from Worksheet];
    D --> K[Show Products];
    K --> L[Set Products Worksheet];
    D --> M[Open Spreadsheet];
    M --> N[Open Spreadsheet in Browser];
```

**Examples:**

* **A:** User clicks on "SummerSale" in the campaign dropdown.
* **B:** `get_directory_names` retrieves a list of subdirectories within the "campaigns" directory (e.g., ["SummerSale", "WinterSale"]).
* **C:** Dropdown widgets are initialized with these campaign names.
* **D:** `initialize_campaign_editor` is called, potentially creating an `AliCampaignEditor` instance and retrieving/setting data, triggering other updates.
* **E:** `update_category_dropdown` populates the category dropdown with the categories for the selected campaign.
* **F:** The initialized widgets (dropdowns, buttons) are displayed in the Jupyter notebook.
* **G:** User selects a category and/or language.
* **H:** Dropdown changes trigger `on_campaign_name_change`, `on_category_change`, or `on_language_change`, which trigger a re-initialization.
* **I:** User clicks the "Save Campaign" button.
* **J:** `AliCampaignEditor.save_categories_from_worksheet` is called.
* **K:** User clicks the "Show Products" button.
* **L:** `AliCampaignEditor.set_products_worksheet` is called.
* **M:** User clicks the "Open Google Spreadsheet" button.
* **N:**  `webbrowser.open` opens the spreadsheet in a new browser tab.

```
```<explanation>

**Imports:**

* `types`: Provides `SimpleNamespace` for creating objects with named attributes.
* `header`: Likely a custom module, assumed for initialization or configuration related to the application (not fully analyzed without access to the `header` module).
* `pathlib`: Enables path manipulation.
* `ipywidgets`: For creating interactive widgets in Jupyter notebooks.
* `IPython.display`: For displaying widgets in notebooks.
* `webbrowser`: To open web pages.
* `src.gs`: Likely a module for Google Sheets related operations, crucial for spreadsheet interaction.
* `src.suppliers.aliexpress.campaign.AliCampaignEditor`: Defines the `AliCampaignEditor` class for handling campaign data interaction.
* `src.suppliers.aliexpress.utils.locales`: Provides localization data (likely languages and currency codes).
* `src.utils.pprint`: Likely for formatted printing or debugging.
* `src.utils.get_directory_names`: Extracts directory names from a path.
* `src.logger`: A logging module for managing application logs (useful for error handling and debugging).

**Relationship with other parts of the project:**

The code strongly relies on modules within the `src` package, demonstrating a clear modular structure and a potential dependency on external services (e.g., Google Sheets API). `AliCampaignEditor` likely interacts with other components in the `src.suppliers.aliexpress` package for data retrieval, saving, and processing.  The reliance on `gs` suggests that interactions with Google Sheets data are paramount to the functionality.

**Classes:**

* `JupyterCampaignEditorWidgets`: This class manages the Jupyter widgets for interacting with AliExpress campaigns.
    * Attributes: `language`, `currency`, `campaign_name`, `category_name`, `category`, `campaign_editor`, `products`, `campaigns_directory` etc. store information and objects related to the campaigns. These attributes are crucial for maintaining the state of the campaign selection process.
    * Methods: `__init__`, `display_widgets`, `initialize_campaign_editor`, `update_category_dropdown`, `setup_callbacks`,  and various `on_change` functions for handling user interactions.  These methods manage the initialization and update of the widgets based on user actions.
    * Interactions: This class interacts with the `AliCampaignEditor` class, using its methods to fetch campaign data and execute actions like saving campaign data and displaying products. It also interacts with  `get_directory_names` for directory retrieval,  and `locales` to handle language selection.

**Functions:**

* `initialize_campaign_editor`: Initializes the `AliCampaignEditor` object based on the selected campaign, category, and language.
* `update_category_dropdown`: Updates the category dropdown options based on the chosen campaign.
* `on_campaign_name_change`, `on_category_change`, `on_language_change`: Handle changes in the respective dropdowns, triggering re-initialization of campaign data and other updates.
* `save_campaign`: Saves the campaign data to Google Sheets.
* `show_products`: Displays products from the selected category.
* `open_spreadsheet`: Opens the Google Spreadsheet in a web browser.
* `get_directory_names`:  A helper function that extracts directory names from a given path.  While this is a common utility function, there's a comment in the code showing it could potentially be a method of the class, so it is worth considering moving it into the class for tighter cohesion.


**Potential Errors/Improvements:**

* **Error Handling:**  The code includes `try...except` blocks for `save_campaign` and `show_products`, but similar error handling could be beneficial in other critical functions.  The lack of specific error types might be problematic for comprehensive debugging.
* **`get_directory_names` Method:**  The method is commented out. Consider removing the comment.
* **`initialize_campaign_editor` Input:**  The `_` argument in `initialize_campaign_editor` is unused and potentially a source of confusion. Consider renaming to a more meaningful argument name for improved readability.
* **`__init__` Initialization:** The code initializes the `campaign_editor`, but the variables may not be used if the selected campaign is invalid. Adding null or error checks might improve resilience.


**Variables:**

* `MODE`: A string variable for development mode.
* `campaigns_directory`: Path to the campaign data directory.
* `language`, `currency`, `campaign_name`, `category_name`, etc.: Variables that store data related to the selection and interaction processes, crucial for correctly retrieving and presenting data for the selected campaign, category, and language.

This code structure exhibits a design that aims to manage the campaign data in a modular manner.  Further improvements would be to implement type hinting, expand the error handling for broader robustness, and to improve the naming conventions to further clarify the functions and classes.