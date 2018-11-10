import trade_tools
class Blotter:
    def __init__(self):
        self.__trades = []
        self.__hello = 'hello'
    def update_hello(self,new_msg):
        if len(new_msg) > 5:
            self.__hello = new_msg
    def add_trade(self,t):
        self.__trades.append(t)
    def print_ledger(self):
        for t in self.__trades:
            t.display_trade()

class Trade:
    def __init__(self, symbol, price, quant):
        self.__symbol = symbol
        self.__price = price
        self.__quant = quant

    def get_symbol(self):
        return self.__symbol
    
    def trade_value(self):
        return self.__price * self.__quant
    
    def display_trade(self):
        print(self.__symbol,self.__quant,self.__price)

ledger = Blotter()
ledger.hello = 'bye'
ledger.add_trade(Trade('IBM', 100, 100))
ledger.add_trade(Trade('SNAP', 200, 100))
ledger.add_trade(Trade('MSFT', 300, 100))
ledger.print_ledger()

class RentalUnit:
    def __init__(self,initial_value):
        self.__rent = initial_value
        #self.rent = initial_value
    def update_rent(self,new_rent):
        if new_rent > 0:
            self.__rent = new_rent


u1 = RentalUnit(5000)
u1.update_rent(-400)

val = 5

def calc_salary(a,b):
    new_salary = val * a * b
    return 5

x = calc_salary(1,2)
print(x)

