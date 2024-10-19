## \file src/suppliers/bangood/grabber.py
"""   Собиратель данных со страницы товара

Функции, специфичные для HB:
- product_reference_and_volume_and_price_for_100():
В НВ поле `supplier_reference` заполняется нестандартным методом: 	
Созданный для НВ локатор `product_reference_and_volume_and_price_for_100` 
получает сразу 4 вебэлемента. У меня не получилось найти их по одному, да это и не надо.

 @section libs imports:
  - gs 
  - product 
  - helpers 
  - tools 
  @file
"""

## \file ../src/suppliers/bangood/grabber.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
import asyncio
from typing import Union

from selenium.webdriver.remote.webelement import WebElement
from src import gs
from src.product import  Product, ProductFields
from src.logger import logger
from src.utils import StringFormatter, StringNormalizer
from src.suppliers import Supplier
from src.webdriver import Driver

StringNormalizer = StringNormalizer()
StringFormatter = StringFormatter()

s: Supplier = None
p: Product = None
f: ProductFields = None
d: Driver = None 
l: dict = None
async_run = gs.async_run




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

	global d
	d = s.driver
	
	global l
	l = s.locators['product']
	
	d.execute_locator(l['close_banner'])
	
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
		global f
		webelements: [WebElement] = d.execute_locator(l['product_reference_and_volume_and_price_for_100'])
        
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
	
	product_reference_and_volume_and_price_for_100()
	
	#
	#
	#	
	#######################################################################################




	######################################################################################## 
	#
	#			Поля `f.id_supplier`, `f.reference`  
	#			Поле `f.supplier_reference` определено в функции `product_reference_and_volume_and_price_for_100()`

	def set_references(f, s):
		""" все, что касается id товара """
		#f.supplier_reference = field_supplier_reference()
		f.id_supplier = s.supplier_id
		f.reference = f'{s.supplier_id}-{f.supplier_reference}'
	
	set_references(f, s)
	#
	#######################################################################################

	


	#f.active = field_active() # Совпадает с f.available_for_order Если товара нет в наличии - выставляю флаг 0
	#f.additional_delivery_times = field_additional_delivery_times()	# [v]  Мое поле. Нахера - не знаю
	f.additional_shipping_cost = field_additional_shipping_cost() # [v]
	#f.advanced_stock_management = field_advanced_stock_management()
	f.affiliate_short_link = d.current_url # field_affiliate_short_link() # [v]
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
	f.available_for_order = f.active
	#f.available_later = field_available_later()
	#f.available_now = field_available_now()
	#f.cache_default_attribute = field_cache_default_attribute()

	#f.cache_has_attachments = field_cache_has_attachments()
	#f.cache_is_pack = field_cache_is_pack()
	#f.category_ids_append = field_category_ids_append() ##<- добавочные категории. Если надо дополнить уже внесенные
	#f.condition = field_condition()
	#f.customizable = field_customizable()
	#f.date_add = field_date_add()
	#f.date_upd = field_date_upd()
	f.default_image_url = field_default_image_url()
	#f.delivery_in_stock = field_delivery_in_stock()	 # [v]	 ##<- заметка о доставке. если товар в наличии
	#f.delivery_out_stock = field_delivery_out_stock() # [v]	 ##<- заметка о доставке, если товара нет в наличии
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
	#f.id_lang = field_id_lang()
	f.id_manufacturer = field_id_manufacturer()
	f.id_product = field_id_product()
	#f.id_shop_default = field_id_shop_default()
	#f.id_supplier = s.supplier_id	# [v]
	#f.id_tax = field_id_tax() # [v]
	#f.id_type_redirected = field_id_type_redirected()
	#f.images_urls = field_images_urls()	# [v]
	#f.indexed = field_indexed()
	f.ingredients = field_ingredients()
	#f.is_virtual = field_is_virtual()
	#f.isbn = field_isbn()

	f.location = field_location()
	#f.low_stock_alert = field_low_stock_alert()
	#f.low_stock_threshold = field_low_stock_threshold()
	f.meta_description = field_meta_description()
	f.meta_keywords = field_meta_keywords()
	f.meta_title = field_meta_title()
	f.minimal_quantity = field_minimal_quantity()
	#f.mpn = field_mpn()

	###########################################################################################################
	_name = d.execute_locator (l['name'])[0]	# чтоб два раза не бегать, Я получаю значение локатора в _name
	f.name = field_name(_name)					# а потом использую для f.name
	f.link_rewrite = field_link_rewrite(_name)  # и для f.link_rewrite
	###########################################################################################################	

	#f.online_only = field_online_only()
	#f.on_sale = field_on_sale()
	#f.out_of_stock = field_out_of_stock()
	#f.pack_stock_type = field_pack_stock_type()
	#f.position_in_category = field_position_in_category()
	f.price = field_price()
	#f.product_type = field_product_type()	 # enum('standard','pack','virtual','combinations','')
	#f.quantity = field_quantity()
	#f.quantity_discount = field_quantity_discount()
	#f.redirect_type = field_redirect_type()
	#f.reference = field_reference()	# [v] заполняется в функции `set_references()`
	#f.show_condition = field_show_condition()
	#f.show_price = field_show_price()
	#f.state = field_state()
	#f.supplier_reference = field_supplier_reference()  # заполняется в функции `set_references()`
	#f.text_fields = field_text_fields()
	#f.unit_price_ratio = field_unit_price_ratio()
	#f.unity = field_unity()
	#f.upc = field_upc()
	#f.uploadable_files = field_uploadable_files()
	f.default_image_url = field_default_image_url()
	#f.volume = field_volume() # <- вычисляется в функции product_reference_and_volume_and_price_for_100()
	#f.visibility = field_visibility()
	#f.weight = field_weight()
	#f.wholesale_price = field_wholesale_price()
	#f.width = field_width()    
	return f
    


	


def field_active():
	"""  
	
	@details
	"""
	return f.active
	...
	
        


def field_additional_delivery_times():
    """  
    
    @details
    """
    return d.execute_locator(l['additional_delivery_times'])
    ...



 

def field_additional_shipping_cost():
    """  
    
    @details
    """
    return d.execute_locator(l['additional_shipping_cost'])
    ...
    


def field_advanced_stock_management():
	"""  
	
	@details
	"""
	return f.advanced_stock_management
	...
	
        

def field_affiliate_short_link():
    """  	 Возвращаю `current_url` поскольку у меня нет affiliate на этом сайте """
    return d.execute_locator(l['affiliate_short_link'])
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
	return d.execute_locator(l['affiliate_image_small'])
        

def field_available_date():
    """  
    
    @details
    """
    return f.available_date
    ...
        
    


def field_available_for_order():
	"""  Если вернулся вебэлемент, это флаг, что товара нет в наличии, а вернулся <p>המלאי אזל
	"""
	available_for_order = d.execute_locator(l['available_for_order'])
	...
	if available_for_order is None:
		f.available_for_order = 1
	else:
		f.available_for_order = 0
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
	...
	return f.condition
        

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
	


def field_delivery_out_stock():
    """  
     Заметка о доставке, когда товара нет в наличии
    """
    webelement = d.execute_locator(l['delivery_out_stock'])
    f.delivery_out_stock = webelement[0].text
	
        
                


def field_depth():
	"""  
	@details
	"""
	return f.depth
	...
	


def field_description():
    descr = d.execute_locator (l['description'] )
    f.description = descr[0].text
    ...


# 
# def field_description_short():
# 	"""   На сайте нет короткого описания. Я закладываю в поле `description_short` значение из `description`
# 	
# 	@details
# 	"""
# 	return str (d.execute_locator (l['description_short'] ) )
# 	...


