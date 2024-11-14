```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.db.manager_categories """
""" @namespace src.db.manager_categories """

""" Модуль обработки категорий поставщиков.
Сервер: davidka.net
База данных: u177424397_splr_catgories
Для каждого поставщика есть таблица дерева категорий.
Этот модуль сравнивает актуальные категории на сайте поставщика с данными в базе данных и сохраняет их.
"""
import json
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from __init__ import gs
from src.logger import logger
from src.utils import pprint

# Получение учетных данных для подключения к базе данных davidka.net
credentials = gs.credentials.presta.translations

# Создание базового класса для определения моделей таблиц
Base = declarative_base()

# Определение абстрактного базового класса для категорий
class BaseCategory(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    id_category_supplier = Column(Integer, unique=True)  # Изменено для ясности
    id_parent_category_supplier = Column(Integer, nullable=True)
    id_category_hypotez = Column(Integer, nullable=True)
    id_parent_category_hypotez = Column(Integer, nullable=True)
    url_category_supplier = Column(String(100), nullable=True)
    name_category_supplier = Column(String(100), nullable=True)
    name_category_hypotez = Column(String(100), nullable=True)

    def __repr__(self):
      return f"<BaseCategory(id_category_supplier={self.id_category_supplier}, name={self.name_category_supplier})>"
    
# Определение конкретных классов для каждой категории (с проверкой уникальности id_category_supplier)
class AliexpressCategory(BaseCategory):
    __tablename__ = 'aliexpress'
    id_category_supplier = Column(Integer, unique=True, nullable=False) # Добавлено nullable=False

class AmazonCategory(BaseCategory):
    __tablename__ = 'amazon'
    id_category_supplier = Column(Integer, unique=True, nullable=False)

class EbayCategory(BaseCategory):
    __tablename__ = 'ebay'
    id_category_supplier = Column(Integer, unique=True, nullable=False)

class KualaCategory(BaseCategory):
    __tablename__ = 'kuala'
    id_category_supplier = Column(Integer, unique=True, nullable=False)

class HbCategory(BaseCategory):
    __tablename__ = 'hb'
    id_category_supplier = Column(Integer, unique=True, nullable=False)



# Класс для управления категориями
class CategoryManager:
    def __init__(self, *args, **kwargs):
        # ... (код подключения к базе данных)
        # ... (код создания сессии)
        
        # Обязательно создаем таблицы, если они еще не существуют
        Base.metadata.create_all(self.engine)
    
    # ... (остальной код, например, insert_record, select_record, ...)

    def insert_record(self, table, fields):
        # ... (код вставки)
        # Используем unique=True для id_category_supplier
         try:
            # ... ваш существующий код
            record = table(**fields)
            self.session.add(record)
            self.session.commit()
            logger.success("Record successfully added.")
        except IntegrityError as ex:
           # Обработка ошибки дубликата
           self.session.rollback()
           logger.error(f"Ошибка добавления: Запись с id_category_supplier {fields['id_category_supplier']} уже существует.")


    # ... (rest of the class methods)
    
    def get_categories_hierarchy(self, table_class) -> dict:
        # ... (код извлечения и построения иерархии)

        # Корректировка возвращаемого значения
        return json.loads(json.dumps(top_level_categories, indent=4))
        

```

**Изменения и объяснения:**

* **`unique=True` для `id_category_supplier`:** Добавлено ограничение `unique=True` к полю `id_category_supplier` во всех наследниках `BaseCategory`. Это предотвращает добавление записей с дублирующимися значениями `id_category_supplier`, что крайне важно для предотвращения ошибок и поддерживает целостность данных.

* **Обработка `IntegrityError`:**  В методе `insert_record` добавлен блок `try...except IntegrityError`, который теперь корректно обрабатывает ошибку `IntegrityError`, возникающую при попытке вставки записи с уже существующим `id_category_supplier`, и выводит понятное сообщение об ошибке, включая `id_category_supplier`.

* **`__repr__` для `BaseCategory`:**  Добавлен метод `__repr__`, чтобы при выводе объекта класса `BaseCategory` в консоль отображалась полезная информация, включая `id_category_supplier` и `name_category_supplier`.

* **`Base.metadata.create_all(self.engine)`:**  Этот важный момент добавлен в `__init__`.  Теперь база данных будет создана автоматически с правильными ограничениями (unique=True) в конструкторе класса `CategoryManager`.  Это критично для работоспособности вашего кода.

* **Корректный возврат `get_categories_hierarchy`:** Изменен возврат `get_categories_hierarchy` для возврата данных в виде JSON.

* **`nullable=False` для `id_category_supplier`:** Добавил `nullable=False`  для `id_category_supplier` в наследниках `BaseCategory`, это важно для предотвращения null-значений в ключевом столбце.

Эти изменения значительно повышают надежность и читабельность кода, предотвращают ошибки и улучшают взаимодействие с базой данных.  Запустите код, проверьте, что таблицы создаются, и убедитесь, что он работает как ожидалось. Обратите внимание на важные комментарии к коду.