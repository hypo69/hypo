## <алгоритм>

1.  **`post_title(d, category)`**:
    *   Принимает объект `Driver` (d) и объект `SimpleNamespace` (category), содержащий заголовок и описание.
    *   Прокручивает страницу назад (скролл) с помощью `d.scroll()`. Если не удаётся прокрутить, возвращает `None`.
    *   Открывает окно добавления поста с помощью `d.execute_locator(locator.open_add_post_box)`. Если не удаётся, возвращает `None`.
    *   Формирует строку сообщения, объединяя заголовок и описание из `category`.
    *   Вставляет сформированное сообщение в текстовое поле с помощью `d.execute_locator(locator.add_message, message)`. Если не удаётся, возвращает `None`.
    *   Возвращает `True`, если все шаги выполнены успешно.
    *   *Пример*: `post_title(driver, SimpleNamespace(title="Заголовок", description="Описание"))`

2.  **`upload_media(d, products, no_video=False)`**:
    *   Принимает объект `Driver` (d), список объектов `SimpleNamespace` (products), содержащих пути к медиафайлам, и опциональный флаг `no_video`.
    *   Открывает форму добавления медиа с помощью `d.execute_locator(locator.open_add_foto_video_form)`. Если не удаётся, возвращает `None`.
    *   Проверяет, что `products` является списком, если нет, преобразует в список.
    *   Итерируется по списку продуктов. Для каждого продукта:
        *   Определяет путь к медиафайлу (`media_path`), выбирая видео, если `no_video` не установлен, иначе выбирает изображение.
        *   Загружает медиафайл с помощью `d.execute_locator(locator.foto_video_input, media_path)`. Если не удаётся, возвращает `None`.
    *   Нажимает кнопку редактирования загруженного медиа с помощью `d.execute_locator(locator.edit_uloaded_media_button)`. Если не удаётся, возвращает `None`.
    *   Находит фрейм загруженного медиа с помощью `d.execute_locator(locator.uploaded_media_frame)`.
    *   Находит все текстовые поля для подписей с помощью `d.execute_locator(locator.edit_image_properties_textarea)`. Если не удаётся, возвращает `None`.
    *   Вызывает `update_images_captions(d, products, textarea_list)` для добавления описаний к медиафайлам.
    *   Возвращает `True` после успешной загрузки и обновления.
    *   *Пример*: `upload_media(driver, [SimpleNamespace(local_image_path="path/image1.jpg"), SimpleNamespace(local_video_path="path/video1.mp4")], no_video=False)`

3.  **`update_images_captions(d, products, textarea_list)`**:
    *   Принимает объект `Driver` (d), список объектов `SimpleNamespace` (products), и список элементов `WebElement` (textarea_list) для добавления подписей.
    *   Загружает локальные настройки из `translations.json` с помощью `j_loads_ns`.
    *   Определяет функцию `handle_product(product, textarea_list, i)` для добавления подписи к одному продукту:
        *   Определяет направление текста (LTR или RTL) на основе языка продукта.
        *   Формирует сообщение, конкатенируя данные о продукте (название, цены, скидки и т.д.) из `product`, используя локальные настройки из `translations.json` в зависимости от направления текста.
        *   Отправляет сообщение в соответствующее поле `textarea_list[i]` с помощью `send_keys`.
    *   Итерируется по `products`, вызывая `handle_product` асинхронно для каждого продукта с помощью `asyncio.to_thread`.
    *   *Пример*: `update_images_captions(driver, [SimpleNamespace(product_title='title', original_price='100', language='ru')], [WebElement, WebElement])`

4.  **`promote_post(d, category, products, no_video=False)`**:
    *   Принимает объект `Driver` (d), объект `SimpleNamespace` (category), список объектов `SimpleNamespace` (products) и опциональный флаг `no_video`.
    *   Вызывает `post_title(d, category)` для добавления заголовка и описания. Если `post_title` возвращает `None`, завершает работу.
    *   Вызывает `upload_media(d, products, no_video)` для загрузки медиафайлов и добавления описаний. Если `upload_media` возвращает `None`, завершает работу.
    *   Нажимает кнопку "Завершить редактирование" с помощью `d.execute_locator(locator.finish_editing_button)`. Если не удаётся, завершает работу.
    *   Нажимает кнопку "Опубликовать" с помощью `d.execute_locator(locator.publish)`. Если не удаётся, завершает работу.
    *   Возвращает `True`, если все шаги выполнены успешно.
    *   *Пример*: `promote_post(driver, SimpleNamespace(title="Заголовок", description="Описание"), [SimpleNamespace(local_image_path="path/image1.jpg")])`

