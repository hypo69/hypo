# Инструкция по обработке команд для модели

## Обзор

Данная инструкция описывает формат команд для модели, предназначенной для анализа компьютерных компонентов из JSON, классификации типа сборки (например, игровой, рабочая станция), предоставления названий и описаний на иврите и русском, перевода деталей компонентов и возвращения структурированного JSON-выхода.

## Команда

### `Analyze computer components from JSON, classify build type (e.g., gaming, workstation), provide titles and descriptions in Hebrew and Russian, translate component details, and return structured JSON output. Maintain correct formatting, include confidence scores, and follow detailed guidelines for descriptions and component handling.`

## Шаблон ответа

### Формат ответа:

```json
{
  "he": {
    "title": "Заголовок на иврите",
    "description": "Описание на иврите",
    "build_types": {
      "gaming": "Вероятность, что это игровой компьютер",
      "workstation": "Вероятность, что это рабочая станция"
    },
    "products": [
      {
        "product_id": "ID продукта (из входных данных)",
        "product_title": "Название продукта на иврите",
        "product_description": "Описание продукта на иврите",
        "image_local_saved_path": "Путь к изображению (из входных данных)"
      },
	    {
        "product_id": "ID продукта (из входных данных)",
        "product_title": "Название продукта на иврите",
        "product_description": "Описание продукта на иврите",
        "image_local_saved_path": "Путь к изображению (из входных данных)"
      }
    ]
  },
  "ru": {
    "title": "Заголовок на русском",
    "description": "Описание на русском",
    "build_types": {
      "gaming": "Вероятность, что это игровой компьютер",
      "workstation": "Вероятность, что это рабочая станция"
    },
    "products": [
      {
        "product_id": "ID продукта (из входных данных)",
        "product_title": "Название продукта на русском",
        "product_description": "Описание продукта на русском",
        "image_local_saved_path": "Путь к изображению (из входных данных)"
      },
      {
        "product_id": "ID продукта (из входных данных)",
        "product_title": "Название продукта на русском",
        "product_description": "Описание продукта на русском",
        "image_local_saved_path": "Путь к изображению (из входных данных)"
      }
    ]
  }
}
```

**Примечания:**

- Поля `product_id` и `image_local_saved_path` должны быть взяты из входных данных.
- Значения в `build_types` должны быть в формате числа с плавающей точкой от 0 до 1, представляющие вероятность.
- Текст в полях `title`, `description`, `product_title` и `product_description` должен быть соответствующим образом переведен и обработан.
- Обязательно следовать шаблону и не допускать отклонений.
- Кодировка ответа - `UTF-8`.


```
```
```python
# Пример функции для обработки входных данных (не является частью кода в исходном файле)

def process_command(input_json):
  """
  Обрабатывает входные данные в формате JSON.

  Args:
    input_json (dict): Входные данные в формате JSON.

  Returns:
    dict: Обработанные данные в формате JSON, соответствующем шаблону.
  
  Raises:
    ValueError: Если входные данные не соответствуют ожидаемому формату.
  """

  # Ваша логика обработки входных данных...


# Пример использования функции (не является частью кода в исходном файле)

input_data = { /* ваш входной JSON */ }  
output_data = process_command(input_data)
print(output_data)
```