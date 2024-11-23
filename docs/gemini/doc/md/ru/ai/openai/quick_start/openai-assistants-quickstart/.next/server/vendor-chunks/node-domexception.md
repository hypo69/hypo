```markdown
# Модуль node-domexception

## Обзор

Данный модуль экспортирует глобальный объект `DOMException`, если он не определён.  Если же `DOMException` уже определён, то экспорт остаётся пустым.


## Функции


### `globalThis.DOMException`

**Описание**:  Глобальный объект `DOMException` из среды выполнения JavaScript.

**Возвращает**:
- `DOMException`: Объект DOMException или `undefined` если он уже определен.


```
```javascript
// Пример использования (не входит в документацию)
if (globalThis.DOMException) {
  // DOMException уже определен
  console.log("DOMException уже определен");
} else {
  // DOMException не определен, поэтому модуль его создаст
  console.log("DOMException был создан");
}
```
```