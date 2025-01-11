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
    -   **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
    -   **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
    -   **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
    -   **Переменные**: Их типы и использование.
    -   Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

### Пошаговая блок-схема:

1.  **`start_admin`**:
    -   **Вход:** `CallbackQuery` с `data == "admin_panel"` от администратора.
    -   **Действие:** Проверяет, является ли пользователь администратором (по `settings.ADMIN_IDS`). Отправляет подтверждение доступа и главное меню администратора.
    -   **Пример:** Пользователь нажимает кнопку "Админ-панель" в боте.
    -   **Выход:** Сообщение с меню администратора.

2.  **`admin_statistic`**:
    -   **Вход:** `CallbackQuery` с `data == "statistic"` от администратора и `AsyncSession`.
    -   **Действие:** Запрашивает статистику пользователей и заказов из базы данных. Формирует текстовое сообщение со статистикой.
    -   **Пример:** Администратор нажимает кнопку "Статистика".
    -   **Выход:** Сообщение со статистикой в чате.

3.  **`admin_process_cancel`**:
    -   **Вход:** `CallbackQuery` с `data == "cancel"` от администратора и `FSMContext`.
    -   **Действие:** Очищает состояние FSM, удаляет последнее сообщение, отправляет подтверждение отмены добавления товара.
    -   **Пример:** Во время добавления товара администратор нажимает кнопку "Отмена".
    -   **Выход:** Подтверждение отмены и возврат в меню администратора.

4.  **`admin_process_start_dell`**:
    -   **Вход:** `CallbackQuery` с `data == "delete_product"` от администратора и `AsyncSession`.
    -   **Действие:** Получает список всех товаров из базы данных и формирует сообщения с информацией о каждом товаре. К каждому сообщению добавляет кнопку для удаления товара.
    -   **Пример:** Администратор нажимает кнопку "Удалить товар".
    -   **Выход:** Сообщения со списком товаров и кнопками удаления.

5.  **`admin_process_start_dell` (обработчик удаления товара)**:
    -   **Вход:** `CallbackQuery` с `data`, начинающимся с `dell_` от администратора и `AsyncSession`.
    -   **Действие:** Извлекает `product_id` из `data`, удаляет товар из базы данных, отправляет подтверждение.
    -   **Пример:** Администратор нажимает кнопку "Удалить" под одним из товаров.
    -   **Выход:** Уведомление об удалении и удаление сообщения с товаром.

6.  **`admin_process_products`**:
    -   **Вход:** `CallbackQuery` с `data == "process_products"` от администратора и `AsyncSession`.
    -   **Действие:** Получает количество товаров из базы данных, отправляет сообщение с меню управления товарами.
    -   **Пример:** Администратор нажимает кнопку "Управление товарами".
    -   **Выход:** Сообщение с меню управления товарами.

7.  **`admin_process_add_product`**:
    -   **Вход:** `CallbackQuery` с `data == "add_product"` от администратора и `FSMContext`.
    -   **Действие:** Начинает процесс добавления товара, запрашивая имя товара. Устанавливает состояние FSM на `AddProduct.name`.
    -   **Пример:** Администратор нажимает кнопку "Добавить товар".
    -   **Выход:** Запрос имени товара и переход в состояние `AddProduct.name`.

8.  **`admin_process_name`**:
    -   **Вход:** `Message` с текстом от администратора в состоянии `AddProduct.name` и `FSMContext`.
    -   **Действие:** Сохраняет имя товара, запрашивает описание товара, устанавливает состояние FSM на `AddProduct.description`.
    -   **Пример:** Администратор вводит имя товара "Новый товар".
    -   **Выход:** Запрос описания товара и переход в состояние `AddProduct.description`.

9.  **`admin_process_description`**:
    -   **Вход:** `Message` с текстом от администратора в состоянии `AddProduct.description` и `FSMContext`, `AsyncSession`.
    -   **Действие:** Сохраняет описание товара, получает список категорий, запрашивает категорию товара. Устанавливает состояние FSM на `AddProduct.category_id`.
    -   **Пример:** Администратор вводит описание товара "Описание нового товара".
    -   **Выход:** Запрос категории товара и переход в состояние `AddProduct.category_id`.

