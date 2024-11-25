html
<h1>Module Name</h1>

<h2>Overview</h2>
<p>This module serves as a computer builder assistant, accepting a JSON array of computer components and generating a detailed description of the resulting build, along with translations to Hebrew and Russian.</p>

<h2>Prompt</h2>

<h3>Input Format</h3>

<p>The input is a JSON array, where each object represents a computer component:</p>
<pre><code>json
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
</code></pre>


<h3>Output Format</h3>

<p>The output is a JSON object with the build's description in Hebrew and Russian:</p>
<pre><code>json
{
  "he": {
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "title": "<Your build title>",
    "description": "<Your build description>",
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
  },
  "ru": {
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "title": "<Your build title>",
    "description": "<Your build description>",
    "products": [
      {
        "product_id": "<product_id>",
        "product_title": "<Russian component name>",
        "product_description": "<Russian component description>",
        "image_local_saved_path": "<leave as is>",
        "language": "ru"
      },
      ...
    ]
  }
}
</code></pre>


<h2>Functions</h2>

<h3><code>assemble_computer</code></h3>

<p><strong>Description</strong>: Takes a JSON array of components and returns a detailed build description, translated to Hebrew and Russian, along with build type confidence scores.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>components</code> (list): A JSON array of component objects.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: A JSON object containing the build description, including titles, descriptions, translated components, and confidence scores for different build types in Hebrew and Russian.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>TypeError</code>: If input is not a list of dictionaries.</li>
  <li><code>ValueError</code>: If input dictionaries do not contain the required keys.</li>
</ul>


<h2>Additional Notes</h2>
<ul>
 <li>Component categorization and price lists are suggested for similar components.</li>
 <li>Avoid vague terms and provide precise descriptions.</li>
 <li>Always include the phone number: 054-422-94-97</li>
 <li>Preserve original specifications and handle missing data appropriately.</li>
</ul>