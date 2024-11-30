```python
import pytest
import json

# Mock classes for testing purposes
class MockAIModel:
    def process_request(self, products_list, attempts):
        # Simulate different responses
        if attempts == 3:
            return {"ru": "Response RU", "he": "Response HE"}
        elif attempts == 2:
            return {"invalid": "data"}
        elif attempts == 1:
            return None
        else:
            raise Exception("Unexpected attempts")


class MockLogger:
    def log_error(self, message):
        self.error_messages = self.error_messages + [message] if hasattr(self, 'error_messages') else [message]

# The user-provided code, converted to Python functions
class ProcessAI:
    def __init__(self, ai_model, logger):
        self.ai_model = ai_model
        self.logger = logger
        self.logger.error_messages = []

    def process_products(self, products_list, attempts=3):
        try:
            response = self.ai_model.process_request(products_list, attempts)

            if response is None:
                self.logger.log_error("no response from gemini")
                return None
            
            try:
                if isinstance(response, list):
                    if len(response) == 2:
                        ru = response[0]
                        he = response[1]
                    elif len(response) == 1:
                        ru = response[0].get("ru")
                        he = response[0].get("he")
                    else:
                        self.logger.log_error("Проблема парсинга ответа")
                        return None
                elif isinstance(response, dict):
                    ru = response.get("ru")
                    he = response.get("he")
                else:
                    self.logger.log_error("Проблема парсинга ответа")
                    return None

                if ru is None or he is None:
                    self.logger.log_error("Invalid ru or he data")
                    return None
                
                return {"ru": ru, "he": he}
            except (AttributeError, KeyError, TypeError) as e:
              self.logger.log_error(f"Error in data from gemini {str(e)}")
              return None

        except Exception as e:
            self.logger.log_error(f"An error occurred processing products: {str(e)}")
            return None


# Fixtures for mocking
@pytest.fixture
def mock_ai_model():
    return MockAIModel()


@pytest.fixture
def mock_logger():
    return MockLogger()

# Test Cases
def test_process_products_valid_input(mock_ai_model, mock_logger):
    ai_processor = ProcessAI(mock_ai_model, mock_logger)
    products_list = [{"id": 1, "name": "product 1"}]
    result = ai_processor.process_products(products_list)
    assert result == {"ru": "Response RU", "he": "Response HE"}
    assert not mock_logger.error_messages

def test_process_products_invalid_input(mock_ai_model, mock_logger):
    ai_processor = ProcessAI(mock_ai_model, mock_logger)
    products_list = [{"id": 1, "name": "product 1"}]
    result = ai_processor.process_products(products_list, attempts=2)
    assert result is None
    assert "Error in data from gemini" in mock_logger.error_messages[0]

def test_process_products_no_response(mock_ai_model, mock_logger):
    ai_processor = ProcessAI(mock_ai_model, mock_logger)
    products_list = [{"id": 1, "name": "product 1"}]
    result = ai_processor.process_products(products_list, attempts=1)
    assert result is None
    assert "no response from gemini" in mock_logger.error_messages[0]


```