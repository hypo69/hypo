## \file /src/db/manager_categories/suppliers_categories.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.db.manager_categories 
	:platform: Windows, Unix
	:synopsis: Модуль обработки категорий.
сервер: davidka.net
db: uXXXXXXX_splr_catgories
 Для каждого поставщика есть таблица дерева категорий.
 Я сравниваю актуальные категории на сайте поставщика и храню их в таблицах поставщиков

"""


""" 
"""
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey 
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

from src import gs
from src.logger.logger import logger
from src.utils.printer import pprint

import header
from src import gs
from src.logger.logger import logger

# Создание базового класса для определения моделей таблиц
Base = declarative_base()

# Определение абстрактного базового класса для категорий
class BaseCategory(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    id_category_supplier = Column(Integer, unique=True)
    id_parent_category_supplier = Column(Integer, nullable=True)
    id_category_hypotez = Column(Integer, nullable=True)
    id_parent_category_hypotez = Column(Integer, nullable=True)
    url_category_supplier = Column(String(100), nullable=True)
    name_category_supplier = Column(String(100), nullable=True)
    name_category_hypotez = Column(String(100), nullable=True)
    

# Определение конкретных классов для каждой категории
class AliexpressCategory(BaseCategory):
    __tablename__ = 'aliexpress'

class AmazonCategory(BaseCategory):
    __tablename__ = 'amazon'

class EbayCategory(BaseCategory):
    __tablename__ = 'ebay'

class KualaCategory(BaseCategory):
    __tablename__ = 'kuala'

class HbCategory(BaseCategory):
    __tablename__ = 'hb'

# Класс для управления категориями
class CategoryManager:
    def __init__(self, *args, **kwargs):
        """ Инициализирует менеджер категорий.

        Подключается к базе данных и создает сессию для выполнения запросов.

        @param args: Позиционные аргументы.
        @param kwargs: Именованные аргументы.
        """
        # Формирование строки подключения к базе данных
        connection_string = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}".format(
            **{
                "host": credentials['db_server'],
                "port": credentials['db_port'],
                "database": credentials['db_name'],
                "user": credentials['db_user'],
                "password": credentials['db_password'],
            }
        )
        # Создание механизма для работы с базой данных
        self.engine = create_engine(connection_string)
        # Создание сессии для выполнения запросов
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session() 
        

        # Создание таблиц, если они еще не существуют
        self.create_table(AliexpressCategory)
        self.create_table(AmazonCategory)
        self.create_table(EbayCategory)
        self.create_table(KualaCategory)
        self.create_table(HbCategory)
        
        # Define __enter__ method to support context manager protocol
    def __enter__(self):
        return self
    ...
    
    # Define __exit__ method to support context manager protocol
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Optionally, add cleanup code here
        ...

    def create_table(self, table):
        """
        Создает таблицу в базе данных, если она еще не существует.

        @param table: Класс таблицы, для которой требуется создать таблицу в базе данных.
        """
        table.__table__.create(self.engine, checkfirst=True)
    ...
        
    

    def insert_record(self, table, fields):
        """
        Выполняет операцию INSERT для указанной таблицы с указанными данными.

        @param table: Класс таблицы, в которую выполняется вставка данных.
        @param fields: Словарь с данными для вставки в формате {поле: значение}.
        @code
        manager = CategoryManager()
        @code
        # Пример данных для вставки в таблицу
        category_fields = {
            'id_category_supplier': 123,  # Пример значения id_category_supplier
            'name_category_supplier': 'Example Category',  # Пример имени категории
            'id_parent_category_supplier': None,  # Пример значения id_parent_category_supplier (если категория верхнего уровня, то None)
            # Добавьте остальные поля категории, если необходимо
        }

        # Вставка записи в таблицу AliexpressCategory (или любую другую, указанную в table)
        manager.insert_record(AliexpressCategory, category_fields)
        @endcode
        """
        try:
            id_category_supplier = fields.get('id_category_supplier')
            id_parent_category_supplier = fields.get('id_parent_category_supplier')

            # Проверка, существует ли запись с такими значениями id_parent_category_supplier и id_category_supplier
            existing_record = self.session.query(table).filter_by(
                id_category_supplier=id_category_supplier,
                id_parent_category_supplier=id_parent_category_supplier
            ).first()

            if existing_record:
                logger.warning(f"""
                               Таблица соответствий категорий моего сайта и алиэкспресс
                               Record with id_category_supplier={id_category_supplier} and 
                               id_parent_category_supplier={id_parent_category_supplier} already exists.""")
                return

            record = table(**fields)
            self.session.add(record)
            self.session.commit()
            logger.success("Record successfully added.")
        except IntegrityError as ex:
            self.session.rollback()
            logger.error("Error adding record:", pprint(ex))
        except Exception as ex:
            self.session.rollback()
            logger.error("Unexpected error adding record:", ex)

    ...
    def select_record(self, table, fields):
        """ Executes an INSERT operation for the specified table with the given data.

        @param table: The table class into which to insert the data.
        @param fields: A dictionary with data to be inserted in the format {field: value}.
        
        @code
        Примеры вызова функции `select_record` с различными комбинациями условий:

        # 1. Простой вызов с одним условием:
    
        records = category_manager.select_record(AmazonCategory, id_category_supplier=123)
    

        # 2. Вызов с несколькими условиями:
    
        records = category_manager.select_record(AmazonCategory, id_category_supplier=123, id_parent_category_supplier=456)
    

        # 3. Использование оператора `OR`:
    
        from sqlalchemy import or_

        records = category_manager.select_record(AmazonCategory, or_(AmazonCategory.id_category_supplier == 123, AmazonCategory.id_parent_category_supplier == 456))
    

        # 4. Использование оператора `LIKE`:
    
        records = category_manager.select_record(AmazonCategory, name_category_supplier='%electronics%')
    

        # 5. Комбинация операторов `AND`, `OR`, `LIKE`:
    
        from sqlalchemy import and_

        records = category_manager.select_record(AmazonCategory, 
                                                and_(AmazonCategory.id_category_supplier == 123, 
                                                     or_(AmazonCategory.id_parent_category_supplier == 456, 
                                                         AmazonCategory.name_category_supplier.like('%electronics%'))))
    

        Можно комбинировать различные условия, чтобы получить нужный результат выборки из базы данных.
            @endcode
        """
        try:
            # Формирование запроса SELECT с учетом переданных условий
            query = self.session.query(table)
            filters = []

            # Добавляем условия из fields
            for key, value in fields.items():
                if value is None:
                    continue
                
                # Если значение начинается с '%' и заканчивается на '%', используем LIKE
                if isinstance(value, str) and value.startswith('%') and value.endswith('%'):
                    filters.append(getattr(table, key).like(value))
                else:
                    filters.append(getattr(table, key) == value)

            if filters:
                query = query.filter(and_(*filters))

            records = query.all()
            return records

        except Exception as ex:
            logger.error("Error selecting records:", ex)
    ...
    
    def update_record(self, table, hypotez_category_id, category_id, **fields):
        """
        Выполняет операцию UPDATE для указанной таблицы с указанными данными и условиями.

        @param table: Класс таблицы, в которой выполняется обновление.
        @param hypotez_category_id: Значение поля hypotez_category_id для определения записи.
        @param category_id: Значение поля category_id для определения записи.
        @param fields: Данные для обновления в формате поле=значение.
        """
        try:
            # Формирование запроса UPDATE с учетом переданных данных и условий
            query = self.session.query(table).filter_by(hypotez_category_id=hypotez_category_id, category_id=category_id).first()
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
    
    def delete_record(self, table, hypotez_category_id, category_id):
        """
        Выполняет операцию DELETE для указанной таблицы с указанными условиями.

        @param table: Класс таблицы, из которой выполняется удаление записи.
        @param hypotez_category_id: Значение поля hypotez_category_id для определения записи.
        @param category_id: Значение поля category_id для определения записи.
        """
        try:
            # Формирование запроса DELETE с учетом переданных условий
            query = self.session.query(table).filter_by(hypotez_category_id=hypotez_category_id, category_id=category_id).first()
            if query:
                self.session.delete(query)
                self.session.commit()
                logger.success("Record successfully deleted.")
            else:
                logger.error("Record not found.")
        except Exception as ex:
            logger.error("Error deleting record:", ex)
    ...
    
    def clear_table(self, table):
        """
        Очищает указанную таблицу.

        @param table: Класс таблицы, которую требуется очистить.
        """
        try:
            # Формируем запрос для удаления всех записей из таблицы
            self.session.query(table).delete()
            self.session.commit()
            logger.success("Table successfully cleared.")
        except Exception as ex:
            logger.error("Error clearing table:", ex)
            
    def get_categories_hierarchy(self, table_class) -> dict:
        """
        Retrieves categories from the specified table and constructs a hierarchical JSON.

        @param table_class: The table class from which to retrieve categories.
        @return: Hierarchical JSON representation of categories.
        @code
        # Usage:
        manager = CategoryManager()
        hierarchical_json = manager.get_categories_hierarchy(AliexpressCategory)  # Specify the category table class here
        print(json.dumps(hierarchical_json, indent=4))
        """
        categories = self.session.query(table_class).all()
        hierarchy = {}

        for category in categories:
            category_dict = {
                'id': category.id_category_supplier,
                'name': category.name_category_supplier,
                'children': []
            }

            if category.id_parent_category_supplier is None:
                hierarchy[category.id_category_supplier] = category_dict
            else:
                parent_id = category.id_parent_category_supplier
                if parent_id not in hierarchy:
                    hierarchy[parent_id] = {'children': []}
                hierarchy[parent_id]['children'].append(category_dict)

        # Convert hierarchy to list of top-level categories
        top_level_categories = []
        for category_id, category_info in hierarchy.items():
            if 'id' in category_info:
                top_level_categories.append(category_info)

        return top_level_categoriess