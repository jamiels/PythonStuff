import random
BUY = True
SELL = False
balance_history = []
initial_balance = 500000
balance = initial_balance
ledger = open('ledger.txt','w+')

def get_bitcoin_price():
  return random.randrange(0,20000)

def trade(side, price, current_balance):
  ## Buy = True, Sell = False
  transaction = str(current_balance)+","+str(side)+","+str(price)
  if side:
    current_balance = current_balance - price
  else:
    current_balance = current_balance + price
  transaction = transaction + "," + str(current_balance) + '\n'
  ledger.write(transaction)
  return current_balance

for i in range (0,100):
  balance=trade(BUY,get_bitcoin_price(),balance)
  balance_history.append(balance)
  balance=trade(SELL,get_bitcoin_price(),balance)
  balance_history.append(balance)

print('Trades made:',len(balance_history))
print('Initial balance:',initial_balance)
print('Ending balance:',balance)
print('Profit/Loss:', balance - initial_balance)
print('Min balance:', min(balance_history))
print('Max balance:', max(balance_history))
print('Average balance:', sum(balance_history) / len(balance_history))
ledger.close()