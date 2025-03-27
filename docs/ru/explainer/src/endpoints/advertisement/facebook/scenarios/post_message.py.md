## Анализ кода `post_message.py`

### 1. <алгоритм>

**Блок-схема:**

1.  **`post_message(d, message, no_video, images, without_captions)`:**
    *   Принимает объект `Driver` (d), сообщение `SimpleNamespace` (message), флаг `no_video`, изображения (`images`), и флаг `without_captions`
    *   Вызывает `post_title(d, message)` для отправки заголовка и описания. Если `post_title` возвращает `False`, завершает работу.
        *   Пример: `message = SimpleNamespace(title="Заголовок", description="Описание")`
    *   Вызывает `upload_media(d, message.products, no_video, without_captions)` для загрузки медиафайлов. Если `upload_media` возвращает `False`, завершает работу.
        *   Пример: `message.products = [SimpleNamespace(local_image_path='path/image.jpg')]`
    *   Если находит локатор `send`, то возвращает `True` (выход для одного изображения).
    *   Вызывает `d.execute_locator(locator.finish_editing_button)`. Если не находит локатор возвращает `False`.
    *   Вызывает `publish(d)`. Если `publish` возвращает `False`, завершает работу.
    *   Возвращает `True`.

2.  **`post_title(d, message)`:**
    *   Принимает объект `Driver` (d) и сообщение (`SimpleNamespace` или `str`).
    *   Выполняет скролл страницы. Если скролл неудачный, возвращает `False`.
        *   Пример: `d.scroll(1, 1200, 'backward')`
    *   Открывает окно добавления поста. Если не открывается, возвращает `False`.
        *   Пример: `d.execute_locator(locator = locator.open_add_post_box)`
    *   Формирует текст сообщения из `message.title` и `message.description` (или использует `message`, если оно не `SimpleNamespace`).
         *   Пример: `message = SimpleNamespace(title="Заголовок", description="Описание")`
        *   Пример `message = "Просто сообщение"`
    *   Вставляет сообщение в поле для ввода текста. Если не удается, возвращает `False`.
        *   Пример: `d.execute_locator(locator.add_message, message=m, timeout=5, timeout_for_event='element_to_be_clickable')`
    *   Возвращает `True`.

3.  **`upload_media(d, media, no_video, without_captions)`:**
    *   Принимает объект `Driver` (d), медиафайлы (`SimpleNamespace`, `List[SimpleNamespace]`, `str`, `list[str]`), флаг `no_video` и флаг `without_captions`.
    *   Если `media` пустой, то возвращает `False`.
    *   Открывает форму добавления медиа. Если не удается, возвращает `False`.
        *   Пример: `d.execute_locator(locator.open_add_foto_video_form)`
    *   Преобразует `media` в список `media_list`, если `media` не список.
    *   Проходит по всем элементам `m` в `media_list`.
        *   Если `m` это `SimpleNamespace`, то определяет `media_path` в зависимости от флага `no_video`.
            *   Пример: `m = SimpleNamespace(local_image_path='path/image.jpg', local_video_path = 'path/video.mp4')`
            *    Если `no_video = True`, `media_path = 'path/image.jpg'`, иначе `media_path = 'path/video.mp4'`
        *   Если `m` это `str` или `Path`, то `media_path = m`.
            *   Пример: `m = 'path/image.jpg'`
        *   Загружает медиафайл. Если загрузка неудачна, возвращает `False`.
             *   Пример: `d.execute_locator(locator = locator.foto_video_input, message = str(media_path), timeout = 20)`
    *   Если `without_captions = True`, то возвращает `True`
    *   Нажимает кнопку редактирования загруженных медиа. Если не удается, возвращает `False`.
        *   Пример: `d.execute_locator(locator.edit_uloaded_media_button)`
    *   Получает `uploaded_media_frame`. Если `uploaded_media_frame` не найден, возвращает `False`.
        *   Пример: `d.execute_locator(locator.uploaded_media_frame)`
    *   Получает список `textarea_list` с полями для подписи. Если `textarea_list` не найден, возвращает `False`.
        *   Пример: `d.execute_locator(locator = locator.edit_image_properties_textarea, timeout = 10, timeout_for_event = 'presence_of_element_located')`
    *   Вызывает функцию `update_images_captions` для добавления описания к загруженным медиафайлам.
    *   Возвращает `True`.

