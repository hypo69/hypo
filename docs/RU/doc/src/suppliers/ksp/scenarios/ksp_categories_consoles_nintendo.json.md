# Документация для `ksp_categories_consoles_nintendo.json`

## Оглавление

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
    - [Сценарии](#сценарии)
        - [Nintendo Switch OLED](#nintendo-switch-oled)
        - [Nintendo Switch](#nintendo-switch)
        - [Nintendo Switch Lite](#nintendo-switch-lite)
        - [Nintendo Classic](#nintendo-classic)

## Обзор

Файл `ksp_categories_consoles_nintendo.json` содержит конфигурационные данные для парсинга категорий игровых консолей Nintendo с сайта KSP. Он определяет сценарии для различных моделей консолей, включая их URL-адреса, бренды, статусы активности и соответствия категориям PrestaShop.

## Структура файла

### Сценарии

Сценарии представляют собой набор конфигураций для каждой конкретной модели консоли Nintendo.

#### Nintendo Switch OLED
**Описание**: Конфигурация для парсинга Nintendo Switch OLED.

**Параметры**:
  - `brand` (str): Бренд консоли, "NINTENDO".
  - `url` (str): URL-адрес страницы с консолью на сайте KSP.
  - `checkbox` (bool): Флаг для чекбокса (игнорируется).
  - `active` (bool): Флаг активности сценария.
  - `condition` (str): Состояние товара "new".
  - `presta_categories` (dict): Словарь с категориями PrestaShop.
      - `template` (dict): Словарь шаблонов категорий.
          - `nintendo` (str): Название категории для Nintendo Switch OLED.

#### Nintendo Switch
**Описание**: Конфигурация для парсинга Nintendo Switch.

**Параметры**:
  - `brand` (str): Бренд консоли, "NINTENDO".
  - `url` (str): URL-адрес страницы с консолью на сайте KSP.
  - `checkbox` (bool): Флаг для чекбокса (игнорируется).
  - `active` (bool): Флаг активности сценария.
  - `condition` (str): Состояние товара "new".
  - `presta_categories` (dict): Словарь с категориями PrestaShop.
      - `template` (dict): Словарь шаблонов категорий.
          - `nintendo` (str): Название категории для Nintendo Switch OLED.
        
#### Nintendo Switch Lite
**Описание**: Конфигурация для парсинга Nintendo Switch Lite.

**Параметры**:
  - `brand` (str): Бренд консоли, "NINTENDO".
  - `url` (str): URL-адрес страницы с консолью на сайте KSP.
  - `checkbox` (bool): Флаг для чекбокса (игнорируется).
  - `active` (bool): Флаг активности сценария.
   - `condition` (str): Состояние товара "new".
  - `presta_categories` (dict): Словарь с категориями PrestaShop.
      - `template` (dict): Словарь шаблонов категорий.
          - `nintendo` (str): Название категории для Nintendo Switch Lite.

#### Nintendo Classic
**Описание**: Конфигурация для парсинга Nintendo Classic.

**Параметры**:
  - `brand` (str): Бренд консоли, "NINTENDO".
  - `url` (str): URL-адрес страницы с консолью на сайте KSP.
  - `checkbox` (bool): Флаг для чекбокса (игнорируется).
  - `active` (bool): Флаг активности сценария.
   - `condition` (str): Состояние товара "new".
  - `presta_categories` (dict): Словарь с категориями PrestaShop.
      - `template` (dict): Словарь шаблонов категорий.
          - `nintendo` (str): Название категории для Nintendo Classic.