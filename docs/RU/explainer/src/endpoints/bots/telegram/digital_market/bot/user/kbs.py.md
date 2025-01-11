## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3.  **<объяснение>**: Предоставьте подробные объяснения:
    - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
    - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
    - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
    - **Переменные**: Их типы и использование.
    - Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

**1. `main_user_kb(user_id: int)`**

   *   **Начало:** Функция принимает `user_id` (целое число) как аргумент.
   *   **Создание клавиатуры:** Инициализируется `InlineKeyboardBuilder` для создания inline-клавиатуры.
   *   **Добавление кнопок:** Добавляются кнопки "👤 Мои покупки", "🛍 Каталог", "ℹ️ О магазине" и "🌟 Поддержать автора 🌟" с соответствующими callback_data или URL.
   *   **Проверка администратора:** Проверяется, является ли `user_id` администратором на основе `settings.ADMIN_IDS`. Если да, то добавляется кнопка "⚙️ Админ панель".
     *   _Пример:_ Если `user_id` равен 12345, и 12345 присутствует в `settings.ADMIN_IDS`, то кнопка "⚙️ Админ панель" будет добавлена.
   *   **Настройка размещения:** Кнопки размещаются в один столбец с помощью `kb.adjust(1)`.
   *   **Возврат:** Функция возвращает готовую `InlineKeyboardMarkup`.
   *   **Конец.**

**2. `catalog_kb(catalog_data: List[Category])`**

   *   **Начало:** Функция принимает список объектов `Category` как аргумент.
   *   **Создание клавиатуры:** Инициализируется `InlineKeyboardBuilder`.
   *   **Итерация по категориям:** Проходится по каждой категории в `catalog_data` и добавляет кнопку с названием категории и callback_data в виде `category_{category.id}`.
     *   _Пример:_ Если есть категория с `category.category_name = "Одежда"` и `category.id = 1`, то будет создана кнопка "Одежда" с `callback_data = "category_1"`.
   *   **Добавление кнопки "На главную":** Добавляется кнопка "🏠 На главную" с `callback_data="home"`.
   *   **Настройка размещения:** Кнопки размещаются в два столбца с помощью `kb.adjust(2)`.
   *   **Возврат:** Функция возвращает готовую `InlineKeyboardMarkup`.
   *   **Конец.**

**3. `purchases_kb()`**

   *   **Начало:** Функция не принимает аргументов.
   *   **Создание клавиатуры:** Инициализируется `InlineKeyboardBuilder`.
   *   **Добавление кнопок:** Добавляются кнопки "🗑 Смотреть покупки" и "🏠 На главную" с соответствующими `callback_data`.
   *   **Настройка размещения:** Кнопки размещаются в один столбец с помощью `kb.adjust(1)`.
   *   **Возврат:** Функция возвращает готовую `InlineKeyboardMarkup`.
   *   **Конец.**

**4. `product_kb(product_id, price, stars_price)`**

   *   **Начало:** Функция принимает `product_id` (идентификатор продукта), `price` (цена) и `stars_price` (цена в звездах) как аргументы.
   *   **Создание клавиатуры:** Инициализируется `InlineKeyboardBuilder`.
   *   **Добавление кнопок оплаты:** Добавляются кнопки для оплаты через ЮКасса, Robocassa и звездами, каждая с уникальным `callback_data`.
     *   _Пример:_ Если `product_id = 12`, `price = 100`, `stars_price = 50`, то будут созданы кнопки с `callback_data`  `buy_yukassa_12_100`, `buy_robocassa_12_100` и `buy_stars_12_50`.
   *   **Добавление кнопок навигации:** Добавляются кнопки "🛍 Назад" и "🏠 На главную" с соответствующими `callback_data`.
   *   **Настройка размещения:** Кнопки размещаются в два столбца с помощью `kb.adjust(2)`.
   *   **Возврат:** Функция возвращает готовую `InlineKeyboardMarkup`.
   *   **Конец.**

