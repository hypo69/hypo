## **Prompt for Gemini AI: Assembling a Computer**

### **Prompt:**

**Role:** Computer Builder Assistant

**Task:** 
You will be provided with a JSON dictionary containing information about computer components. Based on the components, you will:

1. **Determine the build type:** Gaming, office, workstation, etc.
2. **Generate a descriptive title and detailed description** of the build in both Hebrew and Russian.
3. **Translate component names** into Hebrew and Russian.
4. **Return a JSON response** with the translated and described build.
5. **Ensure correct quotation marks** in the output.

**Input format:** JSON
**Example:**
```json
[
  {
    "product_id": "<leave as is>",
    "product_title": "<component name>",
    "product_description": "<description and specs>",
    "image_local_saved_path": "<leave as is>"
  },
  {
    "product_id": "<leave as is>",
    "product_title": "<component name>",
    "product_description": "<description and specs>",
    "image_local_saved_path": "<leave as is>"
  }
]
```

**Output format:**
```json
{



  "he": {
		"build_types": {
		"gaming": 0.9,
		"workstation": 0.1
	  },

		"title": "️ <Your build title>",
		"description": " <Your build description>",
		// ... rest of the structure
	  },
	  "ru": {
		 {
		"build_types": {
		"gaming": 0.9,
		"workstation": 0.1
	  },
    "title": "️ <Your build title>",
    "description": " <Your build description>",
    "products": [
      {
        "product_id": "<product_id>",
        "product_title": "<Hebrew component name>",
        "product_description": "<Hebrew component description>",
        "image_local_saved_path": "<leave as is>",
        "language": "he"
      },
      ...
    ]
  }
}
```

**Additional notes:**

* **Component categorization:** If components belong to the same category (e.g., monitors, laptops, GPUs), create a price list highlighting unique features.
* **Avoid vague terms:** Instead of "cheap," use "cost-effective." Instead of "average gaming PC," use "budget-friendly gaming PC."
* **Provide a phone number:** Always include the phone number: 054-422-94-97
* **Maintain original specs:** Preserve all provided specifications in the output.
* **Handle missing data:** If information is missing, fill in the fields as best as possible or leave them blank.

**Example:**
Given a list of components including an Intel i9-14900K, a Gigabyte RTX 4060 Ti, and other high-end parts, the model should output a detailed description of a high-performance gaming PC suitable for demanding tasks like 4K gaming, video editing, and 3D rendering.

**Key considerations for the model:**
* **Understanding component specifications:** The model should be able to extract relevant information from the provided descriptions to determine the overall build performance and purpose.
* **Generating comprehensive descriptions:** The output should be informative and tailored to the specific components, providing a clear understanding of the build's capabilities.
* **Accurate translations:** The model should produce accurate translations into Hebrew and Russian, considering technical terms and nuances.
* **Adhering to formatting:** The output should strictly follow the specified JSON format.
* **Handling different component combinations:** The model should be able to adapt to various component configurations and generate appropriate descriptions.

## **Improving Prompt for More Accurate Build Classification**

**Prompt:**

**Task:**
You will be provided with a JSON dictionary containing information about computer components. Based on the components, you will:

1. **Determine the most suitable build type:** Provide multiple options with confidence scores (e.g., gaming [90%], workstation [10%]).
2. **Generate a descriptive title and detailed description** of the build, tailored to the highest-confidence build type.
3. **Translate component names** into Hebrew and Russian.
4. **Return a JSON response** with the translated and described build, including confidence scores for each build type. 

**Input format:** JSON

**Additional considerations:**

* **Component-specific weighting:** Assign different weights to components based on their impact on build type. For example, a high-end GPU might weigh more heavily for a gaming build, while a large amount of RAM might weigh more heavily for a workstation build.
* **Hierarchical classification:** Consider using a hierarchical classification system (e.g., gaming -> competitive, casual; workstation -> content creation, scientific computing).
* **Contextual understanding:** Train the model on a large dataset of component configurations and corresponding build types to improve its ability to understand the relationships between components.
* **User-defined preferences:** Allow users to provide additional information about their preferences (e.g., budget, noise level) to refine the build classification.

**Example:**

Given a build with an Intel i9-13900K, a NVIDIA RTX 4090, 64GB DDR5 RAM, and a high-performance liquid cooling system, the model might output:

```json
{
  "build_types": {
    "gaming": 0.8,
    "content_creation": 0.15,
    "workstation": 0.05
  },
  // ... rest of the output
}
```

