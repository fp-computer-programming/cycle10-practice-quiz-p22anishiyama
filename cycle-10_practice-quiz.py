# Author: ATN 1/27/22

def food_costs(groceries, costs):
    # making sure that the original list will not be altered
    groceries_mod = groceries

    for i, v in enumerate(groceries):
        groceries_mod[i] = "{0}: ${1}".format(groceries[i], costs[i])
    return groceries_mod  
        

print(food_costs(['apple','pear','banana','salmon','tuna','cod','milk','eggs','yogurt'],[1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]))

def fibonacci (n):
    x = 0
    sequence = []
    while x < n:
        sequence.append
        x += 1
    return sequence

print(fibonacci(4))