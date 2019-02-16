from uuid import uuid4
from random import shuffle

from numpy import transpose, dot


class Client:
    def __init__(self):
        self.client_id = str(uuid4())
        self.serial_number = 0
        self.tokens = []
        self.exponents = []
        self.signatureFactor = []
        self.permutation = None
        self.inversed_permutation = None
        self.permutation_modulus = []
        self.permutation_exponenets = []

    def generate(self, candidatesQuantity):
        self.permutation = Permutation(candidatesQuantity)


class Permutation:
    def __init__(self, candidatesQuantity=0):
        self.permutation = [i for i in range(candidatesQuantity)]
        shuffle(self.permutation)
        matrix = [[0 for col in range(candidatesQuantity)] for row in range(candidatesQuantity)]

        for i in range(candidatesQuantity):
            matrix[i][self.permutation[i]] = 1

        self.permutation_matrix = matrix


    def inverse(self):
        return dot(self.permutation, self.permutation_matrix)
