rst
How to use the `extract_conversations_from_html` function
====================================================================================================

Description
-------------------------
This Python code defines a function `extract_conversations_from_html` that extracts conversation elements from an HTML file.  It uses the `BeautifulSoup` library to parse the HTML and yields each `div` element with the class "conversation".

Execution steps
-------------------------
1. **Import necessary libraries:** The code imports the `BeautifulSoup` library for parsing HTML and the `Path` object from the `pathlib` module for working with file paths. It also imports the `gs` module (presumably for file path handling), and `header` (likely for other configuration or imports).

2. **Define the `extract_conversations_from_html` function:** This function takes a `Path` object representing the HTML file path as input.

3. **Open the HTML file:** The function opens the specified HTML file in read mode ('r') with UTF-8 encoding.

4. **Parse the HTML:** It uses `BeautifulSoup` to parse the HTML content from the opened file.

5. **Find conversation elements:** It searches for all `div` elements with the class 'conversation' within the parsed HTML.

6. **Yield conversation elements:** The function iterates through the found conversation elements and yields each one.  This allows for processing each conversation element individually without loading the entire file into memory at once.


7. **Example usage (demonstration):** The code provides an example of how to use the function to process a specific HTML file (`chat.html`) located within a data directory.


Usage example
-------------------------
.. code-block:: python

    import header
    from src import gs
    from pathlib import Path
    from bs4 import BeautifulSoup

    def extract_conversations_from_html(file_path: Path):
        with file_path.open('r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            conversations = soup.find_all('div', class_='conversation')
        for conversation in conversations:
            yield conversation

    # Example usage
    file_path = Path(gs.path.data / 'chat_gpt' / 'chat.html')
    for conversation in extract_conversations_from_html(file_path):
        print(conversation.prettify())