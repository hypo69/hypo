## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
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
    *   **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
    *   **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
    *   **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
    *   **Переменные**: Их типы и использование.
    *   Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>
### Функция `main_user_kb`
1.  **Начало**: Функция принимает `user_id` (целое число).
    *   *Пример*: `user_id = 12345`
2.  **Создание клавиатуры**: Инициализируется `InlineKeyboardBuilder`.
3.  **Добавление кнопок**:
    *   Добавляются кнопки "👤 Мои покупки", "🛍 Каталог", "ℹ️ О магазине", "🌟 Поддержать автора 🌟" с соответствующими `callback_data` или `url`.
    *   *Пример:* Кнопка "🛍 Каталог" имеет `callback_data` равное `"catalog"`.
4.  **Проверка на администратора**: Проверяется, входит ли `user_id` в список `settings.ADMIN_IDS`.
    *   *Пример:* Если `user_id = 12345` и `settings.ADMIN_IDS = [12345, 67890]`, то условие верно.
5.  **Добавление админ-кнопки**: Если пользователь администратор, добавляется кнопка "⚙️ Админ панель".
6.  **Настройка отображения**: Устанавливается количество кнопок в строке `kb.adjust(1)`.
7.  **Возврат клавиатуры**: Клавиатура преобразуется в `InlineKeyboardMarkup` и возвращается.

### Функция `catalog_kb`
1.  **Начало**: Функция принимает список `catalog_data` типа `List[Category]`.
    *   *Пример:* `catalog_data = [Category(id=1, category_name="Электроника"), Category(id=2, category_name="Книги")]`
2.  **Создание клавиатуры**: Инициализируется `InlineKeyboardBuilder`.
3.  **Добавление кнопок категорий**: Для каждой категории в `catalog_data` создается кнопка с именем категории и `callback_data` вида `"category_{category.id}"`.
    *   *Пример:* Для категории `Category(id=1, category_name="Электроника")` создается кнопка с текстом "Электроника" и `callback_data` `"category_1"`.
4.  **Добавление кнопки "На главную"**: Добавляется кнопка "🏠 На главную".
5.  **Настройка отображения**: Устанавливается количество кнопок в строке `kb.adjust(2)`.
6.  **Возврат клавиатуры**: Клавиатура преобразуется в `InlineKeyboardMarkup` и возвращается.

### Функция `purchases_kb`
1.  **Начало**: Функция не принимает аргументов.
2.  **Создание клавиатуры**: Инициализируется `InlineKeyboardBuilder`.
3.  **Добавление кнопок**: Добавляются кнопки "🗑 Смотреть покупки" и "🏠 На главную".
4.  **Настройка отображения**: Устанавливается количество кнопок в строке `kb.adjust(1)`.
5.  **Возврат клавиатуры**: Клавиатура преобразуется в `InlineKeyboardMarkup` и возвращается.

### Функция `product_kb`
1.  **Начало**: Функция принимает `product_id`, `price` и `stars_price`.
2.  **Создание клавиатуры**: Инициализируется `InlineKeyboardBuilder`.
3.  **Добавление кнопок**:
    *   Добавляются кнопки "💳 Оплатить ЮКасса", "💳 Оплатить Robocassa", "⭐ Оплатить звездами" с соответствующими `callback_data`.
    *   *Пример:* `product_id=100`, `price=500`, `stars_price=20`, `callback_data` для Юкассы будет `buy_yukassa_100_500`.
    *   Добавляются кнопки "🛍 Назад", "🏠 На главную".
4.  **Настройка отображения**: Устанавливается количество кнопок в строке `kb.adjust(2)`.
5.  **Возврат клавиатуры**: Клавиатура преобразуется в `InlineKeyboardMarkup` и возвращается.

### Функция `get_product_buy_youkassa`
1.  **Начало**: Функция принимает `price` как аргумент.
2.  **Создание клавиатуры**: Создается `InlineKeyboardMarkup` с двумя рядами кнопок:
    *   Кнопка для оплаты через ЮКасса.
    *   Кнопка "Отменить".
