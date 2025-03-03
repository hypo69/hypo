## \file /src/db/manager_translations/category_translations.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.db.manager_translations 
	:platform: Windows, Unix
	:synopsis:

"""


from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_
...
import header
from src import gs
from src.logger.logger import logger

class CategoryTranslationsManager:
    """Пример использования:
    manager = CategoryTranslationsManager()
    manager.insert_record({'id_category': 1, 'lang_iso_code': 'en', 'name': 'Category Name', 'description': 'Category Description'})
    manager.select_record(id_category=1)
    manager.update_record(1, 'en', {'description': 'Updated description'})
    manager.delete_record(1, 'en')
    """
    def __init__(self, *args, credentials, **kwargs):
        
        connection_string = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}".format(
        **{
            "user": credentials['username'],
            "password": credentials['password'],
            "host": credentials['server'],
            "port": credentials['port'],
            "database": credentials['db_name']
            }
        )
        self.engine = create_engine(connection_string)
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.define_model()
        self.create_table()

    def define_model(self):
        class CategoryTranslation(self.Base):
            __tablename__ = 'category_translations'
            
            id_category = Column(Integer, primary_key=True)
            lang_iso_code = Column(String(6), default=None, comment='Двухбуквенный код языка. Например: "en", "ru", "he"')
            lang_code = Column(String(8), default=None, comment='Локаль в том виде, как его часто представляет сервер поставщика. Например: "en-US", "he-IL", "ru-RU"')
            lang_supplier_site = Column(String(8), nullable=False, comment='Язык сайта поставщика. Я могу собирать с мультиязычных сайтов контент на разных языках. Хорошо зранить их как ключ')
            name = Column(String(128), nullable=False)
            description = Column(Text, default=None)
            additional_description = Column(Text, default=None)
            link_rewrite = Column(String(128), nullable=False)
            meta_title = Column(String(255), default=None)
            meta_keywords = Column(String(255), default=None)
            meta_description = Column(String(512), default=None)

        self.CategoryTranslation = CategoryTranslation

    def create_table(self):
        self.Base.metadata.create_all(self.engine)

    def insert_record(self, fields):
        """Функция принимает словарь полей в форме {'field_name':'field_value'}"""
        record = self.CategoryTranslation(**fields)
        self.session.add(record)
        self.session.commit()
        print("Запись успешно добавлена.")

    def select_record(self, **kwargs):
        """Обобщенный список типов операций, которые часто используются при фильтрации записей в ORM (Object-Relational Mapping):

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
        manager.select_record(id_category=1)
    
        # Проверка вхождения значения в список
        manager.select_record(lang_iso_code=['en', 'ru'])
    
        # Поиск подстроки в текстовом поле
        manager.select_record(name_like='%Category%')
    
        # Проверка на отсутствие значения NULL
        manager.select_record(description_is_not_null=True)
    
        # Проверка на принадлежность к списку значений
        manager.select_record(lang_supplier_site_in=['en-US', 'ru-RU'])
    
        # Комбинация условий с использованием логического оператора OR
        manager.select_record(or_(CategoryTranslation.locale == 'en', CategoryTranslation.locale == 'ru'))
        """
        query = self.session.query(self.CategoryTranslation)
        filters = []
    
        for key, value in kwargs.items():
            if value is None:
                continue
        
            if key == 'id_category':
                filters.append(self.CategoryTranslation.id_category == value)
            elif key == 'lang_iso_code':
                filters.append(self.CategoryTranslation.locale == value)
            elif key == 'locale':
                filters.append(self.CategoryTranslation.locale == value)
            elif key.endswith('_like'):
                column_name = key.split('_like')[0]
                filters.append(getattr(self.CategoryTranslation, column_name).like(value))
            elif key.endswith('_in'):
                column_name = key.split('_in')[0]
                filters.append(getattr(self.CategoryTranslation, column_name).in_(value))
            elif key.endswith('_is_null'):
                column_name = key.split('_is_null')[0]
                if value:
                    filters.append(getattr(self.CategoryTranslation, column_name) == None)
                else:
                    filters.append(getattr(self.CategoryTranslation, column_name) != None)
            else:
                filters.append(getattr(self.CategoryTranslation, key) == value)
        
        if filters:
            query = query.filter(or_(*filters))
        
        records = query.all()
        return records

    def update_record(self, id_category, lang_iso_code, **fields):
        query = self.session.query(self.CategoryTranslation).filter_by(id_category=id_category, lang_iso_code=lang_iso_code).first()
        if query:
            for key, value in fields.items():
                setattr(query, key, value)
            self.session.commit()
            print("Запись успешно обновлена.")
        else:
            print("Запись не найдена.")


    def delete_record(self, id_category, lang_iso_code):
        query = self.session.query(self.CategoryTranslation).filter_by(id_category=id_category, lang_iso_code=lang_iso_code).first()
        if query:
            self.session.delete(query)
            self.session.commit()
            print("Запись успешно удалена.")
        else:
            print("Запись не найдена.")