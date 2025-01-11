# Документация для файла `ksp_categories_streamers_google.json`

## Обзор

Этот файл содержит JSON-структуру, описывающую сценарии для категорий стримеров Google, конкретно для Google Chromecast. Он определяет бренд, URL-адрес для поиска продуктов, флаг активности и соответствие категорий PrestaShop.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
    - [Google Chromecast](#google-chromecast)

## Структура JSON

JSON файл содержит единственный ключ `"scenarios"`, значением которого является объект, в котором ключами являются названия сценариев (например, "Google Chromecast").

## Сценарии

### `Google Chromecast`

**Описание**:
Сценарий для обработки устройств Google Chromecast.

**Поля**:

-   `brand` (str): Бренд продукта, в данном случае "GOOGLE".
-   `url` (str): URL-адрес для поиска соответствующих продуктов. В данном случае "https://ksp.co.il/web/cat/573..1358..24585".
-   `checkbox` (bool): Флаг, указывающий, нужно ли отображать чекбокс. В данном случае `false`.
-  `active` (bool): Флаг, указывающий, активен ли сценарий. В данном случае `true`.
- `condition` (str): Состояние товара, в данном случае "new".
-   `presta_categories` (dict): Объект, содержащий соответствие категорий PrestaShop с их именами.
    -   `3405` (str): Категория "GOOGLE PIXEL PRO".
     -   `3198` (str): Категория "CONSUMER ELECTRONICS".
    -   `3202` (str): Категория "computer,smartphone,gaming console,smart device".
    -    `6471` (str): Категория "Smartphones".
    -    `3403` (str): Категория "GOOGLE".