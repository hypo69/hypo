```python
import pytest
import json

# Fixture to load the json data
@pytest.fixture
def string_formatter_data():
    """Provides the json data for testing."""
    json_data = """
    {
      "he": {
        "consoles": {
          "Мodel": {
            "he": [ "דגם" ],
            "ru": [ "модель" ]
          },
          "Region": {
            "he": [ "שיטת שידור" ],
            "ru": [ "регион" ]
          },
          "Overview": {
            "he": [ "סקירה" ],
            "ru": [ "обзор" ]
          },
    
          "CPU": {
            "he": [ "מעבד CPU" ],
            "ru": [ "ЦПУ" ]
          },
    
          "GPU": {
            "he": [ "מעבד גראפי" ,"gpu"],
            "ru": [ "ГПУ" , "графический процессор", "gpu"] },
          "ram": {"he": "זיכרון RAM" },
    
          "storage": {
            "he": [ "אחסון", "כונן" ],
            "ru": ["Диск", "Жесткий диск"]
          },
            "optical drive": {
              "he": [ "כונן אופטי" ],
              "ru": [ "оптический привод" ]
            },
            "Bandwidth": {
              "he": "רוחב פס",
              "ru": ""
            },
            "connections": {
              "he": "חיבור",
              "ru": ""
            },
    
            "streaming": {
              "he": "הזרמת וידאו",
              "ru": ""
            },
            "Xbox Game Pass": {
              "he": "",
              "ru": ""
            },
            "What's in the box": {
              "he": "",
              "ru": ""
            },
            "Games": {
              "he": "המשחקים הטובים ביותר",
              "ru": ""
            },
            "multiplayer": {
              "he": "שירות המולטי-פלייר הטוב ביותר",
              "ru": "мультиплеер"
            },
    
              "Dimensions": "מידות",
              "weight": "משקל",
              "YouTube video": "סרטון יוטיוב",
              "Information from the manufacturer": "מידע מהיצרן",
              "Important note!": "הערה חשובה!"
    
            }
          },
            "ru": { "consoles": [ "cpu" ] }
          }
    """
    return json.loads(json_data)

# Tests for the 'he' language
def test_hebrew_model_translation(string_formatter_data):
    """Checks if 'Model' is translated correctly to Hebrew."""
    assert string_formatter_data["he"]["consoles"]["Мodel"]["he"] == ["דגם"]

def test_hebrew_region_translation(string_formatter_data):
    """Checks if 'Region' is translated correctly to Hebrew."""
    assert string_formatter_data["he"]["consoles"]["Region"]["he"] == ["שיטת שידור"]

def test_hebrew_overview_translation(string_formatter_data):
     """Checks if 'Overview' is translated correctly to Hebrew."""
     assert string_formatter_data["he"]["consoles"]["Overview"]["he"] == ["סקירה"]

def test_hebrew_cpu_translation(string_formatter_data):
    """Checks if 'CPU' is translated correctly to Hebrew."""
    assert string_formatter_data["he"]["consoles"]["CPU"]["he"] == ["מעבד CPU"]

def test_hebrew_gpu_translation(string_formatter_data):
    """Checks if 'GPU' is translated correctly to Hebrew, including multiple options."""
    assert string_formatter_data["he"]["consoles"]["GPU"]["he"] == ["מעבד גראפי", "gpu"]

def test_hebrew_ram_translation(string_formatter_data):
    """Checks if 'ram' is translated correctly to Hebrew."""
    assert string_formatter_data["he"]["consoles"]["ram"]["he"] == "זיכרון RAM"

def test_hebrew_storage_translation(string_formatter_data):
    """Checks if 'storage' is translated correctly to Hebrew, including multiple options."""
    assert string_formatter_data["he"]["consoles"]["storage"]["he"] == ["אחסון", "כונן"]

def test_hebrew_optical_drive_translation(string_formatter_data):
    """Checks if 'optical drive' is translated correctly to Hebrew."""
    assert string_formatter_data["he"]["consoles"]["optical drive"]["he"] == ["כונן אופטי"]

def test_hebrew_bandwidth_translation(string_formatter_data):
    """Checks if 'Bandwidth' is translated correctly to Hebrew."""
    assert string_formatter_data["he"]["consoles"]["Bandwidth"]["he"] == "רוחב פס"

def test_hebrew_connections_translation(string_formatter_data):
     """Checks if 'connections' is translated correctly to Hebrew."""
     assert string_formatter_data["he"]["consoles"]["connections"]["he"] == "חיבור"

def test_hebrew_streaming_translation(string_formatter_data):
    """Checks if 'streaming' is translated correctly to Hebrew."""
    assert string_formatter_data["he"]["consoles"]["streaming"]["he"] == "הזרמת וידאו"

def test_hebrew_games_translation(string_formatter_data):
     """Checks if 'Games' is translated correctly to Hebrew."""
     assert string_formatter_data["he"]["consoles"]["Games"]["he"] == "המשחקים הטובים ביותר"

def test_hebrew_multiplayer_translation(string_formatter_data):
    """Checks if 'multiplayer' is translated correctly to Hebrew."""
    assert string_formatter_data["he"]["consoles"]["multiplayer"]["he"] == "שירות המולטי-פלייר הטוב ביותר"

def test_hebrew_dimensions_translation(string_formatter_data):
     """Checks if 'Dimensions' is translated correctly to Hebrew."""
     assert string_formatter_data["he"]["consoles"]["Dimensions"] == "מידות"

def test_hebrew_weight_translation(string_formatter_data):
     """Checks if 'weight' is translated correctly to Hebrew."""
     assert string_formatter_data["he"]["consoles"]["weight"] == "משקל"

def test_hebrew_youtube_video_translation(string_formatter_data):
     """Checks if 'YouTube video' is translated correctly to Hebrew."""
     assert string_formatter_data["he"]["consoles"]["YouTube video"] == "סרטון יוטיוב"

def test_hebrew_manufacturer_info_translation(string_formatter_data):
     """Checks if 'Information from the manufacturer' is translated correctly to Hebrew."""
     assert string_formatter_data["he"]["consoles"]["Information from the manufacturer"] == "מידע מהיצרן"

def test_hebrew_important_note_translation(string_formatter_data):
    """Checks if 'Important note!' is translated correctly to Hebrew."""
    assert string_formatter_data["he"]["consoles"]["Important note!"] == "הערה חשובה!"


# Tests for the 'ru' language
def test_russian_model_translation(string_formatter_data):
    """Checks if 'Model' is translated correctly to Russian."""
    assert string_formatter_data["he"]["consoles"]["Мodel"]["ru"] == ["модель"]

def test_russian_region_translation(string_formatter_data):
    """Checks if 'Region' is translated correctly to Russian."""
    assert string_formatter_data["he"]["consoles"]["Region"]["ru"] == ["регион"]

def test_russian_overview_translation(string_formatter_data):
    """Checks if 'Overview' is translated correctly to Russian."""
    assert string_formatter_data["he"]["consoles"]["Overview"]["ru"] == ["обзор"]

def test_russian_cpu_translation(string_formatter_data):
    """Checks if 'CPU' is translated correctly to Russian."""
    assert string_formatter_data["he"]["consoles"]["CPU"]["ru"] == ["ЦПУ"]

def test_russian_gpu_translation(string_formatter_data):
    """Checks if 'GPU' is translated correctly to Russian, including multiple options."""
    assert string_formatter_data["he"]["consoles"]["GPU"]["ru"] == ["ГПУ", "графический процессор", "gpu"]

def test_russian_storage_translation(string_formatter_data):
    """Checks if 'storage' is translated correctly to Russian, including multiple options."""
    assert string_formatter_data["he"]["consoles"]["storage"]["ru"] == ["Диск", "Жесткий диск"]

def test_russian_optical_drive_translation(string_formatter_data):
    """Checks if 'optical drive' is translated correctly to Russian."""
    assert string_formatter_data["he"]["consoles"]["optical drive"]["ru"] == ["оптический привод"]

def test_russian_multiplayer_translation(string_formatter_data):
    """Checks if 'multiplayer' is translated correctly to Russian."""
    assert string_formatter_data["he"]["consoles"]["multiplayer"]["ru"] == "мультиплеер"

def test_russian_consoles_translation(string_formatter_data):
     """Checks if 'consoles' in ru language is correct."""
     assert string_formatter_data["ru"]["consoles"] == [ "cpu" ]

#Test for empty string
def test_empty_bandwidth_translation(string_formatter_data):
     """Checks if 'Bandwidth' is translated correctly to Russian and is empty"""
     assert string_formatter_data["he"]["consoles"]["Bandwidth"]["ru"] == ""

def test_empty_connections_translation(string_formatter_data):
    """Checks if 'connections' is translated correctly to Russian and is empty"""
    assert string_formatter_data["he"]["consoles"]["connections"]["ru"] == ""

def test_empty_streaming_translation(string_formatter_data):
    """Checks if 'streaming' is translated correctly to Russian and is empty"""
    assert string_formatter_data["he"]["consoles"]["streaming"]["ru"] == ""

def test_empty_xbox_game_pass_translation(string_formatter_data):
    """Checks if 'Xbox Game Pass' is translated correctly to Russian and is empty"""
    assert string_formatter_data["he"]["consoles"]["Xbox Game Pass"]["ru"] == ""

def test_empty_whats_in_the_box_translation(string_formatter_data):
     """Checks if 'What's in the box' is translated correctly to Russian and is empty"""
     assert string_formatter_data["he"]["consoles"]["What's in the box"]["ru"] == ""

def test_empty_games_translation(string_formatter_data):
    """Checks if 'Games' is translated correctly to Russian and is empty"""
    assert string_formatter_data["he"]["consoles"]["Games"]["ru"] == ""
```