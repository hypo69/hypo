# Документация для `env.py`

## Обзор

Файл `env.py` является частью системы миграций Alembic и предназначен для настройки и запуска миграций базы данных. Он содержит функции для выполнения миграций как в онлайн, так и в оффлайн режимах, а также настройки для подключения к базе данных.

## Подробнее

Этот файл играет важную роль в процессе обновления схемы базы данных, обеспечивая возможность автоматического применения изменений схемы. Он использует SQLAlchemy для взаимодействия с базой данных и Alembic для управления миграциями.

## Содержание

- [Функции](#Функции)
  - [run_migrations_offline](#run_migrations_offline)
  - [do_run_migrations](#do_run_migrations)
  - [run_async_migrations](#run_async_migrations)
  - [run_migrations_online](#run_migrations_online)

## Код

```python
import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

import asyncio
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context
from bot.dao.database import Base, database_url
from bot.dao.models import Product, Purchase, User, Category


config = context.config
config.set_main_option("sqlalchemy.url", database_url)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

## Функции

### `run_migrations_offline`

```python
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    ...
```

**Назначение**: Запускает миграции в "оффлайн" режиме.

**Как работает функция**:
1. Извлекает URL базы данных из конфигурации Alembic.
2. Конфигурирует контекст Alembic с использованием URL, целевой метадаты и опций диалекта.
3. Запускает миграции внутри транзакции.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют.

### `do_run_migrations`

```python
def do_run_migrations(connection: Connection) -> None:
    """ """
    ...
```

**Назначение**: Выполняет миграции, используя предоставленное соединение с базой данных.

**Как работает функция**:
1. Конфигурирует контекст Alembic с использованием предоставленного соединения и целевой метадаты.
2. Запускает миграции внутри транзакции.

**Параметры**:
- `connection` (Connection): Объект соединения с базой данных SQLAlchemy.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют.

### `run_async_migrations`

```python
async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    ...
```

**Назначение**: Запускает миграции асинхронно.

**Как работает функция**:
1. Создает асинхронный движок SQLAlchemy, используя параметры конфигурации.
2. Устанавливает соединение с базой данных.
3. Запускает миграции, используя функцию `do_run_migrations` в синхронном режиме внутри асинхронного контекста.
4. Закрывает соединение.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют.

### `run_migrations_online`

```python
def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    ...
```

**Назначение**: Запускает миграции в "онлайн" режиме.

**Как работает функция**:
1. Запускает асинхронные миграции, используя `asyncio.run`.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют.