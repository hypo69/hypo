# hypotez/src/endpoints/bots/telegram/digital_market/bot/migration/versions/2fda6446e69f_initial_revision.py

## Обзор

Файл содержит скрипт миграции базы данных, созданный с использованием Alembic. Он определяет начальную структуру базы данных для бота цифрового рынка Telegram, включая таблицы `categories`, `users`, `products` и `purchases`. Скрипт содержит функции `upgrade` для создания таблиц и `downgrade` для их удаления, что позволяет применять и откатывать изменения схемы базы данных.

## Подробней

Этот файл является частью системы миграций Alembic, которая используется для управления изменениями схемы базы данных в проекте `hypotez`. Alembic позволяет разработчикам определять изменения базы данных в виде скриптов, которые могут быть применены или отменены в определенном порядке. Это облегчает управление версиями базы данных и обеспечивает возможность отката к предыдущим версиям схемы в случае необходимости.

В данном случае, файл `2fda6446e69f_initial_revision.py` представляет собой начальную ревизию базы данных. Он определяет структуру таблиц, необходимых для работы бота цифрового рынка Telegram.

## Переменные

- `revision` (str): Идентификатор текущей ревизии.
- `down_revision` (Union[str, None]): Идентификатор предыдущей ревизии.
- `branch_labels` (Union[str, Sequence[str], None]): Метки ветвей.
- `depends_on` (Union[str, Sequence[str], None]): Зависимости от других ревизий.

## Функции

### `upgrade`

```python
def upgrade() -> None:
    """
    Применяет изменения к базе данных, создавая таблицы `categories`, `users`, `products` и `purchases`.

    Args:
        None

    Returns:
        None

    Raises:
        Нет явных исключений. Функция выполняет операции с базой данных через `alembic.op`,
        которые могут генерировать исключения в случае ошибок подключения или выполнения запросов.

    Как работает функция:
    Функция `upgrade` выполняет следующие шаги для создания необходимых таблиц в базе данных:
    1.  Создание таблицы `categories`:
        -   Создается таблица с именем `categories`.
        -   Определяются столбцы:
            -   `category_name` (Text, NOT NULL): Название категории.
            -   `id` (Integer, autoincrement=True, NOT NULL): Уникальный идентификатор категории, автоматически увеличивающийся.
            -   `created_at` (TIMESTAMP, server_default=sa.text('(CURRENT_TIMESTAMP)'), NOT NULL): Временная метка создания записи, по умолчанию текущее время.
            -   `updated_at` (TIMESTAMP, server_default=sa.text('(CURRENT_TIMESTAMP)'), NOT NULL): Временная метка обновления записи, по умолчанию текущее время.
        -   Устанавливается первичный ключ `id`.

    2.  Создание таблицы `users`:
        -   Создается таблица с именем `users`.
        -   Определяются столбцы:
            -   `telegram_id` (BigInteger, NOT NULL): Уникальный идентификатор пользователя в Telegram.
            -   `username` (String, nullable=True): Имя пользователя в Telegram (может отсутствовать).
            -   `first_name` (String, nullable=True): Имя пользователя.
            -   `last_name` (String, nullable=True): Фамилия пользователя.
            -   `id` (Integer, autoincrement=True, NOT NULL): Уникальный идентификатор пользователя, автоматически увеличивающийся.
            -   `created_at` (TIMESTAMP, server_default=sa.text('(CURRENT_TIMESTAMP)'), NOT NULL): Временная метка создания записи, по умолчанию текущее время.
            -   `updated_at` (TIMESTAMP, server_default=sa.text('(CURRENT_TIMESTAMP)'), NOT NULL): Временная метка обновления записи, по умолчанию текущее время.
        -   Устанавливается первичный ключ `id`.
        -   Устанавливается ограничение уникальности на столбец `telegram_id`.

    3.  Создание таблицы `products`:
        -   Создается таблица с именем `products`.
        -   Определяются столбцы:
            -   `name` (Text, NOT NULL): Название продукта.
            -   `description` (Text, NOT NULL): Описание продукта.
            -   `price` (Integer, NOT NULL): Цена продукта.
            -   `file_id` (Text, nullable=True): Идентификатор файла продукта (например, изображение).
            -   `category_id` (Integer, NOT NULL): Идентификатор категории продукта.
            -   `id` (Integer, autoincrement=True, NOT NULL): Уникальный идентификатор продукта, автоматически увеличивающийся.
            -   `created_at` (TIMESTAMP, server_default=sa.text('(CURRENT_TIMESTAMP)'), NOT NULL): Временная метка создания записи, по умолчанию текущее время.
            -   `updated_at` (TIMESTAMP, server_default=sa.text('(CURRENT_TIMESTAMP)'), NOT NULL): Временная метка обновления записи, по умолчанию текущее время.
        -   Устанавливается внешний ключ `category_id`, ссылающийся на столбец `id` таблицы `categories`.
        -   Устанавливается первичный ключ `id`.

    4.  Создание таблицы `purchases`:
        -   Создается таблица с именем `purchases`.
        -   Определяются столбцы:
            -   `user_id` (Integer, NOT NULL): Идентификатор пользователя, совершившего покупку.
            -   `product_id` (Integer, NOT NULL): Идентификатор купленного продукта.
            -   `price` (Integer, NOT NULL): Цена покупки.
            -   `id` (Integer, autoincrement=True, NOT NULL): Уникальный идентификатор покупки, автоматически увеличивающийся.
            -   `created_at` (TIMESTAMP, server_default=sa.text('(CURRENT_TIMESTAMP)'), NOT NULL): Временная метка создания записи, по умолчанию текущее время.
            -   `updated_at` (TIMESTAMP, server_default=sa.text('(CURRENT_TIMESTAMP)'), NOT NULL): Временная метка обновления записи, по умолчанию текущее время.
        -   Устанавливаются внешние ключи:
            -   `product_id`, ссылающийся на столбец `id` таблицы `products`.
            -   `user_id`, ссылающийся на столбец `id` таблицы `users`.
        -   Устанавливается первичный ключ `id`.
    """
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('category_name', sa.Text(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('telegram_id', sa.BigInteger(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('telegram_id')
    )
    op.create_table('products',
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Text(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchases',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
```

### `downgrade`

```python
def downgrade() -> None:
    """
    Откатывает изменения, удаляя таблицы `purchases`, `products`, `users` и `categories` из базы данных.

    Args:
        None

    Returns:
        None

    Raises:
        Нет явных исключений. Функция выполняет операции с базой данных через `alembic.op`,
        которые могут генерировать исключения в случае ошибок подключения или выполнения запросов.

    Как работает функция:
    Функция `downgrade` выполняет следующие шаги для удаления таблиц из базы данных:
    1.  Удаление таблицы `purchases`:
        -   Удаляет таблицу покупок, если она существует.

    2.  Удаление таблицы `products`:
        -   Удаляет таблицу продуктов, если она существует.

    3.  Удаление таблицы `users`:
        -   Удаляет таблицу пользователей, если она существует.

    4.  Удаление таблицы `categories`:
        -   Удаляет таблицу категорий, если она существует.
    """
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('purchases')
    op.drop_table('products')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###