## \file /src/suppliers/hb/_experiments/ide_experiments_fields.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.hb._experiments 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.suppliers.hb._experiments """


"""  Файл проверки наполнения полей HB -> product_fields """

import os, sys
from pathlib import Path
from typing import List, Union, Dict
from selenium.webdriver.remote.webelement import WebElement

################# добавление корневой директории позволяет мне плясать от печки ###################
dir_root: Path = Path(os.getcwd()[:os.getcwd().rfind("hypotez") + 7])
sys.path.append(str(dir_root))  # Adding the root folder to sys.path
dir_src = Path(dir_root, 'src')
sys.path.append(str(dir_root))
from src.webdriver import executor
"""  добавление корневой директории позволяет мне плясать от печки. """
####################################################################################################


from src import gs
from src.suppliers import Supplier
from src.product import Product, ProductFields

from src.logger.logger import logger, ExecuteLocatorException
from src.webdriver.driver import Driver
from src.utils import StringFormatter, StringNormalizer

# Функция grabber() собирает поля товара. Для каждого товара есть своя функия - заполнитель поля
# В этом тесте Функция вызывается к конце файла

s: Supplier = Supplier(supplier_prefix = 'hb')
p: Product = Product(s)
l: Dict = s.locators["product"]
d: Driver = s.driver
f: ProductFields = ProductFields(s)

s.current_scenario: Dict =  {
      "url": "https://hbdeadsea.co.il/product-category/bodyspa/feet-hand-treatment/",
      "name": "טיפוח כפות ידיים ורגליים",
      "condition": "new",
      "presta_categories": {
        "default_category": 11259,
        "additional_categories": []
      }
    }

d.get_url(s.current_scenario['url'])


