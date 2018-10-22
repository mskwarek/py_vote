import random

class SerialNumbersgenerator():

    @staticmethod
    def generateSerialNumbersList(listSize, serialNumberBitSize):
        return [random.getrandbits(64) for i in range(0, listSize)]