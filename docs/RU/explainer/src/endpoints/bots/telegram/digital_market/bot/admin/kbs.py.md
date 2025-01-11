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
```markdown
## <алгоритм>

### catalog_admin_kb
1.  **Начало:** Функция принимает список объектов `Category` (например, `[Category(id=1, category_name='Электроника'), Category(id=2, category_name='Одежда')]`).
2.  **Инициализация:** Создается объект `InlineKeyboardBuilder` для построения кнопок.
3.  **Итерация:**
    -   Для каждой категории в списке `catalog_data`:
        -   Создается кнопка с текстом равным `category.category_name` (например, "Электроника") и `callback_data` в формате `add_category_{category.id}` (например, "add_category_1").
        -   Кнопка добавляется в `InlineKeyboardBuilder`.
    -   Пример, для категории 'Электроника' будет создана кнопка с текстом 'Электроника' и `callback_data='add_category_1'`.
    -   Пример, для категории 'Одежда' будет создана кнопка с текстом 'Одежда' и `callback_data='add_category_2'`.
4.  **Добавление кнопки "Отмена":** Создается и добавляется кнопка с текстом "Отмена" и `callback_data="admin_panel"`.
5.  **Настройка расположения:** Кнопки размещаются в два столбца, с помощью `kb.adjust(2)`.
6.  **Возврат:** Функция возвращает готовую `InlineKeyboardMarkup`, представляющую собой набор кнопок для Telegram.

### admin_send_file_kb
1.  **Начало:** Функция не принимает аргументов.
2.  **Инициализация:** Создается объект `InlineKeyboardBuilder`.
3.  **Добавление кнопок:**
    -   Создается кнопка "Без файла" с `callback_data="without_file"`
    -   Создается кнопка "Отмена" с `callback_data="admin_panel"`
4.  **Настройка расположения:** Кнопки размещаются в два столбца, с помощью `kb.adjust(2)`.
5.  **Возврат:** Функция возвращает `InlineKeyboardMarkup`.

### admin_kb
1.  **Начало:** Функция не принимает аргументов.
2.  **Инициализация:** Создается объект `InlineKeyboardBuilder`.
3.  **Добавление кнопок:**
    -   Создается кнопка "📊 Статистика" с `callback_data="statistic"`.
    -   Создается кнопка "🛍️ Управлять товарами" с `callback_data="process_products"`.
    -   Создается кнопка "🏠 На главную" с `callback_data="home"`.
4.  **Настройка расположения:** Кнопки размещаются в два столбца, с помощью `kb.adjust(2)`.
5.  **Возврат:** Функция возвращает `InlineKeyboardMarkup`.

### admin_kb_back
1.  **Начало:** Функция не принимает аргументов.
2.  **Инициализация:** Создается объект `InlineKeyboardBuilder`.
3.  **Добавление кнопок:**
    -   Создается кнопка "⚙️ Админ панель" с `callback_data="admin_panel"`.
    -   Создается кнопка "🏠 На главную" с `callback_data="home"`.
4.  **Настройка расположения:** Кнопки размещаются в один столбец, с помощью `kb.adjust(1)`.
5.  **Возврат:** Функция возвращает `InlineKeyboardMarkup`.

### dell_product_kb
1.  **Начало:** Функция принимает `product_id` типа int.
2.  **Инициализация:** Создается объект `InlineKeyboardBuilder`.
3.  **Добавление кнопок:**
    -   Создается кнопка "🗑️ Удалить" с `callback_data` в формате `dell_{product_id}` (например, "dell_123").
    -   Создается кнопка "⚙️ Админ панель" с `callback_data="admin_panel"`.
    -   Создается кнопка "🏠 На главную" с `callback_data="home"`.
4.  **Настройка расположения:** Кнопки размещаются в три ряда: 2, 2 и 1 кнопка, с помощью `kb.adjust(2, 2, 1)`.
5.  **Возврат:** Функция возвращает `InlineKeyboardMarkup`.

### product_management_kb
1.  **Начало:** Функция не принимает аргументов.
2.  **Инициализация:** Создается объект `InlineKeyboardBuilder`.
3.  **Добавление кнопок:**
    -   Создается кнопка "➕ Добавить товар" с `callback_data="add_product"`.
    -   Создается кнопка "🗑️ Удалить товар" с `callback_data="delete_product"`.
    -   Создается кнопка "⚙️ Админ панель" с `callback_data="admin_panel"`.
    -   Создается кнопка "🏠 На главную" с `callback_data="home"`.
4.  **Настройка расположения:** Кнопки размещаются в три ряда: 2, 2 и 1 кнопка, с помощью `kb.adjust(2, 2, 1)`.
5.  **Возврат:** Функция возвращает `InlineKeyboardMarkup`.

### cancel_kb_inline
1.  **Начало:** Функция не принимает аргументов.
2.  **Инициализация:** Создается объект `InlineKeyboardBuilder`.
3.  **Добавление кнопки:** Создается кнопка "Отмена" с `callback_data="cancel"`.
4.  **Возврат:** Функция возвращает `InlineKeyboardMarkup`.

### admin_confirm_kb
1.  **Начало:** Функция не принимает аргументов.
2.  **Инициализация:** Создается объект `InlineKeyboardBuilder`.
3.  **Добавление кнопок:**
    -   Создается кнопка "Все верно" с `callback_data="confirm_add"`.
    -   Создается кнопка "Отмена" с `callback_data="admin_panel"`.
4.  **Настройка расположения:** Кнопки размещаются в один столбец, с помощью `kb.adjust(1)`.
5.  **Возврат:** Функция возвращает `InlineKeyboardMarkup`.

## <mermaid>

```mermaid
flowchart TD
    subgraph InlineKeyboardBuilder
        direction LR
        StartBuilder[Начало] --> CreateBuilder[<code>InlineKeyboardBuilder()</code><br>Создание билдера клавиатуры]
        CreateBuilder --> AddButton1[<code>kb.button()</code><br>Добавить кнопку]
        AddButton1 --> AddButton2[<code>kb.button()</code><br>Добавить кнопку]
        AddButton2 --> AdjustLayout[<code>kb.adjust()</code><br>Настройка расположения кнопок]
        AdjustLayout --> FinishBuild[<code>kb.as_markup()</code><br>Сборка и возврат клавиатуры]
        
    end
    
    subgraph catalog_admin_kb
        direction TB
         StartCatalog[Начало функции <code>catalog_admin_kb</code>] --> ProcessCategories[Перебор списка категорий]
        ProcessCategories -- для каждой Category --> AddCategoryButton[<code>kb.button(text=category.category_name, callback_data="add_category_{category.id}")</code>]
        AddCategoryButton --> AddCancelButtonCatalog[<code>kb.button(text="Отмена", callback_data="admin_panel")</code>]
        AddCancelButtonCatalog --> AdjustCatalog[<code>kb.adjust(2)</code>]
        AdjustCatalog --> FinishCatalog[<code>kb.as_markup()</code>]
        FinishCatalog --> ReturnCatalog[Возврат <code>InlineKeyboardMarkup</code>]
    end
    
    subgraph admin_send_file_kb
        direction TB
        StartSendFile[Начало функции <code>admin_send_file_kb</code>] --> AddWithoutFileButton[<code>kb.button(text="Без файла", callback_data="without_file")</code>]
        AddWithoutFileButton --> AddCancelButtonSendFile[<code>kb.button(text="Отмена", callback_data="admin_panel")</code>]
        AddCancelButtonSendFile --> AdjustSendFile[<code>kb.adjust(2)</code>]
        AdjustSendFile --> FinishSendFile[<code>kb.as_markup()</code>]
        FinishSendFile --> ReturnSendFile[Возврат <code>InlineKeyboardMarkup</code>]
    end
    
    subgraph admin_kb
        direction TB
        StartAdminKb[Начало функции <code>admin_kb</code>] --> AddStatisticButton[<code>kb.button(text="📊 Статистика", callback_data="statistic")</code>]
        AddStatisticButton --> AddManageProductsButton[<code>kb.button(text="🛍️ Управлять товарами", callback_data="process_products")</code>]
        AddManageProductsButton --> AddHomeButtonAdmin[<code>kb.button(text="🏠 На главную", callback_data="home")</code>]
         AddHomeButtonAdmin --> AdjustAdminKb[<code>kb.adjust(2)</code>]
         AdjustAdminKb --> FinishAdminKb[<code>kb.as_markup()</code>]
         FinishAdminKb --> ReturnAdminKb[Возврат <code>InlineKeyboardMarkup</code>]
    end
    
     subgraph admin_kb_back
        direction TB
        StartAdminBack[Начало функции <code>admin_kb_back</code>] --> AddAdminPanelButton[<code>kb.button(text="⚙️ Админ панель", callback_data="admin_panel")</code>]
        AddAdminPanelButton --> AddHomeButtonAdminBack[<code>kb.button(text="🏠 На главную", callback_data="home")</code>]
        AddHomeButtonAdminBack --> AdjustAdminBack[<code>kb.adjust(1)</code>]
        AdjustAdminBack --> FinishAdminBack[<code>kb.as_markup()</code>]
        FinishAdminBack --> ReturnAdminBack[Возврат <code>InlineKeyboardMarkup</code>]
    end

    subgraph dell_product_kb
        direction TB
        StartDellProduct[Начало функции <code>dell_product_kb</code>] --> AddDeleteButtonDell[<code>kb.button(text="🗑️ Удалить", callback_data="dell_{product_id}")</code>]
        AddDeleteButtonDell --> AddAdminPanelButtonDell[<code>kb.button(text="⚙️ Админ панель", callback_data="admin_panel")</code>]
        AddAdminPanelButtonDell --> AddHomeButtonDell[<code>kb.button(text="🏠 На главную", callback_data="home")</code>]
        AddHomeButtonDell --> AdjustDellProduct[<code>kb.adjust(2, 2, 1)</code>]
        AdjustDellProduct --> FinishDellProduct[<code>kb.as_markup()</code>]
        FinishDellProduct --> ReturnDellProduct[Возврат <code>InlineKeyboardMarkup</code>]
    end
    
     subgraph product_management_kb
        direction TB
        StartProductManagement[Начало функции <code>product_management_kb</code>] --> AddAddProductButton[<code>kb.button(text="➕ Добавить товар", callback_data="add_product")</code>]
        AddAddProductButton --> AddDeleteProductButton[<code>kb.button(text="🗑️ Удалить товар", callback_data="delete_product")</code>]
        AddDeleteProductButton --> AddAdminPanelButtonProduct[<code>kb.button(text="⚙️ Админ панель", callback_data="admin_panel")</code>]
        AddAdminPanelButtonProduct --> AddHomeButtonProduct[<code>kb.button(text="🏠 На главную", callback_data="home")</code>]
        AddHomeButtonProduct --> AdjustProductManagement[<code>kb.adjust(2, 2, 1)</code>]
        AdjustProductManagement --> FinishProductManagement[<code>kb.as_markup()</code>]
        FinishProductManagement --> ReturnProductManagement[Возврат <code>InlineKeyboardMarkup</code>]
    end
    
     subgraph cancel_kb_inline
        direction TB
        StartCancelKb[Начало функции <code>cancel_kb_inline</code>] --> AddCancelButtonCancel[<code>kb.button(text="Отмена", callback_data="cancel")</code>]
        AddCancelButtonCancel --> FinishCancelKb[<code>kb.as_markup()</code>]
        FinishCancelKb --> ReturnCancelKb[Возврат <code>InlineKeyboardMarkup</code>]
    end
    
     subgraph admin_confirm_kb
        direction TB
        StartConfirmKb[Начало функции <code>admin_confirm_kb</code>] --> AddConfirmButton[<code>kb.button(text="Все верно", callback_data="confirm_add")</code>]
        AddConfirmButton --> AddCancelButtonConfirm[<code>kb.button(text="Отмена", callback_data="admin_panel")</code>]
        AddCancelButtonConfirm --> AdjustConfirmKb[<code>kb.adjust(1)</code>]
        AdjustConfirmKb --> FinishConfirmKb[<code>kb.as_markup()</code>]
        FinishConfirmKb --> ReturnConfirmKb[Возврат <code>InlineKeyboardMarkup</code>]
    end
