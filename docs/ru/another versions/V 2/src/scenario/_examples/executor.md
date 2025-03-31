# Примеры использования модуля `executor`

## Обзор

Этот файл содержит примеры использования функций, представленных в модуле `executor`. Примеры демонстрируют, как запускать сценарии, обрабатывать файлы сценариев и взаимодействовать с PrestaShop API.

## Содержание

- [Обзор](#обзор)
- [Примеры](#примеры)
    - [Пример 1: `run_scenario_files`](#пример-1-run_scenario_files)
    - [Пример 2: `run_scenario_file`](#пример-2-run_scenario_file)
    - [Пример 3: `run_scenario`](#пример-3-run_scenario)
    - [Пример 4: `insert_grabbed_data`](#пример-4-insert_grabbed_data)
    - [Пример 5: `add_coupon`](#пример-5-add_coupon)
    - [Пример 6: `execute_PrestaShop_insert_async`](#пример-6-execute_prestashop_insert_async)
    - [Пример 7: `execute_PrestaShop_insert`](#пример-7-execute_prestashop_insert)
- [Пояснение к примерам](#пояснение-к-примерам)

## Примеры

### Пример 1: `run_scenario_files`

```python
def example_run_scenario_files():
    supplier = MockSupplier()
    scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
    result = run_scenario_files(supplier, scenario_files)
    if result:
        print("All scenarios executed successfully.")
    else:
        print("Some scenarios failed.")
```

### Пример 2: `run_scenario_file`

```python
def example_run_scenario_file():
    supplier = MockSupplier()
    scenario_file = Path('scenarios/scenario1.json')
    result = run_scenario_file(supplier, scenario_file)
    if result:
        print("Scenario file executed successfully.")
    else:
        print("Failed to execute scenario file.")
```

### Пример 3: `run_scenario`

```python
def example_run_scenario():
    supplier = MockSupplier()
    scenario = {
        'url': 'http://example.com/category',
        'products': [{'url': 'http://example.com/product1'}, {'url': 'http://example.com/product2'}]
    }
    result = run_scenario(supplier, scenario)
    if result:
        print("Scenario executed successfully.")
    else:
        print("Failed to execute the scenario.")
```

### Пример 4: `insert_grabbed_data`

```python
def example_insert_grabbed_data():
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    insert_grabbed_data(product_fields)
    print("Product data inserted into PrestaShop.")
```

### Пример 5: `add_coupon`

```python
def example_add_coupon():
    credentials = {'api_domain': 'https://example.com/api', 'api_key': 'YOUR_API_KEY'}
    reference = 'REF123'
    coupon_code = 'SUMMER2024'
    start_date = '2024-07-01'
    end_date = '2024-07-31'
    add_coupon(credentials, reference, coupon_code, start_date, end_date)
    print("Coupon added successfully.")
```

### Пример 6: `execute_PrestaShop_insert_async`

```python
async def example_execute_PrestaShop_insert_async():
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    await execute_PrestaShop_insert_async(product_fields)
    print("Product data inserted into PrestaShop asynchronously.")
```

### Пример 7: `execute_PrestaShop_insert`

```python
def example_execute_PrestaShop_insert():
    product_fields = ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )
    result = execute_PrestaShop_insert(product_fields)
    if result:
        print("Product data inserted into PrestaShop.")
    else:
        print("Failed to insert product data into PrestaShop.")
```

## Пояснение к примерам

1.  **Example 1: `run_scenario_files`**  
    Запускает список файлов сценариев и выполняет их один за другим.

2.  **Example 2: `run_scenario_file`**  
    Запускает один файл сценария.

3.  **Example 3: `run_scenario`**  
    Выполняет один сценарий.

4.  **Example 4: `insert_grabbed_data`**  
    Вставляет данные о продукте в PrestaShop.

5.  **Example 5: `add_coupon`**  
    Добавляет купон в базу данных PrestaShop.

6.  **Example 6: `execute_PrestaShop_insert_async`**  
    Асинхронно выполняет вставку данных о продукте в PrestaShop.

7.  **Example 7: `execute_PrestaShop_insert`**  
    Синхронно выполняет вставку данных о продукте в PrestaShop.

Эти примеры помогут вам понять, как можно использовать функции модуля `executor` для различных задач в вашем проекте.