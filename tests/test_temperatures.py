import pytest

from exercises.temperatures import (
    convertToCelsius,
    convertToFahrenheit
)


def test_convertToCelsius_0_degree():
    assert pytest.approx(convertToCelsius(0), 0.1) == -17.8


def test_convertToCelsius_180_degree():
    assert pytest.approx(convertToCelsius(180), 0.1) == 82.2


def test_convertToFahrenheit_0_degree():
    assert convertToFahrenheit(0) == 32


def test_convertToFahrenheit_100_degree():
    assert convertToFahrenheit(100) == 212.0


def test_conversion_to_Fahrenheit_and_back_to_Celsius():
    assert convertToCelsius(convertToFahrenheit(15)) == 15.0