def grab_product_page(supplier: Supplier, async_run = True) -> ProductFields :
	""" Собираю со страницы товара значения вебэлементов и привожу их к полям ProductFields
	
	@param s `Supplier` класс поставщика 
	 - вебдрайвер должен быть установлен на странице товара. 
	- в моей учетной записи я вижу линейку "Affiliate links" - я беру из нее информацию о партнерской ссылке
	 на али работает AJAX, это важно для сбора комбинаций! Они не передаются по URL
   
	"""
	
	global s
	s = supplier

	global p 
	p = Product (s)

	global f
	f = ProductFields (s)

	
	d = s.driver
	
	global l
	l = s.locators["product"]
	d.wait(5)
	d.execute_locator(l["close_banner"])	
	""" закрываю баннер """
	
	d.scroll()
	""" прокручиваю страницу товара, чтобы захватить области, которые подгружаются через AJAX """


	######################################################################################
	# 
	# 
	#			""" Функции, специфичные для конкретного  поставщика """ 
	#
	#
	#
	#	

	
	def product_reference_and_volume_and_price_for_100():
		"""  Функция вытаскивает 3 поля:
		- volume,
		- supplier_reference,
		- цена за единицу товара 
		@todo Реализовать поле `цена за единицу товара`"""
		global f,s
		webelements: List[WebElement] = d.execute_locator(l["product_reference_and_volume_and_price_for_100"])
        
		for webelement in webelements:
			if ('Fl.oz' and 'מ"ל' )	in webelement.text:
				""" объем """
				f.volume = webelement.text
			elif str(r'מחיר ל100 מ"ל') in webelement.text:
				""" цена за единицу товара
				@todo придумать куда
				"""
				print(f'цена за единицу товара:{webelement.text}')
			elif 'מקט' in webelement.text:
				f.supplier_reference = StringNormalizer.get_numbers_only(webelement.text)
			...
		...
		#
		#
		#	
		#######################################################################################

	
	def set_references(f, s):
		""" все, что касается id товара """
		#f.supplier_reference = field_supplier_reference()
		f.id_supplier = int(s.supplier_id)
		f.reference = f'{s.supplier_id}-{f.supplier_reference}'
	
	product_reference_and_volume_and_price_for_100()
	set_references(f, s)


	#f.active = field_active() # Совпадает с f.available_for_order
	#f.additional_delivery_times = field_additional_delivery_times()	# [v]  Мое поле. Нахера - не знаю
	f.additional_shipping_cost  = field_additional_shipping_cost() # [v]
	#f.advanced_stock_management = field_advanced_stock_management()
	f.affiliate_short_link =  field_affiliate_short_link() # [v]
	#f.affiliate_summary = field_affiliate_summary()
	#f.affiliate_image_large = field_affiliate_image_large()
	#f.affiliate_image_medium = field_affiliate_image_medium()
	#f.affiliate_image_small = field_affiliate_image_small()
	#f.affiliate_summary_2 = field_affiliate_summary_2()
	#f.affiliate_text = field_affiliate_text()
	#f.affiliate_image_large = field_affiliate_image_large()
	#f.affiliate_image_medium = field_affiliate_image_medium()
	#f.affiliate_image_small = field_affiliate_image_small()
	#f.available_date = field_available_date()
	f.available_for_order = f.active = field_available_for_order()
	#f.available_later = field_available_later()
	#f.available_now = field_available_now()
	#f.cache_default_attribute = field_cache_default_attribute()
	#f.cache_has_attachments = field_cache_has_attachments()
	#f.cache_is_pack = field_cache_is_pack()
	#f.category_ids_append = field_category_ids_append() ##<- добавочные категории. Если надо дополнить уже внесенные
	f.condition = field_condition()
	#f.customizable = field_customizable()
	#f.date_add = field_date_add()
	#f.date_upd = field_date_upd()

	################################################################################
	_images_urls: list = d.execute_locator(l["additional_images_urls"])
	if len(_images_urls) > 0:
		f.assist_fields_dict['default_image_url'] = _images_urls[0]
	if len(_images_urls) > 1:
		f.assist_fields_dict['images_urls'] = _images_urls[1::]
	################################################################################

	#f.delivery_in_stock = field_delivery_in_stock()	 # [v]	 ##<- доставка
	#f.delivery_out_stock = field_delivery_out_stock()	#   Заметка о доставке, когда товара нет в наличии

	#f.depth = field_depth()
	#f.description = field_description()
	f.description_short = f.description = field_description()
	# f.ean13 = field_ean13()
	# f.ecotax = field_ecotax()
	# f.height = field_height()
	f.how_to_use = field_how_to_use()
	f.id_category_default = field_id_category_default()
	#f.id_default_combination = field_id_default_combination()
	#f.id_default_image = field_id_default_image()
	#f.id_lang = s.locale
	f.id_manufacturer = field_id_manufacturer()
	#f.id_product = field_id_product()
	#f.id_shop_default = field_id_shop_default()   ## <- усранавливается в `product_fields_default_values.json`
	#f.id_supplier = s.supplier_id	# [v] ## <- добывается функцией set_references()
	#f.id_tax = field_id_tax() # [v]
	#f.id_type_redirected = field_id_type_redirected()
	#f.images_urls = field_images_urls()	# [v]
	#f.indexed = field_indexed()
	f.ingredients = field_ingredients()

	#f.is_virtual = field_is_virtual()
	#f.isbn = field_isbn()
	#f.link_rewrite = field_link_rewrite()
	#f.location = field_location()
	#f.low_stock_alert = field_low_stock_alert()
	#f.low_stock_threshold = field_low_stock_threshold()
	#f.meta_description = field_meta_description()
	#f.meta_keywords = field_meta_keywords()
	#f.meta_title = field_meta_title()
	#f.minimal_quantity = field_minimal_quantity()
	#f.mpn = field_mpn()

	###########################################################################################################
	_name = d.execute_locator (l["name"])[0]	# чтоб два раза не бегать, Я получаю значение локатора в _name
	f.name = field_name(_name)					# а потом использую для f.name
	f.link_rewrite = field_link_rewrite(_name)  # и для f.link_rewrite
	###########################################################################################################	

	#f.online_only = field_online_only()
	f.on_sale = field_on_sale()
	#f.out_of_stock = field_out_of_stock()
	#f.pack_stock_type = field_pack_stock_type()
	#f.position_in_category = field_position_in_category()
	f.price = field_price()
	#f.product_type = field_product_type()
	#f.quantity = field_quantity()
	#f.quantity_discount = field_quantity_discount()
	#f.redirect_type = field_redirect_type()
	#f.reference = field_reference()	# [v]  ## <- устанавливается в функции `set_references()`
	#f.show_condition = field_show_condition()
	#f.show_price = field_show_price()
	#f.state = field_state()
	# f.supplier_reference = field_supplier_reference()  # [v]  ## <- устанавливается в функции `set_references()`
	#f.text_fields = field_text_fields()
	#f.unit_price_ratio = field_unit_price_ratio()		<- см описание поля в базе данных
	#f.unity = field_unity()
	#f.upc = field_upc()
	#f.uploadable_files = field_uploadable_files()
	#f.volume = field_volume()		 ## <- устанавливается в функции `product_reference_and_volume_and_price_for_100()`
	f.visibility = field_visibility()
	#f.weight = field_weight()
	#f.wholesale_price = field_wholesale_price()
	#f.width = field_width()    
	...
	return f
    

