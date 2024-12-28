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
```mermaid
graph LR
    A[Start: Инициализация ProductFields] --> B(Загрузка списка полей из файла fields_list.txt);
    B --> C{Успешно?};
    C -- Yes --> D(Инициализация словаря языков:  {'en': 1, 'he': 2, 'ru': 3});
    C -- No --> E(Логирование ошибки загрузки полей);
    D --> F(Создание объекта SimpleNamespace с полями товара);
    F --> G(Инициализация словаря assist_fields_dict с  default_image_url и images_urls);
    G --> H(Загрузка дефолтных значений полей из product_fields_default_values.json);
    H --> I{Успешно?};
     I -- Yes --> J(Установка дефолтных значений в объект класса ProductFields через setattr);
    I -- No --> K(Логирование ошибки загрузки дефолтных значений);

    J --> L{Работа с полями через property и setter};
     L -->M[Пример: Установка id_product];
        M --> N{Проверка на ошибку ProductFieldException};
        N -- Yes --> O(Логирование ошибки установки id_product);
        N -- No --> P(Установка значения id_product);
         P --> Q[Пример: Получение значения  description];
        Q --> R(Возвращение значения description);
    
    K --> S(End);
    O --> S
    R --> S
     
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style L fill:#ccf,stroke:#333,stroke-width:2px
    style B fill:#fff,stroke:#333,stroke-width:1px
        style C fill:#fff,stroke:#333,stroke-width:1px
            style D fill:#fff,stroke:#333,stroke-width:1px
             style E fill:#fff,stroke:#333,stroke-width:1px
                  style F fill:#fff,stroke:#333,stroke-width:1px
                      style G fill:#fff,stroke:#333,stroke-width:1px
                         style H fill:#fff,stroke:#333,stroke-width:1px
                             style I fill:#fff,stroke:#333,stroke-width:1px
                                 style J fill:#fff,stroke:#333,stroke-width:1px
                                     style K fill:#fff,stroke:#333,stroke-width:1px
                                         style M fill:#fff,stroke:#333,stroke-width:1px
                                              style N fill:#fff,stroke:#333,stroke-width:1px
                                                style O fill:#fff,stroke:#333,stroke-width:1px
                                                   style P fill:#fff,stroke:#333,stroke-width:1px
                                                     style Q fill:#fff,stroke:#333,stroke-width:1px
                                                           style R fill:#fff,stroke:#333,stroke-width:1px
```

**Примеры для логических блоков:**

*   **B (Загрузка списка полей):** Из файла `fields_list.txt` загружается список полей, например: `['id_product', 'id_supplier', 'name', 'price', ...]`.
*   **D (Инициализация словаря языков):**  Создается словарь соответствия языков их id в PrestaShop, например: `{'en': 1, 'he': 2, 'ru': 3}`.
*   **F (Создание объекта SimpleNamespace):** Создается объект `presta_fields` с атрибутами, соответствующими полям из `fields_list.txt`, например: `presta_fields.id_product = None, presta_fields.name = None, ...`.
*   **H (Загрузка дефолтных значений):** Из файла `product_fields_default_values.json` загружаются значения по умолчанию, например: `{"active": 1, "on_sale": 0, "price": 0.00, ...}`.
*  **J (Установка дефолтных значений):** Значения из JSON устанавливаются в `presta_fields` с помощью `setattr()`, например: `self.active = 1`, `self.price = 0.00`.
*   **M (Пример: Установка `id_product`):** Вызывается setter `@id_product.setter`,  с проверкой на  `ProductFieldException`. Например, если `id_product` устанавливается как `self.id_product = 123`.
*   **Q (Пример: Получение значения `description`):** Вызывается getter `@description.property`, возвращается значение поля `description` которое может быть, например:
    ```python
    {
    'language':
         [
                {'attrs': {'id': '1'}, 'value': "Описание товара на английском"},
          ]
      }
    ```

## <mermaid>

