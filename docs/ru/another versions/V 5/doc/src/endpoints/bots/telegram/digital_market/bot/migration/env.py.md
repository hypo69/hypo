# Модуль настройки окружения миграций Alembic

## Обзор

Модуль `env.py` предназначен для настройки окружения миграций Alembic. Он содержит функции для запуска миграций в онлайн и офлайн режимах, а также настройки подключения к базе данных.

## Подробнее

Этот модуль является частью процесса миграции базы данных и используется для управления изменениями схемы базы данных. Он определяет, как Alembic должен подключаться к базе данных, какие модели использовать и как запускать миграции в различных режимах.

## Функции

### `run_migrations_offline`

```python
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well. By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
```

**Описание**: Запускает миграции в "офлайн" режиме.

**Как работает функция**:
Функция настраивает контекст Alembic, используя только URL базы данных, без создания объекта Engine. Это позволяет запускать миграции без необходимости наличия активного подключения к базе данных. Вызовы `context.execute()` выводят переданную строку в вывод скрипта.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
```python
run_migrations_offline()
```

### `do_run_migrations`

```python
def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()
```

**Описание**: Запускает миграции, используя предоставленное соединение с базой данных.

**Как работает функция**:
Функция настраивает контекст Alembic, используя предоставленное соединение с базой данных и целевые метаданные. Затем она запускает миграции внутри транзакции.

**Параметры**:
- `connection` (Connection): Объект соединения с базой данных.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
```python
# Пример использования внутри асинхронной функции
async def example():
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()
```

### `run_async_migrations`

```python
async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context.

    """
```

**Описание**: Запускает миграции в асинхронном режиме.

**Как работает функция**:
Функция создает асинхронный объект Engine и устанавливает соединение с базой данных. Затем она запускает миграции, используя функцию `do_run_migrations` внутри асинхронного контекста. После завершения миграций соединение закрывается.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
```python
async def example():
    await run_async_migrations()
```

### `run_migrations_online`

```python
def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
```

**Описание**: Запускает миграции в "онлайн" режиме.

**Как работает функция**:
Функция запускает асинхронные миграции, используя `asyncio.run`.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет исключений.

**Примеры**:
```python
run_migrations_online()
```