def field_ean13():
	"""  
	
	@details
	"""
	return f.ean13
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
	return f.height
	...
	


def field_how_to_use():
	"""  
	
	@details
	"""
	return d.execute_locator ( l ['how_to_use'] ) 
	...
	
                	


def field_id_category_default():
	"""  Главная категория товара. Берется из сценария	"""
	
	return s.current_scenario['presta_categories']['default_category']
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
	
	return 'HB'
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
	return s.supplier_id
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
	return d.execute_locator(l['additional_images_urls'])
	...
	


def field_indexed():
	"""  
	
	@details
	"""
	return f.indexed
	...
	
        

def field_ingredients():
	"""  
	
	@details
	"""
	return d.execute_locator ( l['ingredients'] )[0].text
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
	"""  Создается из переменной `product_name` которая содержит значение локатора l['name'] 	"""	
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
	


def field_name(product_name: str) -> str:
	"""  Название товара 
	Очищаю поля от лишних параметров, которые не проходят в престашоп 
	"""
	return StringNormalizer.normalize_product_name(product_name)
	...
	


def field_online_only():
	"""  	товар только в интернет магазине
	
	@details
	"""
	return f.online_only
	...
	


def field_on_sale():
	"""  	Распродажа	"""
	return f.on_sale
	...
	


def field_out_of_stock():
	"""  Товара нет в наличии """
	return d.execute_locator ( l['out_of_stock']) 
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
	return StringNormalizer.normalize_price ( d.execute_locator (l['price'])[0] ) 
	
	


def field_product_type():
	"""  
	
	@details
	"""
	return f.product_type
	...
	


def field_quantity():
	"""  
	
	@details
	"""
	return f.quantity
	...
	


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



def field_supplier_reference():
	"""  Локатор захватит 3 объекта (по одному я устал их искать). Здесь я делаю обработку результата
	"""
	return d.execute_locator (l['supplier_reference'])
	...
	



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
	return f.visibility
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
		
		#raw_price = asyncio.run ( _d.execute_locator ( _l ['price']['new'] )[0])
		raw_price = asyncio.run ( _d.execute_locator ( _l ['price']['new'] )[0]) if gs.async_run else _d.execute_locator ( _l ['price']['new'] )[0]
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
    #     _price = _d.execute_locator (_l['price_locator'])        
    #     if not _price or len(_price) < 1:
    #         _price = _d.execute_locator(_l['uniform-banner-box-price'])
    #         ''' цена может быть спрятана баннером. Ищу в баннере'''
    #     _price = StringFormatter.clear_price(_price)
    #     return _price
    




def specification():
    #f['product_specification'] = _d.execute_locator(_l['specification_locator'])
    f['product_specification'] = f['product_description']
def summary():
    f['summary'] = f['product_description']
def delivery():

    #__ = _l['dynamic_shipping_block']
    #_d.execute_locator(__l['product_shippihg_locator_button'])
    #''' Открываю панель способов доставки '''
    #shipping_price = _d.execute_locator(__l['dynamic_shipping_titleLayout'])
    #dynamic_shipping_estimated = _d.execute_locator(__l['dynamic_shipping_estimated'])
    #dynamic_tracking_available = _d.execute_locator(__l['dynamic_tracking_available'])
    #close = _d.execute_locator(__l['close'])

    shipping_price = _d.execute_locator(_l['shipping_price_locator'])
    if 'Free Shipping' in shipping_price:
        f['shipping price'] = 0
        return True
    f['shipping price'] = StringFormatter.clear_price(shipping_price)
    return True



def link():
    f['link_to_product']= _d.current_url.split('?')[0]

## images
def images():

    _http_server = f'''http://davidka.esy.es/supplier_imgs/{s.supplier_prefix}'''
    _img_name = f'''{f['sku']}.png'''
    f['img url'] =f'''{_http_server}/{_img_name}'''
    screenshot = _d.execute_locator(_l['main_image_locator'])
    s.save_and_send_viaftp({_img_name:screenshot})

