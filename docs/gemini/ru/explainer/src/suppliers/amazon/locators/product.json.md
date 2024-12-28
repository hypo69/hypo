## АНАЛИЗ КОДА

### <алгоритм>
Этот JSON-файл представляет собой конфигурацию локаторов для извлечения данных о продукте с веб-сайта Amazon. Каждый ключ верхнего уровня представляет собой поле данных о продукте, которое необходимо извлечь. Значение каждого ключа является объектом, который описывает, как найти и извлечь это значение. Вот пошаговая блок-схема процесса:

1. **Инициализация**: Загрузка JSON-конфигурации.

2. **Обход ключей верхнего уровня**: Для каждого ключа, представляющего поле данных о продукте (например, `id`, `id_manufacturer`, `price`, `name` и т. д.):

    -  **Извлечение конфигурации**: Получение объекта конфигурации, связанного с ключом.

    - **Определение метода поиска**: 
       - Проверяется поле `"by"`. 
       - Если `"by"` имеет значение `"VALUE"`, то значение поля `"attribute"` используется как значение. Пример: `"id_supplier"` со значением `2800`, `"id_shop_default"` со значением `"1"`
       - Если `"by"` имеет значение `"XPATH"`, то используется XPath-выражение из поля `"selector"` для поиска элемента на веб-странице. Пример: `"id_manufacturer"` использует XPATH `//span[contains(text(), \'Brand\')]/parent::td/following-sibling::td/span[contains(@class, \'po-break-word\')]`
        - Если `"by"` имеет значение `null`, то поиск не производится, а значение задается null.
       
    - **Определение атрибута**: 
        - Проверяется поле `"attribute"`.
        - Если `"attribute"` имеет значение `innerText`, то текст найденного элемента будет использован в качестве значения. Пример `"name"` использует XPATH `//span[@id=\'productTitle\']` для извлечения текста.
        - Если `"attribute"` имеет значение `src`, то  атрибут  `src` найденного элемента будет использован в качестве значения. Пример `"Screenshot"` использует XPATH `//img[@id=\'landingImage\']` и атрибут `src` для извлечения ссылки.
        - Если `"attribute"` имеет значение `"VALUE"`, то значение поля `"attribute"` используется как значение.
        - Если `"attribute"` имеет значение `null`, то значением поля будет `null`.
        - Если `"attribute"` имеет значение типа `string` с кастомной логикой, то  будет использоваться кастомная логика. Например: `"reference"` со значением `$d.current_url.split(f\'\'\'/\'\'\')[-2]` и `"ASIN"` со значением `$_(driver.current_url[(driver.current_url.index(r\'dp/\') + 3):(driver.current_url.index(r\'dp/\') + 3) + 10:])_$`.

    - **Обработка списка**: 
       -  Если `"if_list"` равно `"first"`, то возвращается первое найденное значение.
       -  Если `"if_list"` равно `"all"`, то возвращается список всех найденных значений.

    - **Действия с мышью**: 
       - Если `"use_mouse"` равно `true`, то имитируется действие мыши. (не используется в данном примере, но возможно использование)

    - **Обязательность**:
       - Если `"mandatory"` равно `true`, то отсутствие элемента при поиске приведет к ошибке.

    - **Таймаут**:
       - Если `"timeout"` задано, то задается время ожидания элемента.
    - **Событие**:
      - Если `"event"` задано, то после нахождения элемента вызывается определенное событие (например, `screenshot()`).

3. **Сохранение результатов**: Сохранение извлеченных данных в структуру данных.

4. **Повтор**: Повторение шагов 2 и 3 для всех полей данных о продукте.

