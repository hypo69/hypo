# Файл desktop.ini

## Обзор

Данный файл представляет собой файл управления свойствами папки в формате Windows, используется для определения свойств папки, например, отображения значка и других визуальных параметров.  Он не содержит функционального Python кода, поэтому документация ограничена описанием формата.

## Формат файла

Файл `desktop.ini` имеет текстовый формат и состоит из строк в формате `ключ=значение`.  Значения могут быть строками, числами или другими допустимыми значениями в зависимости от ключа.

## Пример

```
[ViewState]
Mode=
Vid=
FolderType=Generic
Logo=E:\\Users\\user\\images\\LOGOS\\R.png
```

**Ключи и их возможные значения:**

* **`[ViewState]`:**  Ключ, обозначающий блок настроек отображения.
* **`Mode=`:**  Параметр режима отображения папки. Может принимать различные значения, но обычно пустая строка.
* **`Vid=`:**  Параметр, определяющий идентификатор вида (типа) папки.
* **`FolderType=`:**  Тип папки (Generic, Recycle Bin и др.).
* **`Logo=`:** Путь к файлу изображения, используемому в качестве значка папки.
```