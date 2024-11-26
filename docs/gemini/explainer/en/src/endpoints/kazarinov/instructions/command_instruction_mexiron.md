## **Prompt for Gemini AI: Assembling a Computer**

### **Prompt:**

**Role:** Computer Builder Assistant

**Task:** 
You will be provided with a JSON dictionary containing information about computer components. Based on the components, you will:

1. **Determine the build type:** Gaming, office, workstation, etc.
2. **Generate a descriptive title and detailed description** of the build in both Hebrew and Russian.
3. **Translate component names** into Hebrew and Russian.
4. **Return a JSON response** with the translated and described build.
5. **Ensure correct quotation marks** in the output.


**Input format:** JSON
**Example:**
```json
[
  {
    "product_id": "<leave as is>",
    "product_title": "<component name>",
    "product_description": "<description and specs>",
    "image_local_saved_path": "<leave as is>"
  },
  {
    "product_id": "<leave as is>",
    "product_title": "<component name>",
    "product_description": "<description and specs>",
    "image_local_saved_path": "<leave as is>"
  }
]
```


**Output format:**
```json
{
  "he": {
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "title": "️ <Your build title>",
    "description": " <Your build description>",
    // ... rest of the structure
  },
  "ru": {
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "title": "️ <Your build title>",
    "description": " <Your build description>",
    "products": [
      {
        "product_id": "<product_id>",
        "product_title": "<Hebrew component name>",
        "product_description": "<Hebrew component description>",
        "image_local_saved_path": "<leave as is>",
        "language": "he"
      },
      ...
    ]
  }
}
```

**Additional notes:**
(Same as before)


**Example:**
(Same as before)

**Key considerations for the model:**
(Same as before)


## <algorithm>

The algorithm is implied within the prompt and examples, rather than explicitly coded. The workflow is:

1. **Input:** Receive a JSON array of component data (product_id, product_title, product_description).
2. **Build Type Classification:** Analyze the components to determine the most likely build type (gaming, workstation, etc.), assigning confidence scores to each possibility.  This is done based on the presence and specifications of high-end components like GPUs, CPUs, RAM, and cooling systems.
3. **Description Generation:** Generate a descriptive title and a detailed description of the build tailored to the highest-confidence build type, including translations into Hebrew and Russian.
4. **Translation:** Translate component names to Hebrew and Russian.
5. **Output:** Return a JSON response containing the build type classifications, titles, descriptions, and translated components.


## <explanation>

* **Imports:** There are no imports.  This is a description of a prompt engineering task, not a runnable code.
* **Classes:** No classes are defined. This is a natural language description for a desired function.
* **Functions:**  There are no functions in the provided text. The desired behavior is expressed within natural language descriptions and examples.
* **Variables:** No variables are defined in the prompt.
* **Potential Errors/Improvements:** 
    * **Data Validation:** The prompt lacks a mechanism for handling malformed or incomplete JSON input,  potentially leading to errors or unexpected behavior.  Robust error handling and validation is crucial.
    * **Scalability:** The prompt needs to be adaptable for a large number of components and variations in build types. A proper implementation would need a larger and more structured database of component specifications and their associated build types to achieve accuracy and avoid biases.
    * **Weighting Algorithm:** The prompt suggests component weighting; a precise method for calculating weights should be defined for a well-structured implementation.  A poorly defined weighting scheme might result in incorrect build classification.
    * **Translation Accuracy:** While the prompt emphasizes accurate translation, the details of how translation is performed are not provided.  Integrating a robust translation API (e.g., Google Translate, DeepL) will significantly improve the output quality.


**Relationships with other parts of the project:**

The prompt describes a specific part of a larger system: a computer building tool. The output of this component would likely feed into other parts of the project that handle the ordering, pricing, and potentially the actual assembly of the computer. The necessary data about components (specifications, images, etc.)  likely comes from an external source and would need to be integrated.

**Note:** The code provided is a description of a *task*, not a snippet of executable code.  It outlines the desired behaviour of a hypothetical AI assistant.