## Анализ кода модуля `1720ca777755_add_column_pay_id.py`

**Качество кода**:
- **Соответствие стандартам**: 8/10
- **Плюсы**:
    - Код выполняет поставленную задачу по добавлению и удалению колонки `payment_id`.
    - Используется проверка существования колонки перед добавлением и удалением, что предотвращает ошибки.
    - Применяются `op.add_column` и `op.drop_column` для работы с колонками.
    - Код довольно читаемый и понятный.
- **Минусы**:
    - Отсутствует явное логирование действий, что затрудняет отслеживание изменений.
    - Используются `print` для вывода сообщений, что не соответствует стандартам логирования.
    - Нет документации в формате RST для функций.
    - Используются двойные кавычки в `print` вместо одинарных.

**Рекомендации по улучшению**:
- Добавить логирование через `logger` из `src.logger` для отслеживания процесса добавления/удаления колонки и любых ошибок.
- Использовать одинарные кавычки для строк в коде, за исключением `print`.
- Добавить RST-документацию для функций `upgrade` и `downgrade`.
- Перенести проверку существования колонки в отдельные функции для переиспользования.
- Заменить `print` на логирование с использованием `logger`.

**Оптимизированный код**:
```python
"""add column pay id

Revision ID: 1720ca777755
Revises: 1b95d36c8908
Create Date: 2024-12-20 21:59:03.848433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.logger import logger  # Import logger from src.logger


# revision identifiers, used by Alembic.
revision: str = '1720ca777755'
down_revision: Union[str, None] = '1b95d36c8908'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def _column_exists(table_name: str, column_name: str) -> bool:
    """
    Проверяет, существует ли колонка в таблице.

    :param table_name: Имя таблицы.
    :type table_name: str
    :param column_name: Имя колонки.
    :type column_name: str
    :return: True, если колонка существует, иначе False.
    :rtype: bool
    """
    conn = op.get_bind()
    result = conn.execute(
        sa.text(f'PRAGMA table_info(\'{table_name}\')') # Use f-string for better readability
    )
    columns = [row[1] for row in result] # Индекс 1 — это имя колонки в результатах PRAGMA
    return column_name in columns


def upgrade() -> None:
    """
    Добавляет колонку 'payment_id' в таблицу 'purchases', если её нет.

    :raises Exception: В случае ошибки при выполнении операции.
    """
    if not _column_exists('purchases', 'payment_id'):
        try:
            op.add_column('purchases', sa.Column('payment_id', sa.String(), nullable=False)) # Add column
            op.create_unique_constraint('uq_purchases_payment_id', 'purchases', ['payment_id']) # Add unique constraint
            logger.info('Added column \'payment_id\' to table \'purchases\'') # Log info
        except Exception as e:
           logger.error(f'Error adding column \'payment_id\': {e}') # Log error
    else:
        logger.info('Column \'payment_id\' already exists, skipping addition') # Log info


def downgrade() -> None:
    """
    Удаляет колонку 'payment_id' из таблицы 'purchases', если она существует.

    :raises Exception: В случае ошибки при выполнении операции.
    """
    if _column_exists('purchases', 'payment_id'):
        try:
            op.drop_constraint('uq_purchases_payment_id', 'purchases', type_='unique') # Drop unique constraint
            op.drop_column('purchases', 'payment_id') # Drop column
            logger.info('Removed column \'payment_id\' from table \'purchases\'') # Log info
        except Exception as e:
            logger.error(f'Error removing column \'payment_id\': {e}') # Log error
    else:
        logger.info('Column \'payment_id\' does not exist, skipping removal') # Log info