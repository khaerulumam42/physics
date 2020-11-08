# config
max_iteration = 100
tolerance = 0.000001
x0 = 3

def base_eq(x):
    y_hat = 3.0/(5.0-x)**2 - 5.0/x**2

    return y_hat

def diff_base_eq(x):
    y_hat_diff = 6.0/(5.0-x)**3 + 10.0/x**3 
    
    return y_hat_diff


for i in range(max_iteration):
    x1 = (x0-base_eq(x0))/diff_base_eq(x0)
    
    delta = x1-x0

    if abs(delta) <= tolerance or i == (max_iteration-1):
        print(f"found root of the equation is {x1} at iteration {i}")
        break

    x0 = x1
