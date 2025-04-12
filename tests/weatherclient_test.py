import pytest
from unittest.mock import Mock, patch
from weather_app.weather_client import get_current_weather, get_weather_forecast

@patch("weather_app.weather_client.requests.get")
def test_get_current_weather(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "name": "Lagos",
        "main": {"temp": 27.14, "humidity": 83},
        "weather": [{"description": "broken clouds"}],
        "wind": {"speed": 1.92}
    }

    mock_get.return_value = mock_response

    result = get_current_weather("Lagos")

    # Assert the correct data is returned
    assert result == {
        "city_name": "Lagos",
        "temperature": 27.14, 
        "weather_condition": "broken clouds",
        "humidity_percent": 83,
        "wind_speed": 1.92
    }

    mock_get.assert_called_once_with("http://api.openweathermap.org/data/2.5/weather?q=Lagos&appid=152a3375c68bf74bc797b07c22673ed7&units=metric")

@patch("weather_app.weather_client.requests.get")
def test_get_weather_forecast(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "list": [
            {
                "main": {"temp": 27.14, "humidity": 83},
                "weather": [{"description": "broken clouds"}],
                "wind": {"speed": 1.92}
            },
            {
                "main": {"temp": 27.14, "humidity": 83},
                "weather": [{"description": "broken clouds"}],
                "wind": {"speed": 1.92}
            }
        ]
    }

    mock_get.return_value = mock_response

    result = get_weather_forecast("Lagos")

    # Assert the correct data is returned
    assert result == {
        "city": "Lagos",
        "forecast": [
            {
                "temperature": 27.14, 
                "weather_condition": "broken clouds",
                "humidity_percent": 83,
                "wind_speed": 1.92
            },
            {
                "temperature": 27.14, 
                "weather_condition": "broken clouds",
                "humidity_percent": 83,
                "wind_speed": 1.92
            }       
        ]
    }

    mock_get.assert_called_once_with("http://api.openweathermap.org/data/2.5/forecast?q=Lagos&appid=152a3375c68bf74bc797b07c22673ed7&units=metric")    
            