**5. `get_product_buy_youkassa(price)`**

   *   **Начало:** Функция принимает `price` как аргумент.
   *   **Создание клавиатуры:** Создается `InlineKeyboardMarkup` напрямую, с кнопкой для оплаты через ЮКасса.
     *   _Пример:_ Если `price = 200`, то кнопка будет иметь текст "Оплатить 200₽" и `pay=True`.
   *   **Добавление кнопки отмены:** Добавляется кнопка "Отменить" с `callback_data = "home"`.
   *   **Возврат:** Функция возвращает готовую `InlineKeyboardMarkup`.
   *   **Конец.**

**6. `get_product_buy_robocassa(price: int, payment_link: str)`**

   *   **Начало:** Функция принимает `price` и `payment_link` как аргументы.
   *   **Создание клавиатуры:** Создается `InlineKeyboardMarkup` напрямую, с кнопкой для оплаты через Robocassa.
     *   _Пример:_ Если `price = 300` и `payment_link = "https://example.com/payment"`, то кнопка будет иметь текст "Оплатить 300₽" и `web_app` со ссылкой.
   *   **Добавление кнопки отмены:** Добавляется кнопка "Отменить" с `callback_data = "home"`.
   *   **Возврат:** Функция возвращает готовую `InlineKeyboardMarkup`.
   *   **Конец.**

**7. `get_product_buy_stars(price)`**

   *   **Начало:** Функция принимает `price` как аргумент.
   *   **Создание клавиатуры:** Создается `InlineKeyboardMarkup` напрямую, с кнопкой для оплаты звездами.
     *   _Пример:_ Если `price = 40`, то кнопка будет иметь текст "Оплатить 40 ⭐" и `pay=True`.
   *   **Добавление кнопки отмены:** Добавляется кнопка "Отменить" с `callback_data = "home"`.
   *   **Возврат:** Функция возвращает готовую `InlineKeyboardMarkup`.
   *   **Конец.**

## <mermaid>

