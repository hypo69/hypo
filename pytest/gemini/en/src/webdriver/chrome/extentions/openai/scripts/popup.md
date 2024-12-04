```python
import pytest
import js2py

# Mock the AngularJS $http service for testing
class MockHttp:
    def get(self, url):
        # Mock data for assistants (replace with your actual data)
        if url == 'http://localhost:8000/assistants':
            return {'data': [{'id': 1, 'name': 'Assistant 1'}, {'id': 2, 'name': 'Assistant 2'}]}
        else:
            return None

    def post(self, url, data):
        # Mock response (replace with your actual data)
        if url == 'http://localhost:8000/ask':
            if data['assistant_id'] == 1:
                return {'data': {'response': 'Response from Assistant 1'}}
            elif data['assistant_id'] == 2:
                return {'data': {'response': 'Response from Assistant 2'}}
            else:
                return {'data': {'response': 'Invalid assistant ID'}}
        else:
            return None

#  Convert AngularJS code to Python using js2py
angular_code = """
// Инициализируем Angular приложение
const app = angular.module('openaiApp', []);

// Контроллер для обработки логики
app.controller('MainController', function ($scope, $http) {
    $scope.message = '';
    $scope.response = '';
    $scope.assistants = [];
    $scope.selectedAssistant = null;

    // Функция для получения списка ассистентов
    function loadAssistants() {
        const url = 'http://localhost:8000/assistants';
        $http.get(url)
            .then(function (response) {
                $scope.assistants = response.data;
            })
            .catch(function (error) {
                console.error('Ошибка загрузки ассистентов:', error);
            });
    }

    loadAssistants();

    // Функция для отправки сообщения модели
    $scope.sendMessage = function () {
        const url = 'http://localhost:8000/ask';

        const data = {
            message: $scope.message,
            system_instruction: "You are a helpful assistant.",
            assistant_id: $scope.selectedAssistant.id
        };

        $http.post(url, data)
            .then(function (response) {
                $scope.response = response.data.response;
            })
            .catch(function (error) {
                console.error('Ошибка:', error);
                $scope.response = 'Произошла ошибка. Попробуйте позже.';
            });
    };
});
"""

main_controller = js2py.eval_js(angular_code)


@pytest.fixture
def http_mock():
    return MockHttp()


def test_load_assistants(http_mock):
    # Check if loadAssistants successfully loads assistants
    main_controller.loadAssistants()
    assert len(main_controller.$scope.assistants) == 2
    assert main_controller.$scope.assistants[0]['id'] == 1
    assert main_controller.$scope.assistants[1]['id'] == 2

def test_send_message_success(http_mock):
    #Valid input, check response
    main_controller.$scope.message = "Test message"
    main_controller.$scope.selectedAssistant = {'id': 1}
    main_controller.sendMessage()
    assert main_controller.$scope.response == 'Response from Assistant 1'

def test_send_message_error_invalid_assistant(http_mock):
    # Invalid assistant ID - check error handling
    main_controller.$scope.message = "Test message"
    main_controller.$scope.selectedAssistant = {'id': 3}  # Invalid ID
    main_controller.sendMessage()
    assert main_controller.$scope.response == 'Invalid assistant ID'



def test_send_message_error(http_mock):
    # Mock error for testing error handling
    mocked_error = Exception("Simulated error")
    http_mock.post = lambda url, data: {"data": {"response": mocked_error}}
    main_controller.$scope.message = "Test message"
    main_controller.$scope.selectedAssistant = {'id': 1}
    main_controller.sendMessage()
    assert main_controller.$scope.response == 'Произошла ошибка. Попробуйте позже.'
```