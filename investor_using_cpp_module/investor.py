import investor_c as cmi
import sys

command_line_args = {sys.argv[2*i+1]:sys.argv[2*i+2] for i in range((len(sys.argv)-1)//2)}


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
        alg = command_line_args['-a']
        if (alg != "dynamic"):
            raise ValueError("Unexpected algorithm")
        
        with open(command_line_args['-i'], 'r') as file:
        
            lines = file.readlines()
            
            N, M, S = (int(elem) for elem in lines[0].split())
            if N * M <= 0:
                raise ValueError("Wrong N or M")
                
            maturity_date = N + 30    
                
            arrlots = []
            arrobjects = []
            
            for i in range(1, len(lines)):
                strobl = lines[i]
                lot = Lot(strobl, maturity_date = maturity_date)
                arrlots.append(lot)
                arrobjects.append(cmi.Object(lot.weight, lot.value))
        
    except Exception as e:
        print(str(e))

    return arrlots, arrobjects, S


# --------------- output ---------------


def write(max_profit, arrlots, taken):
    try:
        with open(command_line_args['-o'], 'w') as file:   
            file.write(str(max_profit)+"\n")
            file.write("".join([arrlots[ind].strobl for ind in taken]))      
    except Exception as e:
        print(str(e))

# --------------- launch ---------------


def main():
    arrlots, arrobjects, S = read()
    print("\n".join([str(arrobjects[i].weight) + " " + str(arrobjects[i].value) for i in range(len(arrobjects))]))
    res = cmi.solve_knapsack_problem(arrobjects, S)
    max_profit = res.max_profit
    taken = list(res.taken)
    taken.reverse()
    print(taken)
    write(max_profit, arrlots, taken)


if __name__ == '__main__':
    main()
    