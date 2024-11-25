html
<h1>Module Name: Assembling a Computer</h1>

<h2>Overview</h2>
<p>This module provides a framework for assembling a computer, including classifying the build type, generating descriptions in Hebrew and Russian, translating component names, and preserving original specifications.  It handles missing data gracefully and includes a phone number for service inquiries.</p>

<h2>Functions</h2>

<h3><code>determine_build_type</code></h3>

<p><strong>Description</strong>: This function analyzes the provided components to determine the most suitable build type. It returns a dictionary containing build types with associated confidence scores.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>components</code> (list of dict): A list of dictionaries, each representing a computer component with 'product_title', 'product_description', and other relevant information.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: A dictionary containing build types (e.g., 'gaming', 'workstation') with corresponding confidence scores (e.g., 0.9 for 'gaming').</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>TypeError</code>: If input is not a list of dictionaries.</li>
  <li><code>ValueError</code>: If any component dictionary lacks necessary fields.</li>
</ul>


<h3><code>generate_build_description</code></h3>

<p><strong>Description</strong>: This function generates a detailed description of the computer build, tailored to the highest-confidence build type, in both Hebrew and Russian.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>components</code> (list of dict): A list of dictionaries, each representing a computer component.</li>
  <li><code>build_types</code> (dict): A dictionary containing build types and their confidence scores.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict</code>: A JSON-formatted dictionary containing the build's title, description, and translated component information in Hebrew and Russian, including component specifications.  Includes phone number.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>TypeError</code>: If input data types are inconsistent.</li>
  <li><code>ValueError</code>: If necessary information is missing.</li>
</ul>

<h2>Example Usage</h2>

<pre><code class="language-python">
# Example usage (replace with actual component data)
components = [
    {"product_title": "Intel i9-14900K", "product_description": "..."},
    {"product_title": "Gigabyte RTX 4060 Ti", "product_description": "..."}
]

build_types = determine_build_type(components)  # Example call
description = generate_build_description(components, build_types)

# Access the generated description in Hebrew
print(description['he']['description'])

# Access the translated component names in Russian
print(description['ru']['products'][0]['product_title'])
</code></pre>