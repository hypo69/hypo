# Документация `scenario_executor.mmd`

## Обзор

Данный файл содержит mermaid-диаграмму, описывающую процесс выполнения сценариев. Диаграмма наглядно демонстрирует последовательность шагов от получения списка файлов сценариев до добавления продуктов в PrestaShop.

## Содержание

- [Обзор](#обзор)
- [Диаграмма](#диаграмма)

## Диаграмма

```mermaid
graph TD
    A[Supplier Instance] --> B{Scenario Files List}
    B -- Valid List --> C[Run Scenario Files]
    B -- Invalid List --> D[Error Handling]
    C --> E{Iterate Through Each Scenario File}
    E --> F[Run Scenario File]
    F --> G{Load Scenarios}
    G --> H[Iterate Through Each Scenario]
    H --> I[Run Scenario]
    I --> J[Navigate to URL]
    J --> K[Get List of Products]
    K --> L{Iterate Through Products}
    L --> M[Navigate to Product Page]
    M --> N[Grab Product Fields]
    N --> O[Create Product Object]
    O --> P[Insert Product into PrestaShop]
    P -- Success --> Q[Success]
    P -- Failure --> R[Error Handling]
    Q --> S[Update Journal]
    R --> S
    S --> T[Return True/False]
```