3.  **Возврат клавиатуры**: Клавиатура `InlineKeyboardMarkup` возвращается.

### Функция `get_product_buy_robocassa`
1.  **Начало**: Функция принимает `price` и `payment_link`.
2.  **Создание клавиатуры**: Создается `InlineKeyboardMarkup` с двумя рядами кнопок:
    *   Кнопка для оплаты через Robocassa, использующая `WebAppInfo` с переданным `payment_link`.
    *   Кнопка "Отменить".
3.  **Возврат клавиатуры**: Клавиатура `InlineKeyboardMarkup` возвращается.

### Функция `get_product_buy_stars`
1.  **Начало**: Функция принимает `price`.
2.  **Создание клавиатуры**: Создается `InlineKeyboardMarkup` с двумя рядами кнопок:
    *   Кнопка для оплаты звездами.
    *   Кнопка "Отменить".
3.  **Возврат клавиатуры**: Клавиатура `InlineKeyboardMarkup` возвращается.

## <mermaid>

```mermaid
flowchart TD
    subgraph User Interaction
        MainUserKeyboard(main_user_kb) --> ProfileButton[Мои покупки]
        MainUserKeyboard --> CatalogButton[Каталог]
        MainUserKeyboard --> AboutButton[О магазине]
        MainUserKeyboard --> SupportButton[Поддержать автора]
        MainUserKeyboard --> AdminButton[Админ панель]
        CatalogButton --> CatalogKeyboard(catalog_kb)
        CatalogKeyboard --> CategoryButton[Категория товара]
        CategoryButton --> ProductKeyboard(product_kb)
        ProductKeyboard --> BuyYukassaButton[Оплатить ЮКасса]
        ProductKeyboard --> BuyRobocassaButton[Оплатить Robocassa]
        ProductKeyboard --> BuyStarsButton[Оплатить звездами]
        ProductKeyboard --> BackToCatalogButton[Назад]
        ProductKeyboard --> HomeButton[На главную]
        ProfileButton --> PurchasesKeyboard(purchases_kb)
        PurchasesKeyboard --> WatchPurchasesButton[Смотреть покупки]
         WatchPurchasesButton --> HomeButton
        BuyYukassaButton --> YoukassaPayment(get_product_buy_youkassa)
        BuyRobocassaButton --> RobocassaPayment(get_product_buy_robocassa)
         BuyStarsButton --> StarsPayment(get_product_buy_stars)
        YoukassaPayment --> HomeButton
        RobocassaPayment --> HomeButton
        StarsPayment --> HomeButton
        AboutButton --> HomeButton
        AdminButton --> HomeButton
    end

    subgraph Data Flow
    CategoryData(List[Category])
    ProductData(product_id,price,stars_price)
        CatalogKeyboard -- Использует --> CategoryData
        ProductKeyboard -- Использует --> ProductData
        RobocassaPayment -- Использует --> payment_link
    end

    MainUserKeyboard -- Использует --> UserID(user_id)
    AdminButton -- Проверяет --> AdminIDs(settings.ADMIN_IDS)
```

### Анализ зависимостей `mermaid`

1.  **User Interaction**:
    *   **`MainUserKeyboard`**: Главная клавиатура, которая отображается пользователю, когда он запускает бота.
    *   **`ProfileButton`, `CatalogButton`, `AboutButton`, `SupportButton`, `AdminButton`**: Кнопки главного меню.
    *   **`CatalogKeyboard`**: Клавиатура для отображения списка категорий товаров.
    *   **`CategoryButton`**: Кнопки, представляющие отдельные категории товаров.
    *   **`ProductKeyboard`**: Клавиатура для отображения кнопок оплаты товара.
    *   **`BuyYukassaButton`, `BuyRobocassaButton`, `BuyStarsButton`**: Кнопки для выбора способа оплаты.
    *   **`BackToCatalogButton`, `HomeButton`**: Навигационные кнопки.
        *   `PurchasesKeyboard`: Клавиатура для отображения раздела покупок.
        *   `WatchPurchasesButton`: Кнопка для просмотра списка покупок.
        *    `YoukassaPayment`: Клавиатура оплаты Юкасса.
        *    `RobocassaPayment`: Клавиатура оплаты Robocassa.
        *   `StarsPayment`: Клавиатура оплаты звездами.

