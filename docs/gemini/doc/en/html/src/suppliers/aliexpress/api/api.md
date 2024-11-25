html
<h1>AliexpressApi Module</h1>

<h2>Overview</h2>
<p>This module provides a Python wrapper for the AliExpress Open Platform API, enabling easier access to product information and affiliate links.</p>

<h2>Classes</h2>

<h3><code>AliexpressApi</code></h3>

<p><strong>Description</strong>: Provides methods to interact with the AliExpress API using your API credentials.</p>

<p><strong>Constructor</strong>:</p>

<pre><code class="language-python">def __init__(self,
        key: str,
        secret: str,
        language: model_Language,
        currency: model_Currency,
        tracking_id: str = None,
        app_signature: str = None,
        **kwargs):
    """
    Args:
        key (str): Your API key.
        secret (str): Your API secret.
        language (str): Language code. Defaults to EN.
        currency (str): Currency code. Defaults to USD.
        tracking_id (str, optional): The tracking ID for link generation. Defaults to None.
        app_signature (str, optional): App signature. Defaults to None.
    """
</code></pre>


<p><strong>Methods</strong>:</p>
<ul>
  <li><code>retrieve_product_details</code>: Get product information.</li>
  <li><code>get_affiliate_links</code>: Generate affiliate links.</li>
  <li><code>get_hotproducts</code>: Search for affiliated products with high commission.</li>
  <li><code>get_categories</code>: Get all available categories (parent and child).</li>
  <li><code>get_parent_categories</code>: Get all available parent categories.</li>
  <li><code>get_child_categories</code>: Get child categories for a specific parent category.</li>
</ul>


<h3><code>retrieve_product_details</code></h3>

<pre><code class="language-python">def retrieve_product_details(self,
        product_ids: str | list,
        fields: str | list = None,
        country: str = None,
        **kwargs) -> List[model_Product]:
    """
    Get products information.

    Args:
        product_ids (str | list[str]): One or more links or product IDs.
        fields (str | list[str], optional): The fields to include in the results. Defaults to all.
        country (str, optional): Filter products that can be sent to that country. Returns the price
            according to the country's tax rate policy.

    Returns:
        list[model_Product]: A list of products.

    Raises:
        ProductsNotFoudException: No products found.
        InvalidArgumentException: Invalid input arguments.
        ApiRequestException: An error occurred during the API request.
        ApiRequestResponseException: An error occurred in the API response.
    """
</code></pre>

<h3><code>get_affiliate_links</code></h3>

<pre><code class="language-python">def get_affiliate_links(self,
        links: str | list,
        link_type: model_LinkType = model_LinkType.NORMAL,
        **kwargs) -> List[model_AffiliateLink]:
    """
    Converts a list of links into affiliate links.

    Args:
        links (str | list[str]): One or more links to convert.
        link_type (model_LinkType, optional): Choose between normal link with standard commission or hot link with hot product commission. Defaults to NORMAL.

    Returns:
        list[model_AffiliateLink]: A list containing the affiliate links.

    Raises:
        InvalidArgumentException: Invalid input arguments.
        InvalidTrackingIdException: Tracking ID is missing.
        ProductsNotFoudException: Affiliate links not available.
        ApiRequestException: An error occurred during the API request.
        ApiRequestResponseException: An error occurred in the API response.
    """
</code></pre>


<!-- ... (Other method documentation) ... -->

<h2>Functions</h2>

<!-- ... (Function documentation if any) ... -->

<h2>Exceptions</h2>

<!-- ... (Exception definitions if any) ... -->


<h2>Models</h2>
<!-- ... (Include documentation for models like model_AffiliateLink, model_Category etc) ... -->