10. **`admin_process_category`**:
    -   **Вход:** `CallbackQuery` с `data`, начинающимся с `add_category_` от администратора в состоянии `AddProduct.category_id` и `FSMContext`.
    -   **Действие:** Сохраняет выбранную категорию, запрашивает цену товара, устанавливает состояние FSM на `AddProduct.price`.
    -   **Пример:** Администратор нажимает кнопку с категорией "Электроника".
    -   **Выход:** Запрос цены товара и переход в состояние `AddProduct.price`.

11. **`admin_process_price`**:
    -   **Вход:** `Message` с текстом от администратора в состоянии `AddProduct.price` и `FSMContext`.
    -   **Действие:** Сохраняет цену товара, запрашивает файл товара или подтверждение отсутствия файла, устанавливает состояние FSM на `AddProduct.file_id`.
    -   **Пример:** Администратор вводит цену "100".
    -   **Выход:** Запрос файла или подтверждения его отсутствия и переход в состояние `AddProduct.file_id`.

12. **`admin_process_without_file` (без файла)**:
    -   **Вход:** `CallbackQuery` с `data == "without_file"` от администратора в состоянии `AddProduct.file_id` и `FSMContext`.
    -   **Действие:** Сохраняет отсутствие файла (`file_id = None`), запрашивает скрытый контент, устанавливает состояние FSM на `AddProduct.hidden_content`.
    -   **Пример:** Администратор нажимает кнопку "БЕЗ ФАЙЛА".
    -   **Выход:** Запрос скрытого контента и переход в состояние `AddProduct.hidden_content`.

13. **`admin_process_without_file` (с файлом)**:
    -   **Вход:** `Message` с документом от администратора в состоянии `AddProduct.file_id` и `FSMContext`.
    -   **Действие:** Сохраняет `file_id` документа, запрашивает скрытый контент, устанавливает состояние FSM на `AddProduct.hidden_content`.
    -   **Пример:** Администратор отправляет файл.
    -   **Выход:** Запрос скрытого контента и переход в состояние `AddProduct.hidden_content`.

14. **`admin_process_hidden_content`**:
    -   **Вход:** `Message` с текстом от администратора в состоянии `AddProduct.hidden_content` и `FSMContext`, `AsyncSession`.
    -   **Действие:** Сохраняет скрытый контент, формирует сообщение с информацией о товаре для подтверждения, запрашивает подтверждение добавления товара. Устанавливает состояние FSM на `AddProduct.confirm_add`.
    -   **Пример:** Администратор вводит скрытый контент.
    -   **Выход:** Сообщение с информацией о товаре для подтверждения и переход в состояние `AddProduct.confirm_add`.

15. **`admin_process_confirm_add`**:
    -   **Вход:** `CallbackQuery` с `data == "confirm_add"` от администратора в состоянии `AddProduct.confirm_add` и `FSMContext`, `AsyncSession`.
    -   **Действие:** Сохраняет товар в базе данных, отправляет подтверждение успешного добавления.
    -   **Пример:** Администратор нажимает кнопку "Подтвердить".
    -   **Выход:** Сообщение об успешном добавлении товара.

### Поток данных:

-   **`start_admin`:** `CallbackQuery` -> Сообщение с меню администратора
-   **`admin_statistic`:** `CallbackQuery` -> `UserDAO`, `PurchaseDao` -> Статистика -> Сообщение со статистикой
-   **`admin_process_cancel`:** `CallbackQuery` -> `FSMContext` -> Сообщение с отменой
-   **`admin_process_start_dell`:** `CallbackQuery` -> `ProductDao` -> Список товаров -> Сообщения с товарами и кнопками удаления
-   **`admin_process_start_dell` (удаление товара):** `CallbackQuery` -> `ProductDao` -> Уведомление об удалении
-   **`admin_process_products`:** `CallbackQuery` -> `ProductDao` -> Количество товаров -> Сообщение с меню управления товарами
-   **`admin_process_add_product`:** `CallbackQuery` -> `FSMContext` -> Запрос имени товара
-   **`admin_process_name`:** `Message` -> `FSMContext` -> Запрос описания
-   **`admin_process_description`:** `Message` -> `FSMContext`, `CategoryDao` -> Список категорий -> Запрос категории
-   **`admin_process_category`:** `CallbackQuery` -> `FSMContext` -> Запрос цены
-   **`admin_process_price`:** `Message` -> `FSMContext` -> Запрос файла
-   **`admin_process_without_file` (без файла):** `CallbackQuery` -> `FSMContext` -> Запрос скрытого контента
-   **`admin_process_without_file` (с файлом):** `Message` -> `FSMContext` -> Запрос скрытого контента
-   **`admin_process_hidden_content`:** `Message` -> `FSMContext`, `CategoryDao` -> Информация о товаре -> Запрос подтверждения
-   **`admin_process_confirm_add`:** `CallbackQuery` -> `FSMContext`, `ProductDao` -> Сообщение об успешном добавлении

