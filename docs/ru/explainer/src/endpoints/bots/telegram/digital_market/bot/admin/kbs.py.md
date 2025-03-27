## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid\
    flowchart TD\
        Start --> Header[<code>header.py</code><br> Determine Project Root]\
    \
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] \
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

**1. `catalog_admin_kb`**:
    - **Вход:** Список объектов `Category` (`catalog_data`).
    - **Шаг 1:** Создание объекта `InlineKeyboardBuilder`.
    - **Шаг 2:** Цикл по каждой категории в `catalog_data`.
        - **Пример:** Если `catalog_data` содержит `Category(id=1, category_name='Электроника')` и `Category(id=2, category_name='Одежда')`, то на каждой итерации цикла создается кнопка с текстом `Электроника` и `Одежда` соответственно, callback_data `add_category_1` и `add_category_2`.
        - **Действие:** Добавляет кнопку с названием категории и `callback_data` в виде `add_category_{category.id}`.
    - **Шаг 3:** Добавляет кнопку "Отмена" с `callback_data` `admin_panel`.
    - **Шаг 4:** Настраивает кнопки в 2 столбца.
    - **Выход:** `InlineKeyboardMarkup` с кнопками категорий и "Отмена".

**2. `admin_send_file_kb`**:
    - **Вход:** Нет.
    - **Шаг 1:** Создание объекта `InlineKeyboardBuilder`.
    - **Шаг 2:** Добавляет кнопку "Без файла" с `callback_data` `without_file`.
    - **Шаг 3:** Добавляет кнопку "Отмена" с `callback_data` `admin_panel`.
    - **Шаг 4:** Настраивает кнопки в 2 столбца.
    - **Выход:** `InlineKeyboardMarkup` с кнопками "Без файла" и "Отмена".

**3. `admin_kb`**:
    - **Вход:** Нет.
    - **Шаг 1:** Создание объекта `InlineKeyboardBuilder`.
    - **Шаг 2:** Добавляет кнопку "📊 Статистика" с `callback_data` `statistic`.
    - **Шаг 3:** Добавляет кнопку "🛍️ Управлять товарами" с `callback_data` `process_products`.
    - **Шаг 4:** Добавляет кнопку "🏠 На главную" с `callback_data` `home`.
    - **Шаг 5:** Настраивает кнопки в 2 столбца.
    - **Выход:** `InlineKeyboardMarkup` с кнопками для админ-панели.

**4. `admin_kb_back`**:
    - **Вход:** Нет.
    - **Шаг 1:** Создание объекта `InlineKeyboardBuilder`.
    - **Шаг 2:** Добавляет кнопку "⚙️ Админ панель" с `callback_data` `admin_panel`.
    - **Шаг 3:** Добавляет кнопку "🏠 На главную" с `callback_data` `home`.
    - **Шаг 4:** Настраивает кнопки в 1 столбец.
    - **Выход:** `InlineKeyboardMarkup` с кнопками возврата.

**5. `dell_product_kb`**:
    - **Вход:** ID продукта (`product_id`).
        - **Пример:** `product_id = 5`.
    - **Шаг 1:** Создание объекта `InlineKeyboardBuilder`.
    - **Шаг 2:** Добавляет кнопку "🗑️ Удалить" с `callback_data` в виде `dell_{product_id}`, т.е. `dell_5`.
    - **Шаг 3:** Добавляет кнопку "⚙️ Админ панель" с `callback_data` `admin_panel`.
    - **Шаг 4:** Добавляет кнопку "🏠 На главную" с `callback_data` `home`.
    - **Шаг 5:** Настраивает кнопки: 2 в первом ряду, 2 во втором и 1 в третьем.
    - **Выход:** `InlineKeyboardMarkup` с кнопками удаления и возврата.

