html
<h1>Module autodoc</h1>

<h2>Overview</h2>
<p>This module demonstrates the use of a decorator for automatically updating a function's docstring.  It includes the `autodoc` decorator, which updates the function's documentation string with the time of its last call.  The decorator wraps the function, updating its docstring before execution, adding a timestamp.</p>

<h2>Functions</h2>

<h3><code>autodoc</code></h3>

<p><strong>Description</strong>: A decorator that automatically updates the docstring of a function with the time of its last call.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>func</code> (function): The function to be decorated.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>wrapper</code> (function): The wrapped function with the updated docstring.</li>
</ul>


<h3><code>update_docstring</code></h3>

<p><strong>Description</strong>: Updates the docstring of a function by adding the current time to it.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>func</code> (function): The function whose docstring needs to be updated.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>None (updates the function's docstring in place).</li>
</ul>


<h3><code>example_function</code></h3>

<p><strong>Description</strong>: An example function demonstrating the use of the `autodoc` decorator.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>param1</code> (int): The first parameter.</li>
  <li><code>param2</code> (str): The second parameter.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>None</code>: The function does not explicitly return a value.</li>
</ul>


<h2>Example Usage</h2>
<p>The example demonstrates how to use the decorator and how the docstring is updated with the time of each function call.</p>
<pre><code class="python">
@autodoc
def example_function(param1: int, param2: str) -> None:
    """Пример функции.

    Args:
        param1 (int): Первое значение.
        param2 (str): Второе значение.
    """
    print(f"Processing {param1} and {param2}")

example_function(1, "test")
print(example_function.__doc__)  # Output:  ... (updated docstring)
example_function(2, "another test")
print(example_function.__doc__)  # Output: ... (updated docstring)
</code></pre>