```mermaid
flowchart TD
    Start[Start] --> ProductFieldsInit[ProductFields.__init__];
    ProductFieldsInit --> LoadFieldsList[ProductFields._load_product_fields_list];
    LoadFieldsList --> ReadFile[file.read_text_file]
    ReadFile --> ReturnFieldsList[Return List[str] ]
     ReturnFieldsList-->  SetLanguageDict[self.language = {'en': 1, 'he': 2, 'ru': 3}]
     SetLanguageDict --> CreatePrestaFields[Create SimpleNamespace for presta_fields]
      CreatePrestaFields --> SetAssistFields[self.assist_fields_dict = {'default_image_url': '', 'images_urls': []}]
     SetAssistFields --> LoadDefaultValues[ProductFields._payload]
       LoadDefaultValues --> LoadJsonFromFile[j_loads]
         LoadJsonFromFile --> CheckJsonData[if not data]
            CheckJsonData -- No --> SetDefaultValues[setattr for each field]
        CheckJsonData -- Yes --> LogErrorLoadJson[logger.debug("Ошибка загрузки")]
        SetDefaultValues -->  EndPayload[Return True]
         LogErrorLoadJson--> EndPayload
   
     EndPayload --> EndInit[end __init__]

    
    
    
     
    
    
     
     

    classDef property fill:#ccf,stroke:#333,stroke-width:2px
     classDef setter fill:#cfc,stroke:#333,stroke-width:2px
     classDef function fill:#fff,stroke:#333,stroke-width:1px

    ProductFieldsInit -- Создает --> ProductFields
     ProductFieldsInit  -->  ProductFieldsClass [ProductFields Class]
     ProductFieldsClass  -- Использует --> ReadFile
      ProductFieldsClass  -- Использует --> j_loads
      ReadFile  -- Использует --> Path [pathlib.Path]
         ProductFieldsClass  -- Использует --> logger[src.logger.logger]
             ProductFieldsClass  -- Использует --> ProductFieldException[src.logger.exceptions]

     ProductFieldsClass  -- get -->   AssociationsProperty[ProductFields.associations  property]
     ProductFieldsClass  -- set -->  AssociationsSetter [ProductFields.associations setter]
          AssociationsProperty  -- get -->  presta_fields.associations
             AssociationsSetter  -- set -->  presta_fields.associations
    
    ProductFieldsClass  -- get -->  IdProductProperty[ProductFields.id_product  property]
     ProductFieldsClass  -- set -->   IdProductSetter [ProductFields.id_product setter]
          IdProductProperty  -- get -->  presta_fields.id_product
              IdProductSetter -- set -->  presta_fields.id_product

    ProductFieldsClass -- get -->  IdSupplierProperty[ProductFields.id_supplier  property]
     ProductFieldsClass  -- set -->    IdSupplierSetter [ProductFields.id_supplier setter]
           IdSupplierProperty  -- get -->  presta_fields.id_supplier
                IdSupplierSetter -- set -->  presta_fields.id_supplier

    ProductFieldsClass  -- get -->  IdManufacturerProperty[ProductFields.id_manufacturer  property]
     ProductFieldsClass  -- set -->  IdManufacturerSetter [ProductFields.id_manufacturer setter]
          IdManufacturerProperty  -- get -->  presta_fields.id_manufacturer
               IdManufacturerSetter -- set -->  presta_fields.id_manufacturer


     ProductFieldsClass  -- get -->  IdCategoryDefaultProperty[ProductFields.id_category_default  property]
      ProductFieldsClass  -- set -->  IdCategoryDefaultSetter [ProductFields.id_category_default setter]
            IdCategoryDefaultProperty  -- get -->  presta_fields.id_category_default
                 IdCategoryDefaultSetter -- set -->  presta_fields.id_category_default

     ProductFieldsClass  -- get -->   AdditionalCategoriesProperty[ProductFields.additional_categories  property]
     ProductFieldsClass  -- set -->    AdditionalCategoriesSetter [ProductFields.additional_categories setter]
      AdditionalCategoriesProperty -- get -->   presta_fields.associations.categories
         AdditionalCategoriesSetter -- set -->  presta_fields.associations.categories
         
     ProductFieldsClass  -- get --> IdShopDefaultProperty [ProductFields.id_shop_default  property]
     ProductFieldsClass  -- set --> IdShopDefaultSetter[ProductFields.id_shop_default  setter]
         IdShopDefaultProperty -- get -->  presta_fields.id_shop_default
            IdShopDefaultSetter -- set -->  presta_fields.id_shop_default

     ProductFieldsClass  -- get --> IdShopProperty[ProductFields.id_shop  property]
      ProductFieldsClass  -- set -->IdShopSetter [ProductFields.id_shop  setter]
          IdShopProperty -- get -->  presta_fields.id_shop
            IdShopSetter -- set -->  presta_fields.id_shop
          
    ProductFieldsClass  -- get -->  IdTaxProperty[ProductFields.id_tax  property]
     ProductFieldsClass  -- set -->  IdTaxSetter[ProductFields.id_tax  setter]
       IdTaxProperty -- get -->  presta_fields.id_tax
        IdTaxSetter -- set -->  presta_fields.id_tax

     ProductFieldsClass -- get -->  OnSaleProperty[ProductFields.on_sale  property]
     ProductFieldsClass -- set -->  OnSaleSetter [ProductFields.on_sale  setter]
          OnSaleProperty -- get -->  presta_fields.on_sale
              OnSaleSetter -- set -->  presta_fields.on_sale

      ProductFieldsClass  -- get -->  OnlineOnlyProperty[ProductFields.online_only  property]
       ProductFieldsClass  -- set -->   OnlineOnlySetter[ProductFields.online_only  setter]
          OnlineOnlyProperty -- get -->  presta_fields.online_only
             OnlineOnlySetter -- set -->  presta_fields.online_only

    ProductFieldsClass  -- get --> Ean13Property[ProductFields.ean13 property]
     ProductFieldsClass  -- set --> Ean13Setter [ProductFields.ean13 setter]
          Ean13Property -- get -->  presta_fields.ean13
              Ean13Setter -- set -->  presta_fields.ean13


    ProductFieldsClass -- get -->  IsbnProperty[ProductFields.isbn  property]
    ProductFieldsClass  -- set -->  IsbnSetter [ProductFields.isbn setter]
        IsbnProperty -- get -->  presta_fields.isbn
            IsbnSetter -- set -->  presta_fields.isbn

    ProductFieldsClass  -- get -->  UpcProperty[ProductFields.upc property]
    ProductFieldsClass  -- set --> UpcSetter [ProductFields.upc setter]
        UpcProperty -- get -->  presta_fields.upc
             UpcSetter -- set -->  presta_fields.upc

    ProductFieldsClass -- get -->   MpnProperty[ProductFields.mpn  property]
     ProductFieldsClass  -- set -->   MpnSetter [ProductFields.mpn setter]
        MpnProperty -- get -->  presta_fields.mpn
             MpnSetter -- set -->  presta_fields.mpn

    ProductFieldsClass -- get --> EcotaxProperty[ProductFields.ecotax property]
     ProductFieldsClass -- set --> EcotaxSetter[ProductFields.ecotax setter]
          EcotaxProperty -- get -->  presta_fields.ecotax
            EcotaxSetter -- set -->  presta_fields.ecotax
    

     ProductFieldsClass -- get -->MinimalQuantityProperty[ProductFields.minimal_quantity property]
      ProductFieldsClass -- set -->MinimalQuantitySetter[ProductFields.minimal_quantity setter]
          MinimalQuantityProperty -- get -->  presta_fields.minimal_quantity
               MinimalQuantitySetter -- set -->  presta_fields.minimal_quantity

    ProductFieldsClass -- get -->LowStockThresholdProperty[ProductFields.low_stock_threshold property]
     ProductFieldsClass  -- set -->  LowStockThresholdSetter[ProductFields.low_stock_threshold setter]
        LowStockThresholdProperty -- get -->  presta_fields.low_stock_threshold
             LowStockThresholdSetter -- set -->  presta_fields.low_stock_threshold

     ProductFieldsClass  -- get --> LowStockAlertProperty [ProductFields.low_stock_alert property]
     ProductFieldsClass  -- set --> LowStockAlertSetter [ProductFields.low_stock_alert setter]
          LowStockAlertProperty -- get -->  presta_fields.low_stock_alert
               LowStockAlertSetter -- set -->  presta_fields.low_stock_alert
      
     ProductFieldsClass -- get -->   PriceProperty[ProductFields.price property]
     ProductFieldsClass -- set --> PriceSetter [ProductFields.price setter]
          PriceProperty -- get -->  presta_fields.price
               PriceSetter -- set -->  presta_fields.price

    ProductFieldsClass -- get -->  WholesalePriceProperty[ProductFields.wholesale_price  property]
    ProductFieldsClass  -- set -->  WholesalePriceSetter [ProductFields.wholesale_price  setter]
        WholesalePriceProperty -- get -->  presta_fields.wholesale_price
            WholesalePriceSetter -- set -->  presta_fields.wholesale_price
    
     ProductFieldsClass  -- get -->UnityProperty[ProductFields.unity property]
     ProductFieldsClass  -- set --> UnitySetter [ProductFields.unity setter]
        UnityProperty -- get -->  presta_fields.unity
            UnitySetter -- set -->  presta_fields.unity

    ProductFieldsClass  -- get -->UnitPriceRatioProperty[ProductFields.unit_price_ratio property]
     ProductFieldsClass -- set -->  UnitPriceRatioSetter[ProductFields.unit_price_ratio setter]
         UnitPriceRatioProperty -- get -->  presta_fields.unit_price_ratio
            UnitPriceRatioSetter -- set -->  presta_fields.unit_price_ratio

    ProductFieldsClass -- get -->   AdditionalShippingCostProperty[ProductFields.additional_shipping_cost property]
     ProductFieldsClass  -- set --> AdditionalShippingCostSetter [ProductFields.additional_shipping_cost setter]
          AdditionalShippingCostProperty -- get -->  presta_fields.additional_shipping_cost
            AdditionalShippingCostSetter -- set -->  presta_fields.additional_shipping_cost

    ProductFieldsClass -- get --> ReferenceProperty[ProductFields.reference property]
    ProductFieldsClass -- set -->  ReferenceSetter[ProductFields.reference setter]
          ReferenceProperty -- get -->  presta_fields.reference
             ReferenceSetter -- set -->  presta_fields.reference

    ProductFieldsClass  -- get --> SupplierReferenceProperty[ProductFields.supplier_reference  property]
    ProductFieldsClass  -- set -->  SupplierReferenceSetter[ProductFields.supplier_reference  setter]
          SupplierReferenceProperty -- get -->  presta_fields.supplier_reference
               SupplierReferenceSetter -- set -->  presta_fields.supplier_reference

    ProductFieldsClass  -- get -->LocationProperty[ProductFields.location property]
     ProductFieldsClass -- set -->LocationSetter [ProductFields.location setter]
        LocationProperty -- get -->  presta_fields.location
            LocationSetter -- set -->  presta_fields.location

     ProductFieldsClass  -- get -->WidthProperty [ProductFields.width property]
     ProductFieldsClass -- set -->  WidthSetter[ProductFields.width setter]
           WidthProperty -- get -->  presta_fields.width
            WidthSetter -- set -->  presta_fields.width


     ProductFieldsClass  -- get --> HeightProperty[ProductFields.height  property]
      ProductFieldsClass -- set -->HeightSetter [ProductFields.height  setter]
           HeightProperty -- get -->  presta_fields.height
            HeightSetter -- set -->  presta_fields.height


    ProductFieldsClass  -- get --> DepthProperty[ProductFields.depth  property]
     ProductFieldsClass  -- set -->  DepthSetter[ProductFields.depth  setter]
           DepthProperty -- get -->  presta_fields.depth
             DepthSetter -- set -->  presta_fields.depth

     ProductFieldsClass  -- get -->  WeightProperty[ProductFields.weight  property]
      ProductFieldsClass  -- set -->WeightSetter [ProductFields.weight setter]
            WeightProperty -- get -->  presta_fields.weight
              WeightSetter -- set -->  presta_fields.weight
    

    ProductFieldsClass -- get -->   VolumeProperty[ProductFields.volume  property]
     ProductFieldsClass  -- set -->VolumeSetter [ProductFields.volume  setter]
         VolumeProperty -- get -->  presta_fields.volume
             VolumeSetter -- set -->  presta_fields.volume

     ProductFieldsClass  -- get -->   OutOfStockProperty[ProductFields.out_of_stock  property]
     ProductFieldsClass  -- set -->OutOfStockSetter [ProductFields.out_of_stock  setter]
           OutOfStockProperty -- get -->  presta_fields.out_of_stock
               OutOfStockSetter -- set -->  presta_fields.out_of_stock

      ProductFieldsClass  -- get --> AdditionalDeliveryTimesProperty[ProductFields.additional_delivery_times property]
      ProductFieldsClass -- set --> AdditionalDeliveryTimesSetter[ProductFields.additional_delivery_times setter]
          AdditionalDeliveryTimesProperty -- get -->  presta_fields.additional_delivery_times
              AdditionalDeliveryTimesSetter -- set -->  presta_fields.additional_delivery_times

     ProductFieldsClass  -- get --> QuantityDiscountProperty[ProductFields.quantity_discount  property]
      ProductFieldsClass -- set -->  QuantityDiscountSetter [ProductFields.quantity_discount setter]
          QuantityDiscountProperty -- get -->  presta_fields.quantity_discount
               QuantityDiscountSetter -- set -->  presta_fields.quantity_discount

      ProductFieldsClass  -- get --> CustomizableProperty[ProductFields.customizable  property]
      ProductFieldsClass -- set -->  CustomizableSetter[ProductFields.customizable  setter]
            CustomizableProperty -- get -->  presta_fields.customizable
                 CustomizableSetter -- set -->  presta_fields.customizable

      ProductFieldsClass -- get --> UploadableFilesProperty[ProductFields.uploadable_files property]
      ProductFieldsClass  -- set -->  UploadableFilesSetter[ProductFields.uploadable_files  setter]
          UploadableFilesProperty -- get -->  presta_fields.uploadable_files
               UploadableFilesSetter -- set -->  presta_fields.uploadable_files

    ProductFieldsClass -- get -->   TextFieldsProperty[ProductFields.text_fields  property]
     ProductFieldsClass -- set -->  TextFieldsSetter[ProductFields.text_fields setter]
           TextFieldsProperty -- get -->  presta_fields.text_fields
             TextFieldsSetter -- set -->  presta_fields.text_fields

    ProductFieldsClass -- get -->  ActiveProperty[ProductFields.active property]
     ProductFieldsClass -- set -->  ActiveSetter[ProductFields.active setter]
          ActiveProperty -- get -->  presta_fields.active
            ActiveSetter -- set -->  presta_fields.active

    ProductFieldsClass -- get --> RedirectTypeProperty[ProductFields.redirect_type property]
     ProductFieldsClass  -- set --> RedirectTypeSetter[ProductFields.redirect_type setter]
          RedirectTypeProperty -- get -->  presta_fields.redirect_type
             RedirectTypeSetter -- set -->  presta_fields.redirect_type

    ProductFieldsClass -- get -->  IdTypeRedirectedProperty[ProductFields.id_type_redirected property]
     ProductFieldsClass -- set -->   IdTypeRedirectedSetter[ProductFields.id_type_redirected setter]
            IdTypeRedirectedProperty -- get -->  presta_fields.id_type_redirected
               IdTypeRedirectedSetter -- set -->  presta_fields.id_type_redirected

    ProductFieldsClass -- get --> AvailableForOrderProperty[ProductFields.available_for_order  property]
     ProductFieldsClass -- set -->  AvailableForOrderSetter[ProductFields.available_for_order setter]
        AvailableForOrderProperty -- get -->  presta_fields.available_for_order
            AvailableForOrderSetter -- set -->  presta_fields.available_for_order

    ProductFieldsClass -- get -->  AvailableDateProperty[ProductFields.available_date property]
    ProductFieldsClass -- set -->  AvailableDateSetter[ProductFields.available_date setter]
         AvailableDateProperty -- get -->  presta_fields.available_date
            AvailableDateSetter -- set -->  presta_fields.available_date
    
    ProductFieldsClass -- get -->   ShowConditionProperty[ProductFields.show_condition  property]
     ProductFieldsClass -- set -->  ShowConditionSetter[ProductFields.show_condition  setter]
           ShowConditionProperty -- get -->  presta_fields.show_condition
              ShowConditionSetter -- set -->  presta_fields.show_condition
    
    ProductFieldsClass -- get -->  ConditionProperty[ProductFields.condition property]
    ProductFieldsClass -- set -->  ConditionSetter [ProductFields.condition setter]
           ConditionProperty -- get -->  presta_fields.condition
              ConditionSetter -- set -->  presta_fields.condition

    ProductFieldsClass -- get --> ShowPriceProperty[ProductFields.show_price property]
    ProductFieldsClass -- set --> ShowPriceSetter [ProductFields.show_price setter]
        ShowPriceProperty -- get -->  presta_fields.show_price
            ShowPriceSetter -- set -->  presta_fields.show_price

    ProductFieldsClass -- get -->  IndexedProperty[ProductFields.indexed property]
    ProductFieldsClass -- set -->  IndexedSetter[ProductFields.indexed setter]
         IndexedProperty -- get -->  presta_fields.indexed
            IndexedSetter -- set -->  presta_fields.indexed

    ProductFieldsClass -- get --> VisibilityProperty[ProductFields.visibility  property]
    ProductFieldsClass -- set --> VisibilitySetter[ProductFields.visibility  setter]
         VisibilityProperty -- get -->  presta_fields.visibility
            VisibilitySetter -- set -->  presta_fields.visibility

     ProductFieldsClass -- get --> CacheIsPackProperty[ProductFields.cache_is_pack property]
      ProductFieldsClass  -- set --> CacheIsPackSetter [ProductFields.cache_is_pack setter]
           CacheIsPackProperty -- get -->  presta_fields.cache_is_pack
               CacheIsPackSetter -- set -->  presta_fields.cache_is_pack

    ProductFieldsClass -- get -->   CacheHasAttachmentsProperty[ProductFields.cache_has_attachments  property]
    ProductFieldsClass  -- set --> CacheHasAttachmentsSetter[ProductFields.cache_has_attachments  setter]
        CacheHasAttachmentsProperty -- get -->  presta_fields.cache_has_attachments
            CacheHasAttachmentsSetter -- set -->  presta_fields.cache_has_attachments

     ProductFieldsClass  -- get --> IsVirtualProperty[ProductFields.is_virtual property]
      ProductFieldsClass -- set -->IsVirtualSetter [ProductFields.is_virtual setter]
          IsVirtualProperty -- get -->  presta_fields.is_virtual
            IsVirtualSetter -- set -->  presta_fields.is_virtual
    
     ProductFieldsClass  -- get -->CacheDefaultAttributeProperty [ProductFields.cache_default_attribute  property]
      ProductFieldsClass  -- set --> CacheDefaultAttributeSetter[ProductFields.cache_default_attribute setter]
         CacheDefaultAttributeProperty -- get -->  presta_fields.cache_default_attribute
             CacheDefaultAttributeSetter -- set -->  presta_fields.cache_default_attribute

     ProductFieldsClass  -- get --> DateAddProperty[ProductFields.date_add property]
     ProductFieldsClass  -- set -->DateAddSetter [ProductFields.date_add setter]
        DateAddProperty -- get -->  presta_fields.date_add
            DateAddSetter -- set -->  presta_fields.date_add

     ProductFieldsClass  -- get -->  DateUpdProperty[ProductFields.date_upd  property]
      ProductFieldsClass  -- set -->DateUpdSetter [ProductFields.date_upd setter]
         DateUpdProperty -- get -->  presta_fields.date_upd
            DateUpdSetter -- set -->  presta_fields.date_upd

    ProductFieldsClass -- get -->  AdvancedStockManagementProperty[ProductFields.advanced_stock_management  property]
     ProductFieldsClass  -- set -->AdvancedStockManagementSetter [ProductFields.advanced_stock_management setter]
         AdvancedStockManagementProperty -- get -->  presta_fields.advanced_stock_management
             AdvancedStockManagementSetter -- set -->  presta_fields.advanced_stock_management

    ProductFieldsClass -- get --> PackStockTypeProperty[ProductFields.pack_stock_type  property]
    ProductFieldsClass -- set -->  PackStockTypeSetter[ProductFields.pack_stock_type setter]
         PackStockTypeProperty -- get -->  presta_fields.pack_stock_type
            PackStockTypeSetter -- set -->  presta_fields.pack_stock_type

    ProductFieldsClass  -- get --> StateProperty[ProductFields.state property]
    ProductFieldsClass  -- set -->  StateSetter[ProductFields.state  setter]
           StateProperty -- get -->  presta_fields.state
                StateSetter -- set -->  presta_fields.state


     ProductFieldsClass  -- get -->   ProductTypeProperty[ProductFields.product_type  property]
    ProductFieldsClass  -- set -->ProductTypeSetter [ProductFields.product_type setter]
         ProductTypeProperty -- get -->  presta_fields.product_type
            ProductTypeSetter -- set -->  presta_fields.product_type
     ProductFieldsClass  -- get --> DescriptionProperty[ProductFields.description  property]
      ProductFieldsClass  -- set -->  DescriptionSetter[ProductFields.description  setter]
        DescriptionProperty -- get -->  presta_fields.description
           DescriptionSetter -- set -->  presta_fields.description
         
     ProductFieldsClass  -- get -->DescriptionShortProperty[ProductFields.description_short property]
      ProductFieldsClass  -- set --> DescriptionShortSetter [ProductFields.description_short setter]
          DescriptionShortProperty -- get -->  presta_fields.description_short
            DescriptionShortSetter -- set -->  presta_fields.description_short

    ProductFieldsClass  -- get -->   LinkRewriteProperty[ProductFields.link_rewrite property]
    ProductFieldsClass  -- set -->  LinkRewriteSetter[ProductFields.link_rewrite setter]
        LinkRewriteProperty -- get -->  presta_fields.link_rewrite
           LinkRewriteSetter -- set -->  presta_fields.link_rewrite

    ProductFieldsClass  -- get -->MetaDescriptionProperty[ProductFields.meta_description property]
    ProductFieldsClass  -- set -->  MetaDescriptionSetter[ProductFields.meta_description setter]
        MetaDescriptionProperty -- get -->  presta_fields.meta_description
            MetaDescriptionSetter -- set -->  presta_fields.meta_description
    
     ProductFieldsClass  -- get -->  MetaKeywordsProperty[ProductFields.meta_keywords  property]
     ProductFieldsClass  -- set --> MetaKeywordsSetter[ProductFields.meta_keywords setter]
          MetaKeywordsProperty -- get -->  presta_fields.meta_keywords
            MetaKeywordsSetter -- set -->  presta_fields.meta_keywords

     ProductFieldsClass  -- get -->  MetaTitleProperty[ProductFields.meta_title  property]
      ProductFieldsClass -- set -->MetaTitleSetter[ProductFields.meta_title setter]
         MetaTitleProperty -- get -->  presta_fields.meta_title
             MetaTitleSetter -- set -->  presta_fields.meta_title

    ProductFieldsClass -- get -->   NameProperty[ProductFields.name property]
     ProductFieldsClass  -- set -->  NameSetter[ProductFields.name setter]
          NameProperty -- get -->  presta_fields.name
            NameSetter -- set -->  presta_fields.name

     ProductFieldsClass  -- get -->  AvailableNowProperty[ProductFields.available_now  property]
     ProductFieldsClass -- set --> AvailableNowSetter [ProductFields.available_now setter]
           AvailableNowProperty -- get -->  presta_fields.available_now
            AvailableNowSetter -- set -->  presta_fields.available_now

    ProductFieldsClass -- get -->   AvailableLaterProperty[ProductFields.available_later property]
     ProductFieldsClass  -- set --> AvailableLaterSetter[ProductFields.available_later setter]
        AvailableLaterProperty -- get -->  presta_fields.available_later
            AvailableLaterSetter -- set -->  presta_fields.available_later
    
    ProductFieldsClass -- get --> DeliveryInStockProperty[ProductFields.delivery_in_stock property]
    ProductFieldsClass -- set -->   DeliveryInStockSetter[ProductFields.delivery_in_stock setter]
         DeliveryInStockProperty -- get -->  presta_fields.delivery_in_stock
            DeliveryInStockSetter -- set -->  presta_fields.delivery_in_stock
    
    ProductFieldsClass -- get --> DeliveryOutStockProperty[ProductFields.delivery_out_stock  property]
     ProductFieldsClass -- set --> DeliveryOutStockSetter[ProductFields.delivery_out_stock setter]
          DeliveryOutStockProperty -- get -->  presta_fields.delivery_out_stock
               DeliveryOutStockSetter -- set -->  presta_fields.delivery_out_stock


     ProductFieldsClass  -- get -->  DeliveryAdditionalMessageProperty[ProductFields.delivery_additional_message  property]
    ProductFieldsClass  -- set --> DeliveryAdditionalMessageSetter[ProductFields.delivery_additional_message setter]
          DeliveryAdditionalMessageProperty -- get -->  presta_fields.delivery_additional_message
               DeliveryAdditionalMessageSetter -- set -->  presta_fields.delivery_additional_message

     ProductFieldsClass  -- get -->  AffiliateShortLinkProperty[ProductFields.affiliate_short_link  property]
    ProductFieldsClass -- set --> AffiliateShortLinkSetter [ProductFields.affiliate_short_link setter]
          AffiliateShortLinkProperty -- get -->  presta_fields.affiliate_short_link
                AffiliateShortLinkSetter -- set -->  presta_fields.affiliate_short_link

    ProductFieldsClass -- get -->  AffiliateTextProperty[ProductFields.affiliate_text property]
    ProductFieldsClass -- set -->   AffiliateTextSetter[ProductFields.affiliate_text setter]
          AffiliateTextProperty -- get -->  presta_fields.affiliate_text
                AffiliateTextSetter -- set -->  presta_fields.affiliate_text

    ProductFieldsClass -- get --> AffiliateSummaryProperty[ProductFields.affiliate_summary property]
     ProductFieldsClass  -- set --> AffiliateSummarySetter[ProductFields.affiliate_summary  setter]
          AffiliateSummaryProperty -- get -->  presta_fields.affiliate_summary
               AffiliateSummarySetter -- set -->  presta_fields.affiliate_summary


    ProductFieldsClass -- get --> AffiliateSummary2Property[ProductFields.affiliate_summary_2  property]
      ProductFieldsClass -- set -->   AffiliateSummary2Setter[ProductFields.affiliate_summary_2 setter]
          AffiliateSummary2Property -- get -->  presta_fields.affiliate_summary_2
             AffiliateSummary2Setter -- set -->  presta_fields.affiliate_summary_2

    ProductFieldsClass -- get --> AffiliateImageSmallProperty[ProductFields.affiliate_image_small  property]
     ProductFieldsClass -- set -->  AffiliateImageSmallSetter[ProductFields.affiliate_image_small setter]
           AffiliateImageSmallProperty -- get -->  presta_fields.affiliate_image_small
              AffiliateImageSmallSetter -- set -->  presta_fields.affiliate_image_small

    ProductFieldsClass -- get --> AffiliateImageMediumProperty[ProductFields.affiliate_image_medium property]
      ProductFieldsClass  -- set --> AffiliateImageMediumSetter[ProductFields.affiliate_image_medium setter]
          AffiliateImageMediumProperty -- get -->  presta_fields.affiliate_image_medium
              AffiliateImageMediumSetter -- set -->  presta_fields.affiliate_image_medium


    ProductFieldsClass -- get -->  AffiliateImageLargeProperty[ProductFields.affiliate_image_large property]
     ProductFieldsClass -- set -->  AffiliateImageLargeSetter[ProductFields.affiliate_image_large setter]
         AffiliateImageLargeProperty -- get -->  presta_fields.affiliate_image_large
             AffiliateImageLargeSetter -- set -->  presta_fields.affiliate_image_large
    
     ProductFieldsClass