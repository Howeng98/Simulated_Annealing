from functions import func
from random import randint, uniform
from math import exp
import matplotlib.pyplot as plt


def Acceptance(delta,temperature):    
    return exp(-(delta)/temperature)

def generate_NextState(x1,x2,y1,y2,current_state_x,current_state_y):
    next_state_x = randint(x1,x2)
    next_state_y = randint(y1,y2)
    while next_state_x == current_state_x and next_state_y == current_state_y:
        next_state_x = randint(x1,x2)
        next_state_y = randint(y1,y2)
    return next_state_x,next_state_y 
    

def Simulated_Annealing(x1,x2,y1,y2):    
    # Temperature definecurrent_cost    
    T_Max = 1000
    T_Min = 0.001
    T = T_Max    
    cooling_rate = 0.9999
    cost_list = []
    step_list = []
    t_list = []
    x_list = []
    y_list = []
    prob_list = []
    counter = 0
    probability = 0
    
    # Initial State
    current_state_x = randint(x1,x2)
    current_state_y = randint(y1,y2)
    current_cost = func(current_state_x,current_state_y)
    cost_list.append(abs(current_cost))
    step_list.append(counter)
    t_list.append(T)
    x_list.append(current_state_x)
    y_list.append(current_state_y)
    prob_list.append(0)
    got_change_list = []
    got_change_list.append(0)
    counter = counter + 1

    while T > T_Min:        
        # generate next state        
        next_state_x,next_state_y = generate_NextState(x1,x2,y1,y2,current_state_x,current_state_y)

        # calculate next cost
        next_cost = func(next_state_x,next_state_y)

        # calculate delta energy cost between current state and next state
        delta = next_cost - current_cost

        # if next state cost is better than current 
        if(delta < 0):
            current_state_x = next_state_x
            current_state_y = next_state_y
            current_cost = next_cost
            got_change_list.append(0)
            # cost_list.append(abs(current_cost))
        # next state is worse than current one
        else:
            probability = Acceptance(delta,T)
            threshold = uniform(0,1)
        
            # randomly give a chance to replace
            if(threshold < probability):
                current_state_x = next_state_x
                current_state_y = next_state_y
                current_cost = next_cost
                # cost_list.append(abs(current_cost))
                got_change_list.append(1)
            else:
                got_change_list.append(0)
                

        # Update Temperature
        T = T * cooling_rate

        # plot graph - list
        t_list.append(T)
        step_list.append(counter)
        cost_list.append(abs(current_cost))
        x_list.append(current_state_x)
        y_list.append(current_state_y)
        prob_list.append(probability)
        counter = counter + 1
    
    x_list.sort()
    y_list.sort()
    # cost_list.sort()
    plt.plot(t_list[::200],got_change_list[::200],'b-')
    plt.xlabel('Temperature Variation')
    plt.ylabel('Second Chance is Accepted')
    plt.show()


    ######################################################################################################
    # T_Max = 10000
    # T_Min = 0.001
    # T = T_Max    
    # cooling_rate = 0.99
    # cost_list = []
    # step_list = []
    # t_list = []
    # x_list = []
    # y_list = []
    # counter = 0
    
    # # Initial State
    # current_state_x = randint(x1,x2)
    # current_state_y = randint(y1,y2)
    # current_cost = func(current_state_x,current_state_y)
    # cost_list.append(abs(current_cost))
    # step_list.append(counter)
    # t_list.append(T)
    # x_list.append(current_state_x)
    # y_list.append(current_state_y)
    # counter = counter + 1
    # while T > T_Min:        
    #     # generate next state        
    #     next_state_x,next_state_y = generate_NextState(x1,x2,y1,y2,current_state_x,current_state_y)

    #     # calculate next cost
    #     next_cost = func(next_state_x,next_state_y)

    #     # calculate delta energy cost between current state and next state
    #     delta = next_cost - current_cost

    #     # if next state cost is better than current 
    #     if(delta < 0):
    #         current_state_x = next_state_x
    #         current_state_y = next_state_y
    #         current_cost = next_cost
    #         # cost_list.append(abs(current_cost))
    #     # next state is worse than current one
    #     else:
    #         probability = Acceptance(delta,T)
    #         threshold = uniform(0,1)
        
    #         # randomly give a chance to replace
    #         if(threshold < probability):
    #             current_state_x = next_state_x
    #             current_state_y = next_state_y
    #             current_cost = next_cost
    #             # cost_list.append(abs(current_cost))
                

    #     # Update Temperature
    #     T = T * 0.999

    #     # plot graph - list
    #     t_list.append(T)
    #     step_list.append(counter)
    #     cost_list.append(abs(current_cost))
    #     x_list.append(current_state_x)
    #     y_list.append(current_state_y)
    #     counter = counter + 1
    
    # #for cost in cost_list:
    # '''
    # If plot like the below code,matplotlib will gonna overflow
    # Actually we just no need to print so much data point,
    # Try to print it out every 100 or even 1000 data
    # # plt.plot(x_list,y_list,color='red')   
    # # plt.plot(x_list[::100], y_list[::100])

    # # mpl.rcParams['agg.path.chunksize'] = 10000
    # '''
    # # plt.plot(x_list,y_list,color='red')   
    # x_list.sort()
    # y_list.sort()
    # # cost_list.sort()
    # # plt.plot(step_list[::1], cost_list[::1],'b-')
    # # plt.legend('T = 0.99999','T = 0.999')   
    

    print('------ Simulated_Annealing ------')
    print('X:{} Y:{} Z:{:.2f}'.format(current_state_x,current_state_y,current_cost))        

def Brutal_Force(x1,x2,y1,y2):
    z = 0
    for i in range(x1,x2):
        for j in range(y1,y2):
            result = func(i,j)            
            if result < z:
                x = i
                y = j
                z = result
    print('---------- Brutal_Force ---------')
    print('X:{} Y:{} Z:{:.2f}'.format(x,y,z))

def main():
    # Read input data range
    input_data = []
    f = open('input.txt','r+')
    content = f.read()    
    content = content.split('\n')    
    input_data += content[0].split(',')
    input_data += content[1].split(',')    

    # Calculate Minimum value of Z
    Brutal_Force(int(input_data[0]),int(input_data[1]),int(input_data[2]),int(input_data[3]))
    Simulated_Annealing(int(input_data[0]),int(input_data[1]),int(input_data[2]),int(input_data[3]))

if __name__ == '__main__':
    main()