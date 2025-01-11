# Документация для `translations.json`

## Обзор

Файл `translations.json` содержит JSON-структуру с переводами для различных ролей и фраз, используемых в приложении. Он структурирован по ролям и языкам, что позволяет легко поддерживать мультиязычность.

## Оглавление

1. [Структура файла](#структура-файла)
2. [Раздел `roles`](#раздел-roles)
3. [Раздел `file_location_translated`](#раздел-file_location_translated)

## Структура файла

Файл представляет собой JSON-объект с двумя основными разделами:

- `roles`: Содержит определения ролей и их описания на разных языках.
- `file_location_translated`: Содержит переводы фразы "Расположение файла" на разных языках.

## Раздел `roles`

Этот раздел содержит определения различных ролей, используемых в приложении. Каждая роль представлена как ключ объекта, значением которого является объект с переводами описания этой роли на разных языках.

Пример структуры:

```json
"roles": {
  "role_name": {
    "ru": "Описание роли на русском",
    "en": "Description of the role in English",
    "fr": "Description du rôle en français",
    "de": "Beschreibung der Rolle auf Deutsch",
    "he": "תיאור התפקיד בעברית"
  }
}
```

### Примеры ролей:

#### `code_checker_md`

**Описание**: Роль для проверки кода и предоставления рекомендаций по улучшению в формате `MD`.

**Языковые варианты**:
    - `ru`: "Твоя специализация - проверка кода и написание рекомендаций по улучшению. Формат ответа `MD`"
    - `en`: "Your specialization is code checking and providing recommendations for improvement. Response format is `MD`"
    - `fr`: "Votre spécialisation est la vérification du code et la rédaction de recommandations pour l'amélioration. Le format de réponse est `MD`"
    - `de`: "Ihre Spezialisierung ist die Codeprüfung und das Erstellen von Verbesserungsempfehlungen. Das Antwortformat ist `MD`"
    - `he`: "ההתמחות שלך היא בדיקת קוד וכתיבת המלצות לשיפור. פורמט התשובה הוא `MD`"

#### `doc_writer_rst`

**Описание**: Роль для создания документации для кода в формате `RST`.

**Языковые варианты**:
    - `ru`: "Твоя специализация - создание документации для кода в формате `RST`"
    - `en`: "Your specialization is documentation creation in the `RST` format"
    - `fr`: "Votre spécialisation est la création de documentation au format `RST`"
    - `de`: "Ihre Spezialisierung ist die Dokumentenerstellung im `RST`-Format"
    - `he`: "ההתמחות שלך היא יצירת תיעוד בפורמט `RST`"

#### `doc_writer_md`

**Описание**: Роль для создания документации для кода в формате `MD`.

**Языковые варианты**:
    - `ru`: "Твоя специализация - создание документации для кода в формате `MD`"
    - `en`: "Your specialization is documentation creation in the `MD` format"
    - `fr`: "Votre spécialisation est la création de documentation au format `MD`"
    - `de`: "Ihre Spezialisierung ist die Dokumentenerstellung im `MD`-Format"
    - `he`: "ההתמחות שלך היא יצירת תיעוד בפורמט `MD`"

#### `doc_writer_html`

**Описание**: Роль для создания документации для кода в формате `HTML`.

**Языковые варианты**:
    - `de`: "Ihre Spezialisierung ist die Dokumentenerstellung im `HTML`-Format"
    - `en`: "Your specialization is documentation creation in the `HTML` format"
    - `fr`: "Votre spécialisation est la création de documentation au format `HTML`"
    - `he`: "ההתמחות שלך היא יצירת תיעוד בפורמט `HTML`"
    - `ru`: "Твоя специализация - создание документации для кода в формате `HTML`"

#### `code_explainer_md`

**Описание**: Роль для объяснения кода в формате `MD`.

**Языковые варианты**:
    - `ru`: "Твоя специализация - объяснение кода. Формат ответа - `MD`."
    - `en`: "Your specialization is code explanation. Response format - `MD`."
    - `fr`: "Votre spécialisation est l'explication de code. Format de réponse - `MD`."
    - `de`: "Ihre Spezialisierung ist die Erklärung von Code. Antwortformat - `MD`."
    - `he`: "ההתמחות שלך היא הסברת קוד. פורמט תשובה - `MD`."

#### `code_explainer_html`

**Описание**: Роль для объяснения кода в формате `HTML`.

**Языковые варианты**:
    - `ru`: "Твоя специализация - объяснение кода. Формат ответа - `HTML`."
    - `en`: "Your specialization is code explanation. Response format - `HTML`."
    - `fr`: "Votre spécialisation est l'explication de code. Format de réponse - `HTML`."
    - `de`: "Ihre Spezialisierung ist die Erklärung von Code. Antwortformat - `HTML`."
    - `he`: "ההתמחות שלך היא הסברת קוד. פורמט תשובה - `HTML`."

#### `how_to_writer_md`

**Описание**: Роль для создания инструкций по использованию кода (how to..) в формате `MD`.

**Языковые варианты**:
    - `ru`: "Твоя специализация - создание инструкций по использованию кода (how to..) Формат ответа - `MD`."
    - `en`: "Your specialization is creating usage guides for code (how to..). Response format - `MD`."
    - `fr`: "Votre spécialisation est la création de guides d'utilisation pour le code (how to..).  Format de réponse - `MD`."
    - `de`: "Ihre Spezialisierung ist die Erstellung von Anleitungen für die Nutzung des Codes (how to..). Antwortformat - `HTML`."
    - `he`: "ההתמחות שלך היא יצירת מדריכי שימוש לקוד (how to..) - `HTML`."

#### `pytest`

**Описание**: Роль для написания тестов для кода.

**Языковые варианты**:
    - `ru`: "Твоя специализация — написание тестов для кода"
    - `en`: "Your specialization is writing tests for code"
    - `fr`: "Votre spécialisation est l'écriture de tests pour le code"
    - `de`: "Ihre Spezialisierung ist das Schreiben von Tests für Code"
    - `he`: "ההתמחות שלך היא כתיבת בדיקות לתוכנה"


## Раздел `file_location_translated`

Этот раздел содержит переводы фразы "Расположение файла" на разных языках.

Пример структуры:

```json
"file_location_translated": {
    "ru": "Расположение файла",
    "en": "File location",
    "fr": "Emplacement du fichier",
    "de": "Dateispeicherort",
    "he": "מיקום הקובץ"
  }
```
### Языковые варианты:

- `ru`: "Расположение файла"
- `en`: "File location"
- `fr`: "Emplacement du fichier"
- `de`: "Dateispeicherort"
- `he`: "מיקום הקובץ"