import pytest
import serial_numbers_generator


def test_default_get():
    numbersList = serial_numbers_generator.SerialNumbersgenerator.generateSerialNumbersList(10, 64)
    assert len(numbersList) == 10