## <mermaid>

```mermaid
flowchart TD
    Start[Start] --> PostTitleCall[Call post_title]
    PostTitleCall --> PostTitleCheck{post_title successful?}
    PostTitleCheck -- Yes --> UploadMediaCall[Call upload_media]
    PostTitleCheck -- No --> End[End]
    UploadMediaCall --> UploadMediaCheck{upload_media successful?}
    UploadMediaCheck -- Yes --> FinishEditingCall[Call execute_locator(finish_editing_button)]
    UploadMediaCheck -- No --> End
    FinishEditingCall --> FinishEditingCheck{finish_editing_button successful?}
    FinishEditingCheck -- Yes --> PublishCall[Call execute_locator(publish)]
    FinishEditingCheck -- No --> End
    PublishCall --> PublishCheck{publish successful?}
    PublishCheck -- Yes --> End[End]
    PublishCheck -- No --> End
    
    
    subgraph post_title
    PostTitleStart[Start post_title] --> Scroll[d.scroll(backward)]
    Scroll --> ScrollCheck{Scroll successful?}
    ScrollCheck -- Yes --> OpenPostBox[d.execute_locator(locator.open_add_post_box)]
    ScrollCheck -- No --> PostTitleEnd[End post_title]
    OpenPostBox --> OpenPostBoxCheck{Open post box successful?}
    OpenPostBoxCheck -- Yes --> ConstructMessage[Construct message]
    OpenPostBoxCheck -- No --> PostTitleEnd
    ConstructMessage --> AddMessage[d.execute_locator(locator.add_message, message)]
    AddMessage --> AddMessageCheck{Add message successful?}
    AddMessageCheck -- Yes --> PostTitleEnd[End post_title return True]
    AddMessageCheck -- No --> PostTitleEnd[End post_title]

    end

    subgraph upload_media
    UploadMediaStart[Start upload_media] --> OpenMediaForm[d.execute_locator(locator.open_add_foto_video_form)]
    OpenMediaForm --> OpenMediaFormCheck{Open media form successful?}
    OpenMediaFormCheck -- Yes --> IterateProducts[Iterate over products]
    OpenMediaFormCheck -- No --> UploadMediaEnd[End upload_media]
    IterateProducts --> GetMediaPath[Get media path]
    GetMediaPath --> UploadMediaFile[d.execute_locator(locator.foto_video_input, media_path)]
    UploadMediaFile --> UploadMediaFileCheck{Upload media successful?}
    UploadMediaFileCheck -- Yes --> CheckNextProduct{Next product?}
    UploadMediaFileCheck -- No --> UploadMediaEnd[End upload_media]
    CheckNextProduct -- Yes --> IterateProducts
    CheckNextProduct -- No --> EditMediaButton[d.execute_locator(locator.edit_uloaded_media_button)]
    EditMediaButton --> EditMediaButtonCheck{Edit media button successful?}
    EditMediaButtonCheck -- Yes --> FindMediaFrame[d.execute_locator(locator.uploaded_media_frame)]
    EditMediaButtonCheck -- No --> UploadMediaEnd
    FindMediaFrame --> FindTextareas[d.execute_locator(locator.edit_image_properties_textarea)]
    FindTextareas --> FindTextareasCheck{Find textareas successful?}
    FindTextareasCheck -- Yes --> UpdateCaptions[Call update_images_captions]
     FindTextareasCheck -- No --> UploadMediaEnd
    UpdateCaptions --> UploadMediaEnd[End upload_media return True]
    end


    subgraph update_images_captions
    UpdateCaptionsStart[Start update_images_captions] --> LoadTranslations[j_loads_ns(translations.json)]
    LoadTranslations --> IterateTextareas[Iterate over products and textareas]
    IterateTextareas --> CallHandleProduct[Call handle_product in async thread]
    CallHandleProduct --> CheckNextTextArea{Next product?}
    CheckNextTextArea -- Yes --> IterateTextareas
    CheckNextTextArea -- No --> UpdateCaptionsEnd[End update_images_captions]
    
    
        subgraph handle_product
            HandleProductStart[Start handle_product] --> DetermineTextDirection[Determine text direction (LTR/RTL)]
            DetermineTextDirection --> GenerateMessage[Generate message based on direction]
            GenerateMessage --> SendKeysToTextarea[textarea.send_keys(message)]
            SendKeysToTextarea --> HandleProductEnd[End handle_product]
        end
    
    end

```