2.  **Data Flow**:
    *   **`CategoryData`**: Список объектов `Category`, используемый для динамического создания кнопок категорий.
    *   **`ProductData`**: Данные о товаре (`product_id`, `price`, `stars_price`), используемые для формирования `callback_data` кнопок оплаты.
    *   **`payment_link`**: Ссылка для оплаты через Robocassa.
    *   **`UserID`**:  ID пользователя.
    *   **`AdminIDs`**: Список ID админов.

3.  **Связи**:
    *   Клавиатуры создаются на основе пользовательского ввода и данных.
    *   `CatalogKeyboard` использует `CategoryData` для отображения списка категорий.
    *   `ProductKeyboard` использует `ProductData` для формирования кнопок оплаты.
    *   `RobocassaPayment` использует `payment_link` для создания кнопки оплаты через веб-приложение.
    *   `AdminButton` проверяет `UserID` на наличие в списке `AdminIDs`.
    *   Все клавиатуры связаны друг с другом через навигационные кнопки.

## <объяснение>

### Импорты:
*   `from typing import List`: Импортирует `List` для аннотации типов, представляя списки.
*   `from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, WebAppInfo`: Импортирует классы для создания клавиатур:
    *   `InlineKeyboardMarkup` для кнопок, прикрепленных к сообщению,
    *   `ReplyKeyboardMarkup` для кнопок, отображаемых под полем ввода,
    *   `InlineKeyboardButton` для создания кнопок внутри `InlineKeyboardMarkup`,
    *   `WebAppInfo` для передачи информации о веб-приложении для Robocassa.
*   `from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder`: Импортирует вспомогательные классы для построения клавиатур:
    *   `InlineKeyboardBuilder` для упрощения создания `InlineKeyboardMarkup`,
    *   `ReplyKeyboardBuilder` для упрощения создания `ReplyKeyboardMarkup`.
*   `from bot.app.utils import generate_payment_link`: Импортирует функцию для генерации платежной ссылки.
*   `from bot.config import settings`: Импортирует настройки бота, включая список ID администраторов.
*   `from bot.dao.models import Category`: Импортирует класс `Category` для работы с категориями товаров.

### Функции:

*   `main_user_kb(user_id: int) -> InlineKeyboardMarkup`:
    *   **Аргументы**: `user_id` (int) - ID пользователя.
    *   **Возвращаемое значение**: `InlineKeyboardMarkup` - главная клавиатура пользователя.
    *   **Назначение**: Создает главную клавиатуру пользователя с кнопками "Мои покупки", "Каталог", "О магазине" и "Поддержать автора", и "Админ панель" (если пользователь - администратор).
    *   **Пример**: `main_user_kb(12345)` вернет клавиатуру с кнопками для пользователя с ID 12345.
*   `catalog_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup`:
    *   **Аргументы**: `catalog_data` (List[Category]) - список категорий товаров.
    *   **Возвращаемое значение**: `InlineKeyboardMarkup` - клавиатура с категориями товаров.
    *   **Назначение**: Создает клавиатуру с кнопками категорий товаров на основе данных из `catalog_data`.
    *   **Пример**: `catalog_kb([Category(id=1, category_name="Книги"), Category(id=2, category_name="Электроника")])` вернет клавиатуру с кнопками "Книги" и "Электроника".
*   `purchases_kb() -> InlineKeyboardMarkup`:
    *   **Аргументы**: Нет.
    *   **Возвращаемое значение**: `InlineKeyboardMarkup` - клавиатура для просмотра покупок.
    *   **Назначение**: Создает клавиатуру с кнопками "Смотреть покупки" и "На главную".
    *   **Пример**: `purchases_kb()` вернет клавиатуру для управления покупками.