d.get_url (s.current_scenario["url"])
""" перехожу по URL сценария (обычно, категория)"""

list_products_in_category: list = s.related_modules.get_list_products_in_category(s)
""" собрал список товаров в категории """

if not 	list_products_in_category:
	...


d.get_url(list_products_in_category[0])
""" перешел по первому url из списка """

d.wait(5)
d.execute_locator(s.locators["product"]["close_banner"])

...




# def set_references():
#     global f
#     f.supplier_reference = field_supplier_reference()
#     #f.id_supplier = s.supplier_id ## <- прописан в product.json
#     f.reference = f'{s.supplier_id}-{f.supplier_reference}'


def field_additional_shipping_cost():
	"""  
	 стоимость доставки
	@details
	"""
	return d.execute_locator(l["additional_shipping_cost"])
	

#f.additional_shipping_cost  = field_additional_shipping_cost()


#f.affiliate_short_link = d.current_url

#f.affiliate_summary = f.affiliate_summary_2 = ''   



def field_delivery_in_stock():
	"""  
	 Доставка, когда товар в наличии
	@details
	"""
	return str(d.execute_locator(l["delivery_in_stock"]))
	...




def field_active():
	"""  
	
	@details
	"""
	return f.active	 # <-  поставить в зависимость от delivery_out_stock
	...
	
        


def field_additional_delivery_times():
    """  
    
    @details
    """
    return d.execute_locator(l["additional_delivery_times"])
    ...



 

def field_additional_shipping_cost():
    """  
    
    @details
    """
    return d.execute_locator(l["additional_shipping_cost"])
    ...
    


def field_advanced_stock_management():
	"""  
	
	@details
	"""
	return f.advanced_stock_management
	...
	
        

def field_affiliate_short_link():
    """  
    
    @details
    """
    return d.current_url
    ...
    



def field_affiliate_summary():
    """  
    
    @details
    """
    return f.affiliate_summary
    ...



def field_affiliate_summary_2():
    """  
    
    @details
    """
    return f.affiliate_summary_2
    ...
        


def field_affiliate_text():
	"""  
	
	@details
	"""
	return f.affiliate_text
	...
	
    


def field_affiliate_image_large():
	"""  
	
	@details
	"""
	...
        


def field_affiliate_image_medium():
	"""  
	
	@details
	"""
	...
        


def field_affiliate_image_small():
	"""  
	
	@details
	"""
	return d.execute_locator(l["affiliate_image_small"])
        

def field_available_date():
    """  
    
    @details
    """
    return f.available_date
    ...
        
    


def field_available_for_order():
	"""  Если вернулся вебэлемент, это флаг, что товара нет в наличии, а вернулся <p>המלאי אזל
	"""
	available_for_order = d.execute_locator(l["available_for_order"])
	...
	if available_for_order is None:
		f.available_for_order = 1
	else:
		f.available_for_order = 0
		f.active = 0
	...



def field_available_later():
    """  
    
    @details
    """
    return f.available_later
    ...



def field_available_now():
    """  
    
    @details
    """
    return f.available_now
    ...




def field_category_ids():
	"""  
	
	@details
	"""
	return f.category_ids
	...
	


def field_category_ids_append():
	"""  
	
	@details
	"""
	#return f.category_ids_append
	...
	
                


def field_cache_default_attribute():
    """  
    
    @details
    """
    return f.cache_default_attribute
    ...



def field_cache_has_attachments():
    """  
    
    @details
    """
    return f.cache_has_attachments
    ...	
        
                


