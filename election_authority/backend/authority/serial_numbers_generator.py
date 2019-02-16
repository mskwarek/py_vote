import random

from Crypto.PublicKey import RSA


def generateSerialNumbersList(listSize, serialNumberBitSize):
    return [random.getrandbits(64) for i in range(0, listSize)]


def generateRsaKeyPairList(list_size, rsa_bitlen):
    key = RSA.generate(2048)
    privatekey = key.exportKey()
    publickey = key.publickey().exportKey()
    return privatekey, publickey
