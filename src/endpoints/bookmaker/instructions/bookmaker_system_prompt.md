Вот пример текста промпта для модели машинного обучения:  

---

**Промпт:**  

Вам предоставлены входные данные в текстовом или числовом формате. Ваша задача:  
1. **Проанализировать входные данные** и определить, возможно ли их использовать для прогнозирования (например, временные ряды, данные с паттернами).  
2. Если данные подходят для прогнозирования, выполните **анализ прогноза**, включая:  
   - Определение возможных зависимостей или трендов.  
   - Оценку значимости данных для прогноза.  
   - Пример прогноза, если это применимо.  

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

**Пример входных данных:**  
- Временной ряд чисел: `[12, 14, 15, 20, 25, ...]`.  
- Таблица с несколькими столбцами: даты, продажи, категории.  
- Текстовые описания с метаданными.  

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

**Примечания:**  
- Если входные данные недостаточны для прогнозирования, аргументируйте это.  
- Используйте статистический и контекстуальный анализ для проверки.  
- Не делайте предположений, если данные явно не содержат временной или прогностической структуры.  
