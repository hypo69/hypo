html
<h1>Module graber</h1>

<h2>Overview</h2>
<p>Базовый класс сбора данных со старницы для всех поставщиков. Для нестендартной обработки полей товара просто переопределите функцию в своем классе.
Пример:
```python
s = 'suppler_prefix'
from src.suppliers imoprt Graber
locator = j_loads(gs.path.src.suppliers / f'{s}' / 'locators' / 'product.json')

class G(Graber):

    @close_pop_up()
    async def name(self, value: Any = None):
        self.fields.name = <Ваша реализация>
        )
```
</p>

<h2>Classes</h2>

<h3><code>Context</code></h3>

<p><strong>Description</strong>: Класс для хранения глобальных настроек.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>driver</code> (Driver): Объект драйвера, используется для управления браузером или другим интерфейсом.</li>
  <li><code>locator</code> (SimpleNamespace): Пространство имен для хранения локаторов. (Если будет установлен - выполнится декоратор <code>@close_pop_up</code>. Устанавливается при инициализации поставщика, например: <code>Context.locator = self.locator.close_pop_up</code>)</li>
  <li><code>supplier_prefix</code> (str): Префикс поставщика.</li>
</ul>


<h3><code>Graber</code></h3>

<p><strong>Description</strong>: Базовый класс сбора данных со страницы для всех поставщиков.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>(supplier_prefix: str, driver:Driver):
    <p><strong>Description</strong>: Инициализация класса Graber.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>supplier_prefix</code> (str): Префикс поставщика.</li>
      <li><code>locator</code> (Locator): Экземпляр класса Locator.</li>
      <li><code>driver</code> (Driver): Экземпляр класса Driver.</li>
    </ul>
  </li>
  <li><code>error</code>(field: str):
    <p><strong>Description</strong>: Обработчик ошибок для полей.</p>
  </li>
  <li><code>set_field_value</code>(value: Any, locator_func: Callable[[], Any], field_name: str, default: Any = ''):
    <p><strong>Description</strong>: Универсальная функция для установки значений полей с обработкой ошибок.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>value</code> (Any): Значение для установки.</li>
      <li><code>locator_func</code> (Callable[[], Any]): Функция для получения значения из локатора.</li>
      <li><code>field_name</code> (str): Название поля.</li>
      <li><code>default</code> (Any): Значение по умолчанию. По умолчанию пустая строка.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>Any</code>: Установленное значение.</li>
    </ul>
  </li>
  <li><code>grab_page</code>() -> ProductFields:
    <p><strong>Description</strong>: Асинхронная функция для сбора полей продукта.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>ProductFields</code>: Собранные поля продукта.</li>
    </ul>
  </li>

  <!-- ... (other methods like additional_shipping_cost, delivery_in_stock, etc.) -->

  <li><code>local_saved_image</code>(value: Any = None):
  <p><strong>Description</strong>: Fetch and save image locally.</p>
   <p><strong>Parameters</strong>:</p>
  <ul>
     <li><code>value</code>(Any): это значение можно передать в словаре kwargs через ключ {local_saved_image = `value`} при определении класса.
     Если `value` был передан, его значение подставляется в поле `ProductFields.local_saved_image`.
     </li>
    </ul>
  </li>



   <!-- ... (rest of the methods) -->
</ul>
<p><strong>Decorator</strong>:</p>
<ul>
   <li><code>@close_pop_up()</code>:  Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции. </li>
</ul>


<h2>Functions</h2>

<h3><code>close_pop_up</code>(value: Any = None) -> Callable</h3>

<p><strong>Description</strong>: Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>value</code> (Any): Дополнительное значение для декоратора.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>Callable</code>: Декоратор, оборачивающий функцию.</li>
</ul>


</ul>


<!-- ... (rest of the HTML documentation for functions) -->


```