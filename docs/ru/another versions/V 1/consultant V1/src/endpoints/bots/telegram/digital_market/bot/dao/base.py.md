### Анализ кода модуля `base`

**Качество кода**:

- **Соответствие стандартам**: 8/10
- **Плюсы**:
    - Код хорошо структурирован и разбит на логические блоки, что облегчает его понимание.
    - Используется `pydantic` для валидации данных.
    - Применяется `asyncio` для асинхронных операций.
    - Есть логирование всех основных действий.
    - Используются `TypeVar` и `Generic` для обеспечения типобезопасности.
- **Минусы**:
    - Импорт `logger` выполнен из `loguru`, вместо `src.logger.logger`.
    - Есть повторяющиеся блоки `try-except` с одинаковой логикой обработки ошибок.
    - Не все функции имеют docstring в формате RST.
    - Используются двойные кавычки для логирования.

**Рекомендации по улучшению**:

1.  **Импорт логгера**:
    -   Заменить `from loguru import logger` на `from src.logger.logger import logger`.
2.  **Унификация кавычек**:
    -   Заменить двойные кавычки на одинарные в строках, которые не являются операциями вывода.
3.  **Улучшение обработки ошибок**:
    -   Вместо того чтобы использовать `raise e` после `logger.error`, можно просто использовать `raise`.
4.  **Документирование кода**:
    -   Добавить docstring в формате RST для всех методов.
5.  **Рефакторинг try-except**:
    -   Избавиться от дублирования блоков `try-except` за счет выноса общей логики обработки ошибок в отдельную функцию.
6. **Улучшить читаемость**:
    -  Заменить f-строки в логах на конкатенацию строк для соответствия стандарту.

**Оптимизированный код**:

```python
"""
Модуль, предоставляющий базовый класс для доступа к данным в БД.
==============================================================

Модуль содержит класс :class:`BaseDAO`, который предоставляет
основные методы для выполнения операций CRUD (создание, чтение, обновление, удаление)
с использованием SQLAlchemy и асинхронных сессий.

Пример использования
----------------------
.. code-block:: python

    from sqlalchemy.ext.asyncio import AsyncSession
    from bot.dao.database import Base
    from pydantic import BaseModel
    from typing import List
    
    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)

    class MyModelCreate(BaseModel):
       name: str

    class MyModelFilter(BaseModel):
        id: int | None = None
        name: str | None = None
    
    async def main():
        session: AsyncSession = ... # Replace with your session
        
        # Create instance of DAO for MyModel
        my_dao = BaseDAO[MyModel]
        my_dao.model = MyModel

        # Create
        new_record = await my_dao.add(session, MyModelCreate(name='Test'))
        
        # Read
        record = await my_dao.find_one_or_none_by_id(new_record.id, session)
        
        # Update
        await my_dao.update(session, MyModelFilter(id=new_record.id), MyModelCreate(name='Updated'))

        # Delete
        await my_dao.delete(session, MyModelFilter(id=new_record.id))
    
"""
from typing import List, Any, TypeVar, Generic

from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.logger.logger import logger  # Изменен импорт logger
from bot.dao.database import Base

# Объявляем типовой параметр T с ограничением, что это наследник Base
T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    """
    Базовый класс для доступа к данным.
    
    Предоставляет общие методы для выполнения операций CRUD.
    
    :param model: Модель SQLAlchemy, с которой работает DAO.
    :type model: Type[T]
    """
    model: type[T]

    @classmethod
    async def _handle_error(cls, e: SQLAlchemyError, message: str, session: AsyncSession):
        """
        Обрабатывает ошибки SQLAlchemy, откатывая сессию и логируя ошибку.

        :param e: Объект ошибки SQLAlchemy.
        :type e: SQLAlchemyError
        :param message: Сообщение для логирования.
        :type message: str
        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :raises SQLAlchemyError: Возвращает перехваченную ошибку после логирования.
        """
        await session.rollback()
        logger.error(message + str(e))
        raise  # Оставляем просто raise

    @classmethod
    async def find_one_or_none_by_id(cls, data_id: int, session: AsyncSession) -> T | None:
        """
        Асинхронно ищет запись по ее ID.

        :param data_id: ID записи для поиска.
        :type data_id: int
        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :return: Найденная запись или None, если запись не найдена.
        :rtype: T | None
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса к БД.

        Пример:
            >>> session: AsyncSession = ...
            >>> result = await BaseDAO[MyModel].find_one_or_none_by_id(1, session)
            >>> print(result)
             <MyModel...>
        """
        logger.info('Поиск ' + cls.model.__name__ + ' с ID: ' + str(data_id)) # Изменено на конкатенацию строк
        try:
            query = select(cls.model).filter_by(id=data_id)
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record:
                logger.info('Запись с ID ' + str(data_id) + ' найдена.') # Изменено на конкатенацию строк
            else:
                logger.info('Запись с ID ' + str(data_id) + ' не найдена.') # Изменено на конкатенацию строк
            return record
        except SQLAlchemyError as e:
            await cls._handle_error(e, 'Ошибка при поиске записи с ID ' + str(data_id) + ': ', session)

    @classmethod
    async def find_one_or_none(cls, session: AsyncSession, filters: BaseModel) -> T | None:
        """
        Асинхронно ищет одну запись по заданным фильтрам.

        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :param filters: Фильтры для поиска в виде объекта Pydantic BaseModel.
        :type filters: BaseModel
        :return: Найденная запись или None, если запись не найдена.
        :rtype: T | None
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса к БД.
        
        Пример:
            >>> session: AsyncSession = ...
            >>> filters = MyModelFilter(name='Test')
            >>> result = await BaseDAO[MyModel].find_one_or_none(session, filters)
            >>> print(result)
            <MyModel...>

        """
        filter_dict = filters.model_dump(exclude_unset=True)
        logger.info('Поиск одной записи ' + cls.model.__name__ + ' по фильтрам: ' + str(filter_dict)) # Изменено на конкатенацию строк
        try:
            query = select(cls.model).filter_by(**filter_dict)
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record:
                logger.info('Запись найдена по фильтрам: ' + str(filter_dict)) # Изменено на конкатенацию строк
            else:
                logger.info('Запись не найдена по фильтрам: ' + str(filter_dict)) # Изменено на конкатенацию строк
            return record
        except SQLAlchemyError as e:
            await cls._handle_error(e, 'Ошибка при поиске записи по фильтрам ' + str(filter_dict) + ': ', session)

    @classmethod
    async def find_all(cls, session: AsyncSession, filters: BaseModel | None = None) -> List[T]:
        """
        Асинхронно ищет все записи по заданным фильтрам.

        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :param filters: Фильтры для поиска в виде объекта Pydantic BaseModel или None.
        :type filters: BaseModel | None
        :return: Список найденных записей.
        :rtype: List[T]
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса к БД.
        
        Пример:
            >>> session: AsyncSession = ...
            >>> result = await BaseDAO[MyModel].find_all(session, MyModelFilter(name='Test'))
            >>> print(result)
            [<MyModel...>, <MyModel...>]
        """
        filter_dict = filters.model_dump(exclude_unset=True) if filters else {}
        logger.info('Поиск всех записей ' + cls.model.__name__ + ' по фильтрам: ' + str(filter_dict)) # Изменено на конкатенацию строк
        try:
            query = select(cls.model).filter_by(**filter_dict)
            result = await session.execute(query)
            records = result.scalars().all()
            logger.info('Найдено ' + str(len(records)) + ' записей.') # Изменено на конкатенацию строк
            return records
        except SQLAlchemyError as e:
            await cls._handle_error(e, 'Ошибка при поиске всех записей по фильтрам ' + str(filter_dict) + ': ', session)

    @classmethod
    async def add(cls, session: AsyncSession, values: BaseModel) -> T:
        """
        Асинхронно добавляет новую запись в базу данных.

        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :param values: Значения для новой записи в виде объекта Pydantic BaseModel.
        :type values: BaseModel
        :return: Созданная запись.
        :rtype: T
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса к БД.
        
        Пример:
            >>> session: AsyncSession = ...
            >>> values = MyModelCreate(name='Test')
            >>> result = await BaseDAO[MyModel].add(session, values)
            >>> print(result)
            <MyModel...>
        """
        values_dict = values.model_dump(exclude_unset=True)
        logger.info('Добавление записи ' + cls.model.__name__ + ' с параметрами: ' + str(values_dict)) # Изменено на конкатенацию строк
        new_instance = cls.model(**values_dict)
        session.add(new_instance)
        try:
            await session.flush()
            logger.info('Запись ' + cls.model.__name__ + ' успешно добавлена.') # Изменено на конкатенацию строк
        except SQLAlchemyError as e:
            await cls._handle_error(e, 'Ошибка при добавлении записи: ', session)
        return new_instance

    @classmethod
    async def add_many(cls, session: AsyncSession, instances: List[BaseModel]) -> List[T]:
        """
        Асинхронно добавляет несколько новых записей в базу данных.

        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :param instances: Список объектов Pydantic BaseModel для добавления.
        :type instances: List[BaseModel]
        :return: Список созданных записей.
        :rtype: List[T]
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса к БД.
        
        Пример:
            >>> session: AsyncSession = ...
            >>> values = [MyModelCreate(name='Test1'), MyModelCreate(name='Test2')]
            >>> result = await BaseDAO[MyModel].add_many(session, values)
            >>> print(result)
            [<MyModel...>, <MyModel...>]
        """
        values_list = [item.model_dump(exclude_unset=True) for item in instances]
        logger.info('Добавление нескольких записей ' + cls.model.__name__ + '. Количество: ' + str(len(values_list))) # Изменено на конкатенацию строк
        new_instances = [cls.model(**values) for values in values_list]
        session.add_all(new_instances)
        try:
            await session.flush()
            logger.info('Успешно добавлено ' + str(len(new_instances)) + ' записей.') # Изменено на конкатенацию строк
        except SQLAlchemyError as e:
            await cls._handle_error(e, 'Ошибка при добавлении нескольких записей: ', session)
        return new_instances

    @classmethod
    async def update(cls, session: AsyncSession, filters: BaseModel, values: BaseModel) -> int:
        """
        Асинхронно обновляет записи в базе данных по заданным фильтрам.

        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :param filters: Фильтры для обновления в виде объекта Pydantic BaseModel.
        :type filters: BaseModel
        :param values: Новые значения для обновления в виде объекта Pydantic BaseModel.
        :type values: BaseModel
        :return: Количество обновленных записей.
        :rtype: int
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса к БД.
        
        Пример:
            >>> session: AsyncSession = ...
            >>> filters = MyModelFilter(id=1)
            >>> values = MyModelCreate(name='Updated')
            >>> result = await BaseDAO[MyModel].update(session, filters, values)
            >>> print(result)
            1
        """
        filter_dict = filters.model_dump(exclude_unset=True)
        values_dict = values.model_dump(exclude_unset=True)
        logger.info('Обновление записей ' + cls.model.__name__ + ' по фильтру: ' + str(filter_dict) + ' с параметрами: ' + str(values_dict)) # Изменено на конкатенацию строк
        query = (
            sqlalchemy_update(cls.model)
            .where(*[getattr(cls.model, k) == v for k, v in filter_dict.items()])
            .values(**values_dict)
            .execution_options(synchronize_session='fetch')
        )
        try:
            result = await session.execute(query)
            await session.flush()
            logger.info('Обновлено ' + str(result.rowcount) + ' записей.') # Изменено на конкатенацию строк
            return result.rowcount
        except SQLAlchemyError as e:
            await cls._handle_error(e, 'Ошибка при обновлении записей: ', session)

    @classmethod
    async def delete(cls, session: AsyncSession, filters: BaseModel) -> int:
        """
        Асинхронно удаляет записи из базы данных по заданным фильтрам.

        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :param filters: Фильтры для удаления в виде объекта Pydantic BaseModel.
        :type filters: BaseModel
        :return: Количество удаленных записей.
        :rtype: int
        :raises ValueError: Если не предоставлен ни один фильтр.
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса к БД.
        
        Пример:
            >>> session: AsyncSession = ...
            >>> filters = MyModelFilter(id=1)
            >>> result = await BaseDAO[MyModel].delete(session, filters)
            >>> print(result)
            1
        """
        filter_dict = filters.model_dump(exclude_unset=True)
        logger.info('Удаление записей ' + cls.model.__name__ + ' по фильтру: ' + str(filter_dict)) # Изменено на конкатенацию строк
        if not filter_dict:
            logger.error('Нужен хотя бы один фильтр для удаления.')
            raise ValueError('Нужен хотя бы один фильтр для удаления.')

        query = sqlalchemy_delete(cls.model).filter_by(**filter_dict)
        try:
            result = await session.execute(query)
            await session.flush()
            logger.info('Удалено ' + str(result.rowcount) + ' записей.') # Изменено на конкатенацию строк
            return result.rowcount
        except SQLAlchemyError as e:
            await cls._handle_error(e, 'Ошибка при удалении записей: ', session)

    @classmethod
    async def count(cls, session: AsyncSession, filters: BaseModel | None = None) -> int:
        """
        Асинхронно подсчитывает количество записей в базе данных по заданным фильтрам.

        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :param filters: Фильтры для подсчета в виде объекта Pydantic BaseModel или None.
        :type filters: BaseModel | None
        :return: Количество записей.
        :rtype: int
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса к БД.
        
        Пример:
            >>> session: AsyncSession = ...
            >>> filters = MyModelFilter(name='Test')
            >>> result = await BaseDAO[MyModel].count(session, filters)
            >>> print(result)
            2
        """
        filter_dict = filters.model_dump(exclude_unset=True) if filters else {}
        logger.info('Подсчет количества записей ' + cls.model.__name__ + ' по фильтру: ' + str(filter_dict)) # Изменено на конкатенацию строк
        try:
            query = select(func.count(cls.model.id)).filter_by(**filter_dict)
            result = await session.execute(query)
            count = result.scalar()
            logger.info('Найдено ' + str(count) + ' записей.') # Изменено на конкатенацию строк
            return count
        except SQLAlchemyError as e:
            await cls._handle_error(e, 'Ошибка при подсчете записей: ', session)

    @classmethod
    async def paginate(cls, session: AsyncSession, page: int = 1, page_size: int = 10, filters: BaseModel = None) -> List[T]:
        """
        Асинхронно выполняет пагинацию записей в базе данных по заданным фильтрам.

        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :param page: Номер страницы для отображения, по умолчанию 1.
        :type page: int
        :param page_size: Размер страницы, по умолчанию 10.
        :type page_size: int
        :param filters: Фильтры для пагинации в виде объекта Pydantic BaseModel или None.
        :type filters: BaseModel | None
        :return: Список записей на заданной странице.
        :rtype: List[T]
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса к БД.
        
        Пример:
            >>> session: AsyncSession = ...
            >>> filters = MyModelFilter(name='Test')
            >>> result = await BaseDAO[MyModel].paginate(session, page=2, page_size=10, filters=filters)
            >>> print(result)
            [<MyModel...>, <MyModel...>]
        """
        filter_dict = filters.model_dump(exclude_unset=True) if filters else {}
        logger.info(
            'Пагинация записей ' + cls.model.__name__ + ' по фильтру: ' + str(filter_dict) + ', страница: ' + str(page) + ', размер страницы: ' + str(page_size)) # Изменено на конкатенацию строк
        try:
            query = select(cls.model).filter_by(**filter_dict)
            result = await session.execute(query.offset((page - 1) * page_size).limit(page_size))
            records = result.scalars().all()
            logger.info('Найдено ' + str(len(records)) + ' записей на странице ' + str(page) + '.') # Изменено на конкатенацию строк
            return records
        except SQLAlchemyError as e:
            await cls._handle_error(e, 'Ошибка при пагинации записей: ', session)

    @classmethod
    async def find_by_ids(cls, session: AsyncSession, ids: List[int]) -> List[Any]:
        """
        Асинхронно ищет несколько записей по списку ID.

        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :param ids: Список ID записей для поиска.
        :type ids: List[int]
        :return: Список найденных записей.
        :rtype: List[Any]
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса к БД.
        
        Пример:
            >>> session: AsyncSession = ...
            >>> result = await BaseDAO[MyModel].find_by_ids(session, [1,2,3])
            >>> print(result)
            [<MyModel...>, <MyModel...>, <MyModel...>]
        """
        logger.info('Поиск записей ' + cls.model.__name__ + ' по списку ID: ' + str(ids)) # Изменено на конкатенацию строк
        try:
            query = select(cls.model).filter(cls.model.id.in_(ids))
            result = await session.execute(query)
            records = result.scalars().all()
            logger.info('Найдено ' + str(len(records)) + ' записей по списку ID.') # Изменено на конкатенацию строк
            return records
        except SQLAlchemyError as e:
            await cls._handle_error(e, 'Ошибка при поиске записей по списку ID: ', session)

    @classmethod
    async def upsert(cls, session: AsyncSession, unique_fields: List[str], values: BaseModel) -> T:
        """
        Асинхронно создает или обновляет запись в базе данных на основе уникальных полей.

        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :param unique_fields: Список уникальных полей, используемых для поиска существующей записи.
        :type unique_fields: List[str]
        :param values: Значения для новой или обновляемой записи в виде объекта Pydantic BaseModel.
        :type values: BaseModel
        :return: Созданная или обновленная запись.
        :rtype: T
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса к БД.
        
        Пример:
            >>> session: AsyncSession = ...
            >>> unique_fields = ['name']
            >>> values = MyModelCreate(name='Test')
            >>> result = await BaseDAO[MyModel].upsert(session, unique_fields, values)
            >>> print(result)
            <MyModel...>
        """
        values_dict = values.model_dump(exclude_unset=True)
        filter_dict = {field: values_dict[field] for field in unique_fields if field in values_dict}

        logger.info('Upsert для ' + cls.model.__name__) # Изменено на конкатенацию строк
        try:
            existing = await cls.find_one_or_none(session, BaseModel.construct(**filter_dict))
            if existing:
                # Обновляем существующую запись
                for key, value in values_dict.items():
                    setattr(existing, key, value)
                await session.flush()
                logger.info('Обновлена существующая запись ' + cls.model.__name__) # Изменено на конкатенацию строк
                return existing
            else:
                # Создаем новую запись
                new_instance = cls.model(**values_dict)
                session.add(new_instance)
                await session.flush()
                logger.info('Создана новая запись ' + cls.model.__name__) # Изменено на конкатенацию строк
                return new_instance
        except SQLAlchemyError as e:
            await cls._handle_error(e, 'Ошибка при upsert: ', session)

    @classmethod
    async def bulk_update(cls, session: AsyncSession, records: List[BaseModel]) -> int:
        """
        Асинхронно выполняет массовое обновление записей в базе данных.

        :param session: Асинхронная сессия SQLAlchemy.
        :type session: AsyncSession
        :param records: Список объектов Pydantic BaseModel для обновления.
        :type records: List[BaseModel]
        :return: Количество обновленных записей.
        :rtype: int
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса к БД.
        
        Пример:
            >>> session: AsyncSession = ...
            >>> records = [MyModel(id=1, name='Updated1'), MyModel(id=2, name='Updated2')]
            >>> result = await BaseDAO[MyModel].bulk_update(session, records)
            >>> print(result)
            2
        """
        logger.info('Массовое обновление записей ' + cls.model.__name__) # Изменено на конкатенацию строк
        try:
            updated_count = 0
            for record in records:
                record_dict = record.model_dump(exclude_unset=True)
                if 'id' not in record_dict:
                    continue

                update_data = {k: v for k, v in record_dict.items() if k != 'id'}
                stmt = (
                    sqlalchemy_update(cls.model)
                    .filter_by(id=record_dict['id'])
                    .values(**update_data)
                )
                result = await session.execute(stmt)
                updated_count += result.rowcount

            await session.flush()
            logger.info('Обновлено ' + str(updated_count) + ' записей') # Изменено на конкатенацию строк
            return updated_count
        except SQLAlchemyError as e:
            await cls._handle_error(e, 'Ошибка при массовом обновлении: ', session)