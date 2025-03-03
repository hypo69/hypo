## \file /src/db/manager_translations/product_translations.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.db.manager_translations 
	:platform: Windows, Unix
	:synopsis:

"""


import sys
import traceback
from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_

import header
from src import gs
from src.logger.logger import logger
...

class ProductTranslationsManager:
    """
    Example usage:
    
    1. **Initialize the manager:**
    @code
    manager = ProductTranslationsManager()
    @endcode

    2. **Insert a record:**
    @code
    fields = {
        'product_reference': 'reference_product_value',
        'locale': 'en',
        'name': 'Product Name',
        'description': 'Description of the product',
        'link_rewrite': 'product-name'
    }
    manager.insert_record(fields)
    @endcode

    3. **Select records:**
    @code
    # Select records with a specific product reference
    records = manager.select_record(product_reference='reference_product_value')
    for record in records:
        print(record.name, record.description)

    # Select records with multiple conditions using logical OR
    records = manager.select_record(or_(
        ProductTranslation.locale == 'en',
        ProductTranslation.locale == 'ru'
    ))
    @endcode

    4. **Update a record:**
    @code
    manager.update_record('reference_product_value', 'en', description='Updated description')
    @endcode

    5. **Delete a record:**
    @code
    manager.delete_record('reference_product_value', 'en')
    @endcode

    These examples demonstrate how to use the `ProductTranslationsManager` class to interact with product translation records in the database. Adjust the field values and conditions according to your specific use case.
    """
    credentials = gs.credentials.presta.client

    def __init__(self, credentials:credentials, *args, **kwargs):
        # Initialize the manager
        connection_string = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}".format(
            **{
                "host": credentials.server,
                "port": credentials.port,
                "database": credentials.database,
                "user": credentials.user,
                "password": credentials.password,
            }
        )
        self.engine = create_engine(connection_string)
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.define_model()
        self.create_table()
        ...
        
    # Define __enter__ method to support context manager protocol
    def __enter__(self):
        return self
    ...
    
    # Define __exit__ method to support context manager protocol
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Optionally, add cleanup code here
        ...
        
    def define_model(self):
        class ProductTranslation(self.Base):
            __tablename__ = 'product_translations'
            # Define table structure
            product_reference = Column(String(128), primary_key=True)
            locale = Column(String(8), nullable=False, comment='Locale - the format in which the server usually returns the response. en-US, he-IL, ru-RU')
            name = Column(String(128), nullable=False)
            description = Column(Text, default=None)
            description_short = Column(Text, default=None)
            link_rewrite = Column(String(128), nullable=False)
            meta_description = Column(String(512), default=None)
            meta_keywords = Column(String(255), default=None)
            meta_title = Column(String(128), default=None)
            available_now = Column(String(255), default=None)
            available_later = Column(String(255), default=None)
            delivery_in_stock = Column(String(255), default=None, comment='(Delivery when the product is in stock): Text that will be displayed when the product is in stock.')
            delivery_out_stock = Column(String(255), default=None, comment='(Delivery if the product is out of stock): Text that will be displayed when the product is out of stock.')
            delivery_additional_message = Column(String(256), default=None, comment='Additional message for shipping conditions')
            affiliate_short_link = Column(String(256), default=None)
            affiliate_text = Column(Text, default=None)
            affiliate_summary = Column(Text, default=None)
            affiliate_summary_2 = Column(Text, default=None)
            affiliate_image_small = Column(String(100), default=None)
            affiliate_image_medium = Column(String(100), default=None)
            affiliate_image_large = Column(String(100), default=None)
            ingredients = Column(Text, default=None)
            how_to_use = Column(Text, default=None)
            specification = Column(Text, default=None)

        self.ProductTranslation = ProductTranslation

    def create_table(self):
        self.Base.metadata.create_all(self.engine)

    def insert_record(self, fields):
        """
        Insert a record into the database.

        @param fields: A dictionary containing field names and their values.
        @returns: None
        @code
        # Example usage:
        fields = {
            'product_reference': 'reference_product_value',
            'locale': 'en',
            'name': 'Product Name',
            'description': 'Description of the product',
            'link_rewrite': 'product-name'
        }
        manager.insert_record(fields)
        @endcode
        """
        """
        Inserts a record into the product translation table.

        If a record with the same product_reference and locale already exists,
        it logs a warning.

        @param fields: A dictionary containing field names and their values.
        @type fields: dict
        """
        try:
            # Check if the record already exists
            record_exists = self.session.query(self.ProductTranslation).filter_by(
                product_reference=fields.get('product_reference'),
                locale=fields.get('locale')
            ).first()

            if record_exists:
                logger.warning("Record with product_reference {} and locale {} already exists.".format(
                    fields.get('product_reference'), fields.get('locale')))
                return

            # Insert record into product_translations
            record = self.ProductTranslation(**fields)
            self.session.add(record)
            self.session.commit()
            logger.success("Record successfully added.")
        except Exception as ex:
            logger.error("Error adding record:", ex)

    def select_record(self, **kwargs) -> list:
        """
                @param kwards: Параметр `kwargs` в методе `select_record` позволяет передавать условия фильтрации
       для выборки записей из таблицы. Каждый аргумент в `kwargs` представляет собой пару ключ-значение, 
       где ключ - это название поля в таблице, а значение - это условие, по которому будет осуществляться фильтрация.
       
        Примеры использования `kwargs`:

        1. Сравнение значений:
           @code
           manager.select_record(product_reference='reference_product_value')
           @endcode

        2. Проверка вхождения значения в список:
           @code
           manager.select_record(lang_iso_code=['en', 'ru'])
           @endcode

        3. Поиск подстроки в текстовом поле:
           @code
           manager.select_record(name_like='%Product%')
           @endcode

        4. Проверка на отсутствие значения NULL:
           @code
           manager.select_record(description_is_not_null=True)
           @endcode

        5. Проверка на принадлежность к списку значений:
           @code
           manager.select_record(locale_in=['en-US', 'ru-RU'])
           @endcode

        6. Комбинация условий с использованием логического оператора OR:
           @code
           manager.select_record(or_(ProductTranslation.locale == 'en', ProductTranslation.locale == 'ru'))
           @endcode

        При обработке `kwargs` в методе `select_record` происходит следующее:

        - Каждый ключ в `kwargs` анализируется для определения соответствующего поля в таблице.
        - В зависимости от ключа и возможных модификаторов (например, `like`, `in`, `is_null`), строится соответствующее условие фильтрации.
        - Полученные условия объединяются логическим оператором OR.
        - Наконец, формируется запрос к базе данных с учетом всех условий фильтрации, и возвращается список записей, удовлетворяющих этим условиям.

        Обобщенный список типов операций, которые часто используются при фильтрации записей в ORM (Object-Relational Mapping):

        ### Операции сравнения:
            ==, !=: Сравнение значений.
            >, <, >=, <=: Больше, меньше, больше или равно, меньше или равно.
    
        ### Операции с контейнерами:
            in, not in: Проверка вхождения значения в список.
            like, ilike: Поиск подстроки в текстовых полях.
            regexp, iregexp: Проверка на соответствие регулярному выражению.
    
    
        ### Операции над NULL:
            is null, is not null: Проверка на отсутствие или наличие значения NULL.
        
        ### Операции временных интервалов и дат:
            between: Проверка на принадлежность значения диапазону.
            within_time_range: Проверка на вхождение в определенный временной интервал.
    
        ### Логические операции:
            and, or, not: Комбинация условий с использованием логических операторов.
    
        ### Географические операции:
            within_distance, intersects: Проверка вхождения в географическую область.
    
        ### Проверка на принадлежность к списку или классу:
            has, any: - Проверка на принадлежность к списку или наличие связанных записей.
            is_a: - Проверка на принадлежность к определенному классу.
        
        ## Примеры использования:
    
        # Сравнение значений
        manager.select_record(product_reference='reference_product_value')
    
        # Проверка вхождения значения в список
        manager.select_record(lang_iso_code=['en', 'ru'])
    
        # Поиск подстроки в текстовом поле
        manager.select_record(name_like='%Product%')
    
        # Проверка на отсутствие значения NULL
        manager.select_record(description_is_not_null=True)
    
        # Проверка на принадлежность к списку значений
        manager.select_record(locale_in=['en-US', 'ru-RU'])
    
        # Комбинация условий с использованием логического оператора OR
        manager.select_record(or_(ProductTranslation.locale == 'en', ProductTranslation.locale == 'ru'))
       
        @code
        # Example usage:
        records = manager.select_record(product_reference='reference_product_value')
        for record in records:
            print(record.name, record.description)

        records = manager.select_record(or_(
            ProductTranslation.locale == 'en',
            ProductTranslation.locale == 'ru'
        ))
        @endcode
        """
        try:
            query = self.session.query(self.ProductTranslation)
            filters = []
    
            for key, value in kwargs.items():
                if value is None:
                    continue
        
                if key == 'product_reference':
                    filters.append(self.ProductTranslation.product_reference == value)
                elif key == 'locale':
                    filters.append(self.ProductTranslation.locale == value)
                elif key.endswith('_like'):
                    column_name = key.split('_like')[0]
                    filters.append(getattr(self.ProductTranslation, column_name).like(value))
                elif key.endswith('_in'):
                    column_name = key.split('_in')[0]
                    filters.append(getattr(self.ProductTranslation, column_name).in_(value))
                elif key.endswith('_is_null'):
                    column_name = key.split('_is_null')[0]
                    if value:
                        filters.append(getattr(self.ProductTranslation, column_name) == None)
                    else:
                        filters.append(getattr(self.ProductTranslation, column_name) != None)
                else:
                    filters.append(getattr(self.ProductTranslation, key) == value)
        
            if filters:
                query = query.filter(or_(*filters))
        
            records = query.all()
            return records

        except Exception as ex:
            logger.error("Error selecting records:", ex)
            #traceback.print_exc(file=sys.stdout)

    def update_record(self, product_reference, locale, **fields):
        """
        Update a record in the database.

        @param product_reference: The product reference identifier.
        @param locale: The language locale.
        @param fields: Keyword arguments representing fields to be updated.
        @returns: None
        @code
        # Example usage:
        manager.update_record('reference_product_value', 'en', description='Updated description')
        @endcode
        """
        try:
            query = self.session.query(self.ProductTranslation).filter_by(product_reference=product_reference, locale=locale).first()
            if query:
                for key, value in fields.items():
                    setattr(query, key, value)
                self.session.commit()
                logger.success("Record successfully updated.")
            else:
                logger.error("Record not found.")
        except Exception as ex:
            logger.error("Error updating record:", ex)
            #traceback.print_exc(file=sys.stdout)

    def delete_record(self, product_reference, locale):
        """
        Delete a record from the database.

        @param product_reference: The product reference identifier.
        @param locale: The language locale.
        @returns: None
        @code
        # Example usage:
        manager.delete_record('reference_product_value', 'en')
        @endcode
        """
        try:
            query = self.session.query(self.ProductTranslation).filter_by(product_reference=product_reference, locale=locale).first()
            if query:
                self.session.delete(query)
                self.session.commit()
                logger.success("Record successfully deleted.")
            else:
                logger.error("Record not found.")
        except Exception as ex:
            logger.error("Error deleting record:", ex)
            #traceback.print_exc(file=sys.stdout))