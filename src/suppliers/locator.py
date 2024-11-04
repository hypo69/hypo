## \file ../src/suppliers/locator.py
from types import SimpleNamespace
from src import gs
from src.utils.jjson import j_loads_ns

class Locator:
    """Class for representing a locator with various selection attributes.

    Attributes:
        supplier_prefix (str): The prefix identifying the supplier's folder
            where locator configuration files are stored.
        locator (SimpleNamespace): Namespace containing locator definitions 
            loaded from a JSON file, providing easy access to each locator attribute.
    """

    def __init__(self, supplier_prefix: str):
        """Initializes the Locator instance by loading settings from a JSON file
        based on the supplier prefix.

        Args:
            supplier_prefix (str): Prefix identifying the supplier's folder.

        Raises:
            FileNotFoundError: If the JSON file with locator definitions is not found.
            ValueError: If the JSON content is invalid.
        """
        self.supplier_prefix = supplier_prefix
        self.locator = self._load_locator()

    def _load_locator(self) -> SimpleNamespace:
        """Loads locator settings from a JSON file based on the supplier prefix."""
        locators_path = gs.path.src / 'suppliers' / self.supplier_prefix / 'locators' / 'product.json'
        try:
            return j_loads_ns(locators_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Locator file not found: {locators_path}")
        except ValueError as e:
            raise ValueError(f"Invalid JSON format in {locators_path}: {e}")
