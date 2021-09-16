class fourCal:
    def __init__(self, first, second): #Constructor need two aarguments..
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class moreFourCal(fourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self):
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result

a = moreFourCal(5, 0)

print(a.pow())
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())