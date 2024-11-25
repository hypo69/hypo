html
<h1>affiliated_products_generator.ru.html</h1>

<h2>Overview</h2>
<p>This file provides examples for the `affiliated_products_generator.py` module. It demonstrates how to use the `AliAffiliatedProducts` class to collect product data and process affiliate links.</p>

<h2>Classes</h2>

<h3><code>AliAffiliatedProducts</code></h3>

<p><strong>Description</strong>: A class for generating affiliate links for products on AliExpress.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>process_affiliate_products(prod_urls: list[str]) -> list[Product] | None</code>:
    <p><strong>Description</strong>: Processes a list of product URLs or IDs, retrieves affiliate links, and optionally saves images and videos.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>prod_urls</code> (list[str]): A list of product URLs or IDs to process.  </li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>list[Product] | None</code>: A list of `Product` objects with affiliate links, or `None` if processing failed. </li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>InvalidURLException</code>: If an invalid URL is provided.</li>
      <li><code>APIError</code>: If there's an error interacting with the AliExpress API.</li>
      <li><code>ImageDownloadError</code>: If there's an error downloading an image.</li>
      <li><code>VideoDownloadError</code>: If there's an error downloading a video.</li>
      <li><code>ProductNotFoundError</code>: If a product is not found.</li>

    </ul>
  </li>
</ul>


<h2>Functions</h2>

<h3><code>main</code></h3>

<p><strong>Description</strong>: The main function demonstrates the usage of the `AliAffiliatedProducts` class.</p>

<p><strong>Parameters</strong>:</p>
<ul>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
</ul>


<h2>Example Usage (example_usage.py)</h2>

<pre><code>python
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from typing import List, Optional
from src.suppliers.aliexpress.models import Product


def main():
    # Define campaign parameters
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Can be None
    language = "EN"
    currency = "USD"

    # Create an instance of AliAffiliatedProducts
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Example product URLs or IDs
    prod_urls = [
        "123",
        "https://www.aliexpress.com/item/123.html",
        "456",
        "https://www.aliexpress.com/item/456.html",
    ]

    # Process products and get a list of products with affiliate links
    products: List[Optional[Product]] = parser.process_affiliate_products(prod_urls)

    # Check results
    if products:
        print(f"Retrieved {len(products)} affiliate products.")
        for product in products:
            if product:
              print(f"Product ID: {product.product_id}")
              print(f"Affiliate link: {product.promotion_link}")
              print(f"Local image path: {product.local_saved_image}")
              if product.local_saved_video:
                  print(f"Local video path: {product.local_saved_video}")
              print()
    else:
        print("Failed to retrieve affiliate products.")


if __name__ == "__main__":
    main()
</code></pre>


<p>This example shows how to use the `AliAffiliatedProducts` class to get affiliate products.</p>

<p>This example demonstrates basic usage. Adapt it to your needs for more functionality.  Replace placeholders like `AliAffiliatedProducts` with the actual class names and method signatures from your `affiliated_products_generator.py` file.</p>