```mermaid
flowchart TD
    subgraph Основная логика
        StartMainUserKb(Начало main_user_kb) --> CreateMainKeyboard(Создание InlineKeyboardBuilder)
        CreateMainKeyboard --> AddMainButtons(Добавление основных кнопок)
        AddMainButtons --> CheckAdmin[Проверка user_id на админа]
        CheckAdmin -- Is Admin --> AddAdminButton(Добавить кнопку админ-панели)
        CheckAdmin -- Not Admin --> AdjustMainLayout(Настройка расположения)
        AddAdminButton --> AdjustMainLayout
        AdjustMainLayout --> ReturnMainKeyboard(Возврат InlineKeyboardMarkup)
        ReturnMainKeyboard --> EndMainUserKb(Конец main_user_kb)

        StartCatalogKb(Начало catalog_kb) --> CreateCatalogKeyboard(Создание InlineKeyboardBuilder)
        CreateCatalogKeyboard --> IterateCategories(Итерация по категориям)
        IterateCategories --> AddCategoryButton(Добавление кнопки категории)
        AddCategoryButton --> IterateCategories
        IterateCategories -- End Iteration --> AddHomeButtonCatalog(Добавление кнопки "На главную")
        AddHomeButtonCatalog --> AdjustCatalogLayout(Настройка расположения)
        AdjustCatalogLayout --> ReturnCatalogKeyboard(Возврат InlineKeyboardMarkup)
        ReturnCatalogKeyboard --> EndCatalogKb(Конец catalog_kb)

        StartPurchasesKb(Начало purchases_kb) --> CreatePurchasesKeyboard(Создание InlineKeyboardBuilder)
        CreatePurchasesKeyboard --> AddPurchasesButtons(Добавление кнопок покупок)
        AddPurchasesButtons --> AdjustPurchasesLayout(Настройка расположения)
        AdjustPurchasesLayout --> ReturnPurchasesKeyboard(Возврат InlineKeyboardMarkup)
        ReturnPurchasesKeyboard --> EndPurchasesKb(Конец purchases_kb)

        StartProductKb(Начало product_kb) --> CreateProductKeyboard(Создание InlineKeyboardBuilder)
        CreateProductKeyboard --> AddPaymentButtons(Добавление кнопок оплаты)
        AddPaymentButtons --> AddNavigationButtons(Добавление кнопок навигации)
        AddNavigationButtons --> AdjustProductLayout(Настройка расположения)
        AdjustProductLayout --> ReturnProductKeyboard(Возврат InlineKeyboardMarkup)
        ReturnProductKeyboard --> EndProductKb(Конец product_kb)

        StartYoukassaKb(Начало get_product_buy_youkassa) --> CreateYoukassaKeyboard(Создание InlineKeyboardMarkup)
        CreateYoukassaKeyboard --> AddYoukassaPayButton(Добавление кнопки оплаты ЮКасса)
        AddYoukassaPayButton --> AddYoukassaCancelButton(Добавление кнопки отмены)
        AddYoukassaCancelButton --> ReturnYoukassaKeyboard(Возврат InlineKeyboardMarkup)
        ReturnYoukassaKeyboard --> EndYoukassaKb(Конец get_product_buy_youkassa)

         StartRobocassaKb(Начало get_product_buy_robocassa) --> CreateRobocassaKeyboard(Создание InlineKeyboardMarkup)
        CreateRobocassaKeyboard --> AddRobocassaPayButton(Добавление кнопки оплаты Robocassa)
        AddRobocassaPayButton --> AddRobocassaCancelButton(Добавление кнопки отмены)
        AddRobocassaCancelButton --> ReturnRobocassaKeyboard(Возврат InlineKeyboardMarkup)
        ReturnRobocassaKeyboard --> EndRobocassaKb(Конец get_product_buy_robocassa)

        StartStarsKb(Начало get_product_buy_stars) --> CreateStarsKeyboard(Создание InlineKeyboardMarkup)
        CreateStarsKeyboard --> AddStarsPayButton(Добавление кнопки оплаты звездами)
        AddStarsPayButton --> AddStarsCancelButton(Добавление кнопки отмены)
        AddStarsCancelButton --> ReturnStarsKeyboard(Возврат InlineKeyboardMarkup)
         ReturnStarsKeyboard --> EndStarsKb(Конец get_product_buy_stars)

    end
    subgraph Зависимости
        import_typing(from typing import List)
        import_aiogram_types(from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, WebAppInfo)
        import_aiogram_keyboard(from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder)
         import_payment_link(from bot.app.utils import generate_payment_link)
        import_settings(from bot.config import settings)
        import_category(from bot.dao.models import Category)
        import_typing --> StartMainUserKb
        import_aiogram_types --> StartMainUserKb
        import_aiogram_keyboard --> StartMainUserKb
        import_settings --> StartMainUserKb
        import_typing --> StartCatalogKb
        import_aiogram_types --> StartCatalogKb
         import_aiogram_keyboard --> StartCatalogKb
        import_category --> StartCatalogKb
        import_aiogram_types --> StartPurchasesKb
        import_aiogram_keyboard --> StartPurchasesKb
        import_aiogram_types --> StartProductKb
        import_aiogram_keyboard --> StartProductKb
        import_aiogram_types --> StartYoukassaKb
        import_aiogram_types --> StartRobocassaKb
        import_aiogram_types --> StartStarsKb


    end
```

**Анализ зависимостей `mermaid`:**

*   **`import_typing(from typing import List)`**: Импортирует `List` для аннотации типов, что помогает при создании списка категорий для каталога.
*   **`import_aiogram_types(...)`**: Импортирует типы из `aiogram`, необходимые для создания кнопок, клавиатур и веб-приложений, таких как `InlineKeyboardMarkup`, `ReplyKeyboardMarkup`, `InlineKeyboardButton` и `WebAppInfo`.
*   **`import_aiogram_keyboard(...)`**: Импортирует `InlineKeyboardBuilder` и `ReplyKeyboardBuilder` для удобного создания клавиатур.
*  **`import_payment_link(from bot.app.utils import generate_payment_link)`**: Импортируется функция `generate_payment_link` для генерации ссылок для оплаты.
*   **`import_settings(from bot.config import settings)`**: Импортирует настройки бота, включая список идентификаторов администраторов (`ADMIN_IDS`).
*   **`import_category(from bot.dao.models import Category)`**: Импортирует модель `Category` для работы с категориями товаров.
*   Стрелки показывают зависимости между импортами и их использованием в функциях.