### `mermaid` объяснение

1.  **flowchart TD**: Объявляет начало блок-схемы с направлением слева направо.

2.  **Start**: Начало общего процесса.

3.  **PostTitleCall**: Вызов функции `post_title`.

4.  **PostTitleCheck**: Проверка, успешно ли выполнилась функция `post_title`.

5.  **UploadMediaCall**: Вызов функции `upload_media`.

6.  **UploadMediaCheck**: Проверка, успешно ли выполнилась функция `upload_media`.

7.  **FinishEditingCall**: Вызов `d.execute_locator(locator.finish_editing_button)`.

8.  **FinishEditingCheck**: Проверка, успешно ли выполнился `finish_editing_button`.

9.  **PublishCall**: Вызов `d.execute_locator(locator.publish)`.

10. **PublishCheck**: Проверка, успешно ли выполнился `publish`.

11. **End**: Конец общего процесса.

12. **subgraph post_title**:  Начало подграфа для функции `post_title`.
13.  **PostTitleStart**: Начало выполнения функции `post_title`.
14.  **Scroll**: Вызов метода `d.scroll` для прокрутки страницы.
15.  **ScrollCheck**: Проверка, успешно ли выполнился скролл.
16. **OpenPostBox**: Вызов `d.execute_locator` для открытия окна поста.
17. **OpenPostBoxCheck**: Проверка, успешно ли открылось окно поста.
18. **ConstructMessage**: Создание строки сообщения.
19. **AddMessage**: Вызов `d.execute_locator` для добавления сообщения.
20. **AddMessageCheck**: Проверка, успешно ли добавилось сообщение.
21. **PostTitleEnd**: Конец выполнения функции `post_title`.

22. **subgraph upload_media**: Начало подграфа для функции `upload_media`.
23. **UploadMediaStart**: Начало выполнения функции `upload_media`.
24. **OpenMediaForm**: Вызов `d.execute_locator` для открытия формы медиа.
25. **OpenMediaFormCheck**: Проверка, успешно ли открылась форма медиа.
26. **IterateProducts**: Начало итерации по продуктам.
27. **GetMediaPath**: Получение пути к медиафайлу.
28. **UploadMediaFile**: Вызов `d.execute_locator` для загрузки медиафайла.
29. **UploadMediaFileCheck**: Проверка, успешна ли загрузка медиафайла.
30. **CheckNextProduct**: Проверка, есть ли еще продукты для обработки.
31. **EditMediaButton**: Вызов `d.execute_locator` для редактирования медиа.
32. **EditMediaButtonCheck**: Проверка, успешно ли открыто редактирование медиа.
33. **FindMediaFrame**: Вызов `d.execute_locator` для поиска фрейма медиа.
34. **FindTextareas**: Вызов `d.execute_locator` для поиска текстовых полей.
35. **FindTextareasCheck**: Проверка, найдены ли текстовые поля.
36. **UpdateCaptions**: Вызов функции `update_images_captions`.
37. **UploadMediaEnd**: Конец выполнения функции `upload_media`.
    
38. **subgraph update_images_captions**: Начало подграфа для функции `update_images_captions`.
39. **UpdateCaptionsStart**: Начало выполнения функции `update_images_captions`.
40. **LoadTranslations**: Загрузка данных из `translations.json`.
41. **IterateTextareas**: Начало итерации по текстовым полям.
42. **CallHandleProduct**: Вызов `handle_product` в асинхронном потоке.
43. **CheckNextTextArea**: Проверка, есть ли еще текстовые поля для обработки.
44. **UpdateCaptionsEnd**: Конец выполнения функции `update_images_captions`.

