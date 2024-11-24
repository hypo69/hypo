Module hypotez/src/ai/helicone/version
=====================================

.. module:: hypotez.src.ai.helicone.version
   :platform: Windows, Unix
   :synopsis: This module defines constants related to the project's version and settings.

Variables
---------

.. autodata:: MODE
   :annotation: MODE = 'dev'

.. autodata:: __project_name__
   :annotation: __project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'


.. autodata:: __version__
   :annotation: __version__: str = settings.get("version", '') if settings else ''

.. autodata:: __doc__
   :annotation: __doc__: str = ''

.. autodata:: __details__
   :annotation: __details__: str = ''

.. autodata:: __author__
   :annotation: __author__: str = settings.get("author", '') if settings else ''

.. autodata:: __copyright__
   :annotation: __copyright__: str = settings.get("copyrihgnt", '') if settings else ''

.. autodata:: __cofee__
   :annotation: __cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"

.. autodata:: settings
   :annotation: settings:dict = None

Functions
---------

.. autofunction:: json.load