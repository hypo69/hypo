rst
How to use the Google Search HTML Parser
========================================================================================

Description
-------------------------
This Python code defines a class `GoogleHtmlParser` for parsing HTML content from a Google Search results page.  The parser extracts various information, including estimated search results, featured snippets, knowledge cards, organic search results, and data from scrolling sections (e.g., top stories). It handles both mobile and desktop versions of the HTML.


Execution steps
-------------------------
1. **Import necessary libraries**: The code imports the `lxml` library for HTML parsing.

2. **Define the `GoogleHtmlParser` class**: This class encapsulates the parsing logic.

3. **Initialize the parser**:  The `__init__` method creates an `lxml` HTML tree (`self.tree`) from the input HTML string (`html_str`). It also accepts an optional `user_agent` parameter to specify whether to parse mobile or desktop HTML. If the user agent is invalid, it defaults to 'desktop'.

4. **Implement helper functions**: Functions like `_clean`, `_normalize_dict_key` prepare data for better handling (removing extra whitespace, normalizing keys).

5. **Extract estimated results**: The `_get_estimated_results` function retrieves the total number of search results.  It uses `xpath` to locate the relevant text element.

6. **Extract organic results**: The `_get_organic` function parses the organic results from the page. It iterates through the relevant HTML elements (`div[@class="g"]`) to extract information like URL, title, snippets, and potentially rich snippets.

7. **Extract featured snippet**: The `_get_featured_snippet` function searches for the featured snippet. It returns a dictionary with the title and URL of the featured snippet if found, otherwise returns `None`.

8. **Extract knowledge card**: The `_get_knowledge_card` function parses a knowledge card if present.  It extracts the title, subtitle, description, and more information into a structured dictionary.

9. **Extract scrolling sections**: The `_get_scrolling_sections` function parses potentially scrolling sections like top stories or tweets. It returns a list of dictionaries, where each dictionary represents a section with its title and data.

10. **Get the final data**: The `get_data` function combines the results from the previous steps into a single dictionary. This function differentiates between desktop and mobile user agents.

11. **Return the parsed data**: The function returns a dictionary containing the extracted data.


Usage example
-------------------------
.. code-block:: python

    import requests
    from lxml import html
    from hypotez.src.goog.google_search import GoogleHtmlParser

    # Replace with your search query
    search_query = "python programming"

    # Example of constructing the URL for the Google search page.
    # Adjust as needed based on your search logic.
    url = f"https://www.google.com/search?q={search_query}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        html_content = response.text
        parser = GoogleHtmlParser(html_content)
        parsed_data = parser.get_data()

        print(parsed_data)


    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")