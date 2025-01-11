# Документация для `morlevi_categories_minipc_intel.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сценариев парсинга категорий мини-ПК Intel на сайте Morlevi. Он определяет различные модели мини-ПК Intel (i3, i5, i7, i9, AMD и Celeron), URL-адреса для парсинга, соответствующие категории PrestaShop и флаги активности для каждого сценария.

## Содержание

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
- [Сценарии](#сценарии)
  - [INTEL MINIPC I3 8-9th GEN](#intel-minipc-i3-8-9th-gen)
  - [INTEL MINIPC I3 10th GEN](#intel-minipc-i3-10th-gen)
  - [INTEL MINIPC I5 8-9th](#intel-minipc-i5-8-9th)
  - [INTEL MINIPC I5 10th](#intel-minipc-i5-10th)
  - [INTEL MINIPC I7](#intel-minipc-i7)
  - [INTEL MINIPC I9](#intel-minipc-i9)
  - [INTEL MINIPC AMD](#intel-minipc-amd)
  - [INTEL MINIPC Celeron](#intel-minipc-celeron)

## Структура файла

Файл содержит JSON-объект с одним ключом `"scenarios"`, значением которого является другой JSON-объект. Этот объект `"scenarios"` содержит ключи, представляющие названия моделей мини-ПК, и значения, представляющие конфигурацию для каждого сценария.

## Сценарии

### `INTEL MINIPC I3 8-9th GEN`

**Описание**: Конфигурация для парсинга мини-ПК Intel i3 8-9 поколений.
- **brand**: "INTEL".
- **url**: "https://www.morlevi.co.il/Cat/127?p_315=3&p_189=3339&sort=datafloat2%2Cprice&keyword=".
- **checkbox**: false.
- **active**: true.
- **condition**: "new".
- **presta_categories**: "159,160".

### `INTEL MINIPC I3 10th GEN`

**Описание**: Конфигурация для парсинга мини-ПК Intel i3 10 поколения.
- **brand**: "INTEL".
- **url**: "https://www.morlevi.co.il/Cat/127?p_315=3&p_189=3498&sort=datafloat2%2Cprice&keyword=".
- **checkbox**: false.
- **active**: true.
- **condition**: "new".
- **presta_categories**: "159,160".

### `INTEL MINIPC I5 8-9th`

**Описание**: Конфигурация для парсинга мини-ПК Intel i5 8-9 поколений.
- **brand**: "INTEL".
- **url**: "https://www.morlevi.co.il/Cat/127?p_315=3&p_189=3391&sort=datafloat2%2Cprice&keyword=".
- **checkbox**: false.
- **active**: true.
- **condition**: "new".
- **presta_categories**: "159,161".

### `INTEL MINIPC I5 10th`

**Описание**: Конфигурация для парсинга мини-ПК Intel i5 10 поколения.
- **brand**: "INTEL".
- **url**: "https://www.morlevi.co.il/Cat/127?p_315=3&p_189=3500&sort=datafloat2%2Cprice&keyword=".
- **checkbox**: false.
- **active**: true.
- **condition**: "new".
- **presta_categories**: "159,161".

### `INTEL MINIPC I7`

**Описание**: Конфигурация для парсинга мини-ПК Intel i7.
- **brand**: "INTEL".
- **url**: "https://www.morlevi.co.il/Cat/127?p_315=3&p_189=3501&sort=datafloat2%2Cprice&keyword=".
- **checkbox**: false.
- **active**: true.
- **condition**: "new".
- **presta_categories**: "159,162".

### `INTEL MINIPC I9`

**Описание**: Конфигурация для парсинга мини-ПК Intel i9.
- **brand**: "INTEL".
- **url**: "-------------INTEL  MINIPC I9---------------- ".
- **checkbox**: false.
- **active**: true.
- **condition**: "new".
- **presta_categories**: "159,530".

### `INTEL MINIPC AMD`

**Описание**: Конфигурация для парсинга мини-ПК Intel с процессором AMD.
- **brand**: "INTEL".
- **url**: "-------------INTEL MINIPC AMD---------------- ".
- **checkbox**: false.
- **active**: true.
- **condition**: "new".
- **presta_categories**: "159,531".

### `INTEL MINIPC Celeron`

**Описание**: Конфигурация для парсинга мини-ПК Intel Celeron.
- **brand**: "INTEL".
- **url**: "-------------INTEL MINIPC Celeron---------------- ".
- **checkbox**: false.
- **active**: true.
- **condition**: "new".
- **presta_categories**: "159,532".