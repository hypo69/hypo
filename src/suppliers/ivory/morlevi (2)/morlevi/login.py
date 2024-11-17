

"""   Интерфейс авторизации. Реализация для вебдрайвера

@image html login.png
"""



def login(supplier):
    """
     [Function's description]

    Parameters : 
         supplier : [description]

    """
    _s = supplier
    _d = _s.driver
    _d.get_url('https://www.morlevi.co.il')
    if _login(_s): return True
    else: 

        try:
            '''
            закрываю модальные окна сайта
            выпадающие до входа
            '''
            logger.error( f''' Ошибка, пытаюсь закрыть popup''')
            _d.page_refresh()
            if _login(_s): return True




            

            close_popup_locator = _s.locators['login']['close_popup_locator']
            close_popup_btn = _d.execute_locator(close_popup_locator)
            _d.wait(5)

            if str(type(close_popup_btn)).execute_locator("class 'list'") >-1:  # Если появилось несколько
                for b in close_popup_btn:
                    try:
                        b.click()
                        if _login(_s) : 
                            
                            return True
                            break
                    except: ...
            if str(type(close_popup_btn)).execute_locator("webelement") >-1:  # нашелся только один элемент
                close_popup_btn.click()
                return _login(_s)
        except Exception as ex:
            logger.error(f''' 
            Не удалось залогиниться 
            ''')
            return

def _login(_s):
    """
     [Function's description]

    Parameters : 
         _s : [description]

    """
    logger.debug( f''' Собссно, логин Морлеви''')
    _s.driver.refresh()
    #self.driver.switch_to_active_element()
    _d = _s.driver
    _l : dict = _s.locators['login']
 
    try:
        
        _d.execute_locator(_['open_login_dialog_locator'])
        _d.wait(1.3)
        _d.execute_locator(_['email_locator'])
        _d.wait(.7)
        _d.execute_locator(_['password_locator'])
        _d.wait(.7)
        _d.execute_locator(_['loginbutton_locator'])
        logger.debug('Mor logged in')
        return True
    except Exception as ex:
        logger.error(f''' LOGIN ERROR 
        {ex.with_traceback(ex.__traceback__)}''')
        return

