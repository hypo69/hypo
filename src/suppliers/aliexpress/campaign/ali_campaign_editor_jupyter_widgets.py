## \file hypotez/src/suppliers/aliexpress/campaign/ali_campaign_editor_jupyter_widgets.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress.campaign """

""" Jupyter widgets for the AliExpress campaign editor.

This module contains widgets for managing AliExpress campaigns in Jupyter notebooks.

Testfile:
    file test_ali_campaign_editor_jupyter_widgets.py
"""

from types import SimpleNamespace
import header
from pathlib import Path
from ipywidgets import widgets
from IPython.display import display
import webbrowser

from src import gs
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.suppliers.aliexpress.utils import locales
from src.utils import pprint, get_directory_names
from src.logger import logger


class JupyterCampaignEditorWidgets:
    """Widgets for the AliExpress campaign editor.

    This class provides widgets for interacting with and managing AliExpress campaigns,
    including selecting campaigns, categories, and languages, and performing actions such as
    initializing editors, saving campaigns, and showing products.

    Example:
        >>> editor_widgets: JupyterCampaignEditorWidgets = JupyterCampaignEditorWidgets()
        >>> editor_widgets.display_widgets()
    """

    # Class attributes declaration
    language: str = None
    currency: str = None
    campaign_name: str = None
    category_name: str = None
    category:SimpleNamespace = None
    campaign_editor: AliCampaignEditor = None
    products:list[SimpleNamespace] = None
    def __init__(self):
        """Initialize the widgets and set up the campaign editor.

        Sets up the widgets for selecting campaigns, categories, and languages. Also sets up
        default values and callbacks for the widgets.
        """
        self.campaigns_directory:str = Path(
            gs.path.google_drive, "aliexpress", "campaigns"
        )
        
        if not self.campaigns_directory.exists():
            raise FileNotFoundError(
                f"Directory does not exist: {self.campaigns_directory}"
            )

        #self.languages = {"EN": "USD", "HE": "ILS", "RU": "ILS"}
        self.campaign_name_dropdown = widgets.Dropdown(
            options = get_directory_names(self.campaigns_directory),
            description = "Campaign Name:",
        )
        self.category_name_dropdown = widgets.Dropdown(
            options=[], description="Category:"
        )
        self.language_dropdown = widgets.Dropdown(
            options=[f"{key} {value}" for locale in locales for key, value in locale.items()],
            description="Language/Currency:",
        )
        self.initialize_button = widgets.Button(
            description="Initialize Campaign Editor",
            disabled=False,
        )
        self.save_button = widgets.Button(
            description="Save Campaign",
            disabled=False,
        )
        self.show_products_button = widgets.Button(
            description="Show Products",
            disabled=False,
        )
        self.open_spreadsheet_button = widgets.Button(
            description="Open Google Spreadsheet",
            disabled=False,
        )

        # Set up callbacks
        self.setup_callbacks()

        # Initialize with default values
        self.initialize_campaign_editor(None)
    
    def initialize_campaign_editor(self, _):
        """Initialize the campaign editor.

        Args:
            _: Unused argument, required for button callback.

        Sets up the campaign editor based on the selected campaign and category.
        """
        
        self.campaign_name = self.campaign_name_dropdown.value or None
        self.category_name = self.category_name_dropdown.value or None
        
        self.language, self.currency = self.language_dropdown.value.split()
        if self.campaign_name:
            self.update_category_dropdown(self.campaign_name)
            self.campaign_editor = AliCampaignEditor(campaign_name = self.campaign_name, language = self.language, currency = self.currency)
            
            if self.category_name:
                self.category = self.campaign_editor.get_category(self.category_name)
                self.products = self.campaign_editor.get_category_products(self.category_name)
        else:
            logger.warning(
                "Please select a campaign name before initializing the editor."
            )

    # def get_directory_names(self, path: Path) -> list[str]:
    #     """Get directory names from the specified path.

    #     Args:
    #         path (Path): Path to search for directories.

    #     Returns:
    #         list[str]: List of directory names.

    #     Example:
    #         >>> directories: list[str] = self.get_directory_names(Path("/some/dir"))
    #         >>> print(directories)
    #         ['dir1', 'dir2']
    #     """
    #     return [d.name for d in path.iterdir() if d.is_dir()]

    def update_category_dropdown(self, campaign_name: str):
        """Update the category dropdown based on the selected campaign.

        Args:
            campaign_name (str): The name of the campaign.

        Example:
            >>> self.update_category_dropdown("SummerSale")
        """

        campaign_path = self.campaigns_directory / campaign_name / "category"
        campaign_categories = get_directory_names(campaign_path)
        self.category_name_dropdown.options = campaign_categories

    def on_campaign_name_change(self, change: dict[str, str]):
        """Handle changes in the campaign name dropdown.

        Args:
            change (dict[str, str]): The change dictionary containing the new value.

        Example:
            >>> self.on_campaign_name_change({'new': 'SummerSale'})
        """
        self.campaign_name = change["new"]
        self.update_category_dropdown(self.campaign_name)
        self.initialize_campaign_editor(None)  # Reinitialize with newcampaign

    def on_category_change(self, change: dict[str, str]):
        """Handle changes in the category dropdown.

        Args:
            change (dict[str, str]): The change dictionary containing the new value.

        Example:
            >>> self.on_category_change({'new': 'Electronics'})
        """
        self.category_name = change["new"]
        self.initialize_campaign_editor(None)  # Reinitialize with new category
        
    def on_language_change(self, change: dict[str, str]):
        """Handle changes in the language dropdown.

        Args:
            change (dict[str, str]): The change dictionary containing the new value.

        Example:
            >>> self.on_language_change({'new': 'EN USD'})
        """
        self.language, self.currency = change["new"].split()
        self.initialize_campaign_editor(None)  # Reinitialize with new language/currency

    def save_campaign(self, _):
        """Save the campaign and its categories.

        Args:
            _: Unused argument, required for button callback.

        Example:
            >>> self.save_campaign(None)
        """
        self.campaign_name = self.campaign_name_dropdown.value
        self.category_name = self.category_name_dropdown.value
        self.language, self.currency = self.language_dropdown.value.split()

        if self.campaign_name and self.language:
            self.campaign_editor = AliCampaignEditor(
                campaign_name=self.campaign_name,
                category_name=self.category_name if self.category_name else None,
                language=self.language,
            )
            try:
                self.campaign_editor.save_categories_from_worksheet()
            except Exception as ex:
                logger.error("Error saving campaign.", ex, True)
        else:
            logger.warning (
                "Please select campaign name and language/currency before saving the campaign."
            )

    def show_products(self, _):
        """Display the products in the selected category.

        Args:
            _: Unused argument, required for button callback.

        Example:
            >>> self.show_products(None)
        """
        campaign_name = self.campaign_name_dropdown.value
        category_name = self.category_name_dropdown.value

        try:
            self.campaign_editor = AliCampaignEditor(
                campaign_name=campaign_name,
                language=self.language,
                currency=self.currency,
            )
            self.campaign_editor.set_products_worksheet(category_name)
        except Exception as ex:
            logger.error("Error displaying products.", ex, True)

    def open_spreadsheet(self, _):
        """Open the Google Spreadsheet in a browser.

        Args:
            _: Unused argument, required for button callback.

        Example:
            >>> self.open_spreadsheet(None)
        """
        if self.campaign_editor:
            spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{self.campaign_editor.spreadsheet_id}/edit"
            webbrowser.open(spreadsheet_url)
        else:
            print("Please initialize the campaign editor first.")

    def setup_callbacks(self):
        """Set up callbacks for the widgets."""
        self.campaign_name_dropdown.observe(self.on_campaign_name_change, names="value")
        self.category_name_dropdown.observe(self.on_category_change, names="value")
        self.language_dropdown.observe(self.on_language_change, names="value")
        self.initialize_button.on_click(self.initialize_campaign_editor)
        self.save_button.on_click(self.save_campaign)
        self.show_products_button.on_click(self.show_products)
        self.open_spreadsheet_button.on_click(self.open_spreadsheet)

    def display_widgets(self):
        """Display the widgets for interaction in the Jupyter notebook.

        Initializes the campaign editor automatically with the first campaign selected.

        Example:
            >>> self.display_widgets()
        """
        display(
            self.campaign_name_dropdown,
            self.category_name_dropdown,
            self.language_dropdown,
            self.initialize_button,
            self.save_button,
            self.show_products_button,
            self.open_spreadsheet_button,
        )
        # Initialize the campaign editor with the first campaign selected
        self.initialize_campaign_editor(None)