4. **`update_images_captions(d, media, textarea_list)`:**
    *   Принимает объект `Driver` (d), список медиа `List[SimpleNamespace]` (media), и список элементов `WebElement` (textarea_list).
    *   Загружает локальные переводы из `translations.json`
    *   Определяет функцию `handle_product` для каждого медиафайла.
    *   Циклом проходит по всем `product` в списке `media`
        * Вызывает `handle_product` для каждого `product`.
5. **`handle_product(product, textarea_list, i)`:**
    *   Принимает `SimpleNamespace` (product), список `textarea_list`, и индекс `i`.
    *   Определяет язык (`lang`) и направление (`direction`) текста.
    *   Формирует строку сообщения `message` на основе свойств `product` (`product_title`, `description`, `original_price`, `sale_price`, `discount`, `evaluate_rate`, `promotion_link`) и переводов из `translations.json`.
    *   Отправляет текст сообщения в элемент `textarea_list[i]`.

6. **`publish(d, attempts)`:**
    *   Принимает объект `Driver` (d) и количество попыток (attempts)
    *   Если количество попыток отрицательное то возвращает `False`.
    *   Выполняет клик на кнопку "Завершить редактирование"
    *   Ждет 1 секунду
    *   Выполняет клик на кнопку "Опубликовать"
        * Если `publish` не удался, пробует кликнуть на `close_pop_up` или `not_now`.
        * Рекурсивно вызывает `publish`, уменьшив кол-во попыток на 1.
        * Если кол-во попыток больше 0, то ждет 5 секунд и вызывает рекурсивно `publish`, уменьшив кол-во попыток на 1.
    *   Пока не появится окно добавления нового поста, проверяет клик на `close_pop_up` или `not_now`.
        * Рекурсивно вызывает `publish`, уменьшив кол-во попыток на 1.
        * Если кол-во попыток больше 0, то ждет 2 секунды и вызывает рекурсивно `publish`, уменьшив кол-во попыток на 1.
    *   Возвращает `True`.

### 2. <mermaid>

