import sys
import time
import mem_use_win32

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


# --------------- solution -------------

def solve_knapsack_problem(list_objects, S):

    def _solve_knapsack_problem(objects, W):
        n = len(objects)
        m = [[0 for j in range(W+1)] for i in range(n+1)]
        arrpath_j = [[0 for j in range(W+1)] for i in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(0, W+1):
                wi = objects[i-1][0]
                vi = objects[i-1][1]
                if wi > j:
                    m[i][j] = m[i-1][j]
                else:
                    m[i][j] = max(m[i-1][j], m[i-1][j-wi] + vi)
                if m[i][j] == m[i-1][j]:
                    arrpath_j[i][j] = j
                else:
                    arrpath_j[i][j] = j-wi
            
        taken = []
        
        cur_j = W
        for i in range(n, 0, -1):
            if cur_j != arrpath_j[i][cur_j]:  # element was taken
                taken.append(i-1)
                cur_j = arrpath_j[i][cur_j]    
                    
        return m[n][W], taken

    max_profit, taken = _solve_knapsack_problem(list_objects, S)
    taken.reverse()
    return max_profit, taken


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
                arrobjects.append((lot.weight, lot.value))
        
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
    start_time = time.time()
    max_profit, taken = solve_knapsack_problem(arrobjects, S)
    write(max_profit, arrlots, taken)
    end_time = time.time()
    print("TIME:", end_time - start_time, "s")
    print("MEMORY:", mem_use_win32.get_memory_info())
    
if __name__ == '__main__':
    main()
    