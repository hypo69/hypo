```markdown
# Модуль RSC Server Manifest

## Обзор

Этот модуль содержит константу, представляющую JSON-строку с манифестом сервера RSC (Remote Static Cache).  Эта константа хранит информацию о сервере, включая ключи шифрования, а также данные для статических узлов и узлов с динамической загрузкой (edge).


## Константы

### `__RSC_SERVER_MANIFEST`

**Описание**: Константа, содержащая JSON-строку с манифестом сервера RSC.

**Значение**:
```json
{
  "node": {},
  "edge": {},
  "encryptionKey": "XC9uIXAY0J3Kt1GKReoAsMh7bGSCqrZTkbAMU4yQblc="
}
```

**Примечания**:
* Эта константа предназначена для хранения информации о конфигурации сервера RSC.
* Она содержит ключи `node` и `edge`, которые содержат данные о различных типах узлов (статические, динамические).
* Ключ `encryptionKey` содержит зашифрованный ключ, используемый для безопасности.
```
```