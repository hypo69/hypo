## \file /src/suppliers/aliexpress/category.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.suppliers.aliexpress 
	:platform: Windows, Unix
	:synopsis:  управление категориями aliexpress

"""


from typing import Union
from pathlib import Path

from src import gs
from src.utils.jjson import j_dumps, j_loads
from src.logger.logger import logger

# Импорт класса CategoryManager и модели AliexpressCategory
# Зачем?  CategoryManager занимается переводами
from src.db.manager_categories.suppliers_categories import CategoryManager, AliexpressCategory

credentials = gs.db_translations_credentials
# Создание экземпляра класса CategoryManager
manager = CategoryManager()


def get_list_products_in_category(s) -> list[str, str]:
    """  
     Считывает URL товаров со страницы категории.

    @details Если есть несколько страниц с товарами в одной категории - листает все.
    Важно понимать, что к этому моменту вебдрайвер уже открыл страницу категорий.

    @param s `Supplier` - экземпляр поставщика
    @param run_async `bool` - устанавливает синхронность/асинхронность исполнения функции `async_get_list_products_in_category()`

    @returns list_products_in_category `list` - список собранных URL. Может быть пустым, если в исследуемой категории нет товаров.
    """
    
    return get_prod_urls_from_pagination (s)
        


def get_prod_urls_from_pagination(s) -> list[str]:
    """   Функция собирает ссылки на товары со страницы категории с перелистыванием страниц 
    @param s `Supplier` 
    @returns list_products_in_category `list` :  Список ссылок, собранных со страницы категории"""
    
    _d = s.driver
    _l: dict = s.locators['category']['product_links']
    
    list_products_in_category: list = _d.execute_locator(_l)
    
    if not list_products_in_category:
        """ В категории нет товаров. Это нормально """
        return []

    while True:
        """ @todo Опасная ситуация здесь/ Могу уйти в бесконечный цикл """
        if not _d.execute_locator (s.locators ['category']['pagination']['->'] ):
            """  _rem Если больше некуда нажимать - выходим из цикла """
            break
        list_products_in_category.extend(_d.execute_locator(_l ))
   
    return list_products_in_category if isinstance(list_products_in_category, list) else [list_products_in_category]



# Сверяю файл сценария и текущее состояние списка категорий на сайте 

def update_categories_in_scenario_file(s, scenario_filename: str) -> bool:
    """  Проверка изменений категорий на сайте 
    @details Сличаю фактически файл JSON, полученный с  сайта
    @todo не проверен !!!! """
    
    scenario_json = j_loads(Path(gs.dir_scenarios, f'''{scenario_filename}'''))
    scenarios_in_file = scenario_json['scenarios']
    categoris_on_site = get_list_categories_from_site()

    all_ids_in_file:list=[]
    def _update_all_ids_in_file():
        for _category in scenario_json['scenarios'].items():
            if _category[1]['category ID on site'] > 0:
                # здесь может упасть, если значение 'category ID on site' не определено в файле
                all_ids_in_file.append(_category[1]['category ID on site'])
            else:
                url = _category[1]['url']
                cat = url[url.rfind('/')+1:url.rfind('.html'):].split('_')[1]
                _category[1]['category ID on site']:int = int(cat)
                all_ids_in_file.append(cat)
        #json_dump(scenario_json,Path(gs.dir_scenarios, f'''{scenario_filename}'''))

    _update_all_ids_in_file()

    response = requests.get(scenario_json['store']['shop categories json file'])
    ''' получаю json категорий магазина '''
    if response.status_code == 200:
        categories_from_aliexpress_shop_json = response.json()
    else:
        logger.error(f''' Ошибка чтения JSON  {scenario_json['store']['shop categories json file']}
        response: {response}''')
        return
    

  
    """
    Следующий код производит сравнение списка идентификаторов категорий all_ids_in_file с current_categories_json_on_site,
    идентификаторами категорий, полученными с текущей версии сайта в формате JSON 

    В первой строке кода, из current_categories_json_on_site извлекается список групп категорий и сохраняется в переменной groups.
    Далее создаются два пустых списка all_ids_on_site и all_categories_on_site, которые будут заполняться идентификаторами и категориями в формате словаря, полученными с сайта.
    Для каждой группы в groups, если у нее нет подгрупп (т.е. длина списка subGroupList равна 0), 
    то идентификатор и сама категория добавляются в соответствующие списки all_ids_on_site и all_categories_on_site. 
    Если же у группы есть подгруппы, то для каждой подгруппы производится аналогичное добавление в списки.
    Затем код создает два списка: removed_categories и added_categories. 
    В removed_categories добавляются идентификаторы категорий из списка all_ids_in_file, которые не нашли соответствие в all_ids_on_site. 
    В added_categories добавляются идентификаторы категорий из all_ids_on_site, которых нет в all_ids_in_file.
    Итого, removed_categories и added_categories содержат различия 
    между списками идентификаторов категорий на сайте и в файле, соответственно.
    """
    
    groups = categories_from_aliexpress_shop_json['groups']
    all_ids_on_site:list=[]
    all_categories_on_site:list=[]
    for group in groups:
        if len(group['subGroupList'])==0:
            all_ids_on_site.append(str(group['groupId']))
            all_categories_on_site.append(group)
        else:
            for subgroup in group['subGroupList']:
                 all_ids_on_site.append(str(subgroup['groupId']))
                 all_categories_on_site.append(subgroup)

    removed_categories  = [x for x in all_ids_in_file if x not in set(all_ids_on_site)]
    added_categories = [x for x in all_ids_on_site if x not in set(all_ids_in_file)]



    if len(added_categories)>0:
        for category_id in added_categories: 
            category = [c for c in all_categories_on_site if c['groupId'] == int(category_id)]
            category_name = category[0]['name']
            category_url = category[0]['url']
            categories_in_file.update({category_name:{
                    "category ID on site":int(category_id),
                    "brand":"",
                    "active": True,
                    "url":category_url,
                    "condition":"",
                    "PrestaShop_categories":""
                    }})
        scenario_json['scenarios'] = categories_in_file
        json_dump(scenario_json,Path(gs.dir_scenarios, f'''{scenario_filename}'''))

        post_subject = f'''Добавлены новые категории в файл {scenario_filename}'''
        post_message = f'''
        В файл {scenario_filename} были добавлены новые категории:
        {added_categories}
        '''
        send(post_subject,post_message)


    if len(removed_categories)>0:
        for category_id in removed_categories: 
            category = [v for k,v in categories_in_file.items() if v['category ID on site'] == int(category_id)]
            if len(category) == 0:continue
            category[0]['active'] = False
        
        scenario_json['scenarios'] = categories_in_file
        json_dump(scenario_json,Path(gs.dir_scenarios, f'''{scenario_filename}'''))

        post_subject = f'''Отлючены категории в файле {scenario_filename}'''
        post_message = f'''
        В файл {scenario_filename} были отключены категории:
        {removed_categories}
        '''
        send(post_subject,post_message)
    return True


def get_list_categories_from_site(s,scenario_file,brand=''):
    _d = s.driver
    scenario_json = json_loads(Path(gs.dir_scenarios, f'''{scenario_file}'''))
    _d.get_url(scenario_json['store']['shop categories page'])
    ...
    
class DBAdaptor:
    def select(cat_id:int = None, parent_id:int = None, project_cat_id:int = None ):
        # Пример операции SELECT
        # Выбрать все записи из таблицы AliexpressCategory, где parent_category_id равен 'parent_id_value'
        records = manager.select_record(AliexpressCategory, parent_category_id='parent_id_value')
        print(records)

    def insert():  
        # Пример операции INSERT
        # Вставить новую запись в таблицу AliexpressCategory
        fields = {
            'category_name': 'New Category',
            'parent_category_id': 'Parent ID',
            'hypotez_category_id': 'Hypotez ID'
        }
        manager.insert_record(AliexpressCategory, fields)

    def update(): 
        # Пример операции UPDATE
        # Обновить запись в таблице AliexpressCategory, где hypotez_category_id равен 'hypotez_id_value'
        manager.update_record(AliexpressCategory, 'hypotez_id_value', category_name='Updated Category')

    def delete():
        # Пример операции DELETE
        # Удалить запись из таблицы AliexpressCategory, где hypotez_category_id равен 'hypotez_id_value'
        manager.delete_record(AliexpressCategory, 'hypotez_id_value')

