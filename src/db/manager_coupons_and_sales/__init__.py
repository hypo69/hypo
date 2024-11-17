

""" Менеджер скидок, купонов и т.п. в PrestaShop  """
...

...
from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .product_group_reduction_cache_manager import ProductGroupReductionCacheManager
from .product_campaigns import ProductCampaignsManager