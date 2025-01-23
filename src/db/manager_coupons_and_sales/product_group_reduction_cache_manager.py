## \file /src/db/manager_coupons_and_sales/product_group_reduction_cache_manager.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.db.manager_coupons_and_sales 
	:platform: Windows, Unix
	:synopsis:

"""


""" 
@code
# Create an instance of the manager
manager = ProductGroupReductionCacheManager()

# Example for inserting a record
insert_fields = {
    'id_product': 1,
    'id_group': 2,
    'reduction': 0.1
}
manager.insert_record(insert_fields)

# Example for selecting records
# Select records where id_product equals 1
records = manager.select_record(id_product=1)
for record in records:
    print(record.id_product, record.id_group, record.reduction)

# Example for updating a record
# Update the reduction value for the record with id_product=1 and id_group=2
manager.update_record(1, 2, reduction=0.2)

# Example for deleting a record
# Delete the record where id_product=1 and id_group=2
manager.delete_record(1, 2)

@endcode
"""
...

...
import sys
import traceback
from sqlalchemy import create_engine, Column, Integer, ForeignKey, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_

from src import gs
from src.logger.logger import logger

#credentials = gs.db_translations_credentials

class ProductGroupReductionCacheManager:
    """
    Example usage:

    1. Initialize the manager:
    manager = ProductGroupReductionCacheManager()

    2. Insert a record:
    fields = {
        'id_product': 1,
        'id_group': 2,
        'reduction': 0.1
    }
    manager.insert_record(fields)

    3. Select records:
    records = manager.select_record(id_product=1)
    for record in records:
        print(record.id_product, record.id_group, record.reduction)

    4. Update a record:
    manager.update_record(1, 2, reduction=0.2)

    5. Delete a record:
    manager.delete_record(1, 2)
    """

    def __init__(self, credentials):
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
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.define_model()
        self.create_table()
        
    # Define __enter__ method to support context manager protocol
    def __enter__(self):
        return self
    ...
    
    # Define __exit__ method to support context manager protocol
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Optionally, add cleanup code here
        ...

    def define_model(self):
        class ProductGroupReductionCache(self.Base):
            __tablename__ = 'wxrq_product_group_reduction_cache'
            id = Column(Integer, primary_key=True)
            id_product = Column(Integer, ForeignKey('your_product_table.id'))
            id_group = Column(Integer)
            reduction = Column(Float)

        self.ProductGroupReductionCache = ProductGroupReductionCache

    def create_table(self):
        self.Base.metadata.create_all(self.engine)

    def insert_record(self, fields):
        try:
            record = self.ProductGroupReductionCache(**fields)
            self.session.add(record)
            self.session.commit()
            logger.success("Record successfully added.")
        except Exception as ex:
            logger.error("Error adding record:", ex)

    def select_record(self, **kwargs):
        try:
            query = self.session.query(self.ProductGroupReductionCache)
            filters = []

            for key, value in kwargs.items():
                if value is None:
                    continue

                filters.append(getattr(self.ProductGroupReductionCache, key) == value)

            if filters:
                query = query.filter(*filters)

            records = query.all()
            return records
        except Exception as ex:
            logger.error("Error selecting records:", ex)

    def update_record(self, id_product, id_group, **fields):
        try:
            query = self.session.query(self.ProductGroupReductionCache).filter_by(id_product=id_product, id_group=id_group).first()
            if query:
                for key, value in fields.items():
                    setattr(query, key, value)
                self.session.commit()
                logger.success("Record successfully updated.")
            else:
                logger.error("Record not found.")
        except Exception as ex:
            logger.error("Error updating record:", ex)

    def delete_record(self, id_product, id_group):
        try:
            query = self.session.query(self.ProductGroupReductionCache).filter_by(id_product=id_product, id_group=id_group).first()
            if query:
                self.session.delete(query)
                self.session.commit()
                logger.success("Record successfully deleted.")
            else:
                logger.error("Record not found.")
        except Exception as ex:
            logger.error("Error deleting record:", ex)