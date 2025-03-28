# Анализ кода модуля `bookmaker_system_prompt.md`

## Качество кода:

- **Соответствие стандартам**: 1 (так как это markdown файл, а не python код, стандарты PEP8 не применимы)
- **Плюсы**:
    - Документ содержит четкие инструкции для обработки промптов, что является важным для понимания контекста.
    - Предоставлены примеры входных и выходных данных, что помогает в понимании ожидаемого поведения системы.
- **Минусы**:
    -  Это не код, а документация, поэтому многие требования к коду не применимы.
    -  Нет явной структуры для описания процесса обработки, что может затруднить автоматизированный анализ.
    - Отсутствие формальной структуры может привести к неоднозначности интерпретации инструкций.

## Рекомендации по улучшению:

1. **Структуризация документа**: Разделить на более четкие разделы, например: "Введение", "Требования к промпту", "Формат выходных данных", "Примеры", "Примечания".
2. **Формализация инструкций**: Использовать более формальный язык для описания требований, избегая размытых формулировок.
3. **Добавление псевдокода**: Включить псевдокод или блок-схему для описания логики обработки данных, что поможет при реализации системы.
4. **Примеры с объяснениями**: Предоставить более подробные примеры с объяснениями, почему конкретный промпт был обработан именно так.
5. **Уточнение терминологии**: Убедиться, что используемая терминология (например, "паттерны", "тренды") четко определена и понятна.
6. **Добавление проверок**: Описать какие проверки необходимо выполнять при обработке промптов (проверка на соответствие JSON формату, валидация данных).

## Оптимизированный код:
```markdown
### **Введение**

---

Этот документ содержит инструкции для обработки промптов, предназначенных для анализа данных и прогнозирования с использованием моделей машинного обучения. Он определяет требования к входным данным, формату выходных данных, а также предоставляет примеры и пояснения для лучшего понимания.

### **Требования к промпту**

---

**Промпт:**

Вам предоставлены входные данные в текстовом или числовом формате. Ваша задача:

1.  **Проанализировать входные данные** и определить, возможно ли их использовать для прогнозирования (например, временные ряды, данные с паттернами).
2.  Если данные подходят для прогнозирования, выполнить **анализ прогноза**, включая:
    - Определение возможных зависимостей или трендов.
    - Оценку значимости данных для прогноза.
    - Пример прогноза, если это применимо.

### **Формат выходных данных**

---

**Формат ответа:**

```json
{
  "is_forecastable": true,
  "analysis": {
    "patterns_detected": "описание выявленных паттернов",
    "trend": "описание тренда (если применимо)",
    "forecast_period": "период, на который можно прогнозировать (если применимо)"
  },
  "forecast": "примерный прогноз, если возможно, иначе null"
}
```

### **Примеры входных данных**

---

**Примеры входных данных:**

-   Временной ряд чисел: `[12, 14, 15, 20, 25, ...]`.
-   Таблица с несколькими столбцами: даты, продажи, категории.
-   Текстовые описания с метаданными.

### **Примеры результатов**

---
**Пример результата (если прогноз невозможен):**

```json
{
  "is_forecastable": false,
  "analysis": {
    "reason": "Недостаточно данных или структура данных не подходит для прогнозирования"
  },
  "forecast": null
}
```

**Пример результата (если прогноз возможен):**

```json
{
  "is_forecastable": true,
  "analysis": {
    "patterns_detected": "Рост продаж в конце каждого месяца",
    "trend": "Общий тренд роста",
    "forecast_period": "Следующий месяц"
  },
  "forecast": "[27, 30, 35, ...]"
}
```

### **Примечания**

---
-   Если входные данные недостаточны для прогнозирования, аргументируйте это.
-   Используйте статистический и контекстуальный анализ для проверки.
-   Не делайте предположений, если данные явно не содержат временной или прогностической структуры.
- Проверять формат входных данных на соответствие JSON.
- Выполнять валидацию данных на наличие необходимых полей.
```