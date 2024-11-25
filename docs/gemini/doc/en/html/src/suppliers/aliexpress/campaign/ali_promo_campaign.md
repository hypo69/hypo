html
<h1>AliPromoCampaign Module</h1>

<h2>Overview</h2>
<p>This module provides functionality for managing advertising campaigns on AliExpress. It handles data processing for categories and products, creates and edits JSON files with campaign information, and utilizes AI for campaign data generation.</p>

<h2>Classes</h2>

<h3><code>AliPromoCampaign</code></h3>

<p><strong>Description</strong>: Manages an advertising campaign.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>language</code> (str): Language of the campaign.  Default: <code>None</code>.</li>
  <li><code>currency</code> (str): Currency of the campaign. Default: <code>None</code>.</li>
  <li><code>base_path</code> (Path): Base path for campaign files. Default: <code>None</code>.</li>
  <li><code>campaign_name</code> (str): Name of the campaign. Default: <code>None</code>.</li>
  <li><code>campaign</code> (SimpleNamespace): Campaign data (loaded from JSON). Default: <code>None</code>.</li>
  <li><code>campaign_ai</code> (SimpleNamespace): AI-generated campaign data. Default: <code>None</code>.</li>
  <li><code>gemini</code> (GoogleGenerativeAI): Instance of the Gemini AI model. Default: <code>None</code>.</li>
  <li><code>openai</code> (OpenAIModel): Instance of the OpenAI model. Default: <code>None</code>.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(campaign_name: str, language: Optional[str] = None, currency: Optional[str] = None, model:str = 'openai')</code>: Initializes an <code>AliPromoCampaign</code> object.
    <ul>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>campaign_name</code> (str): Name of the campaign.</li>
          <li><code>language</code> (Optional[str], optional): Language of the campaign. Defaults to <code>None</code>.</li>
          <li><code>currency</code> (Optional[str], optional): Currency of the campaign. Defaults to <code>None</code>.</li>
		  <li><code>model</code> (str, optional): AI model to use ('openai' or 'gemini'). Defaults to 'openai'.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>:
        <ul>
          <li><code>SimpleNamespace</code>: An object representing the campaign data.</li>
        </ul>
      </li>
      <li><strong>Example</strong>:
        <code>campaign = AliPromoCampaign(campaign_name="SummerSale", language="EN", currency="USD")</code></li>
	</ul>
  </li>
  <li><code>process_campaign()</code>: Iterates through campaign categories and processes products using affiliate product generators.</li>
  <li><code>process_category_products(category_name: str) -> Optional[List[SimpleNamespace]]</code>: Processes products within a specific category.
    <ul>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>category_name</code> (str): The name of the category.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>:
        <ul>
          <li><code>Optional[List[SimpleNamespace]]</code>: A list of products in the category.  Returns <code>None</code> if no products are found.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><code>process_ai_category(category_name: Optional[str] = None)</code>: Processes AI-generated data for a category.
    <ul>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>category_name</code> (Optional[str], optional): The category name. Defaults to <code>None</code> (processes all categories).</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><code>process_new_campaign(campaign_name: str, language: Optional[str] = None, currency: Optional[str] = None)</code>: Creates a new campaign.
    <ul>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>campaign_name</code> (str): Name of the campaign.</li>
          <li><code>language</code> (Optional[str], optional): Language of the campaign. Defaults to <code>None</code>.</li>
          <li><code>currency</code> (Optional[str], optional): Currency of the campaign. Defaults to <code>None</code>.</li>
        </ul>
      </li>
	  <li><strong>Returns</strong>: List of tuples with category names and their processed results (can be None).</li>
    </ul>
  </li>
  <li><code>set_categories_from_directories()</code>: Sets campaign categories from directory names.</li>
    <li><code>generate_output(campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace)</code>: Saves product data in various formats.
    <ul>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>campaign_name</code> (str): The name of the campaign.</li>
          <li><code>category_path</code> (str | Path): The path to save the output files.</li>
          <li><code>products_list</code> (list[SimpleNamespace] | SimpleNamespace): List or single product to save.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>: <code>None</code></li>
    </ul>
  </li>
  <li><code>generate_html_for_campaign(campaign_name: str)</code>: Generates HTML pages for the campaign.</li>
</ul>

<h2>Functions</h2>


<!-- Add function documentation here as needed -->

```