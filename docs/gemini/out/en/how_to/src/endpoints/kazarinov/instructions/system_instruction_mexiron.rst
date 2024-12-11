How to use this code block
=========================================================================================

Description
-------------------------
This code block defines a prompt for a Gemini AI model to assemble a computer. It specifies the input format (JSON array of component dictionaries), the output format (JSON with Hebrew and Russian translations), and detailed instructions for the model regarding build classification, terminology, missing data, and output formatting.  It includes examples of input and output data, along with crucial instructions for component categorization, terminology precision, and handling missing data. The prompt also includes specific details about build classification, translation requirements, and a sample use case.  The goal is to produce a detailed computer build description in both Hebrew and Russian.

Execution steps
-------------------------
1. **Understand the Input Format:** The input consists of a JSON array, each object representing a computer component with `product_id`, `product_title`, `product_description`, and `image_local_saved_path`.  The example input shows the structure.

2. **Process the Input Data:**  Parse the JSON array of components. Extract relevant information about each component (e.g., processor type, GPU model).

3. **Classify the Build:** Based on the components, determine the build type (e.g., gaming, office, workstation).  Assign probabilities to build types as demonStarted in the example output.

4. **Generate Titles and Descriptions:** Create a title and detailed description for the build in both Hebrew and Russian. Use accurate and contextually appropriate terminology.

5. **Translate Components:** Translate the `product_title` and `product_description` of each component into both Hebrew and Russian.

6. **Format the Output:** Structure the output as a JSON object with "he" (Hebrew) and "ru" (Russian) keys.  Each key will contain a JSON object with `title`, `description`, `build_types`, and `products` fields.  The `products` field will be an array, each object containing the original `product_id`, the translated `product_title`, translated `product_description`, and other relevant fields.  Ensure consistent formatting with correct quotation marks.

7. **Handle Missing Data:** If any information is incomplete, fill in the best you can or indicate missing data with appropriate placeholders.

8. **Apply Instructions:** Follow all instructions within the prompt, including component categorization, precision, and formatting requirements.

Usage example
-------------------------
```python
# Example input (replace with your actual input data)
input_data = [
    {"product_id": "123", "product_title": "Intel i9-14900K", "product_description": "High-end processor"},
    {"product_id": "456", "product_title": "NVIDIA RTX 4060 Ti", "product_description": "High-performance graphics card"}
]


# This is where your code to process the input and generate the output would go
# ... (your code to process the input_data and create the JSON output)
# Example output (replace with your actual output data)
output_data = {
    "he": {
        "title": "מחשב גיימינג בעל ביצועים גבוהים",
        "description": "מחשב מודרני למשחקים ותוכנות תובעניים.",
        "build_types": {"gaming": 0.9, "workstation": 0.1},
        "products": [
            {"product_id": "123", "product_title": "Intel i9-14900K (מעבד אינטל)", "product_description": "מעבד מתקדם", "image_local_saved_path": "path/to/image", "language": "he"},
            {"product_id": "456", "product_title": "NVIDIA RTX 4060 Ti (כרטיס מסך)", "product_description": "כרטיס מסך בעל ביצועים גבוהים", "image_local_saved_path": "path/to/image", "language": "he"}
        ]
    },
    "ru": {
        "title": "Высокопроизводительный игровой компьютер",
        "description": "Современный компьютер для требовательных игр и приложений.",
        "build_types": {"gaming": 0.9, "workstation": 0.1},
        "products": [
            {"product_id": "123", "product_title": "Intel i9-14900K (процессор Intel)", "product_description": "Высокопроизводительный процессор", "image_local_saved_path": "path/to/image", "language": "ru"},
            {"product_id": "456", "product_title": "NVIDIA RTX 4060 Ti (видеокарта)", "product_description": "Видеокарта с высокой производительностью", "image_local_saved_path": "path/to/image", "language": "ru"}
        ]
    }
}

# Print the output (for demonStartion)
import json
print(json.dumps(output_data, indent=2, ensure_ascii=False))
```