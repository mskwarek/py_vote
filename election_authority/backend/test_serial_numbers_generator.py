import pytest
import serial_numbers_generator
import sys


def test_returened_list_length():
    numbersList = serial_numbers_generator.SerialNumbersgenerator.generateSerialNumbersList(10, 64)
    assert len(numbersList) == 10


def test_returned_numbers_bit_length():
    numbersList = serial_numbers_generator.SerialNumbersgenerator.generateSerialNumbersList(10, 64)
    for item in numbersList:
        assert item.bit_length() <= 64
        assert item.bit_length() > 1