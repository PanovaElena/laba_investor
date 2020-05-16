import random

N = 50
M = 50
S = 100000


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
            res.append("%d %s %0.1f %d" % (date, name, cost(price), number))
                
    return res
    

res = generate_rand_data()
with open("large_input.txt", "w") as file:
    file.write("%d %d %d\n" % (N, M, S))
    for bond in res:
        file.write(bond + "\n")
    
    