```mermaid
flowchart TD
    Start(Начало) --> post_message_func[<code>post_message(d, message, no_video, images, without_captions)</code>];
    post_message_func --> post_title_call{Вызов <code>post_title(d, message)</code>}
    post_title_call -- False --> End(Конец);
    post_title_call -- True --> upload_media_call{Вызов <code>upload_media(d, message.products, no_video, without_captions)</code>}
    upload_media_call -- False --> End;
    upload_media_call -- True --> check_send_locator{Вызов <code>d.execute_locator(locator.send)</code>}
    check_send_locator -- True --> End
    check_send_locator -- False --> finish_editing_button_locator{Вызов <code>d.execute_locator(locator.finish_editing_button)</code>};
    finish_editing_button_locator -- False --> End
    finish_editing_button_locator -- True --> publish_call{Вызов <code>publish(d)</code>};
    publish_call -- False --> End
    publish_call -- True --> End
    
    subgraph post_title
        post_title_func[<code>post_title(d, message)</code>] --> scroll_page{Вызов <code>d.scroll()</code>};
        scroll_page -- False --> post_title_return_false[return False];
        scroll_page -- True --> open_add_post_box{Вызов <code>d.execute_locator(locator.open_add_post_box)</code>};
        open_add_post_box -- False --> post_title_return_false;
        open_add_post_box -- True --> format_message{Форматирование сообщения};
        format_message --> add_message_to_box{Вызов <code>d.execute_locator(locator.add_message)</code>};
        add_message_to_box -- False --> post_title_return_false;
        add_message_to_box -- True --> post_title_return_true[return True];
        post_title_return_false --> end_post_title[return]
        post_title_return_true --> end_post_title
        end_post_title
    end
    
    subgraph upload_media
        upload_media_func[<code>upload_media(d, media, no_video, without_captions)</code>] --> check_media_empty{Проверка <code>media</code> на пустоту};
        check_media_empty -- True --> upload_media_return_false[return False];
        check_media_empty -- False --> open_add_media_form{Вызов <code>d.execute_locator(locator.open_add_foto_video_form)</code>};
        open_add_media_form -- False --> upload_media_return_false;
        open_add_media_form -- True --> prepare_media_list{Преобразование media в список};
        prepare_media_list --> loop_media[Цикл по media_list];
        loop_media --> determine_media_path{Определение <code>media_path</code>};
         determine_media_path --> upload_media_file{Вызов <code>d.execute_locator(locator.foto_video_input)</code>}
         upload_media_file -- False --> upload_media_return_false
         upload_media_file -- True --> check_without_captions{Проверка <code>without_captions</code>};
        check_without_captions -- True --> upload_media_return_true[return True];
        check_without_captions -- False --> edit_uploaded_media_button{Вызов <code>d.execute_locator(locator.edit_uloaded_media_button)</code>};
        edit_uploaded_media_button -- False --> upload_media_return_false;
        edit_uploaded_media_button -- True --> get_uploaded_media_frame{Вызов <code>d.execute_locator(locator.uploaded_media_frame)</code>};
         get_uploaded_media_frame -- False --> upload_media_return_false;
         get_uploaded_media_frame -- True --> get_textarea_list{Вызов <code>d.execute_locator(locator.edit_image_properties_textarea)</code>};
         get_textarea_list -- False --> upload_media_return_false;
         get_textarea_list -- True --> update_captions_call{Вызов <code>update_images_captions(d, media, textarea_list)</code>};
         update_captions_call --> upload_media_return_true;
        upload_media_return_false --> end_upload_media[return];
        upload_media_return_true --> end_upload_media
        end_upload_media
        end
        
    subgraph update_images_captions
        update_images_captions_func[<code>update_images_captions(d, media, textarea_list)</code>] --> load_translations{Загрузка переводов из <code>translations.json</code>};
        load_translations --> loop_products[Цикл по media];
        loop_products --> handle_product_call{Вызов <code>handle_product(product, textarea_list, i)</code>}
    end

    subgraph handle_product
        handle_product_func[<code>handle_product(product, textarea_list, i)</code>] --> determine_language_direction{Определение <code>lang</code> и <code>direction</code>};
        determine_language_direction --> generate_message_text{Формирование текста сообщения};
        generate_message_text --> send_message_to_textarea{Отправка сообщения в <code>textarea_list[i]</code>};
    end

    subgraph publish
        publish_func[<code>publish(d, attempts)</code>] --> check_attempts{Проверка attempts < 0}
        check_attempts -- True --> publish_return_false[return False];
        check_attempts -- False --> finish_editing_click{<code>d.execute_locator(locator.finish_editing_button)</code>}
         finish_editing_click -- False --> publish_return_false
         finish_editing_click -- True --> wait_1{wait(1)};
         wait_1 --> publish_click{<code>d.execute_locator(locator.publish)</code>};
         publish_click -- False --> check_pop_up_or_not_now_publish{Проверка pop_up или not_now}
         publish_click -- True --> check_open_add_post_box{Цикл: <code>d.execute_locator(locator.open_add_post_box)</code>};
         check_pop_up_or_not_now_publish -- True --> publish_recursion_call{<code>publish(d, attempts-1)</code>}
         check_pop_up_or_not_now_publish -- False --> check_attempts_after_publish{Проверка attempts > 0}
         check_attempts_after_publish -- True --> wait_5{wait(5)};
         wait_5 --> publish_recursion_call
         check_attempts_after_publish -- False --> publish_return_false
         check_open_add_post_box -- True --> publish_return_true[return True]
         check_open_add_post_box -- False --> check_pop_up_or_not_now_open_add_post{Проверка pop_up или not_now}
         check_pop_up_or_not_now_open_add_post -- True --> publish_recursion_call_open_add_post{<code>publish(d, attempts-1)</code>}
         check_pop_up_or_not_now_open_add_post -- False --> check_attempts_after_open_add_post{Проверка attempts > 0}
         check_attempts_after_open_add_post -- True --> wait_2{wait(2)}
         wait_2 --> publish_recursion_call_open_add_post
        publish_return_false --> end_publish[return]
        publish_return_true --> end_publish
        end_publish
        end
    
```

