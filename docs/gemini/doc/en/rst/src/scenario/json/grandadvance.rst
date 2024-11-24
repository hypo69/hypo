grandadvance Scenario Configuration
==================================

This file configures the grandadvance scenario for data extraction.  It specifies the supplier, URLs, price rules, and other parameters for the scraping process.

.. code-block:: json
    :linenos:

    {
      "supplier": "grandadvance",
      "supplier_prefix": "GRD-",
      "start_url": "https://www.grandadvance.co.il/",
      "login_url": "https://www.grandadvance.co.il/",
      "price_rule": "*1.43",
      "if_list":"first","use_mouse": false, "mandatory": true,
      "num_items_4_flush": 50,
      "if_login": true,
      "scenario_files": [
        [ "grandadvance_categories_keyboards_logitech.json" ],
        [
          "grandadvance_categories_laptops_acer.json",
          "grandadvance_categories_laptops_lenovo.json",
          "grandadvance_categories_laptops_hp.json",
          "grandadvance_categories_laptops_dell.json"
        ],
        [ "grandadvance_categories_video_nvidia.json" ]
      ],
      "last_runned_scenario": ""
    }

Scenario Files
-------------

This section details the sub-scenarios for different product categories.

.. toctree::
   :maxdepth: 2

   grandadvance_categories_keyboards_logitech.rst
   grandadvance_categories_laptops_acer.rst
   grandadvance_categories_laptops_lenovo.rst
   grandadvance_categories_laptops_hp.rst
   grandadvance_categories_laptops_dell.rst
   grandadvance_categories_video_nvidia.rst