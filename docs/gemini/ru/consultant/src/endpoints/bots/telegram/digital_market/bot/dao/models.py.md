# Анализ кода модуля `models`

**Качество кода**
7
-  Плюсы
    - Код использует `sqlalchemy` для определения моделей базы данных, что является хорошей практикой.
    - Присутствуют отношения между таблицами (пользователи, категории, продукты, покупки) с использованием `relationship`.
    - Добавлены методы `__repr__` для удобства отладки и логирования.
    - Используются `Mapped` и `mapped_column` для определения типов и связей полей, что соответствует современным практикам `SQLAlchemy`.
 -  Минусы
    - Отсутствует описание модуля в начале файла.
    - Нет документации для классов и их методов.
    - Не используется импорт логгера из `src.logger`.
    - Есть возможность для улучшения консистентности использования кавычек, рекомендуется использовать одинарные кавычки для строк в коде Python.

**Рекомендации по улучшению**

1. Добавить описание модуля в начале файла.
2. Добавить документацию для классов и их методов, используя docstring в формате RST.
3. Импортировать `logger` из `src.logger.logger`.
4. Использовать одинарные кавычки (`'`) для строк в коде Python, за исключением строк, используемых для вывода.
5. Добавить `__tablename__` для таблиц `User` и `Purchase` для явного определения имени таблицы.

**Оптимизированный код**

```python
"""
Модуль для определения моделей базы данных для бота Telegram цифрового рынка.
=========================================================================================

Этот модуль содержит классы, представляющие таблицы базы данных: `User`, `Category`, `Product` и `Purchase`.
Они используются для хранения информации о пользователях, категориях товаров, самих товарах и совершенных покупках.

Пример использования
--------------------

Пример создания экземпляра модели `User`:

.. code-block:: python

    from bot.dao.models import User
    user = User(telegram_id=123456789, username='test_user')
"""
from typing import List

# импортируем logger
from src.logger.logger import logger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, Text, ForeignKey, text
from bot.dao.database import Base


class User(Base):
    """
    Модель пользователя.

    Содержит информацию о пользователях бота.

    :param telegram_id: Уникальный идентификатор пользователя в Telegram.
    :type telegram_id: int
    :param username: Имя пользователя в Telegram (может отсутствовать).
    :type username: str | None
    :param first_name: Имя пользователя (может отсутствовать).
    :type first_name: str | None
    :param last_name: Фамилия пользователя (может отсутствовать).
    :type last_name: str | None
    :param purchases: Список покупок пользователя.
    :type purchases: List['Purchase']

    """
    __tablename__ = 'users' #  Добавляем явное имя таблицы
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str | None]
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    purchases: Mapped[List['Purchase']] = relationship(
        'Purchase',
        back_populates='user',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        """
        Возвращает строковое представление объекта User.

        :return: Строковое представление объекта User.
        :rtype: str
        """
        return f'<User(id={self.id}, telegram_id={self.telegram_id}, username=\'{self.username}\')>'


class Category(Base):
    """
    Модель категории товаров.

    Содержит информацию о категориях товаров.

    :param category_name: Название категории.
    :type category_name: str
    :param products: Список продуктов в данной категории.
    :type products: List['Product']
    """
    __tablename__ = 'categories'

    category_name: Mapped[str] = mapped_column(Text, nullable=False)
    products: Mapped[List['Product']] = relationship(
        'Product',
        back_populates='category',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        """
        Возвращает строковое представление объекта Category.

        :return: Строковое представление объекта Category.
        :rtype: str
        """
        return f'<Category(id={self.id}, name=\'{self.category_name}\')>'


class Product(Base):
    """
    Модель продукта.

    Содержит информацию о продукте, включая название, описание, цену и категорию.

    :param name: Название продукта.
    :type name: str
    :param description: Описание продукта.
    :type description: str
    :param price: Цена продукта.
    :type price: int
    :param file_id: Идентификатор файла, связанного с продуктом.
    :type file_id: str | None
    :param category_id: Идентификатор категории продукта.
    :type category_id: int
    :param hidden_content: Скрытый контент продукта.
    :type hidden_content: str
    :param category: Категория продукта.
    :type category: Category
    :param purchases: Список покупок, связанных с продуктом.
    :type purchases: List['Purchase']
    """
    name: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[int]
    file_id: Mapped[str | None] = mapped_column(Text)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    hidden_content: Mapped[str] = mapped_column(Text)
    category: Mapped['Category'] = relationship('Category', back_populates='products')
    purchases: Mapped[List['Purchase']] = relationship(
        'Purchase',
        back_populates='product',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        """
        Возвращает строковое представление объекта Product.

        :return: Строковое представление объекта Product.
        :rtype: str
        """
        return f'<Product(id={self.id}, name=\'{self.name}\', price={self.price})>'


class Purchase(Base):
    """
    Модель покупки.

    Содержит информацию о покупках, включая пользователя, продукт, цену и тип оплаты.

    :param user_id: Идентификатор пользователя, совершившего покупку.
    :type user_id: int
    :param product_id: Идентификатор продукта, который был куплен.
    :type product_id: int
    :param price: Цена покупки.
    :type price: int
    :param payment_type: Тип оплаты.
    :type payment_type: str
    :param payment_id: Уникальный идентификатор платежа.
    :type payment_id: str
    :param user: Пользователь, совершивший покупку.
    :type user: User
    :param product: Купленный продукт.
    :type product: Product
    """
    __tablename__ = 'purchases'  #  Добавляем явное имя таблицы
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    price: Mapped[int]
    payment_type: Mapped[str]
    payment_id: Mapped[str] = mapped_column(unique=True)
    user: Mapped['User'] = relationship('User', back_populates='purchases')
    product: Mapped['Product'] = relationship('Product', back_populates='purchases')

    def __repr__(self):
        """
        Возвращает строковое представление объекта Purchase.

        :return: Строковое представление объекта Purchase.
        :rtype: str
        """
        return f'<Purchase(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, date={self.created_at})>'
```