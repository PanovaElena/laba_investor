from investor import *
import investor_c as cmi
import cProfile
import random
import time

N = 15
M = 20
S = 15000


def generate_rand_data():
    bond_value = 1000
    max_price = 1500
    min_price = 1000
    max_number = 20
    min_number = 1
    name = "name"
    
    def cost(price): return price * 100 / bond_value
    
    res = []
    
    random.seed()
    
    for date in range(1, N+1):
        for lot in range(M+1):
            price = random.randint(min_price, max_price)
            number = random.randint(min_number, max_number)
            strobl = "%d %s %0.1f %d" % (date, name, cost(price), number)
            lot = Lot(strobl, maturity_date = N + 30, bond_value = bond_value)
            res.append(cmi.Object(lot.weight, lot.value))
                
    return res
    

data = generate_rand_data()

start_time = time.time()
cmi.solve_knapsack_problem(data, S)
end_time = time.time()

print(end_time - start_time)

    
    
