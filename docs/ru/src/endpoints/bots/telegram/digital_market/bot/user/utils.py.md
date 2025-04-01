# Модуль для обработки успешных платежей в Telegram боте цифрового рынка

## Обзор

Модуль содержит функцию `successful_payment_logic`, которая обрабатывает логику успешной оплаты товара пользователем в Telegram боте цифрового рынка. Она добавляет информацию о покупке в базу данных, отправляет уведомления администраторам и предоставляет пользователю информацию о приобретенном товаре.

## Подробнее

Этот модуль играет важную роль в обработке финансовых транзакций в боте. Он обеспечивает фиксацию каждой покупки, уведомляет администраторов для контроля и учета, а также информирует пользователя о деталях его приобретения, обеспечивая прозрачность и удобство использования бота. Модуль использует интеграцию с Telegram API через `aiogram` для отправки сообщений и документов.

## Функции

### `successful_payment_logic`

```python
async def successful_payment_logic(session: AsyncSession, payment_data, currency, user_tg_id, bot: Bot):
    """ Функция обрабатывает логику успешной оплаты товара пользователем.

    Args:
        session (AsyncSession): Сессия базы данных SQLAlchemy для выполнения операций с базой данных.
        payment_data (dict): Словарь с данными о платеже, содержащий `product_id`, `price`, `payment_type`, `payment_id` и `user_id`.
        currency (str): Валюта, в которой был произведен платеж.
        user_tg_id (int): ID пользователя в Telegram, совершившего покупку.
        bot (Bot): Экземпляр бота aiogram для отправки сообщений пользователю и администраторам.

    Returns:
        None

    Raises:
        Exception: Если происходит ошибка при отправке уведомления администраторам.
    """
```

**Как работает функция**:

1.  **Извлечение данных о платеже**: Из словаря `payment_data` извлекаются `product_id`, `price`, `payment_type`, `payment_id` и `user_id`.
2.  **Добавление информации о покупке в БД**: Используется `PurchaseDao.add` для добавления записи о покупке в базу данных с использованием предоставленных данных платежа.
3.  **Получение данных о товаре**: Используется `ProductDao.find_one_or_none_by_id` для получения информации о купленном товаре из базы данных по `product_id`.
4.  **Уведомление администраторов**:
    *   Для каждого `admin_id` из `settings.ADMIN_IDS` отправляется уведомление о покупке товара.
    *   В случае ошибки при отправке уведомления, информация об ошибке логируется с использованием `logger.error`.
5.  **Формирование текста сообщения для пользователя**:
    *   Формируется текст сообщения, включающий благодарность за покупку, информацию о товаре (название, описание, цену, скрытое описание) и указание на наличие или отсутствие файла в товаре.
    *   В зависимости от наличия `file_id` у товара, формируется разный текст (`file_text`).
6.  **Отправка информации пользователю**:
    *   Если у товара есть `file_id`, отправляется документ с `file_id` и сформированным текстом в качестве подписи.
    *   Если у товара нет `file_id`, отправляется сообщение с сформированным текстом.
    *   В обоих случаях используется клавиатура `main_user_kb`.
7.  **Автоматический возврат звезд за покупку**:
    *   Если `payment_type` равен `'stars'`, вызывается функция `bot.refund_star_payment` для возврата звезд пользователю.

```
Данные платежа (payment_data) -> PurchaseDao.add(добавление в БД)
↓
ProductDao.find_one_or_none_by_id(получение данных о товаре)
↓
Цикл по admin_id из settings.ADMIN_IDS:
    → Отправка уведомления администратору
    → Обработка ошибок отправки уведомлений
↓
Формирование текста сообщения для пользователя (product_text)
↓
Проверка наличия file_id у товара
↓
Если file_id есть:
    → Отправка документа с file_id и текстом
Иначе:
    → Отправка сообщения с текстом
↓
Если payment_type == 'stars':
    → bot.refund_star_payment(автоматический возврат звезд)
```

**Примеры**:

Пример 1: Успешная оплата товара с файлом.

```python
from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncSession
from bot.dao.dao import PurchaseDao, ProductDao
from bot.user.kbs import main_user_kb
from bot.user.schemas import PaymentData

async def test():
    # Mock объекты и данные для примера
    class MockAsyncSession:
        async def execute(self, statement):
            # Эмулируем выполнение запроса к БД
            return MockResult()
    
        async def commit(self):
            pass

    class MockResult:
        def scalar_one_or_none(self):
            return MockProduct()

    class MockProduct:
        def __init__(self):
            self.name = "Test Product"
            self.description = "Test Description"
            self.hidden_content = "Hidden Content"
            self.file_id = "file123"

    class MockBot:
        async def send_message(self, chat_id, text, reply_markup):
            print(f"Отправлено сообщение пользователю {chat_id}: {text}")

        async def send_document(self, chat_id, document, caption, reply_markup):
            print(f"Отправлен документ пользователю {chat_id}: {document} с подписью {caption}")
            
        async def refund_star_payment(self, user_id: int, telegram_payment_charge_id: str):
            print(f"Возврат звезд пользователю {user_id} за платеж {telegram_payment_charge_id}")
    
    session = MockAsyncSession()
    payment_data = {
        "product_id": "1",
        "price": "100",
        "payment_type": "stars",
        "payment_id": "payment123",
        "user_id": "user123"
    }
    currency = "USD"
    user_tg_id = 123456789
    bot = MockBot()

    await successful_payment_logic(session, payment_data, currency, user_tg_id, bot)
async def main():
    await test()
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

Пример 2: Успешная оплата товара без файла.

```python
from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncSession
from bot.dao.dao import PurchaseDao, ProductDao
from bot.user.kbs import main_user_kb
from bot.user.schemas import PaymentData

async def test():
    # Mock объекты и данные для примера
    class MockAsyncSession:
        async def execute(self, statement):
            # Эмулируем выполнение запроса к БД
            return MockResult()
    
        async def commit(self):
            pass

    class MockResult:
        def scalar_one_or_none(self):
            return MockProduct()

    class MockProduct:
        def __init__(self):
            self.name = "Test Product"
            self.description = "Test Description"
            self.hidden_content = "Hidden Content"
            self.file_id = None  # Нет файла

    class MockBot:
        async def send_message(self, chat_id, text, reply_markup):
            print(f"Отправлено сообщение пользователю {chat_id}: {text}")

        async def send_document(self, chat_id, document, caption, reply_markup):
            print(f"Отправлен документ пользователю {chat_id}: {document} с подписью {caption}")
            
        async def refund_star_payment(self, user_id: int, telegram_payment_charge_id: str):
            print(f"Возврат звезд пользователю {user_id} за платеж {telegram_payment_charge_id}")
    
    session = MockAsyncSession()
    payment_data = {
        "product_id": "1",
        "price": "100",
        "payment_type": "stars",
        "payment_id": "payment123",
        "user_id": "user123"
    }
    currency = "USD"
    user_tg_id = 123456789
    bot = MockBot()

    await successful_payment_logic(session, payment_data, currency, user_tg_id, bot)
async def main():
    await test()
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```