## <объяснение>

**Импорты:**

*   `from typing import List`: Импортирует `List` для типизации списков, например, списка категорий товаров.
*   `from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, WebAppInfo`: Импортирует классы для создания инлайн- и обычных клавиатур, отдельных кнопок, и информации о веб-приложениях из библиотеки `aiogram`.
    *   `InlineKeyboardMarkup`: Класс для создания инлайн-клавиатур, отображаемых под сообщением.
    *   `ReplyKeyboardMarkup`: Класс для создания обычных клавиатур, отображаемых в нижней части чата.
    *   `InlineKeyboardButton`: Класс для создания отдельных кнопок внутри инлайн-клавиатуры.
    *   `WebAppInfo`: Класс для предоставления информации о веб-приложении, используемого в кнопках.
*   `from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder`: Импортирует классы-строители для создания клавиатур, упрощая процесс их формирования.
    *   `InlineKeyboardBuilder`: Помогает создавать инлайн-клавиатуры более гибко.
    *   `ReplyKeyboardBuilder`: Помогает создавать обычные клавиатуры более гибко.
*  `from bot.app.utils import generate_payment_link`: Импортирует функцию для генерации платежных ссылок. Предположительно используется для генерации ссылок для оплаты Robocassa.
*   `from bot.config import settings`: Импортирует настройки бота, включая список идентификаторов администраторов. Предположительно файл `settings.py`, который содержит основные настройки бота.
*   `from bot.dao.models import Category`: Импортирует модель данных `Category` для представления категорий товаров, связанную с базой данных. Предположительно используется для получения списка категорий из базы данных.

**Функции:**

1.  **`main_user_kb(user_id: int) -> InlineKeyboardMarkup`**:
    *   **Аргументы**:
        *   `user_id`: ID пользователя (целое число).
    *   **Возвращает**: `InlineKeyboardMarkup` – инлайн-клавиатура для главного меню пользователя.
    *   **Назначение**: Формирует главное меню пользователя с кнопками "Мои покупки", "Каталог", "О магазине", "Поддержать автора". Добавляет кнопку "Админ панель" для администраторов.
    *   **Пример:** Если `user_id=12345` и `settings.ADMIN_IDS = [12345, 67890]`, то вернёт клавиатуру с кнопкой "Админ панель".
2.  **`catalog_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup`**:
    *   **Аргументы**:
        *   `catalog_data`: Список объектов `Category`, представляющих категории товаров.
    *   **Возвращает**: `InlineKeyboardMarkup` – инлайн-клавиатура для отображения списка категорий.
    *   **Назначение**: Создает клавиатуру с кнопками для каждой категории из списка `catalog_data` и кнопкой "На главную".
    *   **Пример:** Если `catalog_data` содержит `[Category(id=1, category_name='Одежда'), Category(id=2, category_name='Обувь')]`, то вернёт клавиатуру с кнопками "Одежда" и "Обувь".
3.  **`purchases_kb() -> InlineKeyboardMarkup`**:
    *   **Аргументы**: Нет.
    *   **Возвращает**: `InlineKeyboardMarkup` – инлайн-клавиатура для управления покупками.
    *   **Назначение**: Формирует клавиатуру с кнопками "Смотреть покупки" и "На главную".
    *   **Пример:** Вернёт клавиатуру с кнопками просмотра покупок и возврата на главную.
4.  **`product_kb(product_id, price, stars_price) -> InlineKeyboardMarkup`**:
    *   **Аргументы**:
        *   `product_id`: ID продукта.
        *   `price`: Цена продукта.
        *   `stars_price`: Цена продукта в звездах.
    *   **Возвращает**: `InlineKeyboardMarkup` – инлайн-клавиатура для выбора способа оплаты товара.
    *   **Назначение**: Создает кнопки для оплаты продукта через ЮКасса, Robocassa и звездами, а также кнопки для возврата в каталог и на главную.
    *   **Пример:** Если `product_id=5`, `price=100`, `stars_price=50`, то вернёт клавиатуру с кнопками оплаты через ЮКасса, Robocassa и звездами, с ценами.
