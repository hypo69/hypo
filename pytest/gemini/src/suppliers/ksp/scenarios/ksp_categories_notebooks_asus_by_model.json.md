```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def laptop_data():
    """Provides the laptop data from the JSON file."""
    json_data = """
    {
      "scenarios": {
        "Asus Laptop E210 Intel Celeron": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..16177",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2288": "Asus Laptop E210",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4126": "screen 11 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4132": "Intel Celeron",
            "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop E410": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..14699",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2289": "Asus Laptop E410",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4128": "screen 14 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4132": "Intel Celeron",
            "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop E510": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..22586",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2290": "Asus Laptop E510",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4129": "screen 15 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4132": "Intel Celeron",
            "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop X415 Intel Celeron": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..19412..406",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2291": "X415 Intel Celeron",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4128": "screen 14 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4132": "Intel Celeron",
            "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop X415 Core i3-U": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..19412..2179",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2291": "X415 Core i3-U",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4128": "screen 14 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
             "4132": "Intel Celeron",
            "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop X415 Core i3-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..19412..9718",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2291": "Asus Laptop X415 Core i3-G",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4128": "screen 14 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4135": "Core i3",
            "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop X415 Core i5-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..19412..5394",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2291": "Asus Laptop X415 Core i5-G",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4128": "screen 14 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4138": "Core i5",
            "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop X415 Core i7-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..19412..5315",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2291": "X415 Core i7-G",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4128": "screen 14 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4143": "Core i7",
             "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop X515 Intel Celeron": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..22537..406",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2292": "X515 Intel Celeron",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4129": "screen 15 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4132": "Intel Celeron",
             "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop X515 Core i3-U": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..22537..2179",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2292": "X515 Core i3-U",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4129": "screen 15 inch",
            "4148": "Laptops by cpu",
             "9720": "Laptops Intel cpu",
            "4165": "Core i3",
            "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop X515 Core i3-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..22537..9718",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2292": "X515 Core i3-G",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4129": "screen 15 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4165": "Core i3",
            "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop X515 Core i5-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..22537..9718",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2292": "X515 Core i5-G",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4129": "screen 15 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4138": "Core i5",
            "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop X515 Core i7-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..22537..5315",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2292": "X515 Core i7-G",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4129": "screen 15 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4143": "Core i7",
            "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop M509 AMD A6": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..16177..19412..22537",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2293": "M509 AMD A6",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4129": "screen 15 inch",
            "4148": "Laptops by cpu",
            "4150": "Laptops AMD CPU",
            "4154": "AMD A6",
            "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus Laptop M515 Ryzen 3": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..21237..4449",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "2294": "M515 Ryzen 3",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4129": "screen 15 inch",
            "4148": "Laptops by cpu",
            "4150": "Laptops AMD CPU",
            "4155": "Ryzen 3",
            "2258": "ASUS",
            "2287": "Laptops",
             "4166": "Asus Laptop"
          }
        },
        "Asus Laptop M515 Ryzen 5": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..21237..4039",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": {
            "2294": "M515 Ryzen 5",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4129": "screen 15 inch",
            "4148": "Laptops by cpu",
             "4150": "Laptops AMD CPU",
            "4156": "Ryzen 5",
            "2258": "ASUS",
            "2287": "Laptops",
            "4166": "Asus Laptop"
          }
        },
        "Asus VivoBook 13 Slate T3300 Intel Pentium-N ": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..32457..2184",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": {
            "2295": "13 Slate T3300 Intel Pentium-N",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4127": "screen 13 inch",
            "4148": "Laptops by cpu",
             "9720": "Laptops Intel cpu",
            "4133": "Intel Pentium",
             "2258": "ASUS",
            "2287": "Laptops",
            "4165": "Asus VivoBook"
          }
        },
        "Asus Vivobook Go 14 Flip TP1401 Pentium-N": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..35129..2184",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": {
            "4064": "Asus Vivobook Go 14 Flip TP1401 Pentium-N",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
             "4125": "Laptops by screen size",
            "4127": "screen 13 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4133": "Intel Pentium",
            "2258": "ASUS",
            "2287": "Laptops",
            "4165": "Asus VivoBook"
          }
        },
        "Asus VivoBook Flip 14 TM420 Ryzen 7": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..19149..3955",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": {
            "4065": "Asus VivoBook Flip 14 TM420 Ryzen 7",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
             "4125": "Laptops by screen size",
            "4128": "screen 14 inch",
            "4148": "Laptops by cpu",
             "4150": "Laptops AMD CPU",
            "4157": "Ryzen 7",
            "2258": "ASUS",
            "2287": "Laptops",
            "4165": "Asus VivoBook"
          }
        },
        "Asus VivoBook Flip 14 TP470 Core i5-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..33557..5394",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "4066": "Asus VivoBook Flip 14 TP470 Core i5-G",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4128": "screen 14 inch",
            "9720": "Laptops Intel cpu",
            "4133": "Core i5",
             "2258": "ASUS",
            "2287": "Laptops",
            "4165": "Asus VivoBook"
          }
        },
        "Asus VivoBook 14 X413 / K413 Core i5-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..13987..5394",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": {
            "4067": "Asus VivoBook 14 X413 / K413 Core i5-G",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
             "4125": "Laptops by screen size",
            "4128": "screen 14 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4133": "Core i5",
            "2258": "ASUS",
            "2287": "Laptops",
            "4165": "Asus VivoBook"
          }
        },
        "Asus VivoBook 14 X413 / K413 Core i7-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..13987..5315",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": {
            "4067": "Asus VivoBook 14 X413 / K413 Core i7-G",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
             "4125": "Laptops by screen size",
            "4128": "screen 14 inch",
             "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4143": "Core i7",
             "2258": "ASUS",
            "2287": "Laptops",
             "4165": "Asus VivoBook"
          }
        },
        "Asus VivoBook 15 X512 Core i5 - U": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..7653..2183",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": {
            "4068": "Asus VivoBook 15 X512 Core i5 - U",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
            "4129": "screen 15 inch",
             "4148": "Laptops by cpu",
             "9720": "Laptops Intel cpu",
             "4133": "Core i5",
             "2258": "ASUS",
            "2287": "Laptops",
             "4165": "Asus VivoBook"
          }
        },
        "Asus VivoBook 15 X513 / K513 Core i5-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..23221..5394",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": {
            "4069": "Asus VivoBook 15 X513 / K513 Core i5-G",
            "3198": "CONSUMER ELECTRONICS",
            "3202": "computer,smartphone,gaming console,smart device",
            "3225": "Laptops",
            "4125": "Laptops by screen size",
             "4129": "screen 15 inch",
            "4148": "Laptops by cpu",
            "9720": "Laptops Intel cpu",
            "4133": "Core i5",
             "2258": "ASUS",
            "2287": "Laptops",
             "4165": "Asus VivoBook"
          }
        },
        "Asus VivoBook 15 X513 / K513 Core i7-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..5315..23221",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I7", "15" ]
            }
          }
        },
        "Asus VivoBook S14 S433 Core i5-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..13965..5394",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I5", "14" ]
            }
          }
        },
        "Asus VivoBook 14 X1400 Core i3-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..39833..9718",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I3", "14" ]
            }
          }
        },
        "Asus VivoBook 14 X1400 Core i5-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..39833..5394",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I5", "14" ]
            }
          }
        },
        "Asus VivoBook 14 X1400 Core i7-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..39833..5315",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I7", "14" ]
            }
          }
        },
        "Asus VivoBook 14 X1402 Core i3-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..40125..9718",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I3", "14" ]
            }
          }
        },
        "Asus VivoBook 14 X1402 Core i5-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..40125..5394",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I5", "14" ]
            }
          }
        },
        "Asus VivoBook 14 X1402 Core i7-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..40125..5315",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I7", "14" ]
            }
          }
        },
        "Asus VivoBook 15 X1500 Core i3-G": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..40125..9718",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I3", "15" ]
            }
          }
        },
        "Asus Vivobook S 14 OLED K3402 Core i7 - H": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..38716..5274",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I7", "14" ]
            }
          }
        },
         "Asus Vivobook S 15 OLED K3502  Core i7 - H": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..40142..5274",
          "checkbox": false,
          "active": true,
          "condition": "new",
          "presta_categories": {
            "template": {
              "asus": [ "LAPTOPS INTEL I7", "15" ]
            }
          }
        },
         "Asus Vivobook S 14X OLED S5402 Core i7 - H": {
          "brand": "ASUS",
          "url": "https://ksp.co.il/web/cat/271..1358..38616..5274",
          "checkbox