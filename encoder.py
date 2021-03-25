from abc import ABC

class Encoder(ABC):
    
    @classmethod
    def encode(self, data):
        ...
    @classmethod
    def __init__(self, n=9, k=4, r=2):
        self.n = n
        self.k = k
        self.r = r
        ...