## <mermaid>

```mermaid
flowchart TD
    subgraph Admin Panel
        StartAdmin[start_admin]
        Statistic[admin_statistic]
        CancelAdd[admin_process_cancel]
        StartDelete[admin_process_start_dell (delete_product)]
        DeleteProduct[admin_process_start_dell (обработчик удаления товара)]
        ProcessProducts[admin_process_products]
        AddProductStart[admin_process_add_product]
        AddProductName[admin_process_name]
        AddProductDescription[admin_process_description]
         AddProductCategory[admin_process_category]
        AddProductPrice[admin_process_price]
        AddProductWithoutFile[admin_process_without_file (без файла)]
        AddProductWithFile[admin_process_without_file (с файлом)]
        AddProductHiddenContent[admin_process_hidden_content]
        AddProductConfirmAdd[admin_process_confirm_add]
    end

    StartAdmin -- CallbackQuery (admin_panel) --> AdminPanelMenu
    
     AdminPanelMenu --  (statistic) --> Statistic
     AdminPanelMenu -- (delete_product) --> StartDelete
     StartDelete --  (отображение списка товаров) --> DeleteProduct
     DeleteProduct -- CallbackQuery (dell_...) --> ProductDeletion
     ProductDeletion --> AdminPanelMenu
     AdminPanelMenu -- (process_products) --> ProcessProducts
     ProcessProducts --> ProductManagementMenu
      ProductManagementMenu -- (add_product) --> AddProductStart
    AdminPanelMenu -- (отмена) --> CancelAdd
    
    AddProductStart -- CallbackQuery (add_product) --> AddProductName
    AddProductName -- Message (text) --> AddProductDescription
    AddProductDescription -- Message (text) --> AddProductCategory
    AddProductCategory -- CallbackQuery (add_category_...) --> AddProductPrice
    AddProductPrice -- Message (text) --> AddProductFileCheck
    
    subgraph AddProductFileCheck
        AddProductFileCheck -- CallbackQuery (without_file) --> AddProductWithoutFile
        AddProductFileCheck -- Message (document) --> AddProductWithFile
    end
    
     AddProductWithoutFile -- CallbackQuery (without_file) -->  AddProductHiddenContent
     AddProductWithFile  -- Message (document) -->  AddProductHiddenContent
    AddProductHiddenContent -- Message (text) --> AddProductConfirmAdd
    AddProductConfirmAdd -- CallbackQuery (confirm_add) --> ProductAddition
    ProductAddition --> AdminPanelMenu

    
    classDef adminFill fill:#f9f,stroke:#333,stroke-width:2px
    class StartAdmin, Statistic, CancelAdd, StartDelete, DeleteProduct, ProcessProducts, AddProductStart, AddProductName, AddProductDescription,AddProductCategory, AddProductPrice,AddProductWithoutFile, AddProductWithFile, AddProductHiddenContent, AddProductConfirmAdd adminFill
    
    AdminPanelMenu(Админ-панель)
    ProductManagementMenu(Управление товарами)
    ProductDeletion(Удаление товара)
    ProductAddition(Добавление товара)
```

**Анализ зависимостей:**

