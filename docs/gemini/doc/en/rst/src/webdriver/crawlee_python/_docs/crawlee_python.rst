Crawlee Python
==============

.. automodule:: crawlee_python
    :members:
    :undoc-members:
    :show-inheritance:

Functions
--------

.. autofunction:: crawlee_python.CrawleePython.__init__
.. autofunction:: crawlee_python.CrawleePython.setup_crawler
.. autofunction:: crawlee_python.CrawleePython.run_crawler
.. autofunction:: crawlee_python.CrawleePython.export_data
.. autofunction:: crawlee_python.CrawleePython.get_data
.. autofunction:: crawlee_python.CrawleePython.run


Example Usage
------------

.. code-block:: python
    import asyncio
    from crawlee_python import CrawleePython

    async def main():
        crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium')
        await crawler.setup_crawler()
        await crawler.run_crawler(['https://news.ycombinator.com/'])
        crawler.export_data('data.json')
        data = crawler.get_data()
        print(data)

    asyncio.run(main())