Примеры:
- Для `"id"`: `"by": "VALUE"` - значение будет null.
- Для `"id_manufacturer"`:  `"by": "XPATH"`, `"attribute": "innerText"` - извлекается текст из элемента, найденного по XPATH.
- Для `"price"`: имеет вложенные поля `"new"` и `"ref"`, каждое из которых имеет свою конфигурацию поиска.
- Для `"reference"`: `"by": "VALUE"`, `"attribute": "$d.current_url.split(f\'\'\'/\'\'\')[-2]"` - значение вычисляется с помощью кастомной логики.
- Для `"Screenshot"`: `"by": "XPATH"`, `"attribute": "src"`, `"event": "screenshot()"` - извлекается атрибут `src` и делается скриншот.
- Для `"Specification"`:  `"if_list": "all"` - возвращается список всех найденных элементов.
- Для `affiliate_short_link`: имеет вложенные селекторы и атрибуты, которые могут работать в зависимости от кастомной логики.
### <mermaid>
```mermaid
flowchart TD
    subgraph ProductDataExtraction
        Start[Начало] --> LoadConfig[Загрузка JSON-конфигурации]
        LoadConfig --> LoopThroughFields[Цикл по полям данных о продукте]

        subgraph FieldExtraction
            LoopThroughFields --> GetFieldConfig[Получение конфигурации поля]
            GetFieldConfig --> CheckByMethod[Проверка метода поиска (by)]
            CheckByMethod -- "by == VALUE" --> UseValue[Использовать значение атрибута]
            CheckByMethod -- "by == XPATH" --> FindElementXPath[Поиск элемента по XPath]
            CheckByMethod -- "by == null" --> UseNull[Использовать null]
            FindElementXPath --> CheckAttribute[Проверка типа атрибута]
            UseValue --> CheckAttribute
            UseNull --> CheckAttribute
             
            CheckAttribute -- "attribute == innerText" --> GetInnerText[Получение текста элемента]
            CheckAttribute -- "attribute == src" --> GetSrcAttribute[Получение атрибута src элемента]
            CheckAttribute -- "attribute == VALUE" --> GetValueAttribute[Получение значения атрибута]
            CheckAttribute -- "attribute == null" --> SetNullAttribute[Установить null]
             CheckAttribute -- "attribute == custom logic" --> UseCustomLogic[Использовать кастомную логику]
            
            GetInnerText --> CheckIfList[Проверка типа списка (if_list)]
            GetSrcAttribute --> CheckIfList
            GetValueAttribute --> CheckIfList
             SetNullAttribute --> CheckIfList
             UseCustomLogic --> CheckIfList

            CheckIfList -- "if_list == first" --> GetFirstItem[Получить первый элемент]
            CheckIfList -- "if_list == all" --> GetAllItems[Получить все элементы]
            GetFirstItem --> CheckMouseAction[Проверка действий мыши]
            GetAllItems --> CheckMouseAction

            CheckMouseAction --> CheckMandatory[Проверка обязательности поля]
            CheckMandatory -- "mandatory == true" --> CheckTimeout[Проверка таймаута]
            CheckMandatory -- "mandatory == false" --> CheckTimeout
            CheckTimeout --> CheckEvent[Проверка события]
            CheckEvent --> SaveResult[Сохранение результата]
             
            
        end
         SaveResult --> LoopThroughFields
        LoopThroughFields -- "Конец цикла" --> End[Конец]
    end
```

**Описание зависимостей Mermaid:**

- `Start` - начало процесса.
- `LoadConfig` - загрузка JSON конфигурации.
- `LoopThroughFields` - цикл по всем полям в JSON конфигурации.
- `GetFieldConfig` - получает конфигурацию для текущего поля.
- `CheckByMethod` - проверяет метод поиска элемента (`by`).
    - `UseValue` - используется значение из поля `attribute` напрямую.
    - `FindElementXPath` - поиск элемента на странице по XPATH.
    -  `UseNull` - присвоить значению null.
- `CheckAttribute` - проверяет тип атрибута для извлечения (`innerText`, `src`, `VALUE` , `null`, `custom logic`).
    - `GetInnerText` - извлечение текста элемента.
    - `GetSrcAttribute` - извлечение атрибута `src` элемента.
    - `GetValueAttribute` -  использование значения из поля `attribute`.
    - `SetNullAttribute` -  установить значение null.
    - `UseCustomLogic` - вычисление значения на основе кастомной логики.
- `CheckIfList` - проверяет, нужно ли извлекать первый элемент или все.
    - `GetFirstItem` - получает первый найденный элемент.
    - `GetAllItems` - получает все найденные элементы.
- `CheckMouseAction` - проверка наличия действий мыши.
- `CheckMandatory` - проверка обязательности поля (если `true`, ошибка при отсутствии).
- `CheckTimeout` - проверка таймаута.
- `CheckEvent` - проверка события.
- `SaveResult` - сохраняет извлеченное значение.
- `End` - конец процесса.

### <объяснение>