def field_cache_is_pack():
	"""  
	
	@details
	"""
	return f.cache_is_pack
	...
	


def field_condition():
	"""  
	
	@details
	"""
	return d.execute_locator(l.condition)
        

def field_customizable():
	"""  
	
	@details
	"""
	return f.customizable
	...


def field_date_add():
	"""  
	
	@details
	"""
	return f.date_add
	...
	


def field_date_upd():
	"""  
	
	@details
	"""
	return f.date_upd
	...
	


def field_delivery_in_stock():
	"""  
	 Доставка, когда товар в наличии
	@details
	"""
	return d.execute_locator(l["delivery_in_stock"])
	...
	
        


def field_delivery_out_stock():
	"""  
	 Заметка о доставке, когда товара нет в наличии
	"""
	return f.delivery_out_stock
	...
	
                


def field_depth():
	"""  
	@details
	"""
	return d.execute_locator ( l ["depth"] )
	...
	


def field_description():
	"""  поле полного описания товара 
	@details
	"""
	return d.execute_locator (l["description"] )[0].text
	...


def field_id_category_default():
	"""  Главная категория товара. Берется из сценария	"""
	return s.current_scenario["presta_categories"]["default_category"]
	...
	


def field_ean13():
	"""  
	
	@details
	"""
	return d.execute_locator ( l ["ean13"] )
	...



def field_ecotax():
	"""  
	
	@details
	"""
	return f.ecotax
	...
	
        	
                


def field_height():
	"""  
	
	@details
	"""
	return d.execute_locator ( l ["height"] )
	...
	


def field_how_to_use():
	"""  
	
	@details
	"""
	return d.execute_locator ( l ["how_to_use"] ) [0].text
	...
	
                	


def field_id_category_default():
	"""  
	
	@details
	"""
	return s.current_scenario["presta_categories"]["default_category"]
	...
	


def field_id_default_combination():
	"""  
	
	@details
	"""
	return f.id_default_combination
	...
	


def field_id_default_image():
	"""  
	
	@details
	"""
	return f.id_default_image
	...
	

def field_id_lang():
	"""  
	
	@details
	"""
	return f.id_lang
	...
	

def field_id_manufacturer():
	"""  ID бренда. Может быть и названием бренда - престашоп сам разберется """
	
	return d.execute_locator(l["id_manufacturer"])
	...
	

def field_id_product():
	"""  
	
	@details
	"""
	return f.id_product
	...


def field_id_shop_default():
	"""  
	
	@details
	"""
	return f.id_shop_default
	...
	

def field_id_supplier():
	"""  
	
	@details
	"""
	return d.execute_locator(l["id_supplier"])
	...
	

def field_id_tax():
	"""  
	
	@details
	"""
	return f.id_tax
	...
	

def field_id_type_redirected():
	"""  
	
	@details
	"""
	return f.id_type_redirected
	...


def field_images_urls():
	"""  
	 Вначале я загружу дефолтную картинку
	@details
	"""
	return d.execute_locator(l["additional_images_urls"])
	...
	


def field_indexed():
	"""  
	
	@details
	"""
	return f.indexed
	...
	
        

def field_ingredients():
	"""  Состав. Забираю с сайта HTML с картинками ингридиентов """
	
	return d.execute_locator ( l["ingredients"] )[0].text
	...
	



def field_meta_description():
	"""  
	
	@details
	"""
	d.execute_locator ( l['meta_description'] )
	...
	


def field_meta_keywords():
	"""  
	
	@details
	"""
	return d.execute_locator ( l['meta_keywords'] )
	...
	
        


def field_meta_title():
	"""  
	
	@details
	"""
	return d.execute_locator ( l['meta_title'] )
	...
	

	

def field_is_virtual():
	"""  
	
	@details
	"""
	return f.is_virtual
	...



def field_isbn():
	"""  
	
	@details
	"""
	return f.isbn
	...
	


def field_link_rewrite(product_name: str) -> str:
	"""  Создается из переменной `product_name` которая содержит значение локатора l["name"] 	"""	
	return StringNormalizer.normalize_link_rewrite ( product_name )
	...
	
	
        


def field_location():
	"""  
	
	@details
	"""
	return f.location
	...
	