def qty():
    try:
        _qty = _d.execute_locator(_l['qty_locator'])[0]
        f['qty'] = StringFormatter.clear_price(_qty)
        f['tavit im bemlay'] = f['qty']
        return True
    except Exception as ex: 
        #field['qty'] = None
        logger.error(ex)
        return

def byer_protection():
    try:
        f['product_byer_protection'] = str(_d.execute_locator(_l['byer_protection_locator']))
        return True
    except Exception as ex: 
        f['product_byer_protection'] = None
        logger.error(ex)
        return


def customer_reviews():
    try:
        f['product_customer_reviews'] = _d.execute_locator(_l['customer_reviews_locator'])
    except Exception as ex:
        f['product_customer_reviews'] = None
        logger.error(ex)
        return



def rewritted_URL():
    '''
    TODO
    получается длинные
    f['Rewritten URL'] = StringFormatter.rewritted_URL(f['title'])
    '''
    f['Rewritten URL'] = f['id']
    ...

## combinations
def combinations():
    """  У товара может быть насколько комбинаций. Функция вытаскивает все возможные
    @todo не проверена, я отложил реализацию на след версию
    """
    _l = s.locators['product']
    _combfs = p.combinationStringFormatters
    _attr_position = 0

    def product_combinations():
        _type = s.current_scenario['product combinations']
        if not _type: return
        """  _rem у товара не всегда есть комбинации """

        __ = s.locators['product']['combinations']
        _combfs['Product ID'] = f['id']
        _name = _d.execute_locator(__l['name'])
        _value = _d.execute_locator(__l['value'])
            
        _combfs['Attribute (Name:Type:Position)'] = f'''{_name}:{_type}:0'''
        _combfs['Value (Value:Position)'] = f'''{_value}:0'''
        _price = _d.execute_locator(_l['price_locator'])
        """  _rem получаю цену комбинации товара """
            
        _price = StringFormatter.clear_price(_price)

        _qty = _d.execute_locator(_l['qty_locator'])[0]
        _qty = StringFormatter.clear_price(_qty)



        ## форма комбинаций  в Prestashop
        # Attribute (Name:Type:Position)*
        # Value (Value:Position)*

        attr_name = _d.execute_locator(_title)
        attr_type = 'select'
        attr_position = _attr_position

        _combinationStringFormatters['Attribute (Name:Type:Position)'] = f'''{attr_name}:{attr_type}:{attr_position}'''
        
        _vt = _d.execute_locator(_l['product_combinations_container_locator']['product_combinations_value_title'])
        _vp = _attr_position
        _combinationStringFormatters['Value (Value:Position)'] = f'''{_vt}:{_vp}'''

                

        url_dict = _d.get_dictfrom_urlstr()
        _combinationStringFormatters['Supplier reference'] = _combina['Product reference'] = url_dict['params']['sku_id']
                
                
        _d.execute_locator(_l['product_name_locator'])

        _combinationStringFormatters['Image URLs(x,y,z)'] = _d.execute_locator(_l['main_image_locator'])
        _combinationStringFormatters['Quantity'] = _qty
        _combinationStringFormatters['Wholesale price'] = _price

    try:
        _title = _l['product_combinations_container_locator']['product_combinations_title']
        _values_locator = _l['product_combinations_container_locator']['image_attribute_locator'] 
        _values = _d.execute_locator(_values_locator)
        if not _values:
            return
        ''' нет комбинаций '''
            
        if isinstance(_values , list):
            ''' несколько вариантов товара'''
            for x in _values:
                ''' нажимаю на каждую опцию товара '''
                x.click()
                product_combinations()
                _combinot.apply(_combina)

        else:
            ''' один вариант '''
            _values.click()
            values()
            _combinot.apply(_combina)

        return True
    except Exception as ex: 
            
        logger.error(ex)
        return

