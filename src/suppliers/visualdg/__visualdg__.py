## \file hypotez/src/suppliers/visualdg/__visualdg__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.suppliers.visualdg """
"""    Supplier: visualdg.co.il


@namespace src: src
 \package src.suppliers.visualdg
\file __visualdg__.py
 
 @section libs imports:
  - .login 
  - .scrapper 
  - .via_webdriver 
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""





def login(self):
    self.get_url('https://www.visualdg.co.il/customer_login')
        
    email = self.locators['login']['email']
    password = self.locators['login']['password']

    email_locator = (self.locators['login']['email_locator']['by'], 
                        self.locators['login']['email_locator']['selector'])

    password_locator = (self.locators['login']['password_locator']['by'],
                            self.locators['login']['password_locator']['selector'])

    loginbutton_locator =  (self.locators['login']['loginbutton_locator']['by'],
                                self.locators['login']['loginbutton_locator']['selector'])



    self.find(email_locator).send_keys(email)
    self.find(password_locator).send_keys(password)
    self.wait(1)
    self.find(loginbutton_locator).click()
    self.wait(1)
    self.log('VDG logged in')
   
    return True


def update_categories_in_scenario_file(supplier,current_scenario_filename):
    return True