def field_low_stock_alert():
	"""  
	
	@details
	"""
	return f.low_stock_alert
	...
	
    


def field_low_stock_threshold():
	"""  
	
	@details
	"""
	return f.low_stock_threshold
	...
	


def field_meta_description():
	"""  
	
	@details
	"""
	...
	


def field_meta_keywords():
	"""  
	
	@details
	"""
	return f.meta_keywords
	...
	
        


def field_meta_title():
	"""  
	
	@details
	"""
	return f.meta_title
	...
	



def field_minimal_quantity():
	"""  
	
	@details
	"""
	return f.minimal_quantity
	...



def field_mpn():
	"""  
	
	@details
	"""
	return f.mpn
	...
	


def field_name(name: str):
	"""  Название товара 
	Очищаю поля от лишних параметров, которые не проходят в престашоп 
	"""
	return StringNormalizer.normalize_product_name(name)
	...


def field_online_only():
	"""  	товар только в интернет магазине
	
	@details
	"""
	return d.execute_locator ( l['online_only'] )
	...
	


def field_on_sale():
	"""  	Распродажа	"""
	return d.execute_locator ( l['on_sale'] )
	...
	


def field_out_of_stock():
	"""  Товара нет в наличии """
	return d.execute_locator ( l["out_of_stock"]) 
	...
	


def field_pack_stock_type():
	"""  
	
	@details
	"""
	return f.pack_stock_type
	...
	


def field_position_in_category():
	"""  
	
	@details
	"""
	return f.position_in_category
	...
	


def field_price():
	"""  
	
	@details
	"""
	return StringNormalizer.normalize_price (d.execute_locator (l["price"])[0] ) 
	
	


def field_product_type():
	"""  
	
	@details
	"""
	return f.product_type
	...
	

# 
# def field_quantity():
# 	"""  
# 	
# 	@details
# 	"""
# 	return f.quantity
# 	...
	


def field_quantity_discount():
	"""  
	
	@details
	"""
	return f.quantity_discount
	...
	


def field_redirect_type():
	"""  
	
	@details
	"""
	return f.redirect_type
	...
	


def field_reference():
	"""  supplier's SKU """
	return f'{s.supplier_id}-{f.supplier_reference}' 
	...
	


def field_show_condition():
	"""  
	
	@details
	"""
	return f.show_condition
	



def field_show_price():
	"""  
	
	@details
	"""
	return f.show_price
	...



def field_state():
	"""  
	
	@details
	"""
	return f.state
	...



# def field_supplier_reference():
# 	"""  Локатор захватит 3 объекта (по одному я устал их искать). Здесь я делаю обработку результата
# 	"""
# 	return d.execute_locator (l["supplier_reference"])
# 	...
	



def field_text_fields():
	"""  
	
	@details
	"""
	return f.text_fields
	...
	


def field_unit_price_ratio():
	"""  
	
	@details
	"""
	return f.unit_price_ratio
	...
	


def field_unity():
	"""  
	
	@details
	"""
	return f.unity
	...
	
        


def field_upc():
	"""  
	
	@details
	"""
	return f.upc
	...
	


def field_uploadable_files():
	"""  
	
	@details
	"""
	return f.uploadable_files
	...
	


def field_default_image_url():
	"""  
	
	@details
	"""
	return f.default_image_url
	...
        


def field_visibility():
	"""  
	
	@details
	"""
	return d.execute_locator(l["visibility"])
	...
	


def field_weight():
	"""  
	
	@details
	"""
	return f.weight
	...
	


def field_wholesale_price():
	"""  
	
	@details
	"""
	return f.wholesale_price
	...
	


def field_width():
	"""  
	
	@details
	"""
	return f.width
	...
	
        
                