**6. `product_management_kb`**:
    - **Вход:** Нет.
    - **Шаг 1:** Создание объекта `InlineKeyboardBuilder`.
    - **Шаг 2:** Добавляет кнопку "➕ Добавить товар" с `callback_data` `add_product`.
    - **Шаг 3:** Добавляет кнопку "🗑️ Удалить товар" с `callback_data` `delete_product`.
    - **Шаг 4:** Добавляет кнопку "⚙️ Админ панель" с `callback_data` `admin_panel`.
    - **Шаг 5:** Добавляет кнопку "🏠 На главную" с `callback_data` `home`.
    - **Шаг 6:** Настраивает кнопки: 2 в первом ряду, 2 во втором и 1 в третьем.
    - **Выход:** `InlineKeyboardMarkup` с кнопками управления товарами.

**7. `cancel_kb_inline`**:
    - **Вход:** Нет.
    - **Шаг 1:** Создание объекта `InlineKeyboardBuilder`.
    - **Шаг 2:** Добавляет кнопку "Отмена" с `callback_data` `cancel`.
    - **Выход:** `InlineKeyboardMarkup` с кнопкой отмены.

**8. `admin_confirm_kb`**:
     - **Вход:** Нет.
     - **Шаг 1:** Создание объекта `InlineKeyboardBuilder`.
     - **Шаг 2:** Добавляет кнопку "Все верно" с `callback_data` `confirm_add`.
     - **Шаг 3:** Добавляет кнопку "Отмена" с `callback_data` `admin_panel`.
    -  **Шаг 4:** Настраивает кнопки в 1 столбец.
     - **Выход:** `InlineKeyboardMarkup` с кнопками подтверждения и отмены.

## <mermaid>