45. **subgraph handle_product**: Начало подграфа для функции `handle_product`.
46. **HandleProductStart**: Начало выполнения функции `handle_product`.
47. **DetermineTextDirection**: Определение направления текста.
48. **GenerateMessage**: Генерация сообщения.
49. **SendKeysToTextarea**: Отправка текста в текстовое поле.
50. **HandleProductEnd**: Конец выполнения функции `handle_product`.

## <объяснение>

### Импорты:

*   **`time`**: Используется для временных задержек `time.sleep()` в коде, но не используется в предоставленном коде.
*   **`asyncio`**: Используется для асинхронного программирования, в частности для выполнения функций в отдельных потоках `asyncio.to_thread()`.
*   **`pathlib.Path`**: Используется для работы с путями к файлам и директориям.
*   **`types.SimpleNamespace`**: Используется для создания простых объектов с атрибутами, что упрощает работу с данными, передаваемыми между функциями.
*   **`typing.Dict, List`**: Используется для аннотации типов, что делает код более читаемым и понятным.
*   **`selenium.webdriver.remote.webelement.WebElement`**: Используется для представления веб-элементов на странице.
*   **`src.gs`**: Импортирует глобальные настройки из пакета `src`. Используется для доступа к глобальным путям и другим параметрам проекта.
*   **`src.webdriver.driver.Driver`**: Импортирует класс `Driver` из пакета `src.webdriver`, который используется для взаимодействия с веб-браузером.
*   **`src.utils.jjson.j_loads_ns, pprint`**: Импортирует функции `j_loads_ns` для загрузки JSON-данных в объекты `SimpleNamespace` и `pprint` для красивого вывода данных.
*   **`src.logger.logger.logger`**: Импортирует объект `logger` для логирования ошибок и других событий.

Взаимосвязь с другими пакетами `src`:
    *   `src.gs`: Глобальные настройки проекта.
    *   `src.webdriver`:  Управление браузером.
    *   `src.utils`: Утилиты для работы с JSON.
    *   `src.logger`: Логирование событий.

### Классы:

*   **`Driver`**: Класс, предоставляющий интерфейс для взаимодействия с веб-браузером, определён в `src.webdriver.driver`. Имеет методы `execute_locator`, `scroll` и `wait`, которые используются для управления браузером и элементами на веб-странице.
*   **`SimpleNamespace`**: Используется для хранения данных, передаваемых между функциями (например, `category` и `products`). Позволяет создавать простые объекты с динамическими атрибутами.

### Функции:

*   **`post_title(d: Driver, category: SimpleNamespace) -> bool`**:
    *   **Аргументы**:
        *   `d`: Объект `Driver` для взаимодействия с браузером.
        *   `category`: Объект `SimpleNamespace` с атрибутами `title` и `description`.
    *   **Возвращаемое значение**: `bool` или `None`.
    *   **Назначение**: Отправляет заголовок и описание кампании в поле сообщения. Использует методы `scroll` и `execute_locator` класса `Driver`.
    *   **Пример**: `post_title(driver, SimpleNamespace(title="Заголовок", description="Описание"))`
*   **`upload_media(d: Driver, products: List[SimpleNamespace], no_video: bool = False) -> bool`**:
    *   **Аргументы**:
        *   `d`: Объект `Driver` для взаимодействия с браузером.
        *   `products`: Список объектов `SimpleNamespace`, содержащих пути к медиафайлам (`local_image_path` или `local_video_path`).
        *   `no_video`: Опциональный флаг, указывающий, нужно ли использовать видео, по умолчанию `False`.
    *   **Возвращаемое значение**: `bool` или `None`.
    *   **Назначение**: Загружает медиафайлы (изображения или видео) и открывает форму редактирования загруженных файлов. Вызывает функцию `update_images_captions`.
    *   **Пример**: `await upload_media(driver, [SimpleNamespace(local_image_path="path/image1.jpg"), SimpleNamespace(local_video_path="path/video1.mp4")], no_video=False)`
