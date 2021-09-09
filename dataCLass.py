class Tennyclass():
    def __init__(self, name):
        self.name = name

tenny = Tennyclass('itsy')
print(tenny.name)

from dataclasses import dataclass
@dataclass
    class TennyDataClass:
        name : str
teeny = TeenyDataClass('bitsy')
print(tenny.name)
