def func(x, y):
    from math import pow
    from math import exp
    import time
    # time.sleep(0.005)
    scale = 2.0
    # z = -30*(e^(-(x)^2/25)*e^(-(y-15)^2/25))-10*(e^(-(x-10)^2/25)*e^(-(y-5)^2/25))-20*(e^(-(x+10)^2/25)*e^(-(y-5)^2/25))
    x = float(x/scale)
    y = float(y/scale)
    z1 = -30*exp(-pow(x,2)/25)*exp(-pow(y-15,2)/25)
    z2 = -10*exp(-pow(x-10,2)/25)*exp(-pow(y-5,2)/25)
    z3 = -20*exp(-pow(x+10,2)/25)*exp(-pow(y-5,2)/25)
    return z1+z2+z3