async def get_price(_d, _l) -> str | float:
	"""  Привожу денюшку через флаг `format` 
	@details к: 
	- [ ] float 
	- [v] str
	"""
	try:
		
		#raw_price = asyncio.run ( _d.execute_locator ( _l ["price"]["new"] )[0])
		raw_price = asyncio.run ( _d.execute_locator ( _l ["price"]["new"] )[0]) if gs.async_run else _d.execute_locator ( _l ["price"]["new"] )[0]
		''' raw_price получаю в таком виде:
		ILS382.00\nILS382\n.\n00
		'''
		raw_price = str (raw_price).split ('\n')[0]
		return StringNormalizer.normalize_price (raw_price)
	except Exception as ex:
		logger.error (ex)
		return
    
    ## price
    # async def cost_price():
    #     _price = _d.execute_locator (_l["price_locator"])        
    #     if not _price or len(_price) < 1:
    #         _price = _d.execute_locator(_l["uniform-banner-box-price"])
    #         ''' цена может быть спрятана баннером. Ищу в баннере'''
    #     _price = StringFormatter.clear_price(_price)
    #     return _price
    




def specification():
    #f["product_specification"] = _d.execute_locator(_l["specification_locator"])
    f["product_specification"] = f["description"]
def summary():
    f["summary"] = f["description"]
def delivery():

    #__ = _l["dynamic_shipping_block"]
    #_d.execute_locator(__l["product_shippihg_locator_button"])
    #''' Открываю панель способов доставки '''
    #shipping_price = _d.execute_locator(__l["dynamic_shipping_titleLayout"])
    #dynamic_shipping_estimated = _d.execute_locator(__l["dynamic_shipping_estimated"])
    #dynamic_tracking_available = _d.execute_locator(__l["dynamic_tracking_available"])
    #close = _d.execute_locator(__l["close"])

    shipping_price = _d.execute_locator(_l["shipping_price_locator"])
    if 'Free Shipping' in shipping_price:
        f["shipping price"] = 0
        return True
    f["shipping price"] = StringFormatter.clear_price(shipping_price)
    return True



def link():
    f["link_to_product"]= _d.current_url.split('?')[0]

## images
def images():

    _http_server = f'''http://davidka.esy.es/supplier_imgs/{s.supplier_prefix}'''
    _img_name = f'''{f["sku"]}.png'''
    f["img url"] =f'''{_http_server}/{_img_name}'''
    screenshot = _d.execute_locator(_l["main_image_locator"])
    s.save_and_send_viaftp({_img_name:screenshot})

def qty():
    try:
        _qty = _d.execute_locator(_l["qty_locator"])[0]
        f["qty"] = StringFormatter.clear_price(_qty)
        f["tavit im bemlay"] = f["qty"]
        return True
    except Exception as ex: 
        #field["qty"] = None
        logger.error(ex)
        return

def byer_protection():
    try:
        f["product_byer_protection"] = str(_d.execute_locator(_l["byer_protection_locator"]))
        return True
    except Exception as ex: 
        f["product_byer_protection"] = None
        logger.error(ex)
        return


def customer_reviews():
    try:
        f["product_customer_reviews"] = _d.execute_locator(_l["customer_reviews_locator"])
    except Exception as ex:
        f["product_customer_reviews"] = None
        logger.error(ex)
        return



def rewritted_URL():
    '''
    TODO
    получается длинные
    f["Rewritten URL"] = StringFormatter.rewritted_URL(f["title"])
    '''
    f["Rewritten URL"] = f["id"]
    ...


product_fields = grab_product_page (s)

#presta_fields_dict: Dict = product_fields.presta_fields_dict
presta_fields_dict: Dict = {key: value for key, value in product_fields.presta_fields_dict.items() if value}
""" Убираю пустые ключи из словаря """

if 'quantity' in presta_fields_dict: del presta_fields_dict['quantity']
""" `quantity` нельзя задавать при добавлении нового товара """

assist_fields_dict: Dict = product_fields.assist_fields_dict

""" Для `V3` Я могу передать фильтр, как строку `filter[id] = [5]` и как словарь `{'filter[id]':'[5]'}	"""
reference = presta_fields_dict["reference"]
search_filter_str =  f'filter[reference] = [{reference}]'
search_filter_dict = { 'filter[reference]': '['+ reference + ']' }
ret = p.get( search_filter = search_filter_dict, PrestaAPIV = 'V3' ) 

if ret is False or not ret or len(ret) == 0:
	""" Новый товар """
	p.add(presta_fields_dict, 'JSON', 'V3')
...

# product_fields["default_image_url"] = None
# product_fields["images_urls"] = None

# if f.search(_filter = '[reference] = [{f.reference}]'):
# 	p.update(presta_fields_dict)
# else:
# 	p.add(product_fields))