1.  **`aiogram`**:
    *   `Router`: Используется для создания роутера (`admin_router`), который обрабатывает входящие обновления от Telegram.
    *   `F`: Используется для фильтрации входящих обновлений на основе данных, например, `F.data` для callback-запросов или `F.from_user.id` для проверки администратора.
    *   `FSMContext`: Используется для управления состоянием Finite State Machine (FSM), что позволяет отслеживать этапы процесса добавления товара.
    *   `StatesGroup`, `State`: Используются для создания состояний FSM (класс `AddProduct`) для управления процессом добавления товара.
    *   `CallbackQuery`: Тип данных для обработки входящих callback-запросов от inline-кнопок.
    *   `Message`: Тип данных для обработки входящих текстовых и файловых сообщений от пользователей.

2.  **`sqlalchemy`**:
    *   `AsyncSession`: Используется для работы с асинхронными сессиями базы данных.

3.  **`bot.config`**:
    *   `settings`: Содержит настройки бота, включая список ID администраторов (`settings.ADMIN_IDS`).
    *   `bot`: Экземпляр бота `aiogram.Bot`.

4.  **`bot.dao.dao`**:
    *   `UserDAO`, `ProductDao`, `CategoryDao`, `PurchaseDao`: Используются для доступа к данным в базе данных для пользователей, товаров, категорий и покупок.

5.  **`bot.admin.kbs`**:
    *   Содержит различные клавиатуры (reply- и inline-) для административной панели (например, `admin_kb`, `admin_kb_back`, `product_management_kb`).

6.  **`bot.admin.schemas`**:
    *   `ProductModel`, `ProductIDModel`: Используются для валидации и передачи данных товаров между приложением и базой данных.

7.  **`bot.admin.utils`**:
    *   `process_dell_text_msg`: Утилита для удаления предыдущего сообщения с текстом.

## <объяснение>

### Импорты:

-   `asyncio`: Используется для асинхронного программирования.
-   `aiogram`: Библиотека для работы с Telegram Bot API.
-   `sqlalchemy.ext.asyncio`: Библиотека для асинхронной работы с базами данных через SQLAlchemy.
-   `bot.config`: Модуль для конфигурации бота.
    -   `settings`: Содержит настройки, включая `ADMIN_IDS`.
    -   `bot`: Экземпляр бота.
-   `bot.dao.dao`: Модуль для работы с базой данных.
    -   `UserDAO`, `ProductDao`, `CategoryDao`, `PurchaseDao`: Классы для взаимодействия с соответствующими таблицами.
-   `bot.admin.kbs`: Модуль с клавиатурами для админ-панели.
-   `bot.admin.schemas`: Модуль со схемами для валидации данных.
-   `bot.admin.utils`: Модуль с утилитами для админ-панели.

### Классы:

-   **`AddProduct(StatesGroup)`**:
    -   Роль: Класс, определяющий состояния FSM для процесса добавления товара.
    -   Атрибуты:
        -   `name`: Состояние для ввода имени товара.
        -   `description`: Состояние для ввода описания товара.
        -   `price`: Состояние для ввода цены товара.
        -   `file_id`: Состояние для отправки файла товара.
        -   `category_id`: Состояние для выбора категории товара.
        -   `hidden_content`: Состояние для ввода скрытого контента.
        -   `confirm_add`: Состояние для подтверждения добавления товара.
    -   Взаимодействие: Используется с `FSMContext` для управления переходом между состояниями и хранения данных.

### Функции:

-   **`start_admin(call: CallbackQuery)`**:
    -   Аргументы:
        -   `call`: Объект `CallbackQuery` (запрос от inline-кнопки).
    -   Возвращает: `None`.
    -   Назначение: Обрабатывает запрос на вход в админ-панель, проверяет права доступа. Отправляет пользователю главное меню администратора.
    -   Пример: Пользователь нажимает кнопку "Админ-панель".

-   **`admin_statistic(call: CallbackQuery, session_without_commit: AsyncSession)`**:
    -   Аргументы:
        -   `call`: Объект `CallbackQuery`.
        -   `session_without_commit`: Объект `AsyncSession` для работы с базой данных.
    -   Возвращает: `None`.
    -   Назначение: Получает статистику пользователей и заказов из базы данных и отправляет ее администратору.
    -   Пример: Администратор нажимает кнопку "Статистика".