*    `product_kb(product_id, price, stars_price) -> InlineKeyboardMarkup`:
     *   **Аргументы**: `product_id` (int), `price` (int), `stars_price` (int) - ID товара, цена в рублях, цена в звездах.
     *   **Возвращаемое значение**: `InlineKeyboardMarkup` - клавиатура для выбора способа оплаты.
     *   **Назначение**: Создает клавиатуру для выбора способа оплаты товара (ЮКасса, Robocassa, звезды) и навигации (назад в каталог, на главную).
     *   **Пример**: `product_kb(100, 500, 20)` вернет клавиатуру с кнопками для оплаты товара с ID 100, ценой 500 рублей и 20 звездами.
*   `get_product_buy_youkassa(price) -> InlineKeyboardMarkup`:
    *   **Аргументы**: `price` (int) - цена товара.
    *   **Возвращаемое значение**: `InlineKeyboardMarkup` - клавиатура для оплаты через ЮКасса.
    *   **Назначение**: Создает клавиатуру для оплаты товара через ЮКасса.
    *   **Пример**: `get_product_buy_youkassa(500)` вернет клавиатуру с кнопкой "Оплатить 500₽" и кнопкой "Отменить".
*   `get_product_buy_robocassa(price: int, payment_link: str) -> InlineKeyboardMarkup`:
    *   **Аргументы**: `price` (int) - цена товара, `payment_link` (str) - ссылка на оплату.
    *   **Возвращаемое значение**: `InlineKeyboardMarkup` - клавиатура для оплаты через Robocassa.
    *   **Назначение**: Создает клавиатуру для оплаты через Robocassa с использованием `WebAppInfo` для перенаправления пользователя в веб-приложение для оплаты.
    *   **Пример**: `get_product_buy_robocassa(500, "https://robocassa.com/payment/12345")` вернет клавиатуру с кнопкой "Оплатить 500₽" с переходом по ссылке и кнопкой "Отменить".
*   `get_product_buy_stars(price) -> InlineKeyboardMarkup`:
    *   **Аргументы**: `price` (int) - цена товара в звездах.
    *   **Возвращаемое значение**: `InlineKeyboardMarkup` - клавиатура для оплаты звездами.
    *   **Назначение**: Создает клавиатуру для оплаты товара звездами.
    *   **Пример**: `get_product_buy_stars(20)` вернет клавиатуру с кнопкой "Оплатить 20 ⭐" и кнопкой "Отменить".

### Переменные:

*   `user_id` (int): ID пользователя.
*   `catalog_data` (List[Category]): Список категорий товаров.
*   `kb` (InlineKeyboardBuilder): Объект для создания клавиатур.
*   `price` (int): Цена товара.
*   `payment_link` (str): Ссылка на оплату через Robocassa.
*   `stars_price` (int): Цена товара в звездах.
*   `product_id` (int): ID товара.
*   `settings.ADMIN_IDS` (List[int]): Список ID администраторов.

### Потенциальные ошибки и области для улучшения:

*   **Обработка ошибок**: Отсутствует обработка ошибок, например, при неудачной попытке получения списка категорий или при генерации платежной ссылки.
*   **Гибкость**: Код не очень гибкий, так как кнопки жестко закодированы. Можно использовать конфигурационные файлы или базу данных для более динамичного формирования кнопок.
*  **Безопасность**: При передаче цен и других чувствительных данных нужно обеспечить безопасность.
*   **Логика**: Не хватает логики по обработке ответов от платежных систем (например, подтверждения оплаты).
*   **Масштабируемость**: В текущем виде код не масштабируется для большого количества продуктов и категорий.

### Взаимосвязь с другими частями проекта:

*   Код взаимодействует с `bot.config.settings` для получения списка ID администраторов.
*   Код взаимодействует с `bot.dao.models` для получения информации о категориях товаров.
*   Код взаимодействует с `bot.app.utils` для генерации платежной ссылки для Robocassa.
*   Этот код является частью логики бота, и он используется для создания клавиатур, которые помогают пользователям взаимодействовать с ботом.

В целом, код предоставляет функциональность для создания различных клавиатур для телеграм-бота. Код требует доработки в плане обработки ошибок, гибкости, безопасности и масштабируемости.