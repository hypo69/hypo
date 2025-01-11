# Анализ кода модуля `morlevi_locators.json`

**Качество кода**
    
    8
    -  Плюсы
        - Код представляет собой JSON-файл, который содержит структуру локаторов для веб-элементов.
        - Локаторы сгруппированы по функциональным блокам (`pagination`, `store`, `product`, `login`), что облегчает их понимание и использование.
        - Присутствуют описания для некоторых локаторов, например, "Список катагероий магазина".
        - Указаны стратегии поиска элементов (`by`: `XPATH`, `css selector`, `ID`, `tag name`).
        - Указаны атрибуты для поиска и извлечения данных.
        - Есть параметры `timeout` и `timeout_for_event`.
    -  Минусы
        - Не все локаторы имеют описание, что затрудняет понимание их назначения.
        - Значения `"logic for attribue[AND|OR|XOR|VALUE|null]":null` и `"logic for action[AND|OR|XOR|VALUE|null]":null` являются избыточными и не несут смысловой нагрузки.
        - В некоторых локаторах используется `text*=`, что может привести к нестабильности при изменении текста на странице.
        - Присутствуют захардкоженные данные для логина (email и password).
        - В некоторых селекторах (`selector`) присутствуют кириллические символы, что может вызвать проблемы при работе с различными кодировками.
        - Некоторые селекторы (`selector`) используют `contains`, что может замедлить поиск и сделать его менее точным.

**Рекомендации по улучшению**

1.  **Удалить избыточные ключи**: Убрать `"logic for attribue[AND|OR|XOR|VALUE|null]"` и `"logic for action[AND|OR|XOR|VALUE|null]"` как не несущие смысловой нагрузки.
2.  **Добавить описания**:  Добавить описания к каждому локатору, чтобы было понятно, какой элемент он находит.
3.  **Переработать локаторы с `text*=`**: Избегать использования `text*=` в селекторах. Лучше использовать более точные методы поиска, такие как `XPATH` с конкретным текстом или комбинации классов.
4.  **Вынести данные для логина**: Захардкоженные данные для логина (email и password) следует вынести в конфигурационный файл или переменные окружения.
5.  **Унифицировать селекторы**: Привести селекторы к единому виду (например, использовать только `XPATH` или только `css selector`).
6.  **Уточнить селекторы**: Уточнить селекторы, использующие `contains`, чтобы сделать поиск более точным и стабильным.
7.  **Удалить лишние timeout**: По возможности вынести `timeout` в константы и использоввать их
8. **Убрать дубликаты**: Убрать дубликаты в `product` полях `product_name_locator` и `summary_locator`

**Оптимизированный код**

```json
{
  "infinity_scroll": false,
  "checkboxes_for_categories": false,
  "pagination": {
    "ul": {
      "attribute": null,
      "by": "XPATH",
      "selector": "//ul[@class='pagination']",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": "click()"
    },
    "a": {
      "attribute": null,
      "by": "XPATH",
      "selector": "//ul[@class='pagination']//a[@class='page-link']",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": "click()"
    }
  },
  "close_pop_up_locator": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//div[@class='modal-dialog']//button[@class='close']",
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located",
    "event": "click()"
  },
  "store": {
    "store categories": {
      "description": "Список категорий магазина",
      "attribute": {
        "innerText": "href"
      },
      "by": "XPATH",
      "selector": "//li[@class='group-item']//a",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    }
  },
  "product": {
    "link_to_product_locator": {
      "attribute": "href",
      "by": "XPATH",
      "selector": "//div[@class = 'product-thumb']/a",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    },
    "stock available": {
       "attribute": "innerText",
      "by": "XPATH",
      "selector": "//div[contains(@class, 'stockMsg')]",
       "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    },
    "product_name_locator": {
      "description": "Локатор для имени продукта",
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": "h1.d-inline-block",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    },
    "description_locator": {
      "description": "Локатор для описания продукта",
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": ".row.product-params.pt-2.pb-2.pt-sm-5.pb-sm-5",
       "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    },
    "price_locator": {
      "description": "Локатор для цены продукта",
      "attribute": "innerHTML",
      "by": "ID",
      "selector": "basicPrice",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    },
     "brand_locator": {
      "description": "Локатор для бренда продукта",
      "attribute": "innerHTML",
      "by": "css selector",
        "selector": "[text*='éöøï']",
       "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    },
    "sku_locator": {
       "description": "Локатор для артикула продукта",
      "attribute": "innerText",
      "by": "XPATH",
      "selector": "//div[contains(@class,'main-details')]//span[contains(@class,'sku-copy')]",
        "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    },
     "brand_sku_locator": {
       "description": "Локатор для бренда артикула",
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": "span.sku-copy",
        "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    },
    "main_image_locator": {
       "description": "Локатор для основного изображения продукта",
      "attribute": "href",
      "by": "ID",
      "selector": "mainpic",
        "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    },
    "li_locator": {
      "description": "Локатор для li",
      "attribute": "innerHTML",
      "by": "tag name",
      "selector": "li",
        "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    }
  },
  "product_fields_locators": {},
  "laptop_description_fields_selectors": {
     "screen": {
      "description": "Локатор для экрана ноутбука",
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": "[text*='âåãì îñê']",
        "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    },
    "CPUTYPE": {
       "description": "Локатор для типа CPU ноутбука",
      "attribute": "innerHTML",
      "by": "css selector",
       "selector": "[text*='CPUTYPE']",
        "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    },
    "cpu": {
      "description": "Локатор для CPU ноутбука",
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": "[text='îòáã']",
        "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": null
    }
  },
  "stock_locator": {
     "description": "Локатор для статуса наличия товара",
    "attribute": "innerHTML",
    "by": "css selector",
    "selector": ".stockMsg",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
    "event": null
  },
  "login": {
    "open_login_dialog_locator": {
      "description": "Локатор для открытия диалога логина",
      "attribute": null,
      "by": "XPATH",
      "selector": "//a[contains(@data-modal,'User')]",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": "click()"
    },
    "email": "sales@aluf.co.il",
    "email_locator": {
       "description": "Локатор для поля ввода email",
      "attribute": null,
      "by": "ID",
      "selector": "Email",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": "send_keys('sales@aluf.co.il')"
    },
    "password": "9643766",
    "password_locator": {
       "description": "Локатор для поля ввода пароля",
      "attribute": null,
      "by": "ID",
      "selector": "Password",
       "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": "send_keys('9643766')"
    },
    "loginbutton_locator": {
      "description": "Локатор для кнопки логина",
      "attribute": null,
      "by": "css selector",
      "selector": ".btn.btn-primary.btn-lg.w-50.float-left.mr-2",
        "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": "click()"
    }
  }
}