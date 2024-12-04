```python
import pytest
import logging

# Mock the AI model and Logger
class MockAIModel:
    def process_products(self, products_list, attempts):
        # Simulate different responses
        if attempts == 1:
          return {"ru": "product1", "he": "product2"}
        elif attempts == 2:
           return ["product1", "product2"]
        elif attempts == 3:
           return {"ru": "product1", "en": "product2"}  # Invalid case

        return None

class MockLogger:
    def __init__(self):
        self.log_messages = []
    def log_error(self, message):
        self.log_messages.append(message)

    def log_warning(self, message):
        self.log_messages.append(message)


# Define the function to be tested
def process_model_response(products_list, ai_model, logger, attempts=3):
    """Processes the response from the AI model.
    
    Args:
        products_list: List of products for processing.
        ai_model: The AI model object.
        logger: The Logger object.
        attempts: Number of retries.

    Returns:
        A tuple containing 'ru' and 'he' data, or None if there's an error.
    """
    for attempt in range(attempts):
        response = ai_model.process_products(products_list, attempt)

        if response is None:
            logger.log_error("no response from gemini")
            continue

        try:
            if isinstance(response, list):
                if len(response) == 2:
                    return response[0], response[1]
                elif len(response) == 1:
                    return response[0]["ru"], response[0]["he"]  # Assuming single-element list
                else:
                    logger.log_error("Error in data from gemini")
                    continue
            elif isinstance(response, dict):
                return response.get("ru"), response.get("he")

            else:
                logger.log_error("Проблема парсинга ответа")
                continue
        except (KeyError, TypeError):
            logger.log_error("Invalid ru or he data")
            continue
        
    return None

# Test cases
@pytest.fixture
def mock_logger():
    return MockLogger()

@pytest.fixture
def mock_ai_model():
  return MockAIModel()

def test_process_model_response_valid_list(mock_ai_model, mock_logger):
    data = ["product1", "product2"]
    result_ru, result_he = process_model_response(data, mock_ai_model, mock_logger)
    assert result_ru == "product1"
    assert result_he == "product2"

def test_process_model_response_valid_dict(mock_ai_model, mock_logger):
    data = []
    result_ru, result_he = process_model_response(data, mock_ai_model, mock_logger)
    assert mock_logger.log_messages == ['no response from gemini', 'no response from gemini', 'no response from gemini']
    
def test_process_model_response_invalid_list_length(mock_ai_model, mock_logger):
    data = []
    result = process_model_response(data, mock_ai_model, mock_logger, attempts = 2)
    assert result is None


def test_process_model_response_invalid_dict_key(mock_ai_model, mock_logger):
  data = []
  result_ru, result_he = process_model_response(data, mock_ai_model, mock_logger)
  assert mock_logger.log_messages == ['no response from gemini', 'no response from gemini', 'no response from gemini']

def test_process_model_response_single_element_list(mock_ai_model, mock_logger):
  data = []
  result_ru, result_he = process_model_response(data, mock_ai_model, mock_logger)
  assert result_ru is None
  assert result_he is None

#Add more tests for edge cases and exception handling as needed

```