5.  **`get_product_buy_youkassa(price) -> InlineKeyboardMarkup`**:
    *   **Аргументы**:
        *   `price`: Цена продукта.
    *   **Возвращает**: `InlineKeyboardMarkup` – инлайн-клавиатура с кнопкой оплаты через ЮКасса.
    *   **Назначение**: Создает клавиатуру с кнопкой для оплаты через ЮКасса и кнопкой "Отменить". Кнопка оплаты имеет параметр `pay=True`.
    *   **Пример:** Если `price = 150`, то вернет клавиатуру с кнопкой "Оплатить 150₽".
6.  **`get_product_buy_robocassa(price: int, payment_link: str) -> InlineKeyboardMarkup`**:
    *   **Аргументы**:
        *   `price`: Цена продукта.
        *  `payment_link`: Ссылка на оплату в Robocassa
    *   **Возвращает**: `InlineKeyboardMarkup` – инлайн-клавиатура с кнопкой оплаты через Robocassa.
    *   **Назначение**: Создает клавиатуру с кнопкой для оплаты через Robocassa используя веб-приложение, и кнопкой "Отменить". Кнопка оплаты использует `web_app` для перенаправления на платежный шлюз.
    *   **Пример:** Если `price = 200` и `payment_link = "https://example.com/payment"`, то вернет клавиатуру с кнопкой "Оплатить 200₽" и `web_app`, ведущей по ссылке.
7.  **`get_product_buy_stars(price) -> InlineKeyboardMarkup`**:
    *   **Аргументы**:
        *   `price`: Цена продукта в звездах.
    *   **Возвращает**: `InlineKeyboardMarkup` – инлайн-клавиатура с кнопкой оплаты звездами.
    *   **Назначение**: Создает клавиатуру с кнопкой для оплаты звездами и кнопкой "Отменить". Кнопка оплаты имеет параметр `pay=True`.
    *   **Пример:** Если `price = 75`, то вернет клавиатуру с кнопкой "Оплатить 75 ⭐".

**Переменные:**

*   `kb`: Объект `InlineKeyboardBuilder` для создания инлайн-клавиатур.
*   `settings.ADMIN_IDS`: Список целых чисел, представляющих идентификаторы администраторов. Определен в файле настроек.
*   `catalog_data`: Список объектов типа `Category`, представляющих категории товаров.
*   `product_id`, `price`, `stars_price`: Целые числа, представляющие идентификатор продукта, его цену и цену в звездах, соответственно.
* `payment_link`: Строка, представляющая собой ссылку для оплаты Robocassa.

**Потенциальные ошибки и области для улучшения:**

*   **Обработка ошибок:**  Код не содержит явной обработки ошибок. Например, могут возникнуть ошибки при работе с базой данных, при генерации ссылок на оплату, или при отсутствии необходимых данных. Рекомендуется добавить блоки `try...except` для обработки возможных исключений.
*   **Логирование:**  Нет логирования. Рекомендуется добавить логирование для отслеживания работы бота и отладки.
*   **Внешние сервисы:** Для оплаты через Robocassa используется `payment_link`, который передается извне, нужно убедиться, что ссылка валидная и не истекает.
*   **Централизация:** Можно было бы создать базовый класс/функцию для создания кнопок, чтобы не повторять код по созданию кнопок отмены или на главную.

**Взаимосвязь с другими частями проекта:**

*   Этот модуль используется для создания клавиатур в Telegram-боте, взаимодействуя с пользователями через текстовые и навигационные элементы.
*   Функции используют настройки из `bot.config.settings`, такие как список администраторов.
*   Для получения списка категорий используется `bot.dao.models.Category`, подразумевая связь с базой данных.
*   Для Robocassa используется `bot.app.utils.generate_payment_link`.

В целом, код выполняет свою функцию по созданию клавиатур для Telegram-бота, но можно улучшить его надежность и гибкость с помощью добавления обработки ошибок, логирования и рефакторинга повторяющихся частей.