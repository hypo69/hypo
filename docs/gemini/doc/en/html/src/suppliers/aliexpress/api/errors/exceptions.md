html
<h1>hypotez/src/suppliers/aliexpress/api/errors/exceptions.py</h1>

<h2>Overview</h2>
<p>This module defines custom exception classes for handling errors that may occur when interacting with the AliExpress API.</p>

<h2>Classes</h2>

<h3><code>AliexpressException</code></h3>

<p><strong>Description</strong>: Common base class for all AliExpress API exceptions.</p>

<p><strong>Constructor</strong>:</p>

<pre><code>python
def __init__(self, reason: str):
    """
    Args:
        reason (str): The reason for the exception.
    """
    super().__init__()
    self.reason = reason
</code></pre>

<p><strong>String Representation</strong>:</p>

<pre><code>python
def __str__(self) -> str:
    """
    Returns:
        str: The string representation of the exception, including the reason.
    """
    return \'%s\' % self.reason
</code></pre>


<h3><code>InvalidArgumentException</code></h3>

<p><strong>Description</strong>: Raised when arguments passed to a function are not valid.</p>

<p><strong>Inherits from</strong>: <code>AliexpressException</code></p>


<h3><code>ProductIdNotFoundException</code></h3>

<p><strong>Description</strong>: Raised if the specified product ID cannot be found.</p>

<p><strong>Inherits from</strong>: <code>AliexpressException</code></p>


<h3><code>ApiRequestException</code></h3>

<p><strong>Description</strong>: Raised if there is an error during the API request process.</p>

<p><strong>Inherits from</strong>: <code>AliexpressException</code></p>


<h3><code>ApiRequestResponseException</code></h3>

<p><strong>Description</strong>: Raised if the response from the AliExpress API is invalid.</p>

<p><strong>Inherits from</strong>: <code>AliexpressException</code></p>


<h3><code>ProductsNotFoudException</code></h3>

<p><strong>Description</strong>: Raised if no products are found matching the query criteria.</p>

<p><strong>Inherits from</strong>: <code>AliexpressException</code></p>


<h3><code>CategoriesNotFoudException</code></h3>

<p><strong>Description</strong>: Raised if no categories are found matching the query criteria.</p>

<p><strong>Inherits from</strong>: <code>AliexpressException</code></p>


<h3><code>InvalidTrackingIdException</code></h3>

<p><strong>Description</strong>: Raised if the provided tracking ID is invalid or missing.</p>

<p><strong>Inherits from</strong>: <code>AliexpressException</code></p>