```mermaid
flowchart TD
    subgraph InlineKeyboardBuilder Operations
        CreateKeyboardBuilder[Создание InlineKeyboardBuilder]
        AddButton[Добавление кнопок с текстом и callback_data]
        AdjustLayout[Настройка расположения кнопок (столбцы, ряды)]
        GenerateMarkup[Генерация InlineKeyboardMarkup]
    end
    
    subgraph catalog_admin_kb
        StartCatalogAdmin[Начало catalog_admin_kb]
        InputCatalogData[Вход: catalog_data: List[Category]]
        LoopCategories[Цикл по категориям]
        AddCategoryButton[Добавить кнопку категории с callback_data "add_category_{category.id}"]
        AddCancelButtonCatalog[Добавить кнопку "Отмена" с callback_data "admin_panel"]
        ReturnCatalogKeyboard[Возврат: InlineKeyboardMarkup]
        StartCatalogAdmin --> InputCatalogData
        InputCatalogData --> CreateKeyboardBuilder
        CreateKeyboardBuilder --> LoopCategories
        LoopCategories --> AddCategoryButton
         AddCategoryButton --> LoopCategories
        LoopCategories -- конец цикла --> AddCancelButtonCatalog
        AddCancelButtonCatalog --> AdjustLayout
        AdjustLayout --> GenerateMarkup
        GenerateMarkup --> ReturnCatalogKeyboard
    end
     subgraph admin_send_file_kb
        StartSendFileAdmin[Начало admin_send_file_kb]
         CreateKeyboardBuilderSendFile[Создание InlineKeyboardBuilder]
        AddWithoutFileButton[Добавить кнопку "Без файла" с callback_data "without_file"]
        AddCancelButtonSendFile[Добавить кнопку "Отмена" с callback_data "admin_panel"]
        ReturnSendFileKeyboard[Возврат: InlineKeyboardMarkup]
         StartSendFileAdmin -->  CreateKeyboardBuilderSendFile
          CreateKeyboardBuilderSendFile-->  AddWithoutFileButton
         AddWithoutFileButton -->  AddCancelButtonSendFile
          AddCancelButtonSendFile --> AdjustLayout
        AdjustLayout --> GenerateMarkup
        GenerateMarkup --> ReturnSendFileKeyboard
    end
    
    subgraph admin_kb
        StartAdminKb[Начало admin_kb]
        CreateKeyboardBuilderAdmin[Создание InlineKeyboardBuilder]
        AddStatisticButton[Добавить кнопку "📊 Статистика" с callback_data "statistic"]
        AddProcessProductsButton[Добавить кнопку "🛍️ Управлять товарами" с callback_data "process_products"]
        AddHomeButtonAdmin[Добавить кнопку "🏠 На главную" с callback_data "home"]
        ReturnAdminKeyboard[Возврат: InlineKeyboardMarkup]
        StartAdminKb --> CreateKeyboardBuilderAdmin
         CreateKeyboardBuilderAdmin-->  AddStatisticButton
        AddStatisticButton --> AddProcessProductsButton
         AddProcessProductsButton-->  AddHomeButtonAdmin
        AddHomeButtonAdmin --> AdjustLayout
         AdjustLayout --> GenerateMarkup
         GenerateMarkup --> ReturnAdminKeyboard
    end

    subgraph admin_kb_back
        StartAdminKbBack[Начало admin_kb_back]
         CreateKeyboardBuilderAdminBack[Создание InlineKeyboardBuilder]
        AddAdminPanelButton[Добавить кнопку "⚙️ Админ панель" с callback_data "admin_panel"]
        AddHomeButtonAdminBack[Добавить кнопку "🏠 На главную" с callback_data "home"]
        ReturnAdminBackKeyboard[Возврат: InlineKeyboardMarkup]
        StartAdminKbBack -->  CreateKeyboardBuilderAdminBack
           CreateKeyboardBuilderAdminBack--> AddAdminPanelButton
        AddAdminPanelButton --> AddHomeButtonAdminBack
        AddHomeButtonAdminBack -->AdjustLayout
        AdjustLayout --> GenerateMarkup
        GenerateMarkup --> ReturnAdminBackKeyboard
    end

    subgraph dell_product_kb
        StartDellProductKb[Начало dell_product_kb]
        InputProductId[Вход: product_id: int]
         CreateKeyboardBuilderDell[Создание InlineKeyboardBuilder]
        AddDellButton[Добавить кнопку "🗑️ Удалить" с callback_data "dell_{product_id}"]
        AddAdminPanelButtonDell[Добавить кнопку "⚙️ Админ панель" с callback_data "admin_panel"]
        AddHomeButtonDell[Добавить кнопку "🏠 На главную" с callback_data "home"]
        ReturnDellProductKeyboard[Возврат: InlineKeyboardMarkup]
        StartDellProductKb --> InputProductId
         InputProductId -->  CreateKeyboardBuilderDell
         CreateKeyboardBuilderDell-->  AddDellButton
        AddDellButton --> AddAdminPanelButtonDell
        AddAdminPanelButtonDell --> AddHomeButtonDell
         AddHomeButtonDell --> AdjustLayout
         AdjustLayout --> GenerateMarkup
         GenerateMarkup --> ReturnDellProductKeyboard
    end

   subgraph product_management_kb
        StartProductManagementKb[Начало product_management_kb]
        CreateKeyboardBuilderProductManagement[Создание InlineKeyboardBuilder]
        AddAddProductButton[Добавить кнопку "➕ Добавить товар" с callback_data "add_product"]
        AddDeleteProductButton[Добавить кнопку "🗑️ Удалить товар" с callback_data "delete_product"]
        AddAdminPanelButtonProductManagement[Добавить кнопку "⚙️ Админ панель" с callback_data "admin_panel"]
        AddHomeButtonProductManagement[Добавить кнопку "🏠 На главную" с callback_data "home"]
        ReturnProductManagementKeyboard[Возврат: InlineKeyboardMarkup]
        StartProductManagementKb -->  CreateKeyboardBuilderProductManagement
         CreateKeyboardBuilderProductManagement--> AddAddProductButton
        AddAddProductButton --> AddDeleteProductButton
         AddDeleteProductButton --> AddAdminPanelButtonProductManagement
        AddAdminPanelButtonProductManagement --> AddHomeButtonProductManagement
          AddHomeButtonProductManagement --> AdjustLayout
         AdjustLayout --> GenerateMarkup
        GenerateMarkup --> ReturnProductManagementKeyboard
    end
    
  subgraph cancel_kb_inline
        StartCancelKbInline[Начало cancel_kb_inline]
          CreateKeyboardBuilderCancel[Создание InlineKeyboardBuilder]
        AddCancelButtonCancel[Добавить кнопку "Отмена" с callback_data "cancel"]
        ReturnCancelKeyboard[Возврат: InlineKeyboardMarkup]
        StartCancelKbInline --> CreateKeyboardBuilderCancel
         CreateKeyboardBuilderCancel--> AddCancelButtonCancel
           AddCancelButtonCancel --> GenerateMarkup
        GenerateMarkup --> ReturnCancelKeyboard
    end
    
     subgraph admin_confirm_kb
        StartAdminConfirmKb[Начало admin_confirm_kb]
         CreateKeyboardBuilderAdminConfirm[Создание InlineKeyboardBuilder]
        AddConfirmButton[Добавить кнопку "Все верно" с callback_data "confirm_add"]
        AddCancelButtonConfirm[Добавить кнопку "Отмена" с callback_data "admin_panel"]
        ReturnConfirmKeyboard[Возврат: InlineKeyboardMarkup]
        StartAdminConfirmKb -->  CreateKeyboardBuilderAdminConfirm
         CreateKeyboardBuilderAdminConfirm-->   AddConfirmButton
        AddConfirmButton --> AddCancelButtonConfirm
         AddCancelButtonConfirm -->AdjustLayout
        AdjustLayout --> GenerateMarkup
       GenerateMarkup --> ReturnConfirmKeyboard
    end
```

