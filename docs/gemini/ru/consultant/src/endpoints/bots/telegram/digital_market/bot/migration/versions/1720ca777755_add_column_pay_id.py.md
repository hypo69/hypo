# Анализ кода модуля `add_column_pay_id`

**Качество кода**
7
-  Плюсы
    - Код выполняет миграцию базы данных для добавления и удаления колонки `payment_id`.
    - Используются Alembic для управления миграциями.
    - Проверяется существование колонки перед добавлением/удалением, что предотвращает ошибки.
    - Используется `sa.text` для выполнения SQL-запросов, что обеспечивает большую гибкость.
-  Минусы
    -  Отсутствует обработка исключений при выполнении SQL запросов.
    -  Логирование производится с помощью `print`, а не через `logger` из `src.logger.logger`.
    -  Нет описания модуля и функций в формате RST.

**Рекомендации по улучшению**

1.  **Добавить описание модуля:** В начале файла добавить описание модуля в формате RST.
2.  **Добавить документацию к функциям:**  Добавить документацию к функциям `upgrade` и `downgrade` в формате RST, описывающую их назначение и параметры.
3.  **Использовать `logger` для логирования:** Заменить `print` на `logger.info` и `logger.error` для логирования событий, ошибок и прочей информации.
4.  **Обработка исключений:** Добавить блоки `try-except` для обработки исключений, которые могут возникнуть при выполнении SQL-запросов, и логировать ошибки через `logger.error`.
5.  **Упростить получение имен колонок:** Вместо  `columns = [row[1] for row in result]` можно использовать более понятный и итеративный метод через `for`, чтобы выводить `row` для отладки, если ошибка возникнет.
6.  **Избавиться от магических строк:** Вынести `PRAGMA table_info(\'purchases\')` в переменную.
7.  **Использовать f-строки:** Использовать f-строки для форматирования строк логгирования.

**Оптимизированный код**

```python
"""add column pay id
=========================================================================================

Этот модуль содержит миграции Alembic для добавления и удаления колонки `payment_id`
в таблице `purchases`.

Модуль используется для управления изменениями схемы базы данных.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from src.logger.logger import logger


# revision identifiers, used by Alembic.
revision: str = '1720ca777755'
down_revision: Union[str, None] = '1b95d36c8908'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Добавляет колонку `payment_id` в таблицу `purchases`, если она не существует.

    Также создает уникальный индекс `uq_purchases_payment_id` для новой колонки.
    """
    table_info_query = "PRAGMA table_info('purchases')"
    conn = op.get_bind()
    try:
        # Код исполняет запрос для получения информации о таблице
        result = conn.execute(sa.text(table_info_query))
        columns = []
        for row in result:
           # Код добавляет имя колонки в список columns
           columns.append(row[1])
        # Проверка наличия колонки 'payment_id' в таблице
        if 'payment_id' not in columns:
            # Код добавляет колонку 'payment_id'
            op.add_column('purchases', sa.Column('payment_id', sa.String(), nullable=False))
            # Код создает уникальный индекс для колонки 'payment_id'
            op.create_unique_constraint('uq_purchases_payment_id', 'purchases', ['payment_id'])
            logger.info("Колонка 'payment_id' успешно добавлена")
        else:
            logger.info("Колонка 'payment_id' уже существует, пропускаем добавление")
    except Exception as e:
        logger.error(f"Ошибка при добавлении колонки 'payment_id': {e}")


def downgrade() -> None:
    """
    Удаляет колонку `payment_id` из таблицы `purchases`, если она существует.

    Также удаляет уникальный индекс `uq_purchases_payment_id`.
    """
    table_info_query = "PRAGMA table_info('purchases')"
    conn = op.get_bind()
    try:
        # Код исполняет запрос для получения информации о таблице
        result = conn.execute(sa.text(table_info_query))
        columns = []
        for row in result:
           # Код добавляет имя колонки в список columns
           columns.append(row[1])
        # Проверяем наличие колонки 'payment_id' в таблице
        if 'payment_id' in columns:
            # Код удаляет уникальный индекс для колонки 'payment_id'
            op.drop_constraint('uq_purchases_payment_id', 'purchases', type_='unique')
            # Код удаляет колонку 'payment_id'
            op.drop_column('purchases', 'payment_id')
            logger.info("Колонка 'payment_id' успешно удалена")
        else:
            logger.info("Колонка 'payment_id' не существует, пропускаем удаление")
    except Exception as e:
        logger.error(f"Ошибка при удалении колонки 'payment_id': {e}")
```