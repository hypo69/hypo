```
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
... (same as in the original code)


```

```algorithm
**Step 1: Input Processing**
* Input: JSON array of component data.
* Action: Extract product_id, product_title, product_description, and image_path from each JSON object.

**Step 2: Build Type Determination**
* Input: Component data (e.g., CPU, GPU, RAM).
* Action: Evaluate components and assign weights to build types (gaming, workstation, etc.). Use pre-defined rules or a machine learning model to predict the most suitable build type, with confidence scores.

**Step 3: Title and Description Generation**
* Input: Determined build type and component details.
* Action: Based on the build type, generate titles and descriptions in Hebrew and Russian. Consider component specifications to craft tailored text.


**Step 4: Translation**
* Input: Component titles and descriptions.
* Action: Translate component names and descriptions into Hebrew and Russian.  Use appropriate translation services or a language model for accurate translation.

**Step 5: Output Formatting**
* Input: Translated titles, descriptions, component details, and build type scores.
* Action: Format the final output as a JSON object, adhering to the specified structure with Hebrew and Russian sections, including build type probabilities, titles, descriptions, and translated component data.



```explanation
**Imports:** There are no imports in this code snippet.  The code describes a prompt for a large language model (LLM) like Gemini.  The structure defines the expected input (JSON array), the expected output (JSON object), and instructions for handling tasks like determining build type, generating descriptions, and performing translations.  This is not a runnable code block, but a set of instructions for the LLM itself.

**Classes:** No classes are defined. This is a prompt; it describes desired functionality using language rather than object-oriented structures.

**Functions:** No functions are defined. This is a prompt defining how the LLM should perform a set of tasks. The LLM itself will be performing functions.

**Variables:** The prompt mentions variables (e.g., product_id, product_title, build_types) as input or output data to be used by the LLM.

**Potential Errors:** The prompt is highly dependent on the quality of the underlying LLM's ability to translate, generate text, and perform reasoning tasks. Problems might arise from:
* **Inaccurate translations:** Poor quality translation services or inappropriate language models could produce inaccurate translations.
* **Inconsistent component data:** If component data is poorly structured or missing information, the LLM's understanding will be limited.
* **Ambiguous component combinations:** A build with unusual component combinations may require specialized knowledge that the LLM may not possess.
* **Computational cost:** Processing large datasets and performing complex translations will require computational resources.


**Relationship with other parts of the project:** The prompt is the initial step in a pipeline for generating computer build descriptions. Following steps would need to process data from a component database (JSON data), process results in a particular format (JSON output), and possibly store the output (database, file).


**Overall:** The prompt is focused on defining the tasks and expected output, relying on an external LLM (Gemini in this case) to execute the required logic.  It's a well-defined prompt for a powerful language model, but does not contain runnable code itself.