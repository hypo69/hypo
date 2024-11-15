```markdown
# affiliate_link.py

Файл: `C:\Users\user\Documents\repos\hypotez\src\suppliers\aliexpress\api\models\affiliate_link.py`

**Роль:** `doc_creator`

**Описание:**

Данный файл определяет класс `AffiliateLink`, представляющий аффилированную ссылку.  Он предназначен для работы с API AliExpress.

**Класс `AffiliateLink`:**

* `promotion_link`: Строка, содержащая промо-ссылку.
* `source_value`: Строка, содержащая значение источника (например, источник трафика).

**Пример использования (неполный):**

```python
from hypotez.src.suppliers.aliexpress.api.models.affiliate_link import AffiliateLink

affiliate_link = AffiliateLink()
affiliate_link.promotion_link = "https://example.com/promotion"
affiliate_link.source_value = "google_ads"

print(affiliate_link.promotion_link)  # Выведет https://example.com/promotion
```

**Примечания:**

* Файл предполагает использование виртуального окружения (см. ``).
* Документация в виде docstrings может быть расширена для лучшей читаемости и понимания.

**Связанные файлы (если применимо):**

(Укажите здесь связанные файлы, например, другие модели, контроллеры, или сервисы, с которыми взаимодействует этот файл.)


**Дополнительные заметки:**

(Добавьте здесь любые дополнительные пояснения, касающиеся реализации или особенностей работы с этим файлом).
```
