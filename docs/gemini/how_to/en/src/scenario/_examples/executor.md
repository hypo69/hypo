# Руководство по использованию модуля `executor`

Этот документ предоставляет руководство по использованию модуля `executor` из пакета `src.scenario.executor`, демонстрируя различные способы его применения для управления сценариями, обработки файлов сценариев, работы с продуктами и взаимодействия с API PrestaShop.

**Модуль `executor`** отвечает за выполнение сценариев, связанных с работой с продуктами и управлением данными в системе PrestaShop.

## Структура примеров

Файл содержит примеры использования различных функций модуля `executor`, которые иллюстрируют, как:

* Запускать списки файлов сценариев (`run_scenario_files`);
* Запускать отдельные файлы сценариев (`run_scenario_file`);
* Выполнять отдельные сценарии (`run_scenario`);
* Обрабатывать и вставлять данные о продуктах в PrestaShop (`insert_grabbed_data`, `execute_PrestaShop_insert`, `execute_PrestaShop_insert_async`);
* Добавлять купоны через API PrestaShop (`add_coupon`).


## Примеры

**Пример 1: Запуск списка файлов сценариев (`run_scenario_files`)**

```python
def example_run_scenario_files():
    supplier = MockSupplier()
    scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
    result = run_scenario_files(supplier, scenario_files)
    if result:
        print("Все сценарии выполнены успешно.")
    else:
        print("Некоторые сценарии не были выполнены.")
```

Этот пример демонстрирует, как запустить несколько файлов сценариев, передавая список путей к ним и экземпляр класса `MockSupplier`. `MockSupplier` — это заглушка для реального класса, представляющего поставщика сценариев.  **Важно заменить** `MockSupplier` на ваш собственный класс поставщика.

**Пример 2: Запуск одного файла сценария (`run_scenario_file`)**

```python
def example_run_scenario_file():
    supplier = MockSupplier()
    scenario_file = Path('scenarios/scenario1.json')
    result = run_scenario_file(supplier, scenario_file)
    if result:
        print("Файл сценария выполнен успешно.")
    else:
        print("Не удалось выполнить файл сценария.")
```
Аналогично предыдущему, но запускает только один файл.

**Пример 3: Запуск одного сценария (`run_scenario`)**

```python
def example_run_scenario():
    # ... (ваш код) ...
    result = run_scenario(supplier, scenario)
    # ... (обработка результата) ...
```
Этот пример показывает как выполнить конкретный сценарий, представленный в виде словаря.  Не забудьте правильно заполнить `scenario`!

**Пример 4: Вставка данных о продукте в PrestaShop (`insert_grabbed_data`)**

```python
def example_insert_grabbed_data():
    product_fields = ProductFields(...)  # Заполните данные о продукте!
    insert_grabbed_data(product_fields)
    print("Данные о продукте вставлены в PrestaShop.")
```
Этот пример демонстрирует использование функции `insert_grabbed_data`, которая ожидает `ProductFields` объект, содержащий данные продукта. **Убедитесь, что вы правильно создаёте и заполняете`ProductFields`.**

**Пример 5: Добавление купона в PrestaShop (`add_coupon`)**

```python
def example_add_coupon():
    credentials = {'api_domain': '...', 'api_key': '...'} # Замените на ваши данные
    # ...
    add_coupon(credentials, reference, coupon_code, start_date, end_date)
```

Важным моментом является правильное предоставление параметров `credentials` и других необходимых данных, соответствующих вашим настройкам PrestaShop API.

**Важно:**

* Замените все placeholder'ы (например, пути к файлам, данные API) на ваши реальные значения.
* Проверьте корректность данных, передаваемых в функции.
* Обработайте результаты функций, чтобы получить информацию о статусе выполнения.
* Убедитесь, что у вас установлены необходимые пакеты Python (`src.utils`, `src.product`, `src.endpoints.PrestaShop`).

Этот документ предоставляет базовые примеры. Для более сложных сценариев и задач вам нужно будет адаптировать эти примеры к вашим потребностям.  Пожалуйста, предоставьте больше контекста, если вам нужна более конкретная помощь с определёнными сценариями или функциями.