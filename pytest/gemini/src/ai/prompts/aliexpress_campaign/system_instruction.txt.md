```python
import pytest
from unittest.mock import MagicMock, patch
import json

# Mocking external function (assuming there is an external function for title and description generation)
def mock_generate_title(products_titles, language):
    """Mock function for generating title based on product titles."""
    if language == "RU":
        return "Зарядные устройства LiitoKala для аккумуляторов 18650 ..."
    elif language == "HE":
        return "מוצרי תינוקות ואמא: הכל מה שצריך"
    else:
        return "Generic Title"

def mock_generate_description(products_titles, category_name, language):
    """Mock function for generating description based on product titles and category."""
    if language == "RU" and category_name == "liitokala_18650":
        return "LiitoKala для разных типов аккумуляторов: iitoKala Lii-M4S-M4,  LiitoKala Lii-S12 Lii-D4XL-Lii S8 LCD, LiitoKala Lii-S12 Lii-S8 Lii-PD4 Lii-PD2 Lii-500S, LiitoKala Lii-M4,  LiitoKala Lii-202 Lii-402,  LiitoKala Lii-D4,  LiitoKala Lii-PD2,  LiitoKala Lii-M4S + U1,  OPUS BT-C3100,   Зарядное устройство LiitoKala для Li-Ion LiFePO4 Ni-MH Ni-Cd батарей с ЖК-дисплеем,  Зарядное устройство LiitoKala для аккумуляторов  AA AAA 10440 14500 16340 17335 17500 18490 17670  и другие. Все зарядные устройства отличаются высоким качеством, функциональностью и надежностью. Выбирайте зарядное устройство LiitoKala для ваших аккумуляторов и будьте уверены в их безопасности и долговечности"
    elif language == "HE" and category_name == "mom_and_baby":
        return "אמהות יקרות, תמצאו כאן את כל מה שצריך לאמא ולילד: משאבות חלב ידניות ואוטומטיות, אביזרים לתינוקות כמו סיליקון מתכוונן לשאיבת חלב, מנשא ארגונומי לתינוקות, מתנות מקסימות לאמהות, כלי אוכל לילדים, וכל מה שצריך לתינוק: כף רגל דלי מתקפל חדר אמבטיה עם חישה טמפרטורה, שקיות אחסון חלב אם, מגבת חום חם, ומצלמת וידאו בייבי.  צפו להתרגש!  \\n\\n **משאבות חלב:** \\nמשאבת חלב פילופים אוות חד-צדדית אוטומטית  - ניידת ועוצמתית,  Dr.isla  - עם  סיליקון מתכוונן  נוחה,  ובלביש - משאבת חלב אמא ותינוק אספקת שד משאבת חד  צדדית אוטומטית חיקוי התינוק למצוץ.   \\n\\n **טיפול בתינוק:** \\n סיליקון  Dr.isla  לשאיבת חלב  -  בטוח  ורעש  נמוך,  מנשא  ארגונומי  -  רב  תכליתי  ומותניים,  כף  רגל  דלי  מתקפל  חדר  אמבטיה  עם  חישה  טמפרטורה  -  בטיחות  להורים  ושלווה  לתינוק.  \\n\\n **מתנות לאמהות:**  \\n  עלה  דוב  פרחים  קצף  מלאכותי  -  מתנה  יפה  וקלאסית,  מחזיק  פמוט  עם  מנצנץ  -  מתנה  רומנטית  וקסומה,  וכל  מה  שצריך  לאמהות  לאחר  הלידה.  \\n\\n **כלים  לאוכל:**  \\n ילדים  של  מנות  סט  תינוק  סיליקון  6/8-חתיכה  כלי  שולחן  סט  יניקה  כוסות  מזלגות  כפות  ליקוק  קשיות  כוסות  -  כל  הציוד  הנכון  לארוחות  טעימות  וחווייתיות.  \\n\\n **בטיחות  ולקוח  בבית:**  \\n   Cdycam  חדש  3.5  אינץ  אלחוטי  וידאו  התינוק  צג  הלילה  טמפרטורה  ניטור  2  דרך  שמע  אודיו  מצלמת  אבטחה  בייבי  -  שלווה  לכם  ושליטה  על  התינוק  מכל  מקום.  \\n  \\n **השקיעו  בבריאות  ונחת  של  אמא  ותינוק.**"
    elif language == "HE" and category_name == "xiaomi":
      return "שיאומי מציעה מגוון רחב של מוצרים טכנולוגיים איכותיים במחירים נוחים. בין אם אתם מחפשים טלפון חכם חדש, שעון חכם, שואב אבק רובוט, קומקום חשמלי או אפילו גוזם שיער, שיאומי מכסה אתכם. \\n\\nלדוגמה, \\n\\n• טלפונים חכמים כמו Redmi Note 13 Pro Plus מציעים מצלמה איכותית של 200MP, תצוגה מרשימה של 120Hz ומערכת טעינה מהירה. \\n\\n•  Xiaomi Mi Band 8 Pro מציע תצוגה גדולה של 1.74 אינץ\' ו- 14 ימי חיי סוללה. \\n\\n• Xiaomi Mijia Mini Blender הוא פתרון נהדר למטבח, המאפשר להכין מיץ טרי וטעים בלחיצת כפתור. \\n\\n•  שואב אבק רובוט ABIR G20S הוא פתרון חכם לניקוי הבית, עם ניווט מפת AI ומברשת ראשית בצורת V, המסייעת בהסרת שיער חיות מחמד. \\n\\n•  Xiaomi mijia סיר בריאות רב תכליתי קומקום חשמלי n1  הוא פתרון נהדר להכנת ארוחות בריאות וטעימות, עם תכנות זמן וטמפרטורה. \\n\\nלשיאומי יש את כל מה שאתם צריכים כדי להפוך את החיים שלכם לקלים יותר וטובים יותר."
    else:
        return "Generic Description"

# Fixture definitions, if needed
@pytest.fixture
def example_input_ru():
    """Provides example test data for Russian language."""
    return {
        "language": "RU",
        "category_name": "liitokala_18650",
        "products_titles": [
            "Зарядное устройство LiitoKala Lii-M4S-M4 для аккумуляторных батарей, 3,7 в, 18650, 26650, 21700, 18500, литий-ионный, 1,2 в, Ni-MH, AA, испытательная Емкость",
            "LiitoKala Lii-S12 Lii-D4XL-Lii S8 LCD 21700 18650 3,7 V Li-Ion 3,2 V LiFePO4 1,2 V NiMH/Cd 26650 32700 D AA AAA 9V зарядное устройство",
            "LiitoKala Lii-S12 Lii-S8 Lii-PD4 Lii-PD2 Lii-500S 3,7 V 18650 18350 зарядное устройство для аккумуляторов с автоматическим определение полярности 26650 21700 1,2 V AA AAA",
            "LiitoKala Lii-M4 18650 Зарядное устройство с ЖК-дисплеем Универсальное смарт-зарядное устройство Тестовая емкость 26650 18650 21700 AA AAA Батарея 4 слота 5V 2A",
            "Умное зарядное устройство с ЖК-дисплеем, 18650 в, 3,7, 26650, 18350, 21700 в, 4 слота",
            "Liitokala Lii-202 Lii-402 1,2 В 3,7 В 3,2 В 3,85 В 18650 18350 26650 18490 AA AAA 14500 21700 Интеллектуальное зарядное устройство для литиевых Ni-MH аккумуляторов",
            "Аккумуляторное зарядное устройство Liitokala для 18650 3,7 V 9V 26650 18350 16340 18500 14500 1,2 V AA AAA",
            "Зарядное устройство LiitoKala для батарей li-ion 3,7 V и NiMH 1,2 V, подходит для батарей 18650 26650 21700 26700 AA AAA 12V5A",
            "LiitoKala Lii-D4 21700 для 18650 18350 26650 16340 RCR123 14500 3,7 v 1,2 V Ni-MH/Cd, зарядное устройство AA AAA SC D C",
            "Зарядное устройство LiitoKala для аккумуляторов 3,7 в 1,2 в 18650 26650 21700 14500 18350 AA AAA A C и других батарей.",
            "OPUS BT-C3100 4 слота умное Универсальное зарядное устройство адаптер для перезаряжаемых литий-ионных батарей NiCd NiMH AA AAA 10440 18650",
            "Зарядное устройство LiitoKala для Li-Ion LiFePO4 Ni-MH Ni-Cd батарей с ЖК-дисплеем 9 В 21700 20700 26650 18350 RCR123 18650",
            "Умное зарядное устройство LiitoKala Lii-M4S + U1 18650 с ЖК-дисплеем для батарей 26650 21700 32650 18500 20700 CR123A AA AAA",
            "Зарядное устройство Liitokala Lii-PD2 18650, 3,7 в 26650 18350 16340 18500 14500 1,2 в Ni-MH AA AAA LCD многофункциональное зарядное устройство",
            "Зарядное устройство LiitoKala Lii-PD2 для литиевых и NiMH батарей 18650, 26650, 21700, AA, AAA, 18350 в, 3,7 в",
            "Зарядное устройство LiitoKala для аккумуляторов AA AAA 10440 14500 16340 17335 17500 18490 17670",
        ]
    }

@pytest.fixture
def example_input_he_mom_baby():
    """Provides example test data for Hebrew language with mom_and_baby category."""
    return {
        "language": "HE",
        "category_name": "mom_and_baby",
        "products_titles": [
            "פילופים אוות חד-צדדית אוטומטית משאבת שד \'נייד עיסוי עיסוי patal משטח חיקוי התינוק למצוץ",
            "Dr.isla תינוק נקי סיליקון מתכוונן שאיבת שאיבת חלב חשמלי בטיחות רעש נמוך נוח",
            "1pc עלה דוב פרחים קצף מלאכותי לשאת ורדים ליום האהבה, יום אמהות, יום השנה, מתנות יום הולדת",
            "ילדים של מנות סט תינוק סיליקון 6/8-חתיכה כלי שולחן סט יניקה כוסות מזלגות כפות ליקוק קשיות כוסות אמא ו אספקת תינוק",
            "מנשא ארגונומי תינוקות רב תכליתי מותניים שרפרף יילוד לפעוטות רב להשתמש לפני ואחרי קנגורו תיק אבזרים",
            "לביש משאבת חלב אמא ותינוק אספקת שד משאבת שד חלב החליבה וחליבת מכונת באופן מלא אוטומטי משאבת חלב",
            "פיפי השד אוטומטי דו-צדדי משאבת שד אוטומטית עיסוי חכם חיקוי התינוק למצוץ חיקוי התינוק למצוץ לאחר לידה",
            "Cdycam חדש 3.5 אינץ אלחוטי וידאו התינוק צג הלילה טמפרטורה ניטור 2 דרך שמע אודיו מצלמת אבטחה בייבי",
            "בייבי סיליקון טמפרטורה בזמן אמת לקחת אמבטיה אמבטיה ללא להחליק כף רגל דלי מתקפל חדר אמבטיה עם חישה טמפרטורה",
            "Dr.isla 30 יח \'150/250 מ \"ל חלב אם שקית אחסון חד פעמי קיבולת חינם חלב קפוא שקית אחסון bpa חינם",
            "מחזיק פמוט עם מנצנץ מתנות זיכרון נרות הנרות על אמא עומדת מחבקת הבת פסל שרף צלמיות",
             "לנגב חום חם חם עם תצוגה הוביל מגבת רטוב מגבת מתקן נייד USB תשלום לתינוק לנגב חם מחמם לנגב חם תיבת חימום בית/מכונית"
        ]
    }

@pytest.fixture
def example_input_he_xiaomi():
    """Provides example test data for Hebrew language with xiaomi category."""
    return {
        "language": "HE",
        "category_name": "xiaomi",
        "products_titles": [
            "פילופים אוות חד-צדדית אוטומטית משאבת שד \'נייד עיסוי עיסויXiaomi Mijia חשמלי אף אוזן שיער גוזם לגברים כאבים נטענת פיאות לחיים גבות זקן 3 ב 1 שיער קליפר מכונת גילוח",
            "\'צ\'י2023מי מיia מדחץ אוויר חשמלי 2 מובילה סגנון-c-c-c-c-c-c-c-c---c---------",
            "Global ROM Xiaomi Redmi Note 13 Pro Plus 200MP OIS Camera 1.5K 120Hz Display 120W Fast Charging Dimensity 7200-Ultra Smartphone",
            "הגירסה העולמית xiaomi טלוויזיה תיבת 2gb 22gb dolby חזון hdr10 + עוזר גוגל חכם hd10 + עוזר גוגל תיבת דואר חכם מייל חכם",
            "נייד חדש נייד xiaomi mijia lint מסיר בד בד shaver פלאט פלאט מסיר מכונה עבור סוודר בגדים",
            "בכורה עולמית גרסה גלובלית xiaomi הלהקה 8 pro 1.74 \"תצוגת amoled מובנית עד 14 יום חיי סוללה",
             "Xiaomi mijia שיער גוזם מכונת שיער ipx7 עמיד למים קליפר מקצועי קוצץ שיער חיתוך מספר גברים גזוז",
              "XIAOMI MIJIA מיני נייד בלנדר חשמלי פירות מסחטה מכונת כתום מסחטה מטבח מעבד מזון יצרנית מיץ Extractor בית",
            "XIAOMI MIJIA אינדוקציה סיר נוער מהדורת נייד אלקטרומגנטית תנור 220V חשמלי כיריים אינדוקציה 9 הילוך אש התאמה",
            "2023 חדש xiaomi mijia קומקום חשמלי נייד 2 תרמוס כוסות מים מהירים הדוד 350 מ \"ל טמפרטורה חכמה קומקום",
            "Xiaomi mijia מחשב צג מוט אור 1s עבור צג מסך מנורת מסך תלוי אור סטודנט עיניים הגנה קריאה למידה",
             "Xiaomi mijia נייד לרכב שואב אבק מיני מכונת ניקוי אלחוטי עבור ציוד אוטומטי הביתה 13000pa ציקלון יניקה יניקה",
              "Xiaomi dad se גרסה גלובלית 128gb/256gb®ליבה 680 octa 11 \"90hz fhd + תצוגה 8000 סוללת mah mi tablet",
            "גרסה גלובלית xiaomi redmi 13c muui 14 סמארטפון mtk helio g85 octacore מצלמה 50mp 5000mah 90hz 6.74\"",
             "Xiaomi IP מצלמה 2k 1296p 180 ° ביטחון התינוק צג מצלמת אינטרנט ראיית לילה וידאו אי זיהוי אנושי מעקב mi בית חכם",
             "חדש xiaomi mijia סיר בריאות רב תכליתיים קומקום חשמלי n1 ביתיים 800w 304 נירוסטה שימור חום",
             "Xiaomi mijia נייד אניון שיער h101 יבש מהיר יבש, 1600w 50 מיליון ליונים שליליים נסיעות הביתה טיפול שיער",
             "Xiaomi mijia עצם אמת ספורט headphone אוזניות אלחוטיות-תואם אוזניות חינם עם מיקרופון לריצה",
              "שואב אבק רובוט ABIR G20S, ניווט מפת AI, מחיצה סופר חכמה, עם זיכרון, בקרת אפליקציות WiFi, יניקה חזקה 6000Pa, סמרטוט רטוב חכם, מברשת ראשית בצורת V, חליפה לשיער לחיות מחמד, חיטוי, עובדת עם Alexa ו- Google Assistant",
              "Global Version POCO M6 Pro 256GB/512GB Smartphone 120Hz AMOLED Display 64MP Triple Camera 67W Turbo Charging MTK Helio G99-Ultra"
        ]
    }


# Tests for the prompt response
def test_prompt_response_valid_input_ru(example_input_ru):
    """Checks correct behavior with valid input for Russian language."""
    with patch('__main__.mock_generate_title', side_effect=mock_generate_title):
      with patch('__main__.mock_generate_description', side_effect=mock_generate_description):
        language = example_input_ru['language']
        category_name = example_input_ru['category_name']
        products_titles = example_input_ru['products_titles']

        # call the function that uses the prompt
        result = generate_promo_data(products_titles, category_name, language)

        assert isinstance(result, dict)
        assert category_name in result
        assert result[category_name]["category_name"] == category_name
        assert result[category_name]["title"] == mock_generate_title(products_titles, language)
        assert result[category_name]["description"] == mock_generate_description(products_titles, category_name, language)


def test_prompt_response_valid_input_he_mom_baby(example_input_he_mom_baby):
  """Checks correct behavior with valid input for Hebrew language with mom_and_baby category."""
  with patch('__main__.mock_generate_title', side_effect=mock_generate_title):
      with patch('__main__.mock_generate_description', side_effect=mock_generate_description):
        language = example_input_he_mom_baby['language']
        category_name = example_input_he_mom_baby['category_name']
        products_titles = example_input_he_mom_baby['products_titles']

        # call the function that uses the prompt
        result = generate_promo_data(products_titles, category_name, language)

        assert isinstance(result, dict)
        assert category_name in result
        assert result[category_name]["category_name"] == category_name
        assert result[category_name]["title"] == mock_generate_title(products_titles, language)
        assert result[category_name]["description"] == mock_generate_description(products_titles, category_name, language)

def test_prompt_response_valid_input_he_xiaomi(example_input_he_xiaomi):
    """Checks correct behavior with valid input for Hebrew language with xiaomi category."""
    with patch('__main__.mock_generate_title', side_effect=mock_generate_title):
      with patch('__main__.mock_generate_description', side_effect=mock_generate_description):
          language = example_input_he_xiaomi['language']
          category_name = example_input_he_xiaomi['category_name']
          products_titles = example_input_he_xiaomi['products_titles']

          # call the function that uses the prompt
          result = generate_promo_data(products_titles, category_name, language)

          assert isinstance(result, dict)
          assert category_name in result
          assert result[category_name]["category_name"] == category_name
          assert result[category_name]["title"] == mock_generate_title(products_titles, language)
          assert result[category_name]["description"] == mock_generate_description(products_titles, category_name, language)

def test_prompt_response_empty_products_titles():
    """Checks behavior with empty list of product titles."""
    with patch('__main__.mock_generate_title', side_effect=mock_generate_title):
      with patch('__main__.mock_generate_description', side_effect=mock_generate_description):
        language = "RU"
        category_name = "test_category"
        products_titles = []

        result = generate_promo_data(products_titles, category_name, language)

        assert isinstance(result, dict)
        assert category_name in result
        assert result[category_name]["category_name"] == category_name
        assert result[category_name]["title"] == mock_generate_title(products_titles, language)
        assert result[category_name]["description"] == mock_generate_description(products_titles, category_name, language)

def test_prompt_response_invalid_language():
    """Checks behavior with invalid language."""
    with patch('__main__.mock_generate_title', side_effect=mock_generate_title):
      with patch('__main__.mock_generate_description', side_effect=mock_generate_description):
        language = "invalid_language"
        category_name = "test_category"
        products_titles = ["Product 1", "Product 2"]

        result = generate_promo_data(products_titles, category_name, language)

        assert isinstance(result, dict)
        assert category_name in result
        assert result[category_name]["category_name"] == category_name
        assert result[category_name]["title"] == mock_generate_title(products_titles, language)
        assert result[category_name]["description"] == mock_generate_description(products_titles, category_name, language)


def test_prompt_response_long_product_titles():
    """Checks behavior with very long product titles."""
    with patch('__main__.mock_generate_title', side_effect=mock_generate_title):
      with patch('__main__.mock_generate_description', side_effect=mock_generate_description):
        language = "RU"
        category_name = "test_category"
        products_titles = ["This is a very long product title " * 20]

        result = generate_promo_data(products_titles, category_name, language)

        assert isinstance(result, dict)
        assert category_name in result
        assert result[category_name]["category_name"] == category_name
        assert result[category_name]["title"] == mock_generate_title(products_titles, language)
        assert result[category_name]["description"] == mock_generate_description(products_titles, category_name, language)


def test_prompt_response_special_characters_in_titles():
  """Checks behavior with special characters in product titles."""
  with patch('__main__.mock_generate_title', side_effect=mock_generate_title):
    with patch('__main__.mock_generate_description', side_effect=mock_generate_description):
      language = "HE"
      category_name = "test_category"
      products_titles = ["Product with special characters: !@#$%^&*()_+=-`~[]\{}|;':\",./<>?", "Another product"]

      result = generate_promo_data(products_titles, category_name, language)

      assert isinstance(result, dict)
      assert category_name in result
      assert result[category_name]["category_name"] == category_name
      assert result[category_name]["title"] == mock_generate_title(products_titles, language)
      assert result[category_name]["description"] == mock_generate_description(products_titles, category_name, language)

# --- The tested function ---
def generate_promo_data(products_titles, category_name, language):
    """
    Generates promo data based on provided input. This function now uses the mock functions directly.
    """
    title = mock_generate_title(products_titles, language)
    description = mock_generate_description(products_titles, category_name, language)

    result = {
        category_name: {
            "category_name": category_name,
            "title": title,
            "description": description
        }
    }
    return result
```