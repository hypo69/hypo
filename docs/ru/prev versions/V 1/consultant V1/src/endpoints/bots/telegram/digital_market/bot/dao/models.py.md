# Анализ кода модуля `models`

**Качество кода**:
- **Соответствие стандартам**: 8
- **Плюсы**:
    - Код хорошо структурирован и использует ORM SQLAlchemy для работы с базой данных.
    - Присутствуют аннотации типов, что улучшает читаемость и надежность кода.
    - Связи между таблицами определены корректно через `relationship`.
    - Используются `cascade="all, delete-orphan"` для автоматического удаления связанных записей.
- **Минусы**:
    - Отсутствует документация в формате RST для классов и их методов.
    - В `__repr__` методах используются f-строки, что хорошо, но не хватает описания полей.
    - Отсутствует явное указание на использование `Text` для строковых полей, что может быть неочевидно.

**Рекомендации по улучшению**:

1.  **Добавить RST-документацию**:
    *   Добавить docstrings в формате RST для каждого класса, описывая его назначение, поля и методы.
    *   Добавить docstrings в формате RST для каждого метода `__repr__`, описывая его назначение и возвращаемое значение.
2.  **Улучшить `__repr__` методы**:
    *   Добавить в `__repr__` методы описание всех полей, чтобы представление объектов было более информативным.
3.  **Указать тип для строковых полей**:
    *   Явно указывать тип `Text` для строковых полей, чтобы было понятно, что это именно текстовое поле.
4.  **Упорядочить импорты**:
    *   Импорты из sqlalchemy сгруппировать и отсортировать по алфавиту.

**Оптимизированный код**:
```python
from typing import List

from sqlalchemy import BigInteger, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.dao.database import Base


class User(Base):
    """
    Модель пользователя в Telegram.

    :ivar telegram_id: Уникальный идентификатор пользователя в Telegram.
    :vartype telegram_id: int
    :ivar username: Имя пользователя в Telegram (может отсутствовать).
    :vartype username: str | None
    :ivar first_name: Имя пользователя в Telegram (может отсутствовать).
    :vartype first_name: str | None
    :ivar last_name: Фамилия пользователя в Telegram (может отсутствовать).
    :vartype last_name: str | None
    :ivar purchases: Список покупок, совершенных пользователем.
    :vartype purchases: List['Purchase']
    """
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str | None] = mapped_column(Text)  # Явно указан тип Text
    first_name: Mapped[str | None] = mapped_column(Text)  # Явно указан тип Text
    last_name: Mapped[str | None] = mapped_column(Text)  # Явно указан тип Text
    purchases: Mapped[List['Purchase']] = relationship(
        'Purchase',
        back_populates='user',
        cascade='all, delete-orphan'
    )

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта User.

        :return: Строковое представление объекта User.
        :rtype: str
        """
        return f'<User(id={self.id}, telegram_id={self.telegram_id}, username={self.username}, first_name={self.first_name}, last_name={self.last_name})>'


class Category(Base):
    """
    Модель категории товаров.

    :ivar category_name: Название категории.
    :vartype category_name: str
    :ivar products: Список товаров в данной категории.
    :vartype products: List['Product']
    """
    __tablename__ = 'categories'

    category_name: Mapped[str] = mapped_column(Text, nullable=False)
    products: Mapped[List['Product']] = relationship(
        'Product',
        back_populates='category',
        cascade='all, delete-orphan'
    )

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Category.

        :return: Строковое представление объекта Category.
        :rtype: str
        """
        return f'<Category(id={self.id}, name={self.category_name})>'


class Product(Base):
    """
    Модель товара.

    :ivar name: Название товара.
    :vartype name: str
    :ivar description: Описание товара.
    :vartype description: str
    :ivar price: Цена товара.
    :vartype price: int
    :ivar file_id: Идентификатор файла товара (может отсутствовать).
    :vartype file_id: str | None
    :ivar category_id: Идентификатор категории товара.
    :vartype category_id: int
    :ivar hidden_content: Скрытое содержимое товара.
    :vartype hidden_content: str
    :ivar category: Категория товара.
    :vartype category: Category
    :ivar purchases: Список покупок данного товара.
    :vartype purchases: List['Purchase']
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

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Product.

        :return: Строковое представление объекта Product.
        :rtype: str
        """
        return f'<Product(id={self.id}, name={self.name}, price={self.price}, description={self.description}, file_id={self.file_id}, category_id={self.category_id}, hidden_content={self.hidden_content})>'


class Purchase(Base):
    """
    Модель покупки.

    :ivar user_id: Идентификатор пользователя, совершившего покупку.
    :vartype user_id: int
    :ivar product_id: Идентификатор купленного товара.
    :vartype product_id: int
    :ivar price: Цена покупки.
    :vartype price: int
    :ivar payment_type: Тип оплаты.
    :vartype payment_type: str
    :ivar payment_id: Уникальный идентификатор платежа.
    :vartype payment_id: str
    :ivar user: Пользователь, совершивший покупку.
    :vartype user: User
    :ivar product: Купленный товар.
    :vartype product: Product
    """
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    price: Mapped[int]
    payment_type: Mapped[str] = mapped_column(Text) # Явно указан тип Text
    payment_id: Mapped[str] = mapped_column(Text, unique=True) # Явно указан тип Text
    user: Mapped['User'] = relationship('User', back_populates='purchases')
    product: Mapped['Product'] = relationship('Product', back_populates='purchases')

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Purchase.

        :return: Строковое представление объекта Purchase.
        :rtype: str
        """
        return f'<Purchase(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, price={self.price}, payment_type={self.payment_type}, payment_id={self.payment_id}, date={self.created_at})>'
```