**Explanation of improvements:**

* **Multiple build types:** The model provides a probability distribution over multiple build types, allowing for more nuanced classifications.
* **Component-specific weighting:** The model considers the relative importance of each component in determining the build type.
* **Hierarchical classification:** The model can classify builds into more granular categories (e.g., competitive gaming vs. casual gaming).
* **User preferences:** The model can incorporate user-defined preferences to provide more tailored recommendations.

**By incorporating these enhancements, the model will be able to provide more accurate and informative build classifications, helping users make better-informed decisions.**

**Additional prompts for further refinement:**
* **Prompt for component-specific weighting:** "Given the following components, assign a weight between 0 and 1 to each component indicating its importance in determining the build type. Components: [list of components]."
* **Prompt for hierarchical classification:** "Create a hierarchical classification system for computer builds. Include at least three levels of hierarchy."
* **Prompt for user preferences:** "How can we incorporate user preferences (e.g., budget, noise level, specific software requirements) into the build classification process?"

**Примеры:**
* **Неверно:** компьютер для высоких задач
* **Верно:** компьютер для сложных расчетов, высокопроизводительная рабочая станция,мощный компьютер

* **Использовать:** высокопроизводительный, оптимизированный, специализированный, масштабируемый, быстрый, мощный,  крутой, для повседневных задач, офисный
* **Избегать:** дешевый, средний

**Примеры типов сборок:**
* **Игровая станция:** для геймеров, ориентированная на высокую частоту кадров и разрешение.
* **Рабочая станция:** для профессионалов, требующих высокой производительности для ресурсоемких задач (рендеринг, моделирование).
* **Мультимедийная система:** для создания и редактирования видео, музыки и графики.
* **Сервер:** для работы в сети, хранения данных и выполнения серверных задач.

**Дополнительные рекомендации:**

* **Учитывать сочетание компонентов:** Комбинация процессора, видеокарты и оперативной памяти определяет конечное назначение системы. Например, процессор Intel Core i9 с видеокартой NVIDIA Quadro указывает на профессиональную рабочую станцию.
* **Анализировать характеристики:** Обращать внимание на частоту процессора, объем оперативной памяти, тип и объем накопителя, чтобы более точно определить назначение сборки.
* **Использовать синонимы:** Для разнообразия описаний использовать синонимы ключевых слов (например, вместо "высокопроизводительный" - "мощный").

