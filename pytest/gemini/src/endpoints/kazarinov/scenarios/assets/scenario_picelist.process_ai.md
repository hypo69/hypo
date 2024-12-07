```python
import pytest
import json

# Mock classes for testing (replace with actual implementations if available)
class AI_Model:
    def process_products(self, products_list, attempts):
        # Mock AI model response
        if attempts == 0:
          return None
        if attempts == 1:
          return {"ru": "value", "he": "otherValue"}
        elif attempts == 2:
          return [{"ru": "anotherValue", "he": "anotherOtherValue"}]
        elif attempts == 3:
          return {"ru": "value", "he": "otherValue", "extra": "data"}
        elif attempts == 4:
          return "invalid data"
        return {"ru": "valid_ru", "he": "valid_he"}



class Logger:
    def log_error(self, message):
        print(f"Error logged: {message}")



class User:
  def extract_ru_he(self, data):
    if isinstance(data, dict):
      return data.get('ru'), data.get('he')
    elif isinstance(data, list):
      if data:
        return data[0].get('ru'), data[0].get('he')
      else:
        return None, None
    else:
      return None, None


def process_products(products_list, ai_model, logger, attempts=3):
  """Processes products using the AI model."""

  for attempt in range(attempts):
    response = ai_model.process_products(products_list, attempt)
    if response is None:
      logger.log_error("no response from gemini")
      continue

    if isinstance(response, str):
      logger.log_error("Error in data from gemini")
      continue
      

    try:
      ru, he = User().extract_ru_he(response)
      if ru is None or he is None:
        logger.log_error("Проблема парсинга ответа")
        continue
      if not (ru and he):
        logger.log_error("Invalid ru or he data")
        continue
      return ru, he
    except (KeyError, IndexError):
      logger.log_error("Error in data from gemini")
      continue
  return None, None

# Fixtures
@pytest.fixture
def ai_model():
  return AI_Model()

@pytest.fixture
def logger():
  return Logger()


# Tests
def test_process_products_valid_input(ai_model, logger):
  products_list = "some_products"
  ru, he = process_products(products_list, ai_model, logger)
  assert ru == "valid_ru"
  assert he == "valid_he"

def test_process_products_invalid_data(ai_model, logger):
  products_list = "some_products"
  ru, he = process_products(products_list, ai_model, logger, attempts=4)  
  assert ru is None
  assert he is None
  
def test_process_products_list_input(ai_model, logger):
  products_list = "some_products"
  ru, he = process_products(products_list, ai_model, logger)
  assert ru == "anotherValue"
  assert he == "anotherOtherValue"
  

def test_process_products_no_response(ai_model, logger):
  products_list = "some_products"
  ru, he = process_products(products_list, ai_model, logger, attempts=1)  
  assert ru is None
  assert he is None

# Example test for error handling (replace with specific error checks if possible)
def test_process_products_error_response(ai_model, logger):
  products_list = "some_products"
  ru, he = process_products(products_list, ai_model, logger, attempts=4)
  assert ru is None
  assert he is None

```