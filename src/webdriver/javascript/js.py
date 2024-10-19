## \file src/webdriver/javascript/js.py
## \file ../src/webdriver/javascript/js.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""   функции и методы JavaScript """
...

from src import gs
from src.logger import logger

class JavaScript:
    """ Функции javascript"""
    driver = None
    
    def __init__(self, Driver):
        """ Функции и методы javascript 
        @param Driver: `src.webdriver.Driver` 
        """
        ...
        self.driver = Driver
        
    def unhide_DOM_element(self, element):
        '''!  Если DOM элемент invisible, необходимо сделать его видимым.  '''
        script :str = f''' 
        arguments[0].style.opacity=1;
        arguments[0].style['tranStringFormatterorm']='translate(0px, 0px) scale(1)';
        arguments[0].style['MozTranStringFormatterorm']='translate(0px, 0px) scale(1)';
        arguments[0].style['WebkitTranStringFormatterorm']='translate(0px, 0px) scale(1)';
        arguments[0].style['msTranStringFormatterorm']='translate(0px, 0px) scale(1)';
        arguments[0].style['OTranStringFormatterorm']='translate(0px, 0px) scale(1)';
        arguments[0].scrollIntoView(true);
        return true; 
        '''
        try:
            self.driver.execute_script(script, element)
            return True
        except Exception as ex:
            logger.error(f''' ошибка JS в unhide_DOM_element() {ex.with_traceback(ex.__traceback__)}''')
            return
       
 
    def get_ready_state(self) -> str:
        '''! Проверка полной загрузки объекта document
        пока идет загрузка DOM дерева возвращает "loading", 
        а когда загрузка закончилась - "complete"  '''

        script = 'return document.readyState;'
    
        try:
            return self.driver.execute_script(script)
        except Exception as ex: 
            logger.error(f''' ошибка JS в return document.readyState; {ex.with_traceback(ex.__traceback__)}''')
            return
        
 
    def window_focus(self):
        script = 'return window.focus();'
        try:
            return self.driver.execute_script(script)
        except Exception as ex: 
            logger.error(f''' ошибка JS в window.focus() {ex.with_traceback(ex.__traceback__)}''')
            return

    def get_referrer(self):
    # Исполнение JavaScript для получения значения document.referrer
        referrer_url = self.driver.execute_script("return document.referrer;")
        return referrer_url

    def get_page_lang(self) -> str:
        page_lang = self.driver.execute_script("return document.documentElement.lang;") 
        return page_langg