**Объяснение зависимостей `mermaid`:**

*   `flowchart TD`:  Определяет тип диаграммы как блок-схему, и направление сверху вниз.
*   `Start` : Начало работы `post_message.py`.
*   `post_message_func`: Функция `post_message`, которая является точкой входа.
*   `post_title_call`: Вызов функции `post_title`.
*   `upload_media_call`: Вызов функции `upload_media`.
*   `check_send_locator`: Проверка на наличие локатора `send`.
*   `finish_editing_button_locator`: Вызов функции `d.execute_locator` для кнопки `finish_editing_button`.
*   `publish_call`: Вызов функции `publish`.
*   `post_title`: Подграф, представляющий логику функции `post_title`.
*   `upload_media`: Подграф, представляющий логику функции `upload_media`.
*   `update_images_captions`: Подграф, представляющий логику функции `update_images_captions`.
*   `handle_product`: Подграф, представляющий логику функции `handle_product`.
*   `publish`: Подграф, представляющий логику функции `publish`.
*   `end`: Конец работы `post_message.py`.
*   Стрелки (`-->`)  показывают поток управления между блоками, а также условные переходы.
*   Тексты в скобках `{}` или `[]` представляют собой описание действия или условий.
*   Код в `<>` является название функций/методов или кода.
*   Отрицательные сценарии, которые возвращают `False` обозначены `return False`, а положительные `return True`.
*   Вложенные подграфы используются для группировки связанных действий.

### 3. <объяснение>

**Импорты:**

*   `time`: Используется для пауз в выполнении кода (`time.sleep()`).
*   `pathlib.Path`: Работа с путями к файлам и каталогам.
*   `types.SimpleNamespace`: Создание простых объектов с атрибутами, что позволяет динамически создавать объекты для хранения данных (например, `locator`).
*   `typing.Dict, List, Optional`: Аннотации типов для статической проверки кода.
*   `selenium.webdriver.remote.webelement.WebElement`: Тип для представления веб-элементов (например, textarea).
*   `src.gs`: Глобальные настройки проекта.
*   `src.webdriver.driver.Driver`: Класс для управления веб-драйвером (Selenium).
*   `src.utils.jjson.j_loads_ns`: Загрузка JSON-файлов в объекты SimpleNamespace.
*   `src.utils.printer.pprint`: Функция для форматированного вывода.
*   `src.logger.logger.logger`: Объект для логирования.

**Классы:**

*   `Driver`: Класс, представляющий веб-драйвер, содержит методы для взаимодействия со страницей. Используется для выполнения действий (скролл, клик, отправка текста).

**Функции:**

*   `post_title(d: Driver, message: SimpleNamespace | str) -> bool`:
    *   **Аргументы:** `d` (объект Driver) и `message` (объект `SimpleNamespace` или строка).
    *   **Назначение:** Отправляет заголовок и описание в поле для ввода поста.
    *   **Возвращаемое значение:** `True` в случае успеха, иначе `None`.
    *   **Пример:** `post_title(driver, SimpleNamespace(title='Заголовок', description='Описание'))`
*   `upload_media(d: Driver, media: SimpleNamespace | List[SimpleNamespace] | str | list[str],  no_video: bool = False, without_captions: bool = False) -> bool`:
    *   **Аргументы:** `d` (объект Driver), `media` (медиафайлы в различных форматах), `no_video` (флаг для загрузки изображений) и `without_captions` (флаг для отключения подписей).
    *   **Назначение:** Загружает медиафайлы и при необходимости обновляет подписи.
    *   **Возвращаемое значение:** `True` в случае успеха, иначе `None`.
    *   **Пример:** `upload_media(driver, [SimpleNamespace(local_image_path='path/to/image.jpg')])`