```

**Анализ зависимостей `mermaid`:**
-   `aiogram.types.InlineKeyboardMarkup`: Тип данных для представления встроенной клавиатуры Telegram.
-   `aiogram.utils.keyboard.InlineKeyboardBuilder`: Класс для создания встроенных клавиатур.
-   `bot.dao.models.Category`: Модель данных, представляющая категорию товаров (предположительно, определена в другом файле).
    
    **Объяснение зависимостей `mermaid`:**

- `InlineKeyboardBuilder`: Все функции используют этот класс для создания клавиатуры. Класс предоставляет методы для добавления кнопок (`button()`) и настройки их расположения (`adjust()`). Конечный результат работы класса - `InlineKeyboardMarkup`.
- `aiogram.types.InlineKeyboardMarkup`: Этот класс является типом возвращаемого значения всех функций, т.к. в результате работы мы должны получить объект, пригодный для отправки в Telegram.
- `bot.dao.models.Category`: Данные из этой модели используются только в `catalog_admin_kb`.

## <объяснение>

### Импорты
-   `typing.List`: Используется для аннотации типов, указывая, что `catalog_data` является списком.
-   `aiogram.types.InlineKeyboardMarkup`: Класс из библиотеки `aiogram` для создания встроенных клавиатур Telegram.
-   `aiogram.utils.keyboard.InlineKeyboardBuilder`: Класс из библиотеки `aiogram` для удобного создания встроенных клавиатур. Позволяет добавлять кнопки и настраивать их расположение.
-   `bot.dao.models.Category`: Модель данных, представляющая категорию товаров. Этот импорт предполагает, что в проекте есть структура `dao`, в которой определены модели для работы с данными.

### Функции

#### `catalog_admin_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup`
-   **Аргументы**:
    -   `catalog_data`: Список объектов `Category`, представляющих категории товаров.
-   **Возвращает**: `InlineKeyboardMarkup`: Клавиатура с кнопками, каждая из которых представляет категорию.
-   **Назначение**: Создает клавиатуру для администратора с кнопками категорий. Используется, например, для выбора категории при добавлении товара.
-   **Пример**:
    ```python
    categories = [Category(id=1, category_name="Электроника"), Category(id=2, category_name="Одежда")]
    keyboard = catalog_admin_kb(categories)
    # Полученная клавиатура будет иметь две кнопки: "Электроника" и "Одежда", а также кнопку "Отмена".
    ```

#### `admin_send_file_kb() -> InlineKeyboardMarkup`
-   **Аргументы**: Нет.
-   **Возвращает**: `InlineKeyboardMarkup`: Клавиатура с кнопками "Без файла" и "Отмена".
-   **Назначение**: Создает клавиатуру для администратора для выбора, отправлять файл или нет при добавлении товара.
-   **Пример**:
    ```python
    keyboard = admin_send_file_kb()
    # Полученная клавиатура будет иметь две кнопки: "Без файла" и "Отмена".
    ```

#### `admin_kb() -> InlineKeyboardMarkup`
-   **Аргументы**: Нет.
-   **Возвращает**: `InlineKeyboardMarkup`: Клавиатура с кнопками "Статистика", "Управлять товарами" и "На главную".
-   **Назначение**: Создает основную клавиатуру для администратора.
-   **Пример**:
    ```python
    keyboard = admin_kb()
    # Полученная клавиатура будет иметь три кнопки: "📊 Статистика", "🛍️ Управлять товарами", "🏠 На главную".
    ```

#### `admin_kb_back() -> InlineKeyboardMarkup`
-   **Аргументы**: Нет.
-   **Возвращает**: `InlineKeyboardMarkup`: Клавиатура с кнопками "Админ панель" и "На главную".
-   **Назначение**: Создает клавиатуру для возврата к админ-панели или на главную страницу.
-    **Пример**:
    ```python
    keyboard = admin_kb_back()
    # Полученная клавиатура будет иметь две кнопки: "⚙️ Админ панель", "🏠 На главную".
    ```

#### `dell_product_kb(product_id: int) -> InlineKeyboardMarkup`
-   **Аргументы**:
    -   `product_id`: Идентификатор товара, который нужно удалить.
-   **Возвращает**: `InlineKeyboardMarkup`: Клавиатура с кнопками "Удалить", "Админ панель" и "На главную".
-   **Назначение**: Создает клавиатуру для подтверждения удаления товара.
-   **Пример**:
    ```python
    keyboard = dell_product_kb(123)
    # Полученная клавиатура будет иметь три кнопки: "🗑️ Удалить", "⚙️ Админ панель", "🏠 На главную" с callback_data='dell_123'.
    ```

#### `product_management_kb() -> InlineKeyboardMarkup`
-   **Аргументы**: Нет.
-   **Возвращает**: `InlineKeyboardMarkup`: Клавиатура с кнопками "Добавить товар", "Удалить товар", "Админ панель" и "На главную".
-   **Назначение**: Создает клавиатуру для управления товарами.
-   **Пример**:
    ```python
    keyboard = product_management_kb()
    # Полученная клавиатура будет иметь четыре кнопки: "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель", "🏠 На главную".
    ```

#### `cancel_kb_inline() -> InlineKeyboardMarkup`
-   **Аргументы**: Нет.
-   **Возвращает**: `InlineKeyboardMarkup`: Клавиатура с кнопкой "Отмена".
-   **Назначение**: Создает клавиатуру с кнопкой "Отмена" для отмены действия.
-   **Пример**:
    ```python
    keyboard = cancel_kb_inline()
    # Полученная клавиатура будет иметь одну кнопку: "Отмена".
    ```

#### `admin_confirm_kb() -> InlineKeyboardMarkup`
-   **Аргументы**: Нет.
-   **Возвращает**: `InlineKeyboardMarkup`: Клавиатура с кнопками "Все верно" и "Отмена".
-   **Назначение**: Создает клавиатуру для подтверждения действия администратора.
-   **Пример**:
    ```python
    keyboard = admin_confirm_kb()
    # Полученная клавиатура будет иметь две кнопки: "Все верно", "Отмена".
    ```

### Переменные
-   `kb`: Объект `InlineKeyboardBuilder`, используемый для создания клавиатур.
-   `catalog_data`: Список объектов `Category`.
-   `category`: Объект `Category` в цикле `for`.
-   `product_id`: Идентификатор товара (тип `int`).

### Потенциальные ошибки и области для улучшения
-   **Callback data**:
    -   `callback_data` можно стандартизировать, например, использовать JSON-строки для более сложных данных. Это позволит избежать использования f-строк.
-   **Жестко заданные тексты**: Тексты кнопок ("Отмена", "Без файла" и т.д.) могут быть вынесены в константы для упрощения их изменения в будущем или для поддержки нескольких языков.
-   **Логика расположения кнопок**: Логика `adjust` может быть сложнее. Хорошей практикой будет создание отдельного метода для вычисления правильного расположения кнопок.
-   **Обработка callback data:** Данный код занимается только созданием кнопок, однако не обрабатывает приходящие callback data. Это должно быть реализовано в другом месте.

### Взаимосвязи с другими частями проекта
-   Данный файл является частью `telegram bot` и используется для генерации клавиатур.
-   `bot.dao.models.Category` вероятно используется для взаимодействия с базой данных, поэтому связь с БД через `dao` есть.
-   Функции данного файла вероятно вызывают в `handler` для обработки пользовательского взаимодействия.
-   `callback_data` используются в хендлерах для определения действия пользователя.
-   `InlineKeyboardMarkup` используется для отправки клавиатур пользователю в telegram.

В целом, код хорошо структурирован и выполняет свою задачу по созданию клавиатур для админ-панели бота. Улучшения можно внести в стандартизацию `callback_data`, вынесение текстов в константы и логику расположения кнопок.
```