-   **`admin_process_cancel(call: CallbackQuery, state: FSMContext)`**:
    -   Аргументы:
        -   `call`: Объект `CallbackQuery`.
        -   `state`: Объект `FSMContext`.
    -   Возвращает: `None`.
    -   Назначение: Отменяет текущий сценарий добавления товара, очищая состояние FSM.
    -   Пример: Во время добавления товара администратор нажимает кнопку "Отмена".

-   **`admin_process_start_dell(call: CallbackQuery, session_without_commit: AsyncSession)`**:
    -   Аргументы:
        -   `call`: Объект `CallbackQuery`.
        -   `session_without_commit`: Объект `AsyncSession`.
    -   Возвращает: `None`.
    -   Назначение: Запускает процесс удаления товара, отправляет список товаров администратору.
    -   Пример: Администратор нажимает кнопку "Удалить товар".

-   **`admin_process_start_dell(call: CallbackQuery, session_with_commit: AsyncSession)`**:
    -   Аргументы:
        -   `call`: Объект `CallbackQuery`.
        -   `session_with_commit`: Объект `AsyncSession` с поддержкой транзакций.
    -   Возвращает: `None`.
    -   Назначение: Удаляет выбранный товар из базы данных.
    -   Пример: Администратор нажимает кнопку "Удалить" под определенным товаром.

-   **`admin_process_products(call: CallbackQuery, session_without_commit: AsyncSession)`**:
    -   Аргументы:
        -   `call`: Объект `CallbackQuery`.
        -   `session_without_commit`: Объект `AsyncSession`.
    -   Возвращает: `None`.
    -   Назначение: Запускает меню управления товарами.
    -   Пример: Администратор нажимает кнопку "Управление товарами".

-   **`admin_process_add_product(call: CallbackQuery, state: FSMContext)`**:
    -   Аргументы:
        -   `call`: Объект `CallbackQuery`.
        -   `state`: Объект `FSMContext`.
    -   Возвращает: `None`.
    -   Назначение: Запускает процесс добавления нового товара, устанавливает начальное состояние FSM `AddProduct.name`.
    -   Пример: Администратор нажимает кнопку "Добавить товар".

-   **`admin_process_name(message: Message, state: FSMContext)`**:
    -   Аргументы:
        -   `message`: Объект `Message` с текстом.
        -   `state`: Объект `FSMContext`.
    -   Возвращает: `None`.
    -   Назначение: Сохраняет имя товара в FSM, запрашивает описание товара.
    -   Пример: Администратор вводит имя товара "Новый товар".

-  **`admin_process_description(message: Message, state: FSMContext, session_without_commit: AsyncSession)`**:
    -   Аргументы:
        -   `message`: Объект `Message` с текстом.
        -   `state`: Объект `FSMContext`.
        -    `session_without_commit`: Объект `AsyncSession`.
    -   Возвращает: `None`.
    -    Назначение: Сохраняет описание товара в FSM, запрашивает категорию товара.
    -   Пример: Администратор вводит описание товара.

-   **`admin_process_category(call: CallbackQuery, state: FSMContext)`**:
    -   Аргументы:
        -   `call`: Объект `CallbackQuery`.
        -   `state`: Объект `FSMContext`.
    -   Возвращает: `None`.
    -   Назначение: Сохраняет выбранную категорию товара в FSM, запрашивает цену товара.
    -   Пример: Администратор выбирает категорию товара из списка.

-   **`admin_process_price(message: Message, state: FSMContext)`**:
    -   Аргументы:
        -   `message`: Объект `Message` с текстом.
        -   `state`: Объект `FSMContext`.
    -   Возвращает: `None`.
    -   Назначение: Сохраняет цену товара в FSM, запрашивает файл или подтверждение его отсутствия.
    -    Пример: Администратор вводит цену товара.

