KSP Scenario Configuration
=========================

This file configures the KSP scenario, specifying details for data collection.


.. code-block:: json
   :linenos:

   ```json
   {
     "supplier_id": "2787",
     "supplier": "KSP",
     "supplier_prefix": "ksp",
     "start_url": "https://www.ksp.co.il/",
     "price_rule": "+100",
     "if_list":"first","use_mouse": false, "mandatory": true,
     "num_items_4_flush": 300,
     "if_login": false,
     "parcing method [webdriver|api]": "web",
     "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
     "collect_products_from_categorypage": false,
     "scenario_files": [
       # ... (list of scenario files) ...
     ],
     "excluded": [
       # ... (list of excluded files) ...
     ],
     "last_runned_scenario": "ksp_categories_phones_apple.json"
   }
   ```

Scenario Files
-------------

This section lists the included scenario files for data collection.

.. toctree::
   :maxdepth: 2

   ksp_categories_aio_lenovo.rst
   ksp_categories_headphones_jbl.rst
   ksp_categories_headphones_msi.rst
   ksp_categories_headphones_razer.rst
   ksp_categories_headphones_sony.rst
   ksp_categories_headphones_xiaomi.rst
   ksp_categories_monitors_lenovo.rst
   ksp_categories_monitors_lg.rst
   ksp_categories_monitors_samsung.rst
   ksp_categories_motherboards_msi.rst
   ksp_categories_phones_apple.rst
   ksp_categories_phones_asus.rst
   ksp_categories_phones_google.rst
   ksp_categories_phones_nokia.rst
   ksp_categories_phones_oneplus.rst
   ksp_categories_phones_samsung.rst
   ksp_categories_aio_imacs.rst
   ksp_categories_consoles_microsoft.rst
   ksp_categories_consoles_nintendo.rst
   ksp_categories_headphones_bang_olufsen.rst
   ksp_categories_headphones_hyperx.rst
   ksp_categories_headphones_ipods.rst
   ksp_categories_notebooks_hp_by_model.rst
   ksp_categories_phones_oppo.rst
   ksp_categories_notebooks_dell_by_model.rst


Excluded Files
-------------

This section lists the excluded scenario files.

.. toctree::
   :maxdepth: 2
   
   # Note:  Excluded files are not documented here.  (This section may need filling depending on use case)



Last Runned Scenario
-------------------

The last runned scenario is specified here.

.. automodule:: scenario.ksp
   :members:
   :undoc-members:
   :show-inheritance: