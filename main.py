from functions import func
from random import randint


def Acceptance(current_cost,new_cost,temperature):
    delta = new_cost - current_cost
    if  delta > 0:
        return new_cost
    else:
        return exp(-delta/temperature)

def Simulated_Annealing(x1,x2,y1,y2):
    # Temperature define
    T_Max = 100
    T_Min = 0
    T = T_Max
    markov_step = 100
    
    # Initial State
    current_state_x = randint(x1,x2)
    current_state_y = randint(y1,y2)
    current_cost = func(current_state_x,current_state_y)


    while T != T_Min:
        for i in range(1,markov_step):
            if T == 0:
                return current



def Brutal_Force(x1,x2,y1,y2):
    z = 0
    for i in range(x1,x2):
        for j in range(y1,y2):
            result = func(i,j)            
            if result < z:
                x = i
                y = j
                z = result
    print('X:{} Y:{}'.format(x,y))
    print('Z:{:.2f}'.format(z))
    

def main():
    input_data = []
    f = open('input.txt','r+')
    content = f.read()    
    content = content.split('\n')    
    input_data += content[0].split(',')
    input_data += content[1].split(',')    
    Brutal_Force(int(input_data[0]),int(input_data[1]),int(input_data[2]),int(input_data[3]))
    Simulated_Annealing(int(input_data[0]),int(input_data[1]),int(input_data[2]),int(input_data[3]))

if __name__ == '__main__':
    main()