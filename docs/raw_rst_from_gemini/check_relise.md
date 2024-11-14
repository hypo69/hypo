```rst
.. automodule:: check_relise
   :members:

.. automodule:: hypotez.src.check_relise
   :members:

.. autofunction:: check_latest_release
   :noindex:
   :show-inheritance:

   :param owner: The owner of the repository.
   :type owner: str
   :param repo: The name of the repository.
   :type repo: str

   :returns: The latest release version if available, else None.
   :rtype: str
   :raises requests.exceptions.RequestException: An error occurred during the request.
   :raises ValueError: The JSON response could not be parsed.
```