**Общая структура**:
Файл `product.json` представляет собой JSON-словарь, где каждый ключ является именем поля продукта, которое нужно извлечь (например, `id`, `name`, `price`, `description` и т.д.). Значение каждого ключа – это JSON-объект, содержащий параметры для поиска и извлечения соответствующего значения поля.

**Ключи и их значения:**
- **`attribute`**: Указывает, какой атрибут элемента нужно извлечь (например, `innerText`, `src`, `value` или null).
- **`by`**: Указывает метод поиска элемента (`XPATH`, `VALUE` или `null`).
- **`selector`**: XPath выражение для поиска элемента, или `null` если метод поиска `VALUE` или `null`.
- **`if_list`**:  Указывает, как обрабатывать список найденных элементов (`first` - взять первый, `all` - взять все).
- **`use_mouse`**:  Логическое значение, указывающее, нужно ли использовать действия мыши (не используется в данном примере, но возможно использование).
- **`mandatory`**: Логическое значение, указывающее, является ли поле обязательным для извлечения. Если `true`, то при отсутствии значения будет ошибка.
- **`timeout`**:  Время ожидания элемента (в секундах).
- **`timeout_for_event`**: Время ожидания события
- **`event`**: Событие, которое нужно выполнить после извлечения (например, `screenshot()`).
- **`logic for action[AND|OR|XOR|VALUE|null]`**: Логика для действий с несколькими селекторами или атрибутами (не используется в данном примере, но возможно использование).
- **`logic for attribue[AND|OR|XOR|VALUE|null]`**: Логика для работы с несколькими атрибутами  (используется в `affiliate_short_link`, `affiliate_img_HTML` и `affiliate_iframe`).
-  **`multi selectors`**:  Дополнительные XPATH селекторы.

**Примеры**:
- **`id`**:
    - `"attribute": null`, `"by": "VALUE"` - поле будет иметь значение `null`, поскольку `by` равен `"VALUE"` и `"attribute"` равен `null`.
-   **`id_manufacturer`**:
    - `"attribute": "innerText"`, `"by": "XPATH"`, `"selector": "//span[contains(text(), \'Brand\')]/parent::td/following-sibling::td/span[contains(@class, \'po-break-word\')]"`
    -  Ищет элемент по XPATH, получает его текст.
- **`price`**:
  -  Имеет вложенные объекты "new" и "ref", каждый из которых имеет свою конфигурацию для получения цены.
- **`reference`**:
    - `"attribute": "$d.current_url.split(f\'\'\'/\'\'\')[-2]"` `"by": "VALUE"`
    - Извлекает значение из текущего URL, используя Python-подобный код.
- **`Screenshot`**:
    - `"attribute": "src"`, `"by": "XPATH"`, `"selector": "//img[@id=\'landingImage\']", "event": "screenshot()"`
    - Ищет элемент по XPATH и получает его атрибут `src`, а также делает скриншот.
- **`description`**:
    - `"attribute": "innerText"`, `"by": "XPATH"`, `"selector": "//div[@id=\'productDescription\']"`
    -  Ищет элемент по XPATH, получает его текст.
- **`Specification`**:
    - `"attribute": ""`, `"by": "XPATH"`, `"selector": ""`, `"if_list": "all"`
    -  Ищет все элементы по XPATH (в данном случае пустой селектор), которые будут использоваться для извлечения технических характеристик.
- **`affiliate_short_link`**:
  - имеет несколько селекторов и атрибутов, которые применяются в зависимости от логики `"logic for attribue[AND|OR|XOR|VALUE|null]"` и событий `"event"`.
**Ошибки и улучшения**:
- **Отсутствие проверок на ошибки**: В JSON не предусмотрена обработка ошибок, которые могут возникнуть при поиске элементов или извлечении атрибутов.
- **Жёстко закодированные XPath**: Использование XPath-селекторов может привести к поломкам, если структура HTML страницы изменится.
- **Недостаточная универсальность**: Конфигурация жёстко привязана к структуре страниц Amazon, что делает её менее гибкой.
- **Не все поля имеют описание**:  Многие поля имеют `attribute=null` и `by=null`, что может вызвать путаницу.

**Взаимодействие с другими частями проекта**:
Этот JSON-файл используется в модулях, которые занимаются парсингом данных с сайта Amazon. Он предоставляет конфигурацию для поиска элементов на веб-странице и извлечения их значений.