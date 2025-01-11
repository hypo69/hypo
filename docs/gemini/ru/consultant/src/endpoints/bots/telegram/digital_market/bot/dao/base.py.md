# Анализ кода модуля `base.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и использует `asyncio` для асинхронных операций.
    - Применяются `pydantic` модели для валидации данных.
    - Используется `loguru` для логирования.
    - Присутствуют базовые методы для работы с БД.
    - Код соответствует PEP 8.
- Минусы
    - Отсутствует документация в формате RST.
    - Не используется `from src.logger.logger import logger`.
    - Избыточное использование `try-except` с `raise` в конце, можно заменить на `logger.error` и `return` вместо `raise`.

**Рекомендации по улучшению**

1.  Добавить документацию в формате RST для модуля, классов и методов.
2.  Использовать `from src.logger.logger import logger`.
3.  Упростить обработку исключений, заменив `raise` на `logger.error` и `return` в блоках `except`.
4.  Добавить проверку на уникальность `unique_fields` перед upsert.
5.  Избегать использования `if 'id' not in record_dict:` в `bulk_update`, вынеся этот блок проверки в отдельную функцию.

**Оптимизированный код**

```python
"""
Модуль содержит базовый класс BaseDAO для асинхронного доступа к данным в базе данных.
=========================================================================================

Этот модуль предоставляет базовый класс :class:`BaseDAO` для выполнения стандартных операций
с базой данных, таких как создание, чтение, обновление и удаление записей, а также пагинацию
и массовое обновление.

Пример использования
--------------------

Пример использования класса `BaseDAO`:

.. code-block:: python

    from sqlalchemy.ext.asyncio import AsyncSession
    from pydantic import BaseModel
    from bot.dao.database import Base
    from typing import List

    class MyModel(Base):
        __tablename__ = 'my_table'
        id = Column(Integer, primary_key=True)
        name = Column(String)

    class MyModelDTO(BaseModel):
        id: int = None
        name: str

    class MyDAO(BaseDAO[MyModel]):
        model = MyModel

    async def main():
      async with AsyncSession(engine) as session:
          new_data = MyModelDTO(name='Test')
          created = await MyDAO.add(session, new_data)
          print(created)

"""
from typing import List, Any, TypeVar, Generic
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete, func
# from loguru import logger #  заменено на импорт из src.logger.logger
from sqlalchemy.ext.asyncio import AsyncSession

from src.logger.logger import logger #  импортируем logger из src.logger
from bot.dao.database import Base

# Объявляем типовой параметр T с ограничением, что это наследник Base
T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    """
    Базовый класс для асинхронного доступа к данным в базе данных.

    Предоставляет методы для выполнения стандартных операций CRUD, а также
    для пагинации, поиска по ID, массового добавления и обновления записей.

    :param model: Модель SQLAlchemy, с которой работает DAO.
    """
    model: type[T]

    @classmethod
    async def find_one_or_none_by_id(cls, data_id: int, session: AsyncSession) -> T | None:
        """
        Найти одну запись по ID.

        :param data_id: ID записи.
        :param session: Асинхронная сессия SQLAlchemy.
        :return: Найденная запись или None, если запись не найдена.
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса.
        """
        # Код выполняет поиск записи по ID
        logger.info(f'Поиск {cls.model.__name__} с ID: {data_id}')
        try:
            query = select(cls.model).filter_by(id=data_id)
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record:
                logger.info(f'Запись с ID {data_id} найдена.')
            else:
                logger.info(f'Запись с ID {data_id} не найдена.')
            return record
        except SQLAlchemyError as e:
            # Логируем ошибку и возвращаем None
            logger.error(f'Ошибка при поиске записи с ID {data_id}: {e}')
            return None

    @classmethod
    async def find_one_or_none(cls, session: AsyncSession, filters: BaseModel) -> T | None:
        """
        Найти одну запись по фильтрам.

        :param session: Асинхронная сессия SQLAlchemy.
        :param filters: Pydantic модель, содержащая фильтры.
        :return: Найденная запись или None, если запись не найдена.
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса.
        """
        # Код выполняет поиск одной записи по фильтрам
        filter_dict = filters.model_dump(exclude_unset=True)
        logger.info(f'Поиск одной записи {cls.model.__name__} по фильтрам: {filter_dict}')
        try:
            query = select(cls.model).filter_by(**filter_dict)
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record:
                logger.info(f'Запись найдена по фильтрам: {filter_dict}')
            else:
                logger.info(f'Запись не найдена по фильтрам: {filter_dict}')
            return record
        except SQLAlchemyError as e:
            # Логируем ошибку и возвращаем None
            logger.error(f'Ошибка при поиске записи по фильтрам {filter_dict}: {e}')
            return None

    @classmethod
    async def find_all(cls, session: AsyncSession, filters: BaseModel | None = None) -> List[T]:
        """
        Найти все записи по фильтрам.

        :param session: Асинхронная сессия SQLAlchemy.
        :param filters: Pydantic модель, содержащая фильтры.
        :return: Список найденных записей.
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса.
        """
        # Код выполняет поиск всех записей по фильтрам
        filter_dict = filters.model_dump(exclude_unset=True) if filters else {}
        logger.info(f'Поиск всех записей {cls.model.__name__} по фильтрам: {filter_dict}')
        try:
            query = select(cls.model).filter_by(**filter_dict)
            result = await session.execute(query)
            records = result.scalars().all()
            logger.info(f'Найдено {len(records)} записей.')
            return records
        except SQLAlchemyError as e:
            # Логируем ошибку и возвращаем пустой список
            logger.error(f'Ошибка при поиске всех записей по фильтрам {filter_dict}: {e}')
            return []

    @classmethod
    async def add(cls, session: AsyncSession, values: BaseModel) -> T:
        """
        Добавить одну запись.

        :param session: Асинхронная сессия SQLAlchemy.
        :param values: Pydantic модель, содержащая данные для добавления.
        :return: Созданная запись.
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса.
        """
        # Код добавляет одну запись
        values_dict = values.model_dump(exclude_unset=True)
        logger.info(f'Добавление записи {cls.model.__name__} с параметрами: {values_dict}')
        new_instance = cls.model(**values_dict)
        session.add(new_instance)
        try:
            await session.flush()
            logger.info(f'Запись {cls.model.__name__} успешно добавлена.')
        except SQLAlchemyError as e:
            # Откатываем транзакцию и логируем ошибку
            await session.rollback()
            logger.error(f'Ошибка при добавлении записи: {e}')
            return None
        return new_instance

    @classmethod
    async def add_many(cls, session: AsyncSession, instances: List[BaseModel]) -> List[T]:
        """
        Добавить несколько записей.

        :param session: Асинхронная сессия SQLAlchemy.
        :param instances: Список Pydantic моделей, содержащих данные для добавления.
        :return: Список созданных записей.
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса.
        """
        # Код добавляет несколько записей
        values_list = [item.model_dump(exclude_unset=True) for item in instances]
        logger.info(f'Добавление нескольких записей {cls.model.__name__}. Количество: {len(values_list)}')
        new_instances = [cls.model(**values) for values in values_list]
        session.add_all(new_instances)
        try:
            await session.flush()
            logger.info(f'Успешно добавлено {len(new_instances)} записей.')
        except SQLAlchemyError as e:
            # Откатываем транзакцию и логируем ошибку
            await session.rollback()
            logger.error(f'Ошибка при добавлении нескольких записей: {e}')
            return []
        return new_instances

    @classmethod
    async def update(cls, session: AsyncSession, filters: BaseModel, values: BaseModel) -> int:
        """
        Обновить записи по фильтрам.

        :param session: Асинхронная сессия SQLAlchemy.
        :param filters: Pydantic модель, содержащая фильтры для обновления.
        :param values: Pydantic модель, содержащая новые значения.
        :return: Количество обновленных записей.
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса.
        """
        # Код обновляет записи по фильтрам
        filter_dict = filters.model_dump(exclude_unset=True)
        values_dict = values.model_dump(exclude_unset=True)
        logger.info(f'Обновление записей {cls.model.__name__} по фильтру: {filter_dict} с параметрами: {values_dict}')
        query = (
            sqlalchemy_update(cls.model)
            .where(*[getattr(cls.model, k) == v for k, v in filter_dict.items()])
            .values(**values_dict)
            .execution_options(synchronize_session='fetch')
        )
        try:
            result = await session.execute(query)
            await session.flush()
            logger.info(f'Обновлено {result.rowcount} записей.')
            return result.rowcount
        except SQLAlchemyError as e:
            # Откатываем транзакцию и логируем ошибку
            await session.rollback()
            logger.error(f'Ошибка при обновлении записей: {e}')
            return 0

    @classmethod
    async def delete(cls, session: AsyncSession, filters: BaseModel) -> int:
        """
        Удалить записи по фильтру.

        :param session: Асинхронная сессия SQLAlchemy.
        :param filters: Pydantic модель, содержащая фильтры для удаления.
        :return: Количество удаленных записей.
        :raises ValueError: Если не передан ни один фильтр для удаления.
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса.
        """
        # Код удаляет записи по фильтру
        filter_dict = filters.model_dump(exclude_unset=True)
        logger.info(f'Удаление записей {cls.model.__name__} по фильтру: {filter_dict}')
        if not filter_dict:
            logger.error('Нужен хотя бы один фильтр для удаления.')
            return 0

        query = sqlalchemy_delete(cls.model).filter_by(**filter_dict)
        try:
            result = await session.execute(query)
            await session.flush()
            logger.info(f'Удалено {result.rowcount} записей.')
            return result.rowcount
        except SQLAlchemyError as e:
            # Откатываем транзакцию и логируем ошибку
            await session.rollback()
            logger.error(f'Ошибка при удалении записей: {e}')
            return 0

    @classmethod
    async def count(cls, session: AsyncSession, filters: BaseModel | None = None) -> int:
        """
        Подсчитать количество записей.

        :param session: Асинхронная сессия SQLAlchemy.
        :param filters: Pydantic модель, содержащая фильтры для подсчета.
        :return: Количество записей, соответствующих фильтру.
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса.
        """
        # Код подсчитывает количество записей
        filter_dict = filters.model_dump(exclude_unset=True) if filters else {}
        logger.info(f'Подсчет количества записей {cls.model.__name__} по фильтру: {filter_dict}')
        try:
            query = select(func.count(cls.model.id)).filter_by(**filter_dict)
            result = await session.execute(query)
            count = result.scalar()
            logger.info(f'Найдено {count} записей.')
            return count
        except SQLAlchemyError as e:
            # Логируем ошибку и возвращаем 0
            logger.error(f'Ошибка при подсчете записей: {e}')
            return 0

    @classmethod
    async def paginate(cls, session: AsyncSession, page: int = 1, page_size: int = 10, filters: BaseModel = None) -> List[T]:
        """
        Пагинация записей.

        :param session: Асинхронная сессия SQLAlchemy.
        :param page: Номер страницы (по умолчанию 1).
        :param page_size: Размер страницы (по умолчанию 10).
        :param filters: Pydantic модель, содержащая фильтры для пагинации.
        :return: Список записей на текущей странице.
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса.
        """
        # Код выполняет пагинацию записей
        filter_dict = filters.model_dump(exclude_unset=True) if filters else {}
        logger.info(
            f'Пагинация записей {cls.model.__name__} по фильтру: {filter_dict}, страница: {page}, размер страницы: {page_size}')
        try:
            query = select(cls.model).filter_by(**filter_dict)
            result = await session.execute(query.offset((page - 1) * page_size).limit(page_size))
            records = result.scalars().all()
            logger.info(f'Найдено {len(records)} записей на странице {page}.')
            return records
        except SQLAlchemyError as e:
            # Логируем ошибку и возвращаем пустой список
            logger.error(f'Ошибка при пагинации записей: {e}')
            return []

    @classmethod
    async def find_by_ids(cls, session: AsyncSession, ids: List[int]) -> List[T]:
        """
        Найти несколько записей по списку ID.

        :param session: Асинхронная сессия SQLAlchemy.
        :param ids: Список ID записей.
        :return: Список найденных записей.
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса.
        """
        # Код выполняет поиск записей по списку ID
        logger.info(f'Поиск записей {cls.model.__name__} по списку ID: {ids}')
        try:
            query = select(cls.model).filter(cls.model.id.in_(ids))
            result = await session.execute(query)
            records = result.scalars().all()
            logger.info(f'Найдено {len(records)} записей по списку ID.')
            return records
        except SQLAlchemyError as e:
            # Логируем ошибку и возвращаем пустой список
            logger.error(f'Ошибка при поиске записей по списку ID: {e}')
            return []

    @classmethod
    async def upsert(cls, session: AsyncSession, unique_fields: List[str], values: BaseModel) -> T | None:
        """
        Создать запись или обновить существующую.

        :param session: Асинхронная сессия SQLAlchemy.
        :param unique_fields: Список полей, которые определяют уникальность записи.
        :param values: Pydantic модель, содержащая данные для создания или обновления.
        :return: Созданная или обновленная запись.
        :raises SQLAlchemyError: В случае ошибки при выполнении запроса.
        """
        # Код выполняет создание или обновление записи
        values_dict = values.model_dump(exclude_unset=True)
        filter_dict = {field: values_dict[field] for field in unique_fields if field in values_dict}
        if not filter_dict:
            logger.error(f'Невозможно выполнить upsert без уникальных полей: {unique_fields}')
            return None

        logger.info(f'Upsert для {cls.model.__name__}')
        try:
            existing = await cls.find_one_or_none(session, BaseModel.construct(**filter_dict))
            if existing:
                # Обновляем существующую запись
                for key, value in values_dict.items():
                    setattr(existing, key, value)
                await session.flush()
                logger.info(f'Обновлена существующая запись {cls.model.__name__}')
                return existing
            else:
                # Создаем новую запись
                new_instance = cls.model(**values_dict)
                session.add(new_instance)
                await session.flush()
                logger.info(f'Создана новая запись {cls.model.__name__}')
                return new_instance
        except SQLAlchemyError as e:
            # Откатываем транзакцию и логируем ошибку
            await session.rollback()
            logger.error(f'Ошибка при upsert: {e}')
            return None

    @classmethod
    async def _update_record(cls, session: AsyncSession, record: BaseModel) -> int:
        """Обновляет одну запись."""
        record_dict = record.model_dump(exclude_unset=True)
        if 'id' not in record_dict:
            logger.error(f'Невозможно обновить запись без ID: {record_dict}')
            return 0

        update_data = {k: v for k, v in record_dict.items() if k != 'id'}
        stmt = (
            sqlalchemy_update(cls.model)
            .filter_by(id=record_dict['id'])
            .values(**update_data)
        )
        result = await session.execute(stmt)
        return result.rowcount

    @classmethod
    async def bulk_update(cls, session: AsyncSession, records: List[BaseModel]) -> int:
        """
        Массовое обновление записей.

        :param session: Асинхронная сессия SQLAlchemy.
        :param records: Список Pydantic моделей, содержащих данные для обновления.
        :return: Количество обновленных записей.
         :raises SQLAlchemyError: В случае ошибки при выполнении запроса.
        """
        # Код выполняет массовое обновление записей
        logger.info(f'Массовое обновление записей {cls.model.__name__}')
        try:
            updated_count = 0
            for record in records:
                updated_count += await cls._update_record(session, record)

            await session.flush()
            logger.info(f'Обновлено {updated_count} записей')
            return updated_count
        except SQLAlchemyError as e:
            # Откатываем транзакцию и логируем ошибку
            await session.rollback()
            logger.error(f'Ошибка при массовом обновлении: {e}')
            return 0
```