-   **`admin_process_without_file(call: CallbackQuery, state: FSMContext)` (без файла)**:
    -   Аргументы:
        -   `call`: Объект `CallbackQuery`.
        -   `state`: Объект `FSMContext`.
    -   Возвращает: `None`.
    -   Назначение: Устанавливает `file_id` в `None`, запрашивает скрытый контент.
    -   Пример: Администратор нажимает кнопку "БЕЗ ФАЙЛА".

-    **`admin_process_without_file(message: Message, state: FSMContext)` (с файлом)**:
    -   Аргументы:
        -   `message`: Объект `Message` с файлом.
        -   `state`: Объект `FSMContext`.
    -    Возвращает: `None`.
    -   Назначение: Сохраняет `file_id` документа, запрашивает скрытый контент.
    -   Пример: Администратор отправляет файл.

-   **`admin_process_hidden_content(message: Message, state: FSMContext, session_without_commit: AsyncSession)`**:
    -   Аргументы:
        -   `message`: Объект `Message` с текстом.
        -   `state`: Объект `FSMContext`.
        -    `session_without_commit`: Объект `AsyncSession`.
    -   Возвращает: `None`.
    -   Назначение: Сохраняет скрытый контент товара, формирует сообщение для подтверждения, переходит в состояние подтверждения добавления.
    -   Пример: Администратор вводит скрытый контент.

-   **`admin_process_confirm_add(call: CallbackQuery, state: FSMContext, session_with_commit: AsyncSession)`**:
    -   Аргументы:
        -   `call`: Объект `CallbackQuery`.
        -   `state`: Объект `FSMContext`.
        -   `session_with_commit`: Объект `AsyncSession`.
    -   Возвращает: `None`.
    -   Назначение: Добавляет товар в базу данных, отправляет подтверждение.
    -   Пример: Администратор нажимает кнопку "Подтвердить".

### Переменные:

-   `admin_router`: Экземпляр `Router` для обработки обновлений, связанных с админ-панелью.
-   `settings.ADMIN_IDS`: Список ID администраторов, используется для проверки доступа.

### Потенциальные ошибки и области для улучшения:

1.  **Обработка ошибок:** В коде есть общие блоки `try...except Exception as e:`, которые могут скрывать конкретные проблемы. Желательно обрабатывать более специфические исключения (например, `sqlalchemy.exc.SQLAlchemyError`) для более точной диагностики.
2.  **Валидация данных:** Перед сохранением данных в базу желательно проводить дополнительную валидацию, например, проверку длины текста, формата цены и т.д.
3.  **Рефакторинг:** Некоторые блоки кода можно рефакторить, выделив повторяющиеся части в отдельные функции. Например, код отправки сообщения с `reply_markup` или удаления предыдущего сообщения.
4.  **Безопасность:** Хранение ID администраторов в коде (хоть и в settings) не является лучшей практикой. Можно рассмотреть использование переменных окружения или конфигурационных файлов.
5.  **Улучшение UX:** Можно добавить промежуточные сообщения, информирующие администратора о текущем процессе (например, "Идет загрузка файла...", "Сохранение товара...").
6.  **Недостаток комментариев:** Код мог бы быть более читаемым, если добавить комментарии к логически важным частям.

### Взаимосвязь с другими частями проекта:

-   Данный модуль тесно связан с модулями `bot.config`, `bot.dao.dao`, `bot.admin.kbs`, `bot.admin.schemas` и `bot.admin.utils`.
    -   `bot.config` предоставляет общую конфигурацию проекта, включая настройки админ-панели.
    -   `bot.dao.dao` обеспечивает доступ к базе данных, взаимодействуя с таблицами пользователей, товаров, категорий и покупок.
    -   `bot.admin.kbs` содержит клавиатуры для управления админ-панелью.
    -   `bot.admin.schemas` содержит схемы для работы с данными товаров.
    -   `bot.admin.utils` содержит утилиты, используемые в админ-панели.
-   Этот модуль также зависит от `aiogram` для обработки входящих обновлений от Telegram и `sqlalchemy` для работы с базой данных.
-   Код является частью логики административной панели Telegram-бота. Он обеспечивает функциональность для просмотра статистики, управления товарами (добавление, удаление).

Этот анализ предоставляет подробное представление о функциональности и структуре кода, а также о его взаимосвязях с другими частями проекта.