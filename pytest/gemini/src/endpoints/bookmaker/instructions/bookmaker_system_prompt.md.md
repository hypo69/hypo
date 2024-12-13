```python
import pytest
import json

# Fixture definitions, if needed
@pytest.fixture
def valid_forecastable_data():
    """Provides valid forecastable data."""
    return "[12, 14, 15, 20, 25, 30, 35]"

@pytest.fixture
def valid_tabular_data():
     """Provides valid tabular data."""
     return "dates,sales,categories\n2023-01-01,100,A\n2023-01-02,120,B\n2023-01-03,130,A"

@pytest.fixture
def non_forecastable_data():
    """Provides non-forecastable data."""
    return "This is a text with no patterns to analyse for forecasting"

@pytest.fixture
def empty_data():
    """Provides empty data."""
    return ""

@pytest.fixture
def invalid_format_data():
    """Provides data with invalid format."""
    return "[12, 14, 15, 'a', 25]"

def analyze_data(data):
    """
    Analyzes the input data and returns a JSON response according to the provided prompt.
    
    This function will be replaced with the actual implementation
    """
    if not data:
        return {
          "is_forecastable": False,
          "analysis": {
            "reason": "No input data provided."
          },
        "forecast": None
        }

    if "text" in data.lower() or "no patterns" in data.lower():
            return {
                "is_forecastable": False,
                "analysis": {
                    "reason": "Недостаточно данных или структура данных не подходит для прогнозирования"
                },
                 "forecast": None
              }

    if data.startswith("[") and data.endswith("]"):
      try:
        numbers = json.loads(data)
        if all(isinstance(n, (int, float)) for n in numbers):
            if len(numbers) >= 3:
               return {
                    "is_forecastable": True,
                    "analysis": {
                    "patterns_detected": "Возможен восходящий тренд",
                    "trend": "Линейный восходящий тренд",
                    "forecast_period": "На следующие 2-3 шага"
                    },
                     "forecast": "Пример прогноза: 40, 45"
                  }
            else:
                  return {
                    "is_forecastable": False,
                    "analysis": {
                      "reason": "Недостаточно данных для прогнозирования"
                    },
                      "forecast": None
                }
      except json.JSONDecodeError:
             return {
              "is_forecastable": False,
              "analysis": {
                  "reason": "Invalid format"
              },
              "forecast": None
             }
    elif "dates" in data and "sales" in data:
            return {
            "is_forecastable": True,
            "analysis": {
               "patterns_detected": "Анализ временных рядов возможных продаж",
                "trend": "Невозможно определить без более детальных данных",
                 "forecast_period": "Будущие даты продаж"
             },
              "forecast": "Предварительный прогноз: увеличение продаж"
            }

    return {
          "is_forecastable": False,
          "analysis": {
             "reason": "Недостаточно данных или структура данных не подходит для прогнозирования"
         },
          "forecast": None
      }

# Tests for analyze_data
def test_analyze_data_valid_forecastable_input(valid_forecastable_data):
    """Checks correct behavior with valid forecastable data."""
    result = analyze_data(valid_forecastable_data)
    assert result["is_forecastable"] == True
    assert result["analysis"]["patterns_detected"] == "Возможен восходящий тренд"
    assert result["forecast"] is not None

def test_analyze_data_valid_tabular_input(valid_tabular_data):
    """Checks correct behavior with valid tabular data."""
    result = analyze_data(valid_tabular_data)
    assert result["is_forecastable"] == True
    assert result["analysis"]["patterns_detected"] == "Анализ временных рядов возможных продаж"
    assert result["forecast"] is not None

def test_analyze_data_non_forecastable_input(non_forecastable_data):
    """Checks correct behavior with non-forecastable text input."""
    result = analyze_data(non_forecastable_data)
    assert result["is_forecastable"] == False
    assert "reason" in result["analysis"]
    assert result["forecast"] is None

def test_analyze_data_empty_input(empty_data):
    """Checks correct behavior with empty input."""
    result = analyze_data(empty_data)
    assert result["is_forecastable"] == False
    assert "No input data provided" in result["analysis"]["reason"]
    assert result["forecast"] is None

def test_analyze_data_invalid_format_input(invalid_format_data):
    """Checks correct handling of invalid format input."""
    result = analyze_data(invalid_format_data)
    assert result["is_forecastable"] == False
    assert result["analysis"]["reason"] == "Invalid format"
    assert result["forecast"] is None

def test_analyze_data_short_sequence_input():
    """Checks behavior with short sequence."""
    short_sequence = "[1,2]"
    result = analyze_data(short_sequence)
    assert result["is_forecastable"] == False
    assert "Недостаточно данных для прогнозирования" in result["analysis"]["reason"]
    assert result["forecast"] is None

def test_analyze_data_no_json_input():
  """Check behavior when input is not parsable to json"""
  not_json_string = "random string"
  result = analyze_data(not_json_string)
  assert result["is_forecastable"] == False
  assert "Недостаточно данных или структура данных не подходит для прогнозирования" in result["analysis"]["reason"]
  assert result["forecast"] is None
```