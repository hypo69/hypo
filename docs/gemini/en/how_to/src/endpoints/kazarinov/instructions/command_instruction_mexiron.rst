rst
How to use this code block
=========================================================================================

Description
-------------------------
This code block defines instructions for a function that analyzes computer components from JSON data, categorizes the build type (e.g., gaming, workstation), generates titles and descriptions in Hebrew and Russian, translates component details, and returns structured JSON output.  It emphasizes accurate formatting, confidence scores, and adherence to detailed guidelines for descriptions and component handling.


Execution steps
-------------------------
1. **Input JSON Parsing:** The function receives JSON data representing computer components as input.
2. **Component Analysis:** It extracts information about each component (CPU, GPU, RAM, storage, etc.).
3. **Build Type Classification:** It analyzes the components to determine the most likely build type (gaming, workstation, etc.), assigning a confidence score to each type.
4. **Hebrew and Russian Translation/Generation:**  It generates titles and descriptions for each component in both Hebrew and Russian. This likely involves using external translation services or pre-translated databases.  Crucially, the quality and accuracy of the translations are a critical aspect.
5. **Structured JSON Output:** The function constructs a JSON response in a specific format. This includes component details, translations, the build type classification with confidence scores, and importantly, preservation of any provided image paths.


Usage example
-------------------------
.. code-block:: python

    # Input JSON (Example)
    input_json = {
        "components": [
            {"product_id": "123", "cpu": "Intel i7-14700F", "gpu": "Gigabyte RTX 4070", "ram": "16GB DDR4"},
            {"product_id": "456", "storage": "Kingston 4TB SSD"}
        ]
    }


    # Function call (replace with actual function name)
    output_json = analyze_computer_components(input_json)

    # Print the output (example):
    import json
    print(json.dumps(output_json, indent=2, ensure_ascii=False))