*   **`update_images_captions(d: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None`**:
    *   **Аргументы**:
        *   `d`: Объект `Driver` для взаимодействия с браузером.
        *   `products`: Список объектов `SimpleNamespace` с данными о продуктах.
        *   `textarea_list`: Список элементов `WebElement` - полей для ввода подписей.
    *   **Возвращаемое значение**: `None`.
    *   **Назначение**: Добавляет описания к загруженным медиафайлам, асинхронно вызывая функцию `handle_product` для каждого продукта.
    *   **Пример**: `await update_images_captions(driver, [SimpleNamespace(product_title='title', original_price='100', language='ru')], [WebElement, WebElement])`
    *   Внутри себя использует локальную функцию `handle_product`:
        *   **Аргументы**:
            *   `product`: Объект `SimpleNamespace` с данными о продукте.
            *   `textarea_list`: Список элементов `WebElement` - полей для ввода подписей.
            *   `i`: Индекс продукта в списке.
        *   **Возвращаемое значение**: `None`.
        *   **Назначение**: Создает сообщение на основе данных о продукте и отправляет его в соответствующее поле `textarea_list`.
*   **`promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool`**:
    *   **Аргументы**:
        *   `d`: Объект `Driver` для взаимодействия с браузером.
        *   `category`: Объект `SimpleNamespace` с данными о категории.
        *   `products`: Список объектов `SimpleNamespace` с данными о продуктах.
        *   `no_video`: Опциональный флаг, указывающий, нужно ли использовать видео, по умолчанию `False`.
    *   **Возвращаемое значение**: `bool` или `None`.
    *   **Назначение**: Выполняет процесс продвижения поста, последовательно вызывая функции `post_title`, `upload_media` и выполняя клики по кнопкам `finish_editing_button` и `publish`.
    *   **Пример**: `await promote_post(driver, SimpleNamespace(title="Заголовок", description="Описание"), [SimpleNamespace(local_image_path="path/image1.jpg")])`

### Переменные:

*   **`locator`**: Объект `SimpleNamespace`, содержащий локаторы элементов на веб-странице. Загружается из файла `post_message.json`.
*    `local_units`: Объект `SimpleNamespace`, содержащий локализованные строки для формирования сообщений, загружаются из файла `translations.json`

### Потенциальные ошибки и области для улучшения:

1.  **Обработка ошибок**: В некоторых местах (например, в `post_title`, `upload_media` и `promote_post`) функции могут возвращать `None`, если какой-либо шаг не удался, но это не всегда обрабатывается. В `upload_media` есть `try-except` для обработки исключений загрузки файла, но он может быть расширен для других возможных исключений.
2.  **Логирование**:  Логирование осуществляется с помощью `logger.error`, но можно добавить логирование и других событий (например, `logger.info` для успешных шагов), чтобы улучшить отслеживание работы программы.
3.  **Асинхронность**: Функция `update_images_captions` асинхронно вызывает `handle_product`, однако можно рассмотреть асинхронное выполнение других блокирующих операций, например  `d.execute_locator`.
4.  **Улучшение читаемости**: Функция `update_images_captions` достаточно сложная и ее можно разбить на более мелкие функции для улучшения читаемости и возможности повторного использования.

### Взаимосвязи с другими частями проекта:

*   **Локаторы**: Локаторы загружаются из JSON-файла, что позволяет отделить логику кода от специфичных элементов веб-страницы.
*   **Драйвер**: Используется класс `Driver` из `src.webdriver.driver` для управления браузером. Это позволяет использовать этот код с разными браузерами, если класс `Driver` это поддерживает.
*   **Логирование**: Используется для логирования ошибок и других событий, что помогает отслеживать работу и выявлять проблемы.
*   **Глобальные настройки**: Используются глобальные настройки из `src.gs`, что позволяет настраивать пути к файлам, директориям и другие параметры проекта из единого места.
*   **Локализация**: Подписи к изображениям формируются на основе локализованных строк из `translations.json`, что позволяет поддерживать разные языки.