## <объяснение>

**Импорты:**

-   `from typing import List`: Импортирует `List` для аннотации типов, указывая, что переменная является списком.
-   `from aiogram.types import InlineKeyboardMarkup`: Импортирует `InlineKeyboardMarkup` из библиотеки aiogram, который используется для создания клавиатур.
-   `from aiogram.utils.keyboard import InlineKeyboardBuilder`: Импортирует `InlineKeyboardBuilder`, который используется для построения `InlineKeyboardMarkup` клавиатур.
-   `from bot.dao.models import Category`: Импортирует модель `Category` из модуля `bot.dao.models`, предположительно используемую для представления данных о категориях товаров.

**Функции:**

1.  **`catalog_admin_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup`**
    -   **Аргументы:**
        -   `catalog_data`: Список объектов `Category`, представляющих категории товаров.
    -   **Назначение:** Создает клавиатуру с кнопками для каждой категории, позволяя администратору выбирать категорию. Используется для добавления товара в определенную категорию.
    -   **Возвращаемое значение:** Объект `InlineKeyboardMarkup`.
    -   **Пример использования:**
        ```python
        categories = [Category(id=1, category_name="Электроника"), Category(id=2, category_name="Одежда")]
        keyboard = catalog_admin_kb(categories)
        # keyboard будет содержать кнопки "Электроника" и "Одежда", при нажатии на которые сработают callback'и add_category_1 и add_category_2
        ```

2.  **`admin_send_file_kb() -> InlineKeyboardMarkup`**
    -   **Аргументы:** Нет.
    -   **Назначение:** Создает клавиатуру с кнопками "Без файла" и "Отмена", позволяя администратору выбирать, отправлять ли файл.
    -   **Возвращаемое значение:** Объект `InlineKeyboardMarkup`.
    -   **Пример использования:**
        ```python
        keyboard = admin_send_file_kb()
        # keyboard будет содержать кнопки "Без файла" и "Отмена"
        ```

3.  **`admin_kb() -> InlineKeyboardMarkup`**
    -   **Аргументы:** Нет.
    -   **Назначение:** Создает основную клавиатуру для админ-панели с кнопками для статистики, управления товарами и перехода на главную.
    -   **Возвращаемое значение:** Объект `InlineKeyboardMarkup`.
    -   **Пример использования:**
        ```python
        keyboard = admin_kb()
        # keyboard будет содержать кнопки "📊 Статистика", "🛍️ Управлять товарами", "🏠 На главную"
        ```

4.  **`admin_kb_back() -> InlineKeyboardMarkup`**
    -   **Аргументы:** Нет.
    -   **Назначение:** Создает клавиатуру для возврата к админ-панели и на главную страницу.
    -   **Возвращаемое значение:** Объект `InlineKeyboardMarkup`.
    -   **Пример использования:**
        ```python
        keyboard = admin_kb_back()
        # keyboard будет содержать кнопки "⚙️ Админ панель" и "🏠 На главную"
        ```

5.  **`dell_product_kb(product_id: int) -> InlineKeyboardMarkup`**
    -   **Аргументы:**
        -   `product_id`: ID товара, который нужно удалить.
    -   **Назначение:** Создает клавиатуру с кнопкой удаления товара, а также возврата к админ панели и на главную.
    -   **Возвращаемое значение:** Объект `InlineKeyboardMarkup`.
    -   **Пример использования:**
        ```python
        keyboard = dell_product_kb(5)
        # keyboard будет содержать кнопки "🗑️ Удалить" c callback_data "dell_5", "⚙️ Админ панель" и "🏠 На главную"
        ```

6.  **`product_management_kb() -> InlineKeyboardMarkup`**
    -   **Аргументы:** Нет.
    -   **Назначение:** Создает клавиатуру для управления товарами: добавление, удаление, а также возврата к админ панели и на главную.
    -   **Возвращаемое значение:** Объект `InlineKeyboardMarkup`.
    -   **Пример использования:**
        ```python
        keyboard = product_management_kb()
        # keyboard будет содержать кнопки "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную"
        ```

7.  **`cancel_kb_inline() -> InlineKeyboardMarkup`**
    -   **Аргументы:** Нет.
    -   **Назначение:** Создает клавиатуру с кнопкой "Отмена".
    -   **Возвращаемое значение:** Объект `InlineKeyboardMarkup`.
    -   **Пример использования:**
        ```python
        keyboard = cancel_kb_inline()
        # keyboard будет содержать кнопку "Отмена"
        ```

8.   **`admin_confirm_kb() -> InlineKeyboardMarkup`**
    -  **Аргументы:** Нет.
    -  **Назначение:** Создает клавиатуру с кнопками "Все верно" и "Отмена", для подтверждения действий.
    -   **Возвращаемое значение:** Объект `InlineKeyboardMarkup`.
    -   **Пример использования:**
        ```python
        keyboard = admin_confirm_kb()
        # keyboard будет содержать кнопки "Все верно" и "Отмена"
        ```

**Переменные:**

-   `kb`: Объект `InlineKeyboardBuilder`, используется для построения клавиатуры.
-   `category`: Экземпляр модели `Category` при итерации по списку категорий.
-   `product_id`: ID товара, передаваемый в функцию `dell_product_kb`.

**Объяснение:**

-   Код предоставляет набор функций для создания inline-клавиатур, используемых в боте. Каждая функция создает клавиатуру для определенной задачи, будь то выбор категории, подтверждение действия, или навигация по меню.
-   `InlineKeyboardBuilder` используется для создания клавиатур, а `adjust` для настройки количества кнопок в каждом ряду.
-   Callback-данные (`callback_data`) используются для идентификации нажатой пользователем кнопки и обработки этого нажатия ботом.
-   Логика работы бота: пользователь взаимодействует с кнопками, и в зависимости от `callback_data` бот вызывает соответствующие обработчики.

**Потенциальные ошибки и области для улучшения:**

-   В коде используется повторение шаблонного кода для создания клавиатуры, можно было бы создать абстрактную функцию для создания клавиатуры с заданным набором кнопок и их `callback_data`.
-   Можно добавить обработку ошибок, например, проверку на существование категорий перед генерацией клавиатуры.

**Взаимосвязь с другими частями проекта:**

-   Эти функции, вероятно, вызываются из обработчиков сообщений (хендлеров) в коде бота. Когда пользователь отправляет команду или нажимает кнопку, вызываются функции из этого файла для генерации клавиатуры, которая будет отправлена пользователю.
-   `bot.dao.models.Category` используется для доступа к данным о категориях, что указывает на взаимодействие с базой данных через слой DAO (Data Access Object).