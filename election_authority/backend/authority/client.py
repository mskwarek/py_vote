from uuid import uuid4
from authority import Permutation

class Client:
    def __init__(self, candidatesQuantity):
        self.client_id = str(uuid4())
        self.serial_number = 0
        self.tokens = []
        self.exponents = []
        self.signatureFactor = []
        self.permutation = Permutation(candidatesQuantity)
        self.permutation_modulus = []
        self.permutation_exponenets = []

