class RentalUnit:
    def get_name(self):
        return self.tenant_first + " " + self.tenant_last
    def increase_rent(self,pct):
        self.rent = self.rent * (1+ pct)


unit1 = RentalUnit()
unit1.tenant_first = 'Joe'
unit1.tenant_last = 'Shmo'
unit1.rent = 5000
print(unit1.get_name())
print(unit1.rent)
unit1.increase_rent(.2)
print(unit1.rent)

unit2 = RentalUnit()
unit2.tenant_first = 'Susan'
unit2.tenant_last = 'Sun'
unit2.rent = 10000
print(unit2.get_name())
unit2.increase_rent(.15)
print(unit2.rent)