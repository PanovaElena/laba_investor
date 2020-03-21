import investor_c as cmi


class Lot:
    
    def __init__(self, strobl, maturity_date, bond_value = 1000):
        self.bond_value = bond_value
        self.maturity_date = maturity_date
        
        self.strobl = strobl
        arrdata = strobl.split(" ")
        self.date = int(arrdata[0])
        self.name = arrdata[1]
        self.percent = float(arrdata[2])
        self.price = int(self.percent * self.bond_value / 100)
        self.number = int(arrdata[3])
        
        self.weight = self.number * self.price
        self.value = (self.maturity_date - self.date + self.bond_value - self.price) * self.number


# --------------- input ----------------


def read():
    try:
        N, M, S = (int(elem) for elem in input().split())
        if N * M <= 0:
            raise ValueError()
            
        maturity_date = N + 30    
            
        arrlots = []
        arrobjects = []
        strobl = input()
        while strobl:
            lot = Lot(strobl, maturity_date = maturity_date)
            arrlots.append(lot)
            arrobjects.append(cmi.Object(lot.weight, lot.value))
            strobl = input()
        
    except Exception as e:
        print("ERROR: WRONG INPUT\n", str(e))

    return arrlots, arrobjects, S    


# --------------- output ---------------


def write(max_profit, arrlots, taken):
    taken.reverse()
    print(max_profit)
    print("\n".join([arrlots[ind].strobl for ind in taken]))
    print()


# --------------- launch ---------------


def main():
    arrlots, arrobjects, S = read()    
    res = cmi.solve_knapsack_problem(arrobjects, S)
    write(res.max_profit, arrlots, res.taken)


if __name__ == '__main__':
    main()
    