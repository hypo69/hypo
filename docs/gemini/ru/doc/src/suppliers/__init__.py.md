# Модуль `src.suppliers`

## Обзор

Модуль `src.suppliers` предоставляет функциональность для работы с поставщиками. Основная цель модуля - предоставить базовый класс `Supplier` и механизмы для добавления специфичных методов извлечения информации для каждого поставщика через интерфейс `supplier.related_functions`.

Методы каждого конкретного поставщика организованы в директориях с именем `<supplier_prefix>`, например, `amazon`, `aliexpress`, `morlevi` и т.д.  Префикс задается при создании нового поставщика в системе.

## Взаимосвязь сущностей Supplier, Driver, Product

![Взаимосвязь Supplier, Driver, Product](supplier-warehouse-client.png)

## Содержание

- [Обзор](#обзор)
- [Взаимосвязь сущностей Supplier, Driver, Product](#взаимосвязь-сущностей-supplier-driver-product)
- [Содержание](#содержание)
- [Описание](#описание)

## Описание

Модуль содержит классы и функции для управления информацией о поставщиках.

Файл `__init__.py` инициализирует модуль `src.suppliers` и содержит общее описание модуля.

Модуль предназначен для гибкого добавления и управления поставщиками, где каждый поставщик может иметь свои собственные уникальные методы извлечения данных.