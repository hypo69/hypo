## \file /src/db/manager_coupons_and_sales/product_campaigns.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.db.manager_coupons_and_sales 
	:platform: Windows, Unix
	:synopsis: Купоны, скидки и т.п. для товаров PrestaShop

"""


from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import Column, Integer, DateTime, String, MetaData, Table, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import header
from src import gs
from src.logger.logger import logger

Base = declarative_base()
metadata = MetaData()

class ProductCampaignsManager:
    """
    Manager class for interacting with product campaigns in the database.
    """

    def __init__(self, credentials):
        """
        Initializes the ProductCampaignsManager.
        """
        # Create database engine
        connection_string = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}".format(
            **{ 
                "host": credentials['db_server'],
                "port": credentials['db_port'],
                "database": credentials['db_name'],
                "user": credentials['db_user'],
                "password": credentials['db_password'], 
            }
        )
        self.engine = create_engine(connection_string)

        # Create session maker
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        # Define model and create table
        self.define_model()
        self.create_table()
        ...
    ...
    
    # Define __enter__ method to support context manager protocol
    def __enter__(self):
        return self
    ...
    
    # Define __exit__ method to support context manager protocol
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Optionally, add cleanup code here
        ...
    ...
    class ProductCampaign(Base):
        __tablename__ = 'wxrq_product_campaigns'
        id = Column(Integer, primary_key=True)
        id_campaign = Column(Integer)
        #id_product = Column(Integer, ForeignKey('wxrq_product.id_product'))  # Foreign key to wxrq_product
        id_product = Column(Integer)
        coupon_code = Column(Integer)
        campaign_start_date = Column(DateTime)
        campaign_end_date = Column(DateTime)
        

    def define_model(self):
        """
        Defines the model for the product campaign table.
        """
        global metadata
        wxrq_product = Table(
            'wxrq_product',
            metadata,
            #Column('id_product', Integer, primary_key=True),
            Column('id_product', Integer),
            Column('reference', String(50)),  
                                            # <- Add other columns as needed
            extend_existing=True
        )
        ...

    ...
    
    def create_table(self):
        """
        Creates the table in the database if it doesn't exist.
        """
        Base.metadata.create_all(self.engine)
    ...
    
    def insert_record(self, fields):
        """
        Inserts a record into the product campaign table.

        @param fields: A dictionary containing field names and their values.
        @type fields: dict

        @code
            fields = {
                'id_product': 1,
                'id_campaign': 3,
                'coupon_code': 1,
                'campaign_start_date': 'DDMMYYHHMM',
                'campaign_end_date': 'DDMMYYHHMM',
            }
            manager.insert_record(fields)
        """
        try:
            # Get id_product from wxrq_product based on reference
            reference = fields.get('reference')
            if reference:
                wxrq_product = metadata.tables['wxrq_product']

                query = select(wxrq_product).where(wxrq_product.c.reference == reference)
                result = self.session.execute(query)
                product_row = result.fetchone()
                if product_row:
                    #fields['id_product'] = product_row['id_product']
                    fields['id_product'] = product_row[0]
                else:
                    logger.error("No product found with reference: ", reference)
                    ...
                    return

            # Insert record into wxrq_product_campaigns
            del fields['reference']    
            record = self.ProductCampaign(**fields)
            self.session.add(record)
            self.session.commit()
            logger.success("Record successfully added.")
        except Exception as ex:
            ...
            logger.error("Error adding record:", ex)
    
    def select_record(self, **kwargs):
        """
        Selects records from the product campaign table based on the provided criteria.

        @param kwargs: Keyword arguments representing field names and their values for filtering.
        @type kwargs: dict

        @return: A list of records that match the provided criteria.
        @rtype: list

        @code
            records = manager.select_record(id_cart=1)
        """
        try:
            query = self.session.query(self.ProductCampaign)
            filters = []

            for key, value in kwargs.items():
                if value is not None:
                    filters.append(getattr(self.ProductCampaign, key) == value)

            if filters:
                query = query.filter(*filters)

            records = query.all()
            return records
        except Exception as ex:
            logger.error("Error selecting records:", ex)
    ...
    
    def update_record(self, id_cart, id_product, **fields):
        """
        Updates a record in the product campaign table.

        @param id_cart: The cart ID.
        @type id_cart: int
        @param id_product: The product ID.
        @type id_product: int
        @param fields: Keyword arguments representing fields to be updated.
        @type fields: dict

        @code
            manager.update_record(1, 2, id_address_delivery=4)
        """
        try:
            query = self.session.query(self.ProductCampaign).filter_by(id_cart=id_cart, id_product=id_product).first()
            if query:
                for key, value in fields.items():
                    setattr(query, key, value)
                self.session.commit()
                logger.success("Record successfully updated.")
            else:
                logger.error("Record not found.")
        except Exception as ex:
            logger.error("Error updating record:", ex)
    ...
    
    def delete_record(self, id_cart, id_product):
        """
        Deletes a record from the product campaign table.

        @param id_cart: The cart ID.
        @type id_cart: int
        @param id_product: The product ID.
        @type id_product: int

        @code
            manager.delete_record(1, 2)
        """
        try:
            query = self.session.query(self.ProductCampaign).filter_by(id_cart=id_cart, id_product=id_product).first()
            if query:
                self.session.delete(query)
                self.session.commit()
                logger.success("Record successfully deleted.")
            else:
                logger.error("Record not found.")
        except Exception as ex:
            logger.error("Error deleting record:", ex)