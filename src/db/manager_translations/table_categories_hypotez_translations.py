## \file /src/db/manager_translations/table_categories_hypotez_translations.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.db.manager_translations 
	:platform: Windows, Unix
	:synopsis:

"""


...
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_
...
import header
from src import gs
from src.logger.logger import logger

class CategoriesHypotezFullListManager:
    """Пример использования:
    manager = CategoriesHypotezFullListManager(credentials)
    manager.insert_record(1, 1, 1, 0, 1, 2, 1, '2024-04-11 12:00:00', '2024-04-11 12:00:00', 1, 0)
    manager.select_record(id_category=1, id_parent=1, id_shop_default=1, active=1)
    manager.update_record(1, 1, 1, '2024-04-11 12:00:00', 'Updated category description')
    """
    def __init__(self, credentials, *args, **kwargs):
        
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

    def define_model(self):
        class CategoryManager(self.Base):
            __tablename__ = 'categories_hypotez'
            
            id_category = Column(Integer, primary_key=True)
            id_parent = Column(Integer)
            id_shop_default = Column(Integer)
            level_depth = Column(Integer)
            nleft = Column(Integer)
            nright = Column(Integer)
            active = Column(Boolean)
            date_add = Column(DateTime, nullable=False)
            date_upd = Column(DateTime, nullable=False)
            position = Column(Integer)
            is_root_category = Column(Boolean)

        self.CategoryManager = CategoryManager

    def create_table(self):
        self.Base.metadata.create_all(self.engine)

    def insert_record(self, id_category, id_parent, id_shop_default, level_depth, nleft, nright, active, date_add, date_upd, position, is_root_category):
        new_translation = self.CategoryManager(
            id_category=id_category,
            id_parent=id_parent,
            id_shop_default=id_shop_default,
            level_depth=level_depth,
            nleft=nleft,
            nright=nright,
            active=active,
            date_add=date_add,
            date_upd=date_upd,
            position=position,
            is_root_category=is_root_category
        )
        self.session.add(new_translation)
        self.session.commit()
        print("Запись успешно добавлена.")

    def select_record(self, **kwargs):
        query = self.session.query(self.CategoryManager)
        
        # Построение фильтра на основе переданных аргументов
        filters = []
        for key, value in kwargs.items():
            if value is None:
                # Если значение аргумента пустое, игнорируем его
                continue
            # Добавляем условие для фильтрации
            filters.append(getattr(self.CategoryManager, key) == value)
            
        # Применяем фильтры
        if filters:
            query = query.filter(*filters)
        
        # Выполняем запрос
        categories = query.all()
        for category in categories:
            print("ID категории:", category.id_category)
            print("ID родительской категории:", category.id_parent)
            print("ID магазина по умолчанию:", category.id_shop_default)
            print("Уровень глубины:", category.level_depth)
            print("Левый индекс:", category.nleft)
            print("Правый индекс:", category.nright)
            print("Активная:", category.active)
            print("Дата добавления:", category.date_add)
            print("Дата обновления:", category.date_upd)
            print("Позиция:", category.position)
            print("Это корневая категория:", category.is_root_category)

    def update_record(self, id_category, id_parent, id_shop_default, date_upd, new_description):
        translation = self.session.query(self.CategoryManager).filter_by(id_category=id_category, id_parent=id_parent))