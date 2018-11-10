class RentalUnit:
    def __init__(self,r,f,l):
        self.__rent = r
        self.__fname = f
        self.__lname = l
    def annualize(self):
        return self.__rent * 12
    def increase_rent(self,pct):
        self.__rent = self.__rent * (1 + pct)
    def get_full_name(self):
        return self.__fname + " " + self.__lname
    def get_rent(self):
        return self.__rent
    def set_rent(self,r):
        self.__rent = r

u1 = RentalUnit(5000,'John','Doe')
print(u1.annualize())
print(u1.get_full_name())

num = 500
print(type(num ))

print(type(u1))

print(u1.__dict__)
