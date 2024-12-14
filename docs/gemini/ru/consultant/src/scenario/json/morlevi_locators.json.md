# Анализ кода модуля morlevi_locators.json

**Качество кода**
6
- Плюсы
    - Код представляет собой JSON-файл, что соответствует формату хранения данных.
    - Присутствуют комментарии к некоторым полям.
    - Код структурирован и разделен на логические блоки (pagination, store, product и т.д.).
- Минусы
    -  Отсутствует описание назначения файла (модуля).
    -  Некоторые значения `attribute` имеют значение `null`, что может быть нежелательным.
    -  В `selector` присутствуют нечитаемые символы, которые затрудняют понимание (например, `text*=\'éöøï\'`, `text*=\'âåãì îñê\'`).
    -  Присутствуют множественные повторения ключей `"logic for attribue[AND|OR|XOR|VALUE|null]"` и `"logic for action[AND|OR|XOR|VALUE|null]"` со значением `null`, которые можно оптимизировать.
    -  Много повторяющихся значений `"timeout":0,"timeout_for_event":"presence_of_element_located"`.

**Рекомендации по улучшению**

1. **Добавить описание модуля:**
   - Добавить в начало файла reStructuredText описание назначения этого файла и его структуры.
2. **Удалить или прокомментировать неиспользуемые ключи:**
   - Убрать повторяющиеся ключи `"logic for attribue[AND|OR|XOR|VALUE|null]"` и `"logic for action[AND|OR|XOR|VALUE|null]"` со значением `null` или вынести их в общую часть для переиспользования.
3. **Заменить нечитаемые символы:**
   - Заменить нечитаемые символы в `selector` на более понятные или использовать корректные значения.
4. **Оптимизировать структуру:**
   - Вынести повторяющиеся значения ` "timeout":0,"timeout_for_event":"presence_of_element_located"` в общую секцию или добавить константы
5. **Привести к общему виду:**
   -  Все ключи `selector`  должны быть строковыми значениями.

**Оптимизированный код**
```json
{
  "description": "Конфигурационный файл с локаторами для парсинга сайта morlevi.co.il.\n=========================================================================\n\nСодержит настройки для пагинации, элементов магазина, товаров и полей товаров.\n\nПример использования:\n--------------------\n\n.. code-block:: json\n\n   {\n     \"pagination\": {\n        \"ul\": {\n           \"by\": \"XPATH\",\n           \"selector\": \"//ul[@class='pagination']\",\n           \"timeout\":0,\"timeout_for_event\":\"presence_of_element_located\",\n           \"event\": \"click()\"\n         },\n        \"a\": {\n          \"by\": \"XPATH\",\n          \"selector\": \"//ul[@class='pagination']//a[@class='page-link']\",\n          \"timeout\":0,\"timeout_for_event\":\"presence_of_element_located\",\n           \"event\": \"click()\"\n         }\n      },\n      ...\n   }\n",
  "infinity_scroll": false,
  "checkboxes_for_categories": false,
  "default_timeout": {
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located"
  },
  "pagination": {
    "ul": {
      "by": "XPATH",
      "selector": "//ul[@class='pagination']",
       "event": "click()",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "a": {
      "by": "XPATH",
      "selector": "//ul[@class='pagination']//a[@class='page-link']",
       "event": "click()",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    }
  },
  "close_pop_up_locator": {
    "by": "XPATH",
    "selector": "//div[@class='modal-dialog']//button[@class='close']",
    "event": "click()",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
  },
  "store": {
    "store categories": {
      "description": "Список катагероий магазина",
       "attribute": {
         "innerText": "href"
       },
      "by": "XPATH",
      "selector": "//li[@class='group-item']//a",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    }
  },
  "product": {
    "link_to_product_locator": {
       "attribute": "href",
      "by": "XPATH",
      "selector": "//div[@class = 'product-thumb']/a",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "stock available": {
      "attribute": "innerText",
      "by": "XPATH",
      "selector": "//div[contains(@class , 'stockMsg')]",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "product_name_locator": {
       "attribute": "innerHTML",
      "by": "css selector",
      "selector": "h1.d-inline-block",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "summary_locator": {
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": "h1.d-inline-block",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "description_locator": {
       "attribute": "innerHTML",
      "by": "css selector",
      "selector": ".row.product-params.pt-2.pb-2.pt-sm-5.pb-sm-5",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "price_locator": {
       "attribute": "innerHTML",
      "by": "ID",
      "selector": "basicPrice",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "brand_locator": {
        "attribute": "innerHTML",
      "by": "css selector",
      "selector": "text*='éöøï'",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "sku_locator": {
      "attribute": "innerText",
      "by": "XPATH",
      "selector": "//div[contains(@class,'main-details')]//span[contains(@class,'sku-copy')]",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "brand_sku_locator": {
      "attribute": "innerHTML",
      "by": "css selector",
      "selector": "span.sku-copy",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "main_image_locator": {
        "attribute": "href",
      "by": "ID",
      "selector": "mainpic",
       "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "li_locator": {
       "attribute": "innerHTML",
      "by": "tag name",
      "selector": "li",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    }
  },
  "product_fields_locators": {},
  "laptop_description_fields_selectors": {
    "screen": {
        "attribute": "innerHTML",
      "by": "css selector",
      "selector": "text*='âåãì îñê'",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "CPUTYPE": {
        "attribute": "innerHTML",
      "by": "css selector",
      "selector": "text*='CPUTYPE'",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "cpu": {
        "attribute": "innerHTML",
      "by": "css selector",
      "selector": "text='îòáã'",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    }
  },
  "stock_locator": {
      "attribute": "innerHTML",
    "by": "css selector",
    "selector": ".stockMsg",
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located"
  },
  "login": {
    "open_login_dialog_locator": {
      "by": "XPATH",
      "selector": "//a[contains(@data-modal,'User')]",
      "event": "click()",
       "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "email": "sales@aluf.co.il",
    "email_locator": {
      "by": "ID",
      "selector": "Email",
       "event": "send_keys('sales@aluf.co.il')",
       "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "password": "9643766",
    "password_locator": {
      "by": "ID",
      "selector": "Password",
        "event": "send_keys('9643766')",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    },
    "loginbutton_locator": {
      "by": "css selector",
      "selector": ".btn.btn-primary.btn-lg.w-50.float-left.mr-2",
      "event": "click()",
        "timeout": 0,
      "timeout_for_event": "presence_of_element_located"
    }
  }
}