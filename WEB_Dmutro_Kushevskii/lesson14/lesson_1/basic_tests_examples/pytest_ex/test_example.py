import requests
from unittest.mock import Mock, patch

import pytest

def devide_numbers(x, y):
    return x / y


def multiply_numbers(x, y):
    return x * y


def test_multiply_two_positive_numbers(log):
    result = multiply_numbers(2, 3)

    log.write(f"Very important log\n")

    assert result == 6, f"{result} != 6"


@pytest.mark.parametrize("a, b, result", [
    (3, 1, 3),
    (6, 2, 3),
])
def test_devide_two_positive_numbers(a, b, result, log):
    log.write(f"Positive check starts\n")

    test_result = devide_numbers(a, b)
    assert test_result == result, f"{test_result} != {result}"


def send_request(url):
    response = requests.get(url)
    return response.status_code


def test_send_request():
    mock_get = Mock(return_value=Mock(status_code=200))
    with patch('requests.get', mock_get):
        status_code = send_request('http://example.com')
        assert status_code == 200
        mock_get.assert_called_once_with('http://example.com')


def test_send_request_mocker(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    status_code = send_request('http://example.com')
    assert status_code == 200
    mock_get.assert_called_once_with('http://example.com')
