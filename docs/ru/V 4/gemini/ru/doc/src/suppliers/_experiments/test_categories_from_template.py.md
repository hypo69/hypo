# Модуль test_categories_from_template

## Обзор

Модуль `test_categories_from_template` содержит тесты для функции `buid_templates`, которая, по-видимому, предназначена для построения шаблонов категорий из JSON-файлов, расположенных в указанной директории. Тесты проверяют как успешное создание шаблонов из существующей директории, так и обработку ситуации, когда директория не существует.
Модуль использует библиотеку `unittest` для организации тестов, `tempfile` для создания временных директорий и `os` для работы с файловой системой.

## Подробней

Этот модуль предназначен для тестирования функциональности, связанной с созданием шаблонов категорий на основе JSON-файлов. 
Он включает в себя тесты, которые проверяют правильность обработки JSON-файлов из директорий, а также корректную обработку ошибок при отсутствии директории.
Модуль использует временные директории для изоляции тестов и обеспечивает надежную проверку функциональности `buid_templates`.

## Классы

### `TestBuildtemplates`

**Описание**: Класс, содержащий тестовые методы для проверки функции `buid_templates`.

**Методы**:
- `test_build_templates_with_existing_directory`: Проверяет создание шаблонов из существующей директории с JSON-файлами.
- `test_build_templates_with_non_existing_directory`: Проверяет возникновение исключения `FileNotFoundError` при попытке создания шаблонов из несуществующей директории.

#### `test_build_templates_with_existing_directory`

**Описание**: Проверяет создание шаблонов категорий из существующей директории, содержащей JSON-файлы.

**Параметры**:
- Нет.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- Нет.

**Примеры**:
```python
    def test_build_templates_with_existing_directory(self):
        # Create a temporary directory and add some JSON files
        with tempfile.TemporaryDirectory() as tmpdir:
            json_data = '{"category1": {"template1": "some content"}, "category2": {"template2": "some content"}}'
            file1_path = os.path.join(tmpdir, 'file1.json')
            with open(file1_path, 'w') as f:
                f.write(json_data)
            file2_path = os.path.join(tmpdir, 'subdir', 'file2.json')
            os.makedirs(os.path.dirname(file2_path))
            with open(file2_path, 'w') as f:
                f.write(json_data)

            # Call the function and check the output
            expected_output = {"category1": {
                "template1": "some content"}, "category2": {"template2": "some content"}}
            self.assertEqual(buid_templates(tmpdir), expected_output)
```

#### `test_build_templates_with_non_existing_directory`

**Описание**: Проверяет, что при попытке создать шаблоны категорий из несуществующей директории возникает исключение `FileNotFoundError`.

**Параметры**:
- Нет.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- `FileNotFoundError`: Если директория не существует.

**Примеры**:
```python
    def test_build_templates_with_non_existing_directory(self):
        # Call the function with a non-existing directory and check that it raises an exception
        with self.assertRaises(FileNotFoundError):
            buid_templates('/non/existing/path/')
```