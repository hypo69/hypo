```rst
aliexpress API Base Module
==========================

.. automodule:: hypotez.src.suppliers.aliexpress.api.skd.api.base
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: hypotez.src.suppliers.aliexpress.api.skd.api.base.sign
   :noindex:

   Args:
       secret (str): 签名需要的密钥.
       parameters (dict | str): 支持字典和字符串两种参数类型.

   Returns:
       str: 生成的签名.

.. autofunction:: hypotez.src.suppliers.aliexpress.api.skd.api.base.mixStr
   :noindex:

   Args:
       pstr (str | bytes | object): 输入的参数.

   Returns:
       str | bytes: 编码后的参数.

Classes
-------

.. autoclass:: hypotez.src.suppliers.aliexpress.api.skd.api.base.FileItem
    :members:
    :show-inheritance:

.. autoclass:: hypotez.src.suppliers.aliexpress.api.skd.api.base.MultiPartForm
    :members:
    :show-inheritance:

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.MultiPartForm.get_content_type
       :noindex:

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.MultiPartForm.add_field
       :noindex:

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.MultiPartForm.add_file
       :noindex:

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.MultiPartForm.__str__
       :noindex:



.. autoclass:: hypotez.src.suppliers.aliexpress.api.skd.api.base.TopException
    :members:
    :show-inheritance:

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.TopException.__init__
       :noindex:

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.TopException.__str__
       :noindex:


.. autoclass:: hypotez.src.suppliers.aliexpress.api.skd.api.base.RequestException
    :members:
    :show-inheritance:


.. autoclass:: hypotez.src.suppliers.aliexpress.api.skd.api.base.RestApi
    :members:
    :undoc-members:
    :show-inheritance:

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.RestApi.__init__
       :noindex:
       Args:
           domain (str, optional): 请求的域名或IP地址. Defaults to "api-sg.aliexpress.com".
           port (int, optional): 请求的端口. Defaults to 80.

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.RestApi.get_request_header
       :noindex:

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.RestApi.set_app_info
       :noindex:

       Args:
           appinfo (object): 应用程序信息对象.

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.RestApi.getapiname
       :noindex:

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.RestApi.getMultipartParas
       :noindex:

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.RestApi.getTranslateParas
       :noindex:

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.RestApi._check_requst
       :noindex:

    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.RestApi.getResponse
       :noindex:

       Args:
           authrize (str, optional): 授权信息. Defaults to None.
           timeout (int, optional): 超时时间 (秒). Defaults to 30.

       Returns:
           dict: 返回的JSON数据.
           Raises:
               TopException:  如果请求返回错误.
               RequestException:  如果HTTP请求失败.


    .. automethod:: hypotez.src.suppliers.aliexpress.api.skd.api.base.RestApi.getApplicationParameters
       :noindex:


```