*   `update_images_captions(d: Driver, media: List[SimpleNamespace], textarea_list: List[WebElement]) -> None`:
    *   **Аргументы:** `d` (объект Driver), `media` (список продуктов с деталями) и `textarea_list` (список текстовых полей для подписей).
    *   **Назначение:** Добавляет описание к загруженным медиафайлам.
    *   **Возвращаемое значение:** `None`
    *   **Пример:** `update_images_captions(driver, products, textarea_list)`
*   `publish(d:Driver, attempts = 5) -> bool`:
    *   **Аргументы:** `d` (объект Driver) и `attempts` (количество попыток).
    *   **Назначение:** Завершает публикацию поста.
    *    **Возвращаемое значение:** `True` в случае успеха, иначе `None`.
    *   **Пример:** `publish(driver, 5)`
*   `promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool`:
    *   **Аргументы:** `d` (объект Driver), `category` (категория поста), `products` (список продуктов) и `no_video` (флаг для загрузки изображений).
    *   **Назначение:** Комбинирует публикацию заголовка, загрузку медиа и завершение публикации.
    *   **Возвращаемое значение:** `True` в случае успеха, иначе `None`.
    *    **Пример:** `promote_post(driver, SimpleNamespace(title='Заголовок', description='Описание'), [SimpleNamespace(local_image_path='path/to/image.jpg')])`
*   `post_message(d: Driver, message: SimpleNamespace,  no_video: bool = False, images: Optional[str | list[str]] = None, without_captions: bool = False) -> bool`:
    *   **Аргументы:** `d` (объект Driver), `message` (сообщение), `no_video` (флаг для загрузки изображений), `images` (изображения) и `without_captions` (флаг для отключения подписей).
    *   **Назначение:** Основная функция для создания и публикации поста.
    *   **Возвращаемое значение:** `True` в случае успеха, иначе `None`.
    *   **Пример:** `post_message(driver, SimpleNamespace(title='Заголовок', description='Описание', products=[SimpleNamespace(local_image_path='path/to/image.jpg')]))`

**Переменные:**

*   `locator`: Объект `SimpleNamespace`, содержащий локаторы элементов, загруженные из `post_message.json`.

**Потенциальные ошибки и улучшения:**

*   **Обработка ошибок:** В некоторых местах есть общая обработка ошибок `except Exception as ex:`. Лучше использовать более конкретные исключения.
*   **Логирование:** Присутствует логирование, но не все ошибки логируются достаточно подробно. Можно добавить больше контекста в сообщения.
*   **Рекурсия в publish:** В функции `publish` есть рекурсивный вызов, что может привести к проблемам, если попыток слишком много. Возможно, лучше использовать цикл `while`.
*   **Использование `time.sleep`:** Использования `time.sleep` не всегда оправдано. Можно заменить на явные ожидания через `WebDriverWait`, чтобы снизить общее время ожидания.
*   **Общая структура:** Можно рассмотреть разбивку кода на еще более мелкие функции для лучшей читаемости и переиспользования.
*   **Обработка `no_video`:**  Уточнить поведение параметра `no_video`, так как он влияет на выбор поля `local_video_path` или `local_image_path`, однако не используется в других местах.
*    **Использование `publish`:** Функция `publish` вызывается рекурсивно при ошибках, но есть ветвления `if`, которые могут не позволить ее вызвать повторно.

**Взаимосвязи с другими частями проекта:**

*   **`src.gs`:** Используется для получения пути к файлам.
*   **`src.webdriver.driver.Driver`:** Используется для взаимодействия с браузером через Selenium.
*   **`src.utils.jjson`:** Используется для загрузки локаторов из JSON-файлов.
*   **`src.utils.printer`:** Используется для отладочного вывода.
*   **`src.logger`:** Используется для логирования событий.
*   **`src.endpoints.advertisement.facebook.locators`**: Содержит json-файл с локаторами, необходимыми для работы с веб-страницей facebook.
*   **`src.endpoints.advertisement.facebook.scenarios`**: Содержит json-файл `translations.json` с переводами.

Этот код представляет собой сценарий для публикации сообщений в Facebook, включающий отправку текста, загрузку медиафайлов и добавление подписей к ним. Он использует Selenium для взаимодействия с веб-интерфейсом.