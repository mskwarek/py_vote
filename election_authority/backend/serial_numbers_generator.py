import random

class SerialNumbersgenerator():

    @staticmethod
    def generateSerialNumbersList(listSize, serialNumberBitSize):
        return [random.randint(0, 1) for i in range(0, listSize)]