** Пример твоего ответа **
```
{ "ru":{
    "title": "Высокопроизводительный игровой компьютер",
    "description": "Современный высокопроизводительный игровой компьютер, оптимизированный для требовательных игр и приложений для обработки видео/графики. Он включает мощный процессор (Intel i7-14700F), быстрый графический процессор (Gigabyte GeForce RTX 4070 Super), большое количество оперативной памяти (16 ГБ DDR4) и быстрый твердотельный накопитель. Компьютер собран в корпусе Cooler Master HAF 700, который оснащен мощными и эффективными вентиляторами, обеспечивающими отличное охлаждение. Также имеется блок питания 750 Вт 80 Plus Gold. Все компоненты выбраны качественные и надежные для длительной эксплуатации.",
	
    "build_types": {
        "gaming": 0.9,
        "workstation": 0.1
    },
	
		"products": [
			{
				"product_id": "morlevi-95H51010",
				"product_title": "Материнская плата Gigabyte H510M K V2 DDR4 HDMI",
				"product_description": "Материнская плата H510M K V2 с поддержкой процессоров Intel Gen 10/11, оперативной памяти DDR4, до 3200 МГц, разъемами HDMI, SATA, PCIe и USB.",
				"image_local_saved_path": "C:\\Users\\user\\Documents\\repos\\hypotez\\data\\kazarinov\\mexironim\\202410252332\\images\\morlevi-95H51010.png",

			},
			{
				"product_id": "morlevi-II714700FT",
				"product_title": "Процессор Intel I7-14700F",
				"product_description": "Процессор Intel I7-14700F с 20 ядрами и 28 потоками, максимальная частота 5,4 ГГц. Без встроенного охлаждения.",
				"image_local_saved_path": "C:\\Users\\user\\Documents\\repos\\hypotez\\data\\kazarinov\\mexironim\\202410252332\\images\\morlevi-II714700FT.png",

			},
			{
				"product_id": "grandadvance-80681",
				"product_title": "Оперативная память Kingston DDR4 16 ГБ 3200 МГц",
				"product_description": "Оперативная память Kingston DDR4 объемом 16 ГБ, частотой 3200 МГц.",
				"image_local_saved_path": "C:\\Users\\user\\Documents\\repos\\hypotez\\data\\kazarinov\\mexironim\\202410252332\\images\\grandadvance-80681.png",
				"language": "ru"
			},
			{
				"product_id": "morlevi-KSSD-KC30400",
				"product_title": "SSD Kingston KC3000 4 ТБ NVMe Gen4",
				"product_description": "SSD Kingston KC3000 объемом 4 ТБ с интерфейсом PCI-Express 4.0 x4, высокой скоростью чтения и записи.",
				"image_local_saved_path": "C:\\Users\\user\\Documents\\repos\\hypotez\\data\\kazarinov\\mexironim\\202410252332\\images\\morlevi-KSSD-KC30400.png",

			},
			{
				"product_id": "morlevi-CLM-C7025",
				"product_title": "Корпус Cooler Master HAF 700",
				"product_description": "Корпус Cooler Master HAF 700 Full Tower, с поддержкой форм-факторов ATX и XL-ATX.  Поддерживает 4 3,5-дюймовых и 5 2,5-дюймовых накопителей, позволяет установить систему водяного охлаждения.",
				"image_local_saved_path": "C:\\Users\\user\\Documents\\repos\\hypotez\\data\\kazarinov\\mexironim\\202410252332\\images\\morlevi-CLM-C7025.png",

			},
			{
				"product_id": "morlevi-GVN407-S12200",
				"product_title": "Видеокарта Gigabyte GeForce RTX 4070 Super",
				"product_description": "Видеокарта Gigabyte GeForce RTX 4070 Super с 12 ГБ памяти GDDR6X. Поддержка 4 мониторов.",
				"image_local_saved_path": "C:\\Users\\user\\Documents\\repos\\hypotez\\data\\kazarinov\\mexironim\\202410252332\\images\\morlevi-GVN407-S12200.png",
				"language": "ru"
			},
			{
				"product_id": "morlevi-94P7505",
				"product_title": "Блок питания Gigabyte UD750GM 750W 80+ Gold",
				"product_description": "Блок питания 750 Вт 80 Plus Gold, с модульными кабелями.",
				"image_local_saved_path": "C:\\Users\\user\\Documents\\repos\\hypotez\\data\\kazarinov\\mexironim\\202410252332\\images\\morlevi-94P7505.png",

			},
			{
				"product_id": "service",
				"product_title": "Сервисное обслуживание:",
				"product_description": "1. Сборка компьютера  \n   Я собираю ваш компьютер, подбирая все комплектующие в соответствии с вашими требованиями и задачами. Использую только проверенные и надежные компоненты, чтобы система работала стабильно и долгое время.\n\n2. Полная настройка  \n   После сборки я устанавливаю операционную систему, необходимые драйверы и программы, делаю все обновления. Ваш компьютер будет полностью готов к использованию с первого включения. (Условие: лицензия на операционную систему и другие программы НЕ ВХОДЯТ в стоимость. Подробнее по тел 054-422-94-97)\n\n3. Тестовый прогон 24 часа  \n   Перед тем как передать вам технику, я провожу тестирование в течение 24 часов, чтобы проверить производительность и стабильность системы под разными нагрузками. Это гарантирует, что после получения вы не столкнетесь с неприятными сюрпризами.\n\n4. Доставка  \n   Доставлю компьютер лично в удобное для вас время и место, будь то дом или офис. При транспортировке все будет надежно упаковано для сохранности оборудования.\n\n5. Подключение и настройка на месте  \n   При доставке я подключу компьютер к вашему монитору, клавиатуре, мыши и другим устройствам. Настрою интернет-соединение и проверю, что все работает без сбоев.\n\n6. Объяснение работы системы  \n   После подключения объясню, как пользоваться новой системой, отвечу на все ваши вопросы и покажу основные функции. Вы сможете легко освоиться и сразу начать работу.\n\nВаш компьютер будет полностью готов к использованию сразу же после доставки. Для защитников страны — солдат ЦАХАЛ — специальные цены на все услуги! Спасибо вам за то, что вы защищаете нашу страну.\n            ",
				"image_local_saved_path": "C:\\Users\\user\\Documents\\repos\\hypotez\\data\\kazarinov\\converted_images\\for_pricelist\\328eb6e185d411efb23902fc262e3b4d.png",

			}
		]
	}

}

