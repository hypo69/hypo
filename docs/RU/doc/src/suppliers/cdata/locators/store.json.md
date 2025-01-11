# Описание файла `store.json`

## Обзор

Файл `store.json` содержит локаторы для элементов пользовательского интерфейса, используемых в контексте поставщиков (suppliers) в системе. Эти локаторы применяются для автоматизации тестирования и взаимодействия с элементами веб-страниц.

## Содержание

1. [Обзор](#обзор)
2. [Локаторы](#локаторы)
    - [search_input](#search_input)
    - [search_button](#search_button)
    - [suppliers_table](#suppliers_table)
    - [supplier_row](#supplier_row)
    - [supplier_name](#supplier_name)
    - [supplier_email](#supplier_email)
    - [supplier_phone](#supplier_phone)
    - [edit_supplier_button](#edit_supplier_button)
    - [delete_supplier_button](#delete_supplier_button)
    - [add_supplier_button](#add_supplier_button)
    - [confirm_delete_button](#confirm_delete_button)
    - [cancel_delete_button](#cancel_delete_button)
    - [popup_title](#popup_title)
    - [close_popup_button](#close_popup_button)
    - [form_container](#form_container)
    - [form_name_input](#form_name_input)
    - [form_email_input](#form_email_input)
    - [form_phone_input](#form_phone_input)
    - [form_submit_button](#form_submit_button)
    - [form_cancel_button](#form_cancel_button)
    - [form_error_message](#form_error_message)

## Локаторы

### `search_input`

**Описание**: Локатор для поля ввода поиска поставщиков.

**Значение**: `xpath://input[@placeholder="Search by name or email"]`

### `search_button`

**Описание**: Локатор для кнопки поиска поставщиков.

**Значение**: `xpath://button[contains(text(), "Search")]`

### `suppliers_table`

**Описание**: Локатор для таблицы со списком поставщиков.

**Значение**: `xpath://table[@class="table"]`

### `supplier_row`

**Описание**: Локатор для строки таблицы с данными поставщика.

**Значение**: `xpath://tbody/tr`

### `supplier_name`

**Описание**: Локатор для ячейки с именем поставщика.

**Значение**: `xpath://td[1]`

### `supplier_email`

**Описание**: Локатор для ячейки с email поставщика.

**Значение**: `xpath://td[2]`

### `supplier_phone`

**Описание**: Локатор для ячейки с телефоном поставщика.

**Значение**: `xpath://td[3]`

### `edit_supplier_button`

**Описание**: Локатор для кнопки редактирования поставщика.

**Значение**: `xpath//button[contains(text(), "Edit")]`

### `delete_supplier_button`

**Описание**: Локатор для кнопки удаления поставщика.

**Значение**: `xpath//button[contains(text(), "Delete")]`

### `add_supplier_button`

**Описание**: Локатор для кнопки добавления нового поставщика.

**Значение**: `xpath//button[contains(text(), "Add")]`

### `confirm_delete_button`

**Описание**: Локатор для кнопки подтверждения удаления поставщика.

**Значение**: `xpath//button[contains(text(), "Confirm")]`

### `cancel_delete_button`

**Описание**: Локатор для кнопки отмены удаления поставщика.

**Значение**: `xpath//button[contains(text(), "Cancel")]`

### `popup_title`

**Описание**: Локатор для заголовка всплывающего окна.

**Значение**: `xpath//div[@class='modal-header']/h5`

### `close_popup_button`

**Описание**: Локатор для кнопки закрытия всплывающего окна.

**Значение**: `xpath//button[@class='close']`

### `form_container`

**Описание**: Локатор для контейнера формы.

**Значение**: `xpath//div[@class='modal-body']`

### `form_name_input`

**Описание**: Локатор для поля ввода имени поставщика в форме.

**Значение**: `xpath//input[@name="name"]`

### `form_email_input`

**Описание**: Локатор для поля ввода email поставщика в форме.

**Значение**: `xpath//input[@name="email"]`

### `form_phone_input`

**Описание**: Локатор для поля ввода телефона поставщика в форме.

**Значение**: `xpath//input[@name="phone"]`

### `form_submit_button`

**Описание**: Локатор для кнопки подтверждения отправки формы.

**Значение**: `xpath//button[contains(text(), "Submit")]`

### `form_cancel_button`

**Описание**: Локатор для кнопки отмены отправки формы.

**Значение**: `xpath//button[contains(text(), "Cancel")]`

### `form_error_message`

**Описание**: Локатор для сообщения об ошибке в форме.

**Значение**: `xpath//div